import asyncio

from mcp import Client, CallToolRequest


async def main() -> None:
    async with Client("http://localhost:8000/mcp") as client:
        # print(await client.list_tools())
        resource = await client.read_resource("greeting://bhavith")
        
        print(resource.contents[0].text)
        result = await client.call_tool("add", {"a": 1, "b": 2})
        print(result.structured_content)  # {'result': 3}
        call_tool_result = await client.call_tool("weather", {"city": "mysore"})
        print(call_tool_result.content[0])


asyncio.run(main())

