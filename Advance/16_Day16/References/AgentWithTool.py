import asyncio

from openai import AsyncOpenAI
from agents import Agent, Runner, function_tool, OpenAIChatCompletionsModel, set_tracing_disabled
from Creds import Creds
import subprocess

cred = Creds()

openai = AsyncOpenAI(api_key=cred.api_key, base_url=cred.base_url)

model = OpenAIChatCompletionsModel(openai_client= openai, model=cred.model_name)

set_tracing_disabled(True)

@function_tool
def speak(text: str):
    """Speak the given text"""
    print(f"I am singing... {text}")
    result = subprocess.run(["say", text], capture_output=True, text=True, check=True)
    return result.stdout

@function_tool
def ls_la_tool():
    """List all files in current dir"""
    print("Listing all current dir entries..")
    result = subprocess.run(["ls", "-la"], capture_output=True, text=True, check=True)
    return result.stdout

@function_tool
def print_hello():
    """Print hello on console"""
    return "Hello Bhavith"

@function_tool
def check_info():
    """System info"""
    print("Checking uname...")
    result = subprocess.run(["uname", "-a"], capture_output=True, text=True, check=True)
    return result.stdout


computer_agent = Agent(name = "Computer", 
      instructions=("Use the available tools when appropriate. "
                    "If no available tool can answer, say you don't know."),
      model=model,
      tools=[ls_la_tool, print_hello, check_info, speak]
    )

async def main():
    result = await Runner.run(
        computer_agent, 
        ("Can you say simple two line poem?"
         " Print your poem before you speak"
          " you can use speak tool to say using computer speaker"))
    print(result.final_output)


if __name__ == "__main__":
    # ls_la_tool()
    asyncio.run(main())
    # check_info()
