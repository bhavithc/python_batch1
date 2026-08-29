# pip install --upgrade openai-agents "mcp[cli]" openai
from mcp.server import MCPServer

mcp = MCPServer("resource server")

# @log
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    print("Add tool is been invoked !")
    # logging.debug(f"Add tool is been invoked !")
    return a + b

# @log
@mcp.tool()
def sub(a: int, b: int) -> int:
    """Sub two numbers."""
    # logging.debug(f"Sub tool is been invoked !")
    return a - b


@mcp.resource("employee://info")
def employee_info() -> str:
    """Reading employee infos"""
    print("invoked")
    return """
    name: Dilip, designation: senior engineer,
    name: Ravi, designation: senior devopsengineer
"""

@mcp.prompt()
def list_file_prompt() -> str:
    """List the files prompt"""
    return """You are a list agent and you can return list of the files present in the given directory"""

if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="127.0.0.1", port=8080)
    # mcp.run(transport="stdio")
