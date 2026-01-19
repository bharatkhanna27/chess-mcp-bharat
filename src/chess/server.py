from mcp.server.fastmcp import FastMCP

mcp = FastMCP('Chess.com')

from .chess_api import get_player_profile, get_player_stats

@mcp.tool()
def get_chess_profile(username: str) -> dict:
    """Get the public profile for a chess.com player by username."""
    return get_player_profile(username)

@mcp.tool()
def get_chess_stats(username: str) -> dict:
    """Get the stats for a chess.com player by username."""
    return get_player_stats(username)

def main():
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()