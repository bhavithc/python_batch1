import asyncio
from openai import AsyncOpenAI
from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled

set_tracing_disabled(True)

# 1. Point client directly to your local workstation port
local_lm_studio_client = AsyncOpenAI(
    api_key="lm-studio-dummy-key",         # LM Studio bypasses authentication checks
    base_url="http://localhost:1234/v1"     # Default local instance server port endpoint
)
# 2. Initialize the wrapper layer
# The 'model' parameter can be set to any identifier string; 
# LM Studio automatically uses whatever model is currently loaded in the active UI memory.
local_chat_model = OpenAIChatCompletionsModel(
    model="llama-3.2-1b-instruct", 
    openai_client=local_lm_studio_client
)
# 3. Instantiate agents normally
local_math_agent = Agent(
    name="Math tutor",
    instructions="You are a precise mathematics teacher. Output answers cleanly without markdown.",
    model=local_chat_model
)
async def main():
    print("Executing query on local workstation inference engine...")
    result = await Runner.run(local_math_agent, "What is 45 plus 55?")
    print(f"Result: {result.final_output}")
if __name__ == "__main__":
    asyncio.run(main())