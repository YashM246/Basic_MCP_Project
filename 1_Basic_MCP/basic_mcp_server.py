from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

load_dotenv("../.env")

# Create an MCP Server
mcp = FastMCP(
    name="Calculator",
    host="0.0.0.0",
    port=8050,
)

# Adding a Calculator Tool
@mcp.tool()
def calculator(operation: str, a: float, b: float) -> float:
    '''Basic 2 number calculator to perform "add", "subtract", "multiply", "divide"'''

    # Validate operation
    valid_operations = ['add', 'subtract', 'multiply', 'divide']
    if operation not in valid_operations:
        raise ValueError(f"Invalid operation '{operation}'. Must be one of: {', '.join(valid_operations)}")

    # Perform the calculation
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b


# Run the server
if __name__ == "__main__":
    transport = "sse"

    if transport == "stdio":
        print("Running server with stdio transport")
    elif transport == "sse":
        print("Running server with sse transport")
    else:
        raise ValueError(f"Unknown transport: {transport}")
        
    mcp.run(transport=transport)
