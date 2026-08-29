from mcp.server import MCPServer
import httpx

mcp = MCPServer("Demo")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


@mcp.resource("greeting://{name}")
def greeting(name: str) -> str:
    """Greet someone by name."""
    return f"Hello, {name}!"

@mcp.tool()
async def weather(city: str, country: str = "India") -> dict:
    """Get current weather by city, e.g. Bangalore or Tumkur."""
    location = f"{city},{country}"

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