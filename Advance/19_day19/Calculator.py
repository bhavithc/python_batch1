# pip install --upgrade openai-agents "mcp[cli]" openai
from mcp.server import MCPServer
import logging
from functools import wraps
import httpx

mcp = MCPServer("calculator-server")

logging.basicConfig(
    filename = "server.log",
    level = logging.DEBUG,
    format = "%(asctime)s %(levelname)s %(threadName)s %(taskName)s :%(name)s:%(message)s"
)


def log(fun):
    @wraps(fun)
    def wrapper(*pargs, **kwrgs):
        logging.debug(f"{fun.__name__} entered")
        retvalue = fun(*pargs, **kwrgs)
        logging.debug(f"{fun.__name__} exit")
        return retvalue
    return wrapper


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

@mcp.tool()
async def weather(city: str, country: str = "India") -> dict:
    """Get current weather by city, e.g. Bangalore or Tumkur."""
    location = f"{city},{country}"

    print("Weather tool is been invoked!")
    async with httpx.AsyncClient() as http:
        response = await http.get(
            f"https://wttr.in/{location}",
            params={"format": "j1"},
        )
        response.raise_for_status()

    data = response.json()
    current = data["current_condition"][0]
    nearest = data["nearest_area"][0]

    return {
        "location": nearest["areaName"][0]["value"],
        "country": nearest["country"][0]["value"],
        "temperature_c": current["temp_C"],
        "feels_like_c": current["FeelsLikeC"],
        "condition": current["weatherDesc"][0]["value"],
        "humidity_percent": current["humidity"],
        "wind_kmh": current["windspeedKmph"],
    }




if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="127.0.0.1", port=8000)
    # mcp.run(transport="stdio")
