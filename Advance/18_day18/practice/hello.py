import asyncio
import creds
import gradio as gr
from openai import AsyncOpenAI
from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled

# def hello(name):
#     return f"Hello {name} how are you?"

# interface = gr.Interface(fn=hello, 
#              inputs=gr.Textbox(label="Your name"), 
#              outputs=gr.Textbox(label="Response"),
#              title="Hello world")

# interface.launch()


creds = creds.Creds()
set_tracing_disabled(True)

open_ai_client = AsyncOpenAI(
    api_key=creds.api_key,
    base_url=creds.base_url)

chat_model = OpenAIChatCompletionsModel(
    model=creds.model_name,
    openai_client=open_ai_client)

planner_agent = Agent(
    name="Draft planner",
    instructions=(
        "You are a draft planner. Create a short plan for the user's task "
        "in the requested tone. Respond in one or two concise sentences."
    ),
    model=chat_model
)

async def draft_plan(task, tone):
    try: 
        result = await Runner.run(
            planner_agent,
            f"Task: {task}\nTone: {tone}",
        )
        return result.final_output
    except Exception as ex:
        return f"### Error: {ex}"

with gr.Blocks(title="Agent control panel") as block:
    gr.Markdown("# Agent control panel")
    gr.Markdown("Configure a simple planning agent")

    with gr.Row():
        task = gr.Textbox(
            label="Task for the agent",
            placeholder="Example: create a launch plan for a new product",
            lines=4
        )

        tone = gr.Dropdown(
            choices=["Proffesional", "Friendly", "Consise"],
            value="Proffesional",
            label="Response style"
        )

    run_button = gr.Button("Create plan", variant="primary")
    output = gr.Markdown(label="Agent output")

    run_button.click(
        fn=draft_plan,
        inputs=[task, tone],
        outputs=output
    )

block.launch()

