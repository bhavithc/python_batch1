import asyncio
import sys
from pathlib import Path

import creds

from openai import AsyncOpenAI
from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled
from agents.mcp import MCPServerStdio


credentials = creds.Creds()

open_ai_client = AsyncOpenAI(
    api_key=credentials.api_key,
    base_url=credentials.base_url,
)

chat_model = OpenAIChatCompletionsModel(
    model=credentials.model_name,
    openai_client=open_ai_client,
)

set_tracing_disabled(True)

async def main():
    server_file = Path(__file__).with_name("server2.py")

    async with MCPServerStdio(
        name="Campus MCP Server",
        params={
            "command": sys.executable,
            "args": [str(server_file)],
        },
        cache_tools_list=True,
    ) as campus_server:

        campus_agent = Agent(
            name="Campus Assistant",
            instructions=(
                "You are a helpful campus assistant. "
                "Use the Campus MCP tools whenever the user asks about campus hours. "
                "Answer only from the tool result. "
                "Do not respond in Markdown."
            ),
            model=chat_model,
            mcp_servers=[campus_server],
        )

        result = await Runner.run(
            campus_agent,
            "What are the campus hours on Sunday?",
        )

        print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())