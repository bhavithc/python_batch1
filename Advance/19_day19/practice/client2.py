import asyncio

from mcp import Client, StdioServerParameters


async def main() -> None:
    server = StdioServerParameters(
        command="python3",
        args=["server2.py"],
    )

    async with Client(server) as client:
        available_tools = await client.list_tools()
        print("Available tools:", [tool.name for tool in available_tools.tools])

        result = await client.call_tool(
            "campus_hours",
            {"day": "Friday"},
        )

        for item in result.content:
            if item.type == "text":
                print(item.text)

        # start 
        resources = await client.list_resources()
        print("Resources:", [resource.uri for resource in resources.resources])

        guide = await client.read_resource("campus://visitor-guide")
        print("Visitor guide:", guide.contents[0].text)

        templates = await client.list_resource_templates()
        print("Resource templates:", [item.uri_template for item in templates.resource_templates])

        room = await client.read_resource("campus://room/101")
        print("Room information:", room.contents[0].text)

        prompts = await client.list_prompts()
        print("Prompts:", [prompt.name for prompt in prompts.prompts])

        rendered_prompt = await client.get_prompt(
            "campus_visit_plan",
            {"visitor_type": "parent"},
        )
        print("Rendered prompt:", rendered_prompt.messages[0].content.text)
        #end 


if __name__ == "__main__":
    asyncio.run(main())



