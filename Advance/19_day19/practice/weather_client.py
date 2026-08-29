import httpx
from mcp.server import MCPServer

mcp = MCPServer("Demo")


@mcp.tool()
async def current_weather(latitude: float, longitude: float) -> dict:
    """Get live weather for latitude and longitude."""
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m",
    }

    async with httpx.AsyncClient() as http:
        response = await http.get(url, params=params)
        response.raise_for_status()
        return response.json()


if __name__ == "__main__":
    mcp.run(transport="streamable-http", port=8000)