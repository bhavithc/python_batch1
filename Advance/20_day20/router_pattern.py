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

router_agent = Agent(
    name="Language Classifier",
    instructions="Classify the incoming programming query. Respond with exactly one token: 'python' or 'cpp'.",
    model=chat_model
)

python_specialist = Agent(
    name="Python Guru",
    instructions="You are an expert Python developer. Resolve this task using clean PEP8 compliant code syntax.",
    model=chat_model
)

cpp_specialist = Agent(
    name="C++ Core Engineer",
    instructions="You are a performance systems engineer. Resolve this using Modern C++ guidelines without allocations.",
    model=chat_model
)

async def route_and_execute(user_query: str):
    # Route step
    route_decision = await Runner.run(router_agent, user_query)
    chosen_path = route_decision.final_output.strip().lower()
    print(f"\nRouter Decision: {chosen_path}")
    
    # Dynamic execution path selection
    if "python" in chosen_path:
        print("Python specialist is choosen")
        result = await Runner.run(python_specialist, user_query)
    elif "cpp" in chosen_path:
        print("C++ specialist is choosen")
        result = await Runner.run(cpp_specialist, user_query)
    else:
        return "Routing error: unknown path layout execution requested."
        
    return result.final_output
async def main():
    q1 = "How do I implement custom malloc using c++"
    q2 = "Write a AI agent using open AI python SDK"

    print(await route_and_execute(q1))
    print(await route_and_execute(q2))
if __name__ == "__main__":
    asyncio.run(main())