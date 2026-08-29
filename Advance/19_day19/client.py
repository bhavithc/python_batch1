import asyncio

# from mcp import Client
import mcp

async def main() -> None:
    async with mcp.Client("http://127.0.0.1:8080/mcp") as client:
        # list_tool_results = await client.list_tools()
        # for tool in list_tool_results.tools:
        #     print(tool.name)

        # result  = await client.call_tool("add", {"a": 10, "b": 30})
        # print(result.structured_content['result'])

        print(await client.list_resources())
        print(await client.read_resource("employee://info"))

        print(await client.list_prompts())
        list_file_prompt = await client.get_prompt("list_file_prompt")
        print(list_file_prompt.messages[0].content.text)


asyncio.run(main())
