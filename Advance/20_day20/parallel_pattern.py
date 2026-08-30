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

# Specialist Workers
security_expert = Agent(
    name="Security Analyst",
    instructions="Analyze the given system idea for potential security vulnerabilities. Be brief and concise.",
    model=chat_model
)
cloud_expert = Agent(
    name="Cloud Infrastructure Architect",
    instructions="Provide a targeted AWS infrastructure roadmap for the given system idea. Be brief.",
    model=chat_model
)

# Synthesizing Aggregator
aggregator_agent = Agent(
    name="Technical Coordinator",
    instructions="You are given a security review and a cloud layout. Synthesize them into an executive summary.",
    model=chat_model
)

async def main():
    #target_idea = "A real-time ride-sharing application using peer-to-peer data links."
    target_idea = "A real-time movie booking application"
    
    print("--- Running Concurrent Parallel Analysis ---")
    # Fan-out: Execute concurrent tasks using asyncio.gather
    security_task = Runner.run(security_expert, target_idea)
    cloud_task = Runner.run(cloud_expert, target_idea)
    
    security_res, cloud_res = await asyncio.gather(security_task, cloud_task)
    
    # Fan-in: Concat context for unified aggregation
    combined_context = f"Security Analysis:\n{security_res.final_output}\n\nCloud Layout:\n{cloud_res.final_output}"

    print("--- Merging Coordinated Results ---")
    final_summary = await Runner.run(aggregator_agent, combined_context)
    print(final_summary.final_output)
if __name__ == "__main__":
    asyncio.run(main())