import gradio as gr
from openai import OpenAI

client = OpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1",
)

MODEL = "google/gemini-2.5-flash"
# Other examples:
# MODEL = "openai/gpt-4.1-mini"
# MODEL = "anthropic/claude-sonnet-4"
# MODEL = "deepseek/deepseek-chat"

def reply(message, history):
    messages = []

    for user_msg, assistant_msg in history:
        messages.append({"role": "user", "content": user_msg})
        if assistant_msg:
            messages.append({"role": "assistant", "content": assistant_msg})

    messages.append({"role": "user", "content": message})

    stream = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        stream=True,
        temperature=0.7,
    )

    answer = ""

    for chunk in stream:
        delta = chunk.choices[0].delta.content
        if delta:
            answer += delta
            yield answer


gr.ChatInterface(
    fn=reply,
    title="OpenRouter Chat",
    description=f"Model: {MODEL}",
).launch()

