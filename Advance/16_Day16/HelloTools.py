import asyncio
import creds

from openai import AsyncOpenAI
from agents import Agent, Runner, function_tool, OpenAIChatCompletionsModel
import subprocess

creds = creds.Creds()

@function_tool
def ls_la_tool():
    """List all the files in my current directory
    """
    print("executing ls -la command ....")
    result = subprocess.run(["ls", "-la"], capture_output=True, text=True, check=True)
    return result.stdout

@function_tool
def system_info():
    """Provides the system information
    """
    print("executing uname -a command ....")
    result = subprocess.run(["uname", "-a"], capture_output=True, text=True, check=True)
    return result.stdout

@function_tool
def open_music():
    """Open the Apple Music application
    """
    print("Opening music app ....")
    result = subprocess.run(["open", "-a", "Music"], capture_output=True, text=True, check=True)
    return result.stdout

openai =  AsyncOpenAI(api_key=creds.api_key, base_url=creds.base_url)

chat_model = OpenAIChatCompletionsModel(openai_client=openai, model=creds.model_name)

computer_agent = Agent(name= "Computer agent",
    instructions="There are multiple tools available for you to work with my computer"
                    " use when ever it is required, if you don't get any tool say I don't know how to complete this job",
    model=chat_model,
    tools=[ls_la_tool, system_info, open_music])

async def main():
    result = await Runner.run(computer_agent, 
                              "Can you play a song? if my question does not related to any of the tool which I provided jsut you say get lost and go to hell")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
    # result = ls_la_tool()
    # print(result)
