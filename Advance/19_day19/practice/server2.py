from mcp.server import MCPServer

mcp = MCPServer("Campus information")

CAMPUS_HOURS = {
    "monday": "08:00–20:00",
    "tuesday": "08:00–20:00",
    "wednesday": "08:00–20:00",
    "thursday": "08:00–20:00",
    "friday": "08:00–18:00",
    "saturday": "10:00–14:00",
    "sunday": "Closed",
}


@mcp.tool()
def campus_hours(day: str) -> str:
    """Return public campus opening hours for a day of the week."""
    normalized_day = day.strip().lower()
    hours = CAMPUS_HOURS.get(normalized_day)

    if hours is None:
        return "Unknown day. Please use a day such as Monday or Tuesday."

    return f"Campus hours on {normalized_day.title()}: {hours}"


@mcp.resource("campus://visitor-guide")
def visitor_guide() -> str:
    """Read the public visitor guide for the campus."""
    return """# Campus visitor guide

- Check in at the reception desk.
- Visitors need a photo ID.
- The library is on the second floor.
"""


@mcp.resource("campus://room/{room_number}")
def room_information(room_number: str) -> str:
    """Read public information about a campus room."""
    rooms = {
        "101": "Room 101: Introductory Programming Lab, 30 seats.",
        "202": "Room 202: Student Help Desk, open weekdays.",
    }
    return rooms.get(room_number, f"No public information for room {room_number}.")


@mcp.prompt()
def campus_visit_plan(visitor_type: str = "prospective student") -> str:
    """Create a helpful plan for a campus visit."""
    return f"""You are a friendly campus guide.

Create a short visit plan for a {visitor_type}. Include arrival, check-in,
and three useful locations to visit. Be accurate, practical, and welcoming.
"""


if __name__ == "__main__":
    # Used when a local stdio client starts this file as a subprocess.
    mcp.run(transport="stdio")