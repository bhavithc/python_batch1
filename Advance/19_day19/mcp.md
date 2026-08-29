# Teaching MCP with Python and the OpenAI SDK

## Goal of this class

By the end, students will be able to:

1. Explain the roles of an MCP server and client.
2. Build a local MCP server in Python that exposes a tool.
3. Build a Python MCP client that discovers and calls that tool.
4. Use the OpenAI Python SDK to turn a tool result into a natural-language answer.
5. Describe how a deployed HTTPS MCP server can be given directly to the OpenAI Responses API.

## 1. The idea in one minute

**MCP (Model Context Protocol)** is a standard way for an AI application to discover and use external capabilities. Think of it as a common plug socket for AI tools.

| Part | Responsibility | Example in this lesson |
| --- | --- | --- |
| MCP server | Publishes capabilities such as tools, resources, and prompts | `campus_hours` tool |
| MCP client | Connects, discovers capabilities, and invokes them | `client.py` |
| OpenAI SDK | Calls an OpenAI model through the Responses API | Explains the tool result naturally |

Flow for the local demo:

```text
Student program → MCP client → local MCP server → tool result
                                      ↓
                                OpenAI SDK/model
                                      ↓
                                friendly answer
```

### Key vocabulary

- **Tool**: a named operation the server offers; for example, `campus_hours(day)`.
- **Schema**: the structured description of tool inputs. Python type hints help generate it.
- **Transport**: how client and server communicate. We use **stdio** locally: the client starts the server and exchanges messages over standard input/output.
- **Streamable HTTP**: the usual transport for a deployed, remote MCP server.

## 2. Prerequisites

- Python 3.10+
- An OpenAI API key for the AI-summary portion

Create a folder and virtual environment:

```bash
mkdir mcp-class-demo && cd mcp-class-demo
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\\Scripts\\activate
pip install "mcp[cli]" openai python-dotenv
```

Create a file named `.env` (do not commit it):

```env
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-5
```

## 3. Build the MCP server

Create `server.py`:

```python
from mcp.server import MCPServer

mcp = MCPServer("Campus information")

CAMPUS_HOURS = {
    "monday": "08:00–20:00",
    "tuesday": "08:00–20:00",
    "wednesday": "08:00–20:00",
    "thursday": "08:00–20:00",
    "friday": "08:00–18:00",
    "saturday": "10:00–14:00",
    "sunday": "Closed",
}


@mcp.tool()
def campus_hours(day: str) -> str:
    """Return public campus opening hours for a day of the week."""
    normalized_day = day.strip().lower()
    hours = CAMPUS_HOURS.get(normalized_day)

    if hours is None:
        return "Unknown day. Please use a day such as Monday or Tuesday."

    return f"Campus hours on {normalized_day.title()}: {hours}"


@mcp.resource("campus://visitor-guide")
def visitor_guide() -> str:
    """Read the public visitor guide for the campus."""
    return """# Campus visitor guide

- Check in at the reception desk.
- Visitors need a photo ID.
- The library is on the second floor.
"""


@mcp.resource("campus://room/{room_number}")
def room_information(room_number: str) -> str:
    """Read public information about a campus room."""
    rooms = {
        "101": "Room 101: Introductory Programming Lab, 30 seats.",
        "202": "Room 202: Student Help Desk, open weekdays.",
    }
    return rooms.get(room_number, f"No public information for room {room_number}.")


@mcp.prompt()
def campus_visit_plan(visitor_type: str = "prospective student") -> str:
    """Create a helpful plan for a campus visit."""
    return f"""You are a friendly campus guide.

Create a short visit plan for a {visitor_type}. Include arrival, check-in,
and three useful locations to visit. Be accurate, practical, and welcoming.
"""


if __name__ == "__main__":
    # Used when a local stdio client starts this file as a subprocess.
    mcp.run(transport="stdio")

```

> **Version note:** these notes use MCP Python SDK **v2**, the current stable release. `FastMCP` was renamed to `MCPServer`. If you see `No module named 'mcp.server.fastmcp'`, change the import exactly as shown above; do not mix v1 code with an unpinned v2 installation.

### What the server code does

- `MCPServer(...)` creates an MCP server.
- `@mcp.tool()` publishes the function to MCP clients.
- The function name becomes the tool name: `campus_hours`.
- The docstring becomes useful tool documentation for a client/model.
- `day: str` tells clients the argument is text.
- `stdio` means **do not add ordinary `print()` statements** to this program; stdout carries protocol messages.

### Tools vs. resources vs. prompts

| MCP primitive | Who normally chooses it? | Use it for | Example here |
| --- | --- | --- | --- |
| **Tool** | The model/client | An action or computed lookup with inputs | `campus_hours(day)` |
| **Resource** | The application/user | Read-only context addressed by a URI | `campus://visitor-guide` |
| **Prompt** | The user | A reusable conversation template | `campus_visit_plan(visitor_type)` |

The distinction matters. A tool is an operation the model may decide to invoke. A resource is information to read. A prompt is a user-selected template—like a well-designed slash command—not a tool the model silently chooses.

### Resource examples explained

- `campus://visitor-guide` is a fixed resource: it always represents one piece of information.
- `campus://room/{room_number}` is a **resource template**. The client fills in the URI variable, such as `campus://room/101`, before reading it.
- Resources should generally be read-only. Do not expose private files or student data simply because a client can read resources.

### Prompt example explained

`@mcp.prompt()` registers a reusable message template. Its docstring is shown as the prompt description, and function parameters become fields the user can fill in. Because `visitor_type` has a default, it is optional.

## 4. Build a plain MCP client

Create `client.py`:

```python
import asyncio

from mcp import Client, StdioServerParameters


async def main() -> None:
    server = StdioServerParameters(
        command="python3",
        args=["server.py"],
    )

    async with Client(server) as client:
        available_tools = await client.list_tools()
        print("Available tools:", [tool.name for tool in available_tools.tools])

        result = await client.call_tool(
            "campus_hours",
            {"day": "Friday"},
        )

        for item in result.content:
            if item.type == "text":
                print(item.text)


if __name__ == "__main__":
    asyncio.run(main())
```

Run it:

```bash
python client.py
```

Expected result:

```text
Available tools: ['campus_hours']
Campus hours on Friday: 08:00–18:00
```

## 4a. Discover and use a resource and prompt

Add the following calls inside the same `Client` block in `client.py`, after the tool example:

```python
        resources = await client.list_resources()
        print("Resources:", [resource.uri for resource in resources.resources])

        guide = await client.read_resource("campus://visitor-guide")
        print("Visitor guide:", guide.contents[0].text)

        templates = await client.list_resource_templates()
        print("Resource templates:", [item.uri_template for item in templates.resource_templates])

        room = await client.read_resource("campus://room/101")
        print("Room information:", room.contents[0].text)

        prompts = await client.list_prompts()
        print("Prompts:", [prompt.name for prompt in prompts.prompts])

        rendered_prompt = await client.get_prompt(
            "campus_visit_plan",
            {"visitor_type": "parent"},
        )
        print("Rendered prompt:", rendered_prompt.messages[0].content.text)
```

Expected output will include the fixed resource URI and prompt name, then the visitor-guide text, room information, and a rendered campus-visit instruction. A host application would typically insert the rendered prompt message into its chat conversation rather than print it.

### The request lifecycle

1. The client starts `server.py` as a subprocess.
2. Entering `async with Client(...)` connects and agrees on protocol capabilities.
3. `list_tools()` lets the client discover `campus_hours`; `call_tool()` runs it with JSON-like arguments.
4. `list_resources()` and `read_resource()` discover and load read-only context.
5. `list_prompts()` and `get_prompt()` discover and render user-selected templates.
6. The server returns structured content or rendered messages.

## 5. Add the OpenAI Python SDK

The next script still calls the local MCP tool explicitly, then gives its result to an OpenAI model to compose a helpful answer. This split is excellent for a first lesson because students can see exactly when the external tool runs.

Create `ai_client.py`:

```python
import asyncio
import os

from dotenv import load_dotenv
from mcp import Client, StdioServerParameters
from openai import OpenAI

load_dotenv()


async def get_campus_hours(day: str) -> str:
    server = StdioServerParameters(command="python3", args=["server.py"])

    async with Client(server) as client:
        result = await client.call_tool("campus_hours", {"day": day})
        return "\n".join(
            item.text for item in result.content if item.type == "text"
        )


async def main() -> None:
    day = "Saturday"
    tool_result = await get_campus_hours(day)

    openai_client = OpenAI()
    response = openai_client.responses.create(
        model=os.getenv("OPENAI_MODEL", "gpt-5"),
        input=(
            "Answer the student's question using only the verified campus tool result. "
            "Be concise and friendly.\n\n"
            f"Question: Is campus open on {day}?\n"
            f"Verified tool result: {tool_result}"
        ),
    )

    print(response.output_text)


if __name__ == "__main__":
    asyncio.run(main())
```

Run it:

```bash
python ai_client.py
```

The official OpenAI Python SDK reads `OPENAI_API_KEY` from the environment. `responses.create(...)` returns a response, and `response.output_text` is the SDK convenience property for its aggregated text output.

## 6. Let the Responses API use a *remote* MCP server

The previous example uses a local `stdio` server. For the OpenAI Responses API to call MCP tools directly, deploy the server behind a public HTTPS MCP endpoint (normally using Streamable HTTP). Then configure it as an MCP tool:

```python
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-5",
    input="What time does the campus open on Monday?",
    tools=[
        {
            "type": "mcp",
            "server_label": "campus",
            "server_url": "https://your-domain.example/mcp",
            # Use "never" only for a well-understood, read-only tool.
            "require_approval": "never",
        }
    ],
)

print(response.output_text)
```

Important: use approval for tools that can change data, spend money, send messages, or expose sensitive information. The `never` setting is only suitable for a controlled read-only class example. A remote server is a third-party data recipient, so do not send secrets or student records unless your security and privacy design explicitly permits it.

## 7. Common mistakes and fixes

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| Client hangs or protocol errors | Server wrote debug output to stdout | Remove `print()` from the stdio server; log to stderr instead. |
| `ModuleNotFoundError` | Virtual environment is not active or dependencies are missing | Activate `.venv` and reinstall packages. |
| `No module named mcp.server.fastmcp` | You installed MCP SDK v2 but are running v1 code | Use `from mcp.server import MCPServer`, or deliberately pin `mcp<2`. |
| Tool is not listed | Decorator or initialization was omitted | Check `@mcp.tool()` and `await session.initialize()`. |
| OpenAI authentication error | API key is missing/invalid | Set `OPENAI_API_KEY` in the environment or `.env`. |
| Model cannot reach local server | API-hosted tool execution cannot access your laptop's stdio process | Use the local MCP client pattern, or deploy a public HTTPS MCP endpoint. |

## 8. Teaching prompts and exercises

1. Add a `library_status()` tool that returns “open” or “closed.”
2. Create a `campus://map` resource containing a small Markdown map.
3. Create a `study_plan(subject, level="beginner")` prompt for a student to select.
4. Add validation so `campus_hours()` accepts common abbreviations such as `Mon`.
5. Ask students which tool operations should require approval and why.
6. Have students write three unit tests for `campus_hours()` before exposing it as a tool.

## 9. Takeaways

- MCP separates a useful capability (the server) from the app or model that uses it (the client).
- Start local with `stdio`; deploy with authenticated HTTPS only when needed.
- Keep tools narrow, validate inputs, and return clear results.
- Treat every tool call as a security boundary: least privilege, explicit approval for actions, and no unnecessary sensitive data.

## Further reading

- [OpenAI Developer quickstart](https://platform.openai.com/docs/quickstart/make-your-first-api-request) — installation, environment variables, and the Responses API.
- [OpenAI Responses API reference](https://platform.openai.com/docs/api-reference/responses) — tool configuration, including remote MCP tools and approval settings.
- [Official MCP Python SDK](https://py.sdk.modelcontextprotocol.io/) — current Python SDK overview and examples for tools, resources, and prompts.
- [Official MCP v1 → v2 migration guide](https://py.sdk.modelcontextprotocol.io/migration/) — `FastMCP` rename and other v2 changes.
- [Official MCP prompt guide](https://py.sdk.modelcontextprotocol.io/servers/prompts/) — prompt behavior and argument handling.
