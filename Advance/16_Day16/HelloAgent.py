import asyncio
import creds

from openai import AsyncOpenAI
from agents import Agent, Runner, OpenAIChatCompletionsModel


creds = creds.Creds()

open_ai_client = AsyncOpenAI(api_key=creds.api_key, base_url=creds.base_url)

chat_model = OpenAIChatCompletionsModel(
    model=creds.model_name,
    openai_client=open_ai_client)

math_agent = Agent(name="Math tutor",
      instructions="You are a math teacher you can do math, Don't respond in markdown format "
                    " If user ask anything apart from math question, say \"get lost !\"",
      model=chat_model)

async def main():
    print("main")
    result = await Runner.run(math_agent, 
                              "I have two apples and I gave one to Dilip, what is the color of apple which I gave?")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
