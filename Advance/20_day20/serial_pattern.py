import asyncio
from openai import AsyncOpenAI
from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled

set_tracing_disabled(True)

# Client configuration pointing to OpenRouter
open_ai_client = AsyncOpenAI(
    api_key="your_openrouter_api_key", 
    base_url="http://localhost:1234/v1"
)
chat_model = OpenAIChatCompletionsModel(
    model="llama-3.2-1b-instruct",
    openai_client=open_ai_client
)
# Step 1 Agent: Focuses solely on core structural layout
architect_agent = Agent(
    name="System Architect",
    instructions="You are a software architect. Given a requirement, output ONLY a flat list of microservices needed. Do not write markdown, code blocks, or introductions.",
    model=chat_model
)

# Step 2 Agent: Uses the previous architectural list to draft specific interfaces
api_designer_agent = Agent(
    name="API Designer",
    instructions="You take a list of microservices and write gRPC proto3 definitions for them. Output valid protobuf syntax only.",
    model=chat_model
)

async def main():
    user_requirement = "Build an e-commerce platform with a shopping cart, payment processing, and inventory tracking."
    
    print("--- Executing Step 1: Architecting Services ---")
    step1_result = await Runner.run(architect_agent, user_requirement)
    services_list = step1_result.final_output
    print(services_list)
    
    print("\n--- Executing Step 2: Generating gRPC Interfaces ---")
    # Clean pipeline handoff: Pass output directly as next input context
    step2_result = await Runner.run(api_designer_agent, services_list)
    print(step2_result.final_output)
if __name__ == "__main__":
    asyncio.run(main())