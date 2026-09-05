import json
import gradio as gr
import requests

API_URL = "http://localhost:8000/api/v1/chat"


def extract_text(content) -> str:
    """Helper to reliably extract plain text from Gradio message content

    whether it is a string, a list of components, or a dict.
    """
    if isinstance(content, str):
        return content
    elif isinstance(content, list):
        parts = []
        for item in content:
            if isinstance(item, str):
                parts.append(item)
            elif isinstance(item, dict) and "text" in item:
                parts.append(str(item["text"]))
            else:
                parts.append(str(item))
        return " ".join(parts)
    elif isinstance(content, dict) and "text" in content:
        return str(content["text"])
    return str(content) if content else ""


def stream_rag_chat(message: str, history: list):
    """Consumes the FastAPI SSE endpoint and yields tokens incrementally

    into Gradio's chat interface while updating metadata and metrics panels.
    """
    clean_message = extract_text(message).strip()
    if not clean_message:
        yield "", "No question provided.", "{}"
        return

    payload = {"question": clean_message}
    accumulated_text = ""
    retrieval_info = "Searching knowledge base..."
    metrics_info = "{}"

    try:
        with requests.post(
            API_URL, json=payload, headers={"Content-Type": "application/json"}, stream=True
        ) as response:
            if response.status_code != 200:
                error_msg = f"API Error: HTTP {response.status_code} - {response.text}"
                yield error_msg, retrieval_info, metrics_info
                return

            for line in response.iter_lines(decode_unicode=True):
                if not line or not line.startswith("data: "):
                    continue

                raw_data = line[len("data: ") :].strip()

                if raw_data == "[DONE]":
                    break

                try:
                    event = json.loads(raw_data)
                    event_type = event.get("event")
                    event_data = event.get("data")

                    if event_type == "retrieval":
                        matched_chunk = event_data.get("matched_chunk", "")
                        score = event_data.get("similarity", 0.0)
                        tokens = event_data.get("embedding_tokens", 0)
                        retrieval_info = (
                            f"**Cosine Similarity:** `{score}`\n\n"
                            f"**Embedding Tokens:** `{tokens}`\n\n"
                            f"**Matched Chunk:**\n> {matched_chunk}"
                        )
                        yield accumulated_text, retrieval_info, metrics_info

                    elif event_type == "token":
                        accumulated_text += event_data
                        yield accumulated_text, retrieval_info, metrics_info

                    elif event_type == "metrics":
                        metrics_info = json.dumps(event_data, indent=2)
                        yield accumulated_text, retrieval_info, metrics_info

                except json.JSONDecodeError:
                    continue

    except requests.exceptions.ConnectionError:
        yield (
            "Error: Could not reach the FastAPI server at http://localhost:8000. Is it running?",
            "Connection failed.",
            "{}",
        )


# =========================================================
# Gradio UI Layout
# =========================================================
custom_css = """
#chatbot { min-height: 480px; }
.metadata-box textarea { font-family: monospace; font-size: 12px; }
"""

with gr.Blocks(title="Local RAG Agent UI") as demo:
    gr.Markdown(
        """
        # Local RAG Agent Web Client
        *Connected to FastAPI &bull; Streaming SSE &bull; LMStudio (`bge-small` + `qwen2.5-0.5b`)*
        """
    )

    with gr.Row():
        # Left column: Interactive Chatbot
        with gr.Column(scale=3):
            chatbot = gr.Chatbot(label="Conversation", elem_id="chatbot")
            with gr.Row():
                msg_input = gr.Textbox(
                    placeholder="Ask a question about course policies...",
                    show_label=False,
                    scale=8,
                    container=False,
                )
                submit_btn = gr.Button("Send", variant="primary", scale=1)

            clear_btn = gr.Button("Clear Chat History")

            gr.Examples(
                examples=[
                    "When can I meet with the instructor in person?",
                    "What happens if I submit my homework 4 hours late?",
                    "What textbook do we need to purchase for this course?",
                ],
                inputs=msg_input,
            )

        # Right column: Live Telemetry Panels
        with gr.Column(scale=2):
            retrieval_display = gr.Markdown(
                label="Retrieval Telemetry",
                value="*Awaiting user query to display top vector match...*",
            )
            metrics_display = gr.Code(
                label="Telemetry & Cost Savings (JSON)",
                language="json",
                value="{\n  \"status\": \"idle\"\n}",
                elem_classes=["metadata-box"],
            )

    # ---------------------------------------------------------
    # Event Wiring
    # ---------------------------------------------------------
    def user_turn(user_message, chat_history):
        clean_user_message = extract_text(user_message).strip()
        if not clean_user_message:
            return "", chat_history
        
        chat_history = chat_history or []
        updated_history = chat_history + [
            {"role": "user", "content": clean_user_message},
            {"role": "assistant", "content": ""},
        ]
        return "", updated_history

    def bot_turn(chat_history):
        if not chat_history or len(chat_history) < 2:
            return

        # Extract latest user message using safe extraction
        raw_user_content = chat_history[-2]["content"]
        clean_user_message = extract_text(raw_user_content)

        for partial_text, retrieval_md, metrics_json in stream_rag_chat(
            clean_user_message, chat_history
        ):
            chat_history[-1]["content"] = partial_text
            yield chat_history, retrieval_md, metrics_json

    submit_event = msg_input.submit(
        user_turn, [msg_input, chatbot], [msg_input, chatbot], queue=False
    ).then(
        bot_turn, chatbot, [chatbot, retrieval_display, metrics_display]
    )

    submit_btn.click(
        user_turn, [msg_input, chatbot], [msg_input, chatbot], queue=False
    ).then(
        bot_turn, chatbot, [chatbot, retrieval_display, metrics_display]
    )

    clear_btn.click(lambda: [], None, chatbot, queue=False)

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        theme=gr.themes.Soft(),
        css=custom_css,
    )
