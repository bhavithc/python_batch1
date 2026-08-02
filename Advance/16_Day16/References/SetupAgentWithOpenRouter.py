import asyncio
import Creds

from openai import AsyncOpenAI
from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled


creds = Creds.Creds()

client = AsyncOpenAI(
    api_key= creds.api_key,
    base_url= creds.base_url
)

model = OpenAIChatCompletionsModel (
    model=creds.model_name,
    openai_client=client)

agent = Agent(
    name="History tutor",
    instructions="You answer history questions clearly and concisely.",
    model=model
)

async def main() -> None:
    result = await Runner.run(agent, "what is 100 + 200 ?")
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())

