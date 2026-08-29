# Gradio for AI Agent Builders

A practical, chapter-by-chapter workshop guide with runnable examples.

## Who this is for

This course is for developers who already understand the basic idea of an AI agent—an LLM that can converse, use tools, and produce an outcome—and want to give that agent a clean web interface.

## Prerequisites

- Python 3.10+
- Basic Python functions and virtual environments
- An LLM API key for the LLM chapters (optional at first)

Install the libraries:

```bash
pip install --upgrade gradio openai
```

Set your API key before running LLM examples:

```bash
export OPENAI_API_KEY="your_api_key_here"
```

On Windows PowerShell:

```powershell
$env:OPENAI_API_KEY="your_api_key_here"
```

---

# Chapter 1 — What Gradio does for AI agents

Gradio turns normal Python functions into browser interfaces. For agent builders, it is especially helpful for:

- testing prompts interactively;
- showing a chat interface around an LLM;
- displaying tool activity and results;
- accepting uploads, settings, and feedback;
- sharing an internal prototype with teammates.

The basic pattern is:

```text
User input → Gradio component → Python agent function → Gradio output
```

## Your first Gradio app

Create `chapter_01_hello.py`:

```python
import gradio as gr

def greet(name):
    return f"Hello, {name}. Your Gradio app is working!"

demo = gr.Interface(
    fn=greet,
    inputs=gr.Textbox(label="Your name"),
    outputs=gr.Textbox(label="Response"),
    title="My First Gradio App",
)

demo.launch()
```

Run it:

```bash
python chapter_01_hello.py
```

Open the local address shown in your terminal.

## Teaching point

`gr.Interface` is the fastest option when your app is one function with clear inputs and outputs.

---

# Chapter 2 — Build an agent control panel with Blocks

AI agents often need more than one input: a task, a model choice, a system instruction, and perhaps a tool setting. `gr.Blocks` gives you layout control.

Create `chapter_02_blocks.py`:

```python
import gradio as gr

def draft_plan(task, tone):
    return f"""## Agent plan

**Task:** {task}

**Tone:** {tone}

1. Understand the goal.
2. Identify the information required.
3. Use available tools when needed.
4. Produce a clear final response.
"""

with gr.Blocks(title="Agent Control Panel") as demo:
    gr.Markdown("# Agent Control Panel")
    gr.Markdown("Configure a simple planning agent.")

    with gr.Row():
        task = gr.Textbox(
            label="Task for the agent",
            placeholder="Example: Create a launch plan for a new product",
            lines=4,
        )
        tone = gr.Dropdown(
            choices=["Professional", "Friendly", "Concise"],
            value="Professional",
            label="Response style",
        )

    run_button = gr.Button("Create plan", variant="primary")
    output = gr.Markdown(label="Agent output")

    run_button.click(
        fn=draft_plan,
        inputs=[task, tone],
        outputs=output,
    )

demo.launch()
```

## Teaching point

Use `Blocks` when you need a real application layout: rows, columns, tabs, buttons, settings, logs, and multiple outputs.

---

# Chapter 3 — Make a basic chatbot

For a conversational agent, Gradio provides `gr.ChatInterface`. Your function receives:

- `message`: the latest user message;
- `history`: the prior conversation.

Create `chapter_03_echo_chat.py`:

```python
import gradio as gr

def agent_reply(message, history):
    return f"I received: {message}"

demo = gr.ChatInterface(
    fn=agent_reply,
    title="Starter Agent",
    description="A minimal chat UI for testing agent behavior.",
    examples=[
        "Help me plan a team meeting.",
        "Explain what an AI agent is.",
        "Give me three product ideas.",
    ],
)

demo.launch()
```

## Exercise

Change the reply so the agent:

1. Greets the user.
2. Counts how many prior messages exist.
3. Recommends a next step.

Example solution:

```python
def agent_reply(message, history):
    turns = len(history)
    return (
        f"Hello! This is conversation turn {turns + 1}. "
        f"You said: {message}\n\n"
        "Suggested next step: give me a concrete goal and any constraints."
    )
```

---

# Chapter 4 — Connect Gradio to an LLM

Now replace the fake chatbot response with an LLM call.

Create `chapter_04_llm_chat.py`:

```python
import os
import gradio as gr
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

SYSTEM_PROMPT = """
You are a helpful AI agent assistant.
Be concise, practical, and transparent when you need more information.
"""

def run_agent(message, history):
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    for item in history:
        messages.append({
            "role": item["role"],
            "content": item["content"],
        })

    messages.append({"role": "user", "content": message})

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages,
        temperature=0.4,
    )

    return response.choices[0].message.content

demo = gr.ChatInterface(
    fn=run_agent,
    title="LLM Agent",
    description="A Gradio chat interface connected to an LLM.",
)

demo.launch()
```

## Important notes

- Keep API keys in environment variables—never hard-code them in a Python file.
- The `history` object lets the model remember the active conversation.
- Change the model name to one available to your organization if needed.
- Use a focused system prompt to establish the agent’s role and boundaries.

---

# Chapter 5 — Stream responses as they are generated

Streaming makes an agent feel responsive, especially when it is producing a long answer.

Create `chapter_05_streaming.py`:

```python
import time
import gradio as gr

def stream_agent(message, history):
    response = f"Here is my response to: {message}"
    partial_response = ""

    for character in response:
        partial_response += character
        time.sleep(0.03)
        yield partial_response

demo = gr.ChatInterface(
    fn=stream_agent,
    title="Streaming Agent",
    description="The response appears progressively.",
)

demo.launch()
```

## Teaching point

Any Python function that uses `yield` becomes a streaming Gradio function. This is useful for:

- streamed LLM tokens;
- progress updates;
- long-running research tasks;
- showing stages of an agent workflow.

## Exercise

Stream this structure:

```text
Understanding your goal...
Choosing an approach...
Preparing the final response...

[final answer]
```

Do not present hidden model reasoning as if it were reliable internal logic. Instead, show useful user-facing status updates such as “Searching sources” or “Summarizing findings.”

---

# Chapter 6 — Add agent settings

A practical agent UI should expose only the controls users genuinely need.

Create `chapter_06_settings.py`:

```python
import gradio as gr

def configured_agent(message, history, style, use_web):
    tool_note = "Web research is enabled." if use_web else "Web research is disabled."

    return f"""### Agent response

**Style:** {style}  
**Tool status:** {tool_note}

You asked: {message}
"""

style = gr.Dropdown(
    choices=["Concise", "Detailed", "Executive summary"],
    value="Concise",
    label="Response style",
)

use_web = gr.Checkbox(
    label="Allow web research",
    value=False,
)

demo = gr.ChatInterface(
    fn=configured_agent,
    additional_inputs=[style, use_web],
    title="Configurable Agent",
)

demo.launch()
```

## Good settings to teach

- response style;
- model selection;
- maximum research sources;
- enable/disable a tool;
- output format: text, Markdown, JSON, table;
- approval requirement for actions.

## Design rule

Do not expose every model parameter to every user. Start with controls that affect a meaningful decision.

---

# Chapter 7 — Build a tool-using agent

An agent becomes more useful when it can choose and run tools. This example uses a safe calculator tool.

Create `chapter_07_tools.py`:

```python
import ast
import operator
import gradio as gr

OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
}

def safe_calculate(expression):
    def evaluate(node):
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return node.value

        if isinstance(node, ast.BinOp) and type(node.op) in OPERATORS:
            left = evaluate(node.left)
            right = evaluate(node.right)
            return OPERATORS[type(node.op)](left, right)

        raise ValueError("Only basic arithmetic is allowed.")

    tree = ast.parse(expression, mode="eval")
    return evaluate(tree.body)

def run_tool_agent(task):
    task_lower = task.lower()

    if task_lower.startswith("calculate "):
        expression = task[len("calculate "):]

        try:
            result = safe_calculate(expression)
            log = f"Tool call: calculator(expression='{expression}')"
            answer = f"The answer is **{result}**."
        except Exception as error:
            log = f"Tool call failed: calculator(expression='{expression}')"
            answer = f"I could not calculate that safely: {error}"

        return answer, log

    return (
        "I can currently use one tool. Start your request with `calculate`.",
        "No tool call was needed.",
    )

with gr.Blocks() as demo:
    gr.Markdown("# Tool-Using Agent")

    task = gr.Textbox(
        label="Task",
        placeholder="Example: calculate (18 * 7) + 4",
    )
    run = gr.Button("Run agent", variant="primary")

    answer = gr.Markdown(label="Final answer")
    tool_log = gr.Textbox(label="Tool activity", lines=4)

    run.click(
        fn=run_tool_agent,
        inputs=task,
        outputs=[answer, tool_log],
    )

demo.launch()
```

## Teaching point

Separate the agent’s user-facing answer from its observable tool activity.

```text
User request → Agent chooses tool → Tool runs → Result is shown → Agent responds
```

## Exercise

Add a second tool:

- `word_count(text)`;
- `convert_to_uppercase(text)`;
- a mock “company knowledge-base search” that returns items from a Python dictionary.

---

# Chapter 8 — Show agent activity and status

Users should be able to tell whether an agent is working, waiting for approval, or finished.

Create `chapter_08_observability.py`:

```python
import time
import gradio as gr

def research_agent(topic, progress=gr.Progress()):
    log = []

    progress(0.1, desc="Understanding the task")
    log.append("1. Received research request")
    yield "Working on it...", "\n".join(log)

    time.sleep(1)
    progress(0.5, desc="Collecting information")
    log.append("2. Collected initial information")
    yield "Gathering information...", "\n".join(log)

    time.sleep(1)
    progress(0.8, desc="Writing summary")
    log.append("3. Prepared summary")
    answer = f"""# Brief on {topic}

- Key idea one
- Key idea two
- Recommended next step: validate this with trusted sources
"""
    yield answer, "\n".join(log)

with gr.Blocks() as demo:
    gr.Markdown("# Observable Research Agent")

    topic = gr.Textbox(label="Research topic")
    run = gr.Button("Research", variant="primary")

    final_answer = gr.Markdown(label="Answer")
    activity_log = gr.Textbox(label="Activity log", lines=8)

    run.click(
        fn=research_agent,
        inputs=topic,
        outputs=[final_answer, activity_log],
    )

demo.launch()
```

## What to display

Good agent visibility includes:

- current status;
- tool name;
- source links or source titles;
- error messages;
- duration;
- whether user approval is required.

Avoid displaying sensitive keys, private user data, or raw hidden reasoning traces.

---

# Chapter 9 — Add human approval before an action

Many agent actions should not happen automatically. Examples include sending an email, modifying a record, purchasing something, or deleting a file.

Create `chapter_09_approval.py`:

```python
import gradio as gr

def prepare_action(recipient, message):
    return f"""## Proposed action

**Recipient:** {recipient}

**Message:**
{message}

Review the action, then choose Approve or Reject.
"""

def approve_action(recipient, message):
    # Replace this with a real email/API action only after approval.
    return f"Approved. The message would now be sent to {recipient}."

def reject_action():
    return "Rejected. No action was taken."

with gr.Blocks() as demo:
    gr.Markdown("# Human-in-the-Loop Agent")

    recipient = gr.Textbox(label="Recipient")
    message = gr.Textbox(label="Draft message", lines=5)

    preview = gr.Markdown()
    status = gr.Textbox(label="Status")

    with gr.Row():
        review = gr.Button("Preview action")
        approve = gr.Button("Approve", variant="primary")
        reject = gr.Button("Reject", variant="stop")

    review.click(
        fn=prepare_action,
        inputs=[recipient, message],
        outputs=preview,
    )

    approve.click(
        fn=approve_action,
        inputs=[recipient, message],
        outputs=status,
    )

    reject.click(
        fn=reject_action,
        outputs=status,
    )

demo.launch()
```

## Teaching point

For consequential actions:

1. show exactly what the agent proposes;
2. request explicit user approval;
3. execute only after approval;
4. return a clear confirmation or error.

---

# Chapter 10 — Work with uploaded files

Many useful agents need documents, spreadsheets, or images as input.

Create `chapter_10_files.py`:

```python
from pathlib import Path
import gradio as gr

def inspect_file(uploaded_file):
    if uploaded_file is None:
        return "Please upload a file."

    path = Path(uploaded_file)
    size_kb = path.stat().st_size / 1024

    return f"""## File received

- **Name:** `{path.name}`
- **Type:** `{path.suffix or "unknown"}`
- **Size:** {size_kb:.1f} KB

An agent could now extract text, analyze data, or summarize this file.
"""

with gr.Blocks() as demo:
    gr.Markdown("# File-Aware Agent")

    file_input = gr.File(label="Upload a document or data file")
    inspect = gr.Button("Inspect file", variant="primary")
    result = gr.Markdown()

    inspect.click(
        fn=inspect_file,
        inputs=file_input,
        outputs=result,
    )

demo.launch()
```

## Exercise

Extend this to build one of these agents:

- PDF summary agent;
- CSV analysis agent;
- image-description agent;
- meeting-notes action-item extractor.

## Security checklist

- Validate file type and size.
- Store uploads only as long as necessary.
- Do not allow uploaded content to override system instructions.
- Treat document text as untrusted input.

---

# Chapter 11 — Keep session state

`gr.State` stores temporary data for one user session. This is useful for a task list, selected sources, or an agent plan.

Create `chapter_11_state.py`:

```python
import gradio as gr

def add_task(task, tasks):
    tasks = tasks or []

    if task.strip():
        tasks.append(task.strip())

    display = "\n".join(
        f"{index + 1}. {item}"
        for index, item in enumerate(tasks)
    )

    return tasks, display or "No tasks yet.", ""

with gr.Blocks() as demo:
    gr.Markdown("# Agent Task Memory")

    task_state = gr.State([])

    task_input = gr.Textbox(
        label="New task",
        placeholder="Example: Compare two LLM providers",
    )
    add_button = gr.Button("Add task", variant="primary")
    task_list = gr.Markdown("No tasks yet.")

    add_button.click(
        fn=add_task,
        inputs=[task_input, task_state],
        outputs=[task_state, task_list, task_input],
    )

demo.launch()
```

## Teaching point

Use session state for temporary, per-user information. For long-term memory, use a database or a dedicated storage layer with proper access controls.

---

# Chapter 12 — Capstone: a simple research agent UI

This capstone combines user input, agent settings, progress updates, tool activity, and human-readable output.

Create `capstone_research_agent.py`:

```python
import time
import gradio as gr

def research_agent(question, depth, progress=gr.Progress()):
    activity = []

    progress(0.1, desc="Understanding the question")
    activity.append("Received question")
    yield "Starting research...", "\n".join(activity)

    time.sleep(1)
    progress(0.4, desc="Planning research")
    activity.append(f"Selected research depth: {depth}")
    yield "Planning the research approach...", "\n".join(activity)

    time.sleep(1)
    progress(0.7, desc="Reviewing findings")
    activity.append("Reviewed available information")
    yield "Synthesizing findings...", "\n".join(activity)

    time.sleep(1)
    progress(1.0, desc="Complete")
    activity.append("Created final response")

    answer = f"""# Research brief

## Question

{question}

## Summary

This demo shows the structure of a research agent. In a production version, the agent would use approved search or knowledge-base tools, cite its sources, and distinguish verified facts from inference.

## Recommended next step

Validate key claims with primary sources before making a decision.
"""

    yield answer, "\n".join(activity)

with gr.Blocks(title="Research Agent") as demo:
    gr.Markdown("# Research Agent")
    gr.Markdown("Ask a question and observe the agent workflow.")

    question = gr.Textbox(
        label="Research question",
        placeholder="Example: What should a small company consider before adopting AI agents?",
        lines=3,
    )

    depth = gr.Radio(
        choices=["Quick", "Standard", "Deep"],
        value="Standard",
        label="Research depth",
    )

    run = gr.Button("Run research", variant="primary")

    with gr.Row():
        with gr.Column(scale=2):
            answer = gr.Markdown(label="Research brief")
        with gr.Column(scale=1):
            activity = gr.Textbox(
                label="Agent activity",
                lines=14,
            )

    run.click(
        fn=research_agent,
        inputs=[question, depth],
        outputs=[answer, activity],
    )

demo.launch()
```

---

# Final teaching project ideas

1. **Research agent**  
   Accepts a question, searches approved sources, shows citations, and generates a brief.

2. **Document Q&A agent**  
   Accepts PDFs or DOCX files, extracts content, and answers questions with page references.

3. **Data analyst agent**  
   Accepts a CSV, produces a summary, creates charts, and explains findings.

4. **Support agent**  
   Uses a knowledge base, drafts answers, and escalates uncertain cases to a human.

5. **Multi-agent coordinator**  
   Delegates work to “research,” “writer,” and “reviewer” roles, then presents a combined result.

---

# Recommended course flow

| Session | Topic | Student outcome |
|---|---|---|
| 1 | Gradio basics | Build a simple browser UI |
| 2 | Blocks and layouts | Build an agent control panel |
| 3 | Chat interfaces | Create a conversational agent |
| 4 | LLM integration | Connect an LLM safely |
| 5 | Streaming | Make long-running work feel responsive |
| 6 | Tools | Show agent tool usage |
| 7 | Observability | Display progress and tool logs |
| 8 | Approval flows | Add safe human oversight |
| 9 | Files and state | Build file-aware, session-aware apps |
| 10 | Capstone | Deliver a polished agent UI |

## Key takeaway

Gradio is not the agent itself. It is the interaction layer that helps users configure, inspect, trust, and safely use an agent.

For current component and chat-interface details, refer to the official [Gradio ChatInterface documentation](https://www.gradio.app/docs/gradio/chatinterface) and [Gradio State documentation](https://www.gradio.app/docs/gradio/state).