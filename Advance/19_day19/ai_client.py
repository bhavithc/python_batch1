import asyncio
import creds
import sys
from pathlib import Path

from openai import AsyncOpenAI
from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled
from agents.mcp import MCPServerStdio, MCPServerSse, MCPServerStreamableHttp


creds = creds.Creds()

open_ai_client = AsyncOpenAI(api_key=creds.api_key, base_url=creds.base_url)

chat_model = OpenAIChatCompletionsModel(model=creds.model_name,
                                        openai_client=open_ai_client)

set_tracing_disabled(True)

async def main():
    async with MCPServerStreamableHttp(
        name="Math MCP server",
        params={"url": "http://127.0.0.1:8000/mcp"},
        cache_tools_list=True,
    ) as mcp_server:
        math_agent = Agent(
            name="math agent",
            instructions=(
                "You are a math teacher. Use the calculator tools when needed. "
                "Print results in plain text, not Markdown."
            ),
            model=chat_model,
            mcp_servers=[mcp_server],
        )
        weather_agent = Agent(
                    name="weather agent",
                    instructions=(
                        "You are a weather agent, I provide a city name, you let me know the weather information"
                    ),
                    model=chat_model,
                    mcp_servers=[mcp_server],
                )

        result = await Runner.run(weather_agent, "What is current temperature in Bangalore?")
        print(result.final_output)
if __name__ == "__main__":
    asyncio.run(main())