import asyncio
import nest_asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

nest_asyncio.apply()
# To run interactive python

async def main():
    # Define server parameters
    server_params = StdioServerParameters(
        command="python",       # The command to run your server
        args = ["basic_mcp_server.py"],   # Arguments to the command
    )

    # Connect to server
    async with stdio_client(server_params) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:

            # Initialize connection
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