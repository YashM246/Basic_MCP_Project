import asyncio
import nest_asyncio
from mcp import ClientSession
from mcp.client.sse import sse_client

nest_asyncio.apply()
# Needed to run interactive python

"""
Make sure 
1) server is running before this script.
2) server is configured to use sse transport
3) server is listening on port 8050

To run the server:
uv run basic_mcp_server.py

"""

async def main():
    # Connect to server using SSE
    async with sse_client("http://localhost:8050/sse") as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            # Initialize the connection
            await session.initialize()

            # List available tools
            tools_result = await session.list_tools()
            print("Available tools:")
            for tool in tools_result.tools:
                print(f"    - {tool.name}:  {tool.description}")

            # Call our calculator tool
            result = await session.call_tool("calculator", arguments={"operation": "multiply", "a":45, "b":61})
            print(f"45 * 61 = {result.content[0].text}")


if __name__ == "__main__":
    asyncio.run(main())