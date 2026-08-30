import asyncio
from openai import AsyncOpenAI
from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled
from agents.mcp import MCPServerStreamableHttp

open_ai_client = AsyncOpenAI(
    api_key="your_openrouter_api_key", 
    base_url="http://localhost:1234/v1"  # Retargeting local workstations if needed
)
chat_model = OpenAIChatCompletionsModel(
    model="qwen2.5-0.5b-instruct-mlx",
    openai_client=open_ai_client
)

set_tracing_disabled(True)

async def main():
    # Connect directly to your streaming HTTP MCP Server
    async with MCPServerStreamableHttp(
        name="Math MCP server",
        params={"url": "http://127.0.0.1:8000/mcp"},
        cache_tools_list=True,
    ) as mcp_server:
        
        print("====================================================")
        print("DEMO 1: Programmatic Consumption of MCP Resources")
        print("====================================================")
        # 1. Fetch read-only structured data natively using its URI identifier string
        resource_payload = await mcp_server.read_resource("employee://info")
        print(f"[Client Log] Read Resource Data from Server:\n{resource_payload}")
        
        # 2. Supply the retrieved source directly into an Agent context layer
        resource_assistant = Agent(
            name="Resource Query Agent",
            instructions=(
                f"You are a management supervisor. Use the following dynamic data "
                f"to answer user questions: {resource_payload}. "
                f"Print answers in plain text without Markdown syntax."
            ),
            model=chat_model
        )

        hr_query = "What is Ravi's designation?"
        print(f"\n[Run] Asking Agent: '{hr_query}'")
        hr_result = await Runner.run(resource_assistant, hr_query)
        print(f"[Output]: {hr_result.final_output}\n")
        
        print("====================================================")
        print("DEMO 2: Dynamic Persona Generation via MCP Prompts")
        print("====================================================")
        # 1. Pull down the reusable prompt template object registered on the server
        prompt_result = await mcp_server.get_prompt("list_file_prompt")
        
        # FIX: Unpack the text content from the first message object in GetPromptResult
        prompt_instructions = prompt_result.messages[0].content.text
        print(f"[Client Log] Unpacked Prompt Instructions:\n\"{prompt_instructions}\"")
        
        # 2. Instantiate your downstream Agent utilizing the raw instruction string
        prompt_driven_agent = Agent(
            name="Template Agent",
            instructions=prompt_instructions,
            model=chat_model
        )
        
        user_intent = "Explain what files you are currently scanning."
        print(f"\n[Run] Asking Agent: '{user_intent}'")
        prompt_result = await Runner.run(prompt_driven_agent, user_intent)
        print(f"[Output]: {prompt_result.final_output}\n")

        print("====================================================")
        print("DEMO 3: Executing Server-Side Tools via Agent Loops")
        print("====================================================")
        # 1. Provide the connected mcp_server object directly inside the agent configuration array.
        weather_agent = Agent(
            name="Weather Operations Agent",
            instructions=(
                "You are an expert meteorological assistant. If a user asks about the weather "
                "in a specific city, you MUST call the matching weather tool parameter. "
                "Provide a short plain text breakdown of the conditions returned."
            ),
            model=chat_model,
            mcp_servers=[mcp_server]  # Registers server tools to the model context loop
        )

        math_agent = Agent(
            name="Calculator Agent",
            instructions=(
                "You are math teacher, so the given tool to answer by questions"
                "If user give two number always choose bigger number as first parameter to the tool and smaller number as second parameter"
            ),
            model=chat_model,
            mcp_servers=[mcp_server]
        )

        # 2. Execute an API tool call loop request
        weather_query = "What is the current temperature in Bangalore?"
        print(f"[Run] Asking Agent: '{weather_query}'")
        weather_result = await Runner.run(weather_agent, weather_query)
        print(f"[Output]: {weather_result.final_output}\n")

        # 3. Execute an arithmetic calculation tool call request
        math_query = "What is difference between 40 and 60? always consider bigger number minus smaller number"
        print(f"[Run] Asking Agent: '{math_query}'")
        math_result = await Runner.run(math_agent, math_query)
        print(f"[Output]: {math_result.final_output}")

if __name__ == "__main__":
    asyncio.run(main())