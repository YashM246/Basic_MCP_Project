MCP Demo - Enhanced Calculator Server
=========================================

This project demonstrates a basic Model Context Protocol (MCP) server implementation
using FastMCP that provides an enhanced calculator tool for AI models.

FEATURES
--------
- Multi-operation calculator supporting add, subtract, multiply, and divide
- Variable argument support for most operations
- Strict validation for division (requires exactly 2 arguments)
- Comprehensive error handling for invalid operations and edge cases
- Server-Sent Events (SSE) transport support

REQUIREMENTS
------------
- Python 3.7+
- mcp library (pip install mcp)
- python-dotenv (pip install python-dotenv)

SETUP
-----
1. Install dependencies:
   pip install -r requirements.txt

2. Create a .env file in the parent directory if needed for environment variables

3. Run the server:
   python basic_mcp_server.py

CALCULATOR TOOL USAGE
---------------------
The calculator tool accepts the following parameters:

operation (string): The operation to perform
  - "add": Sum all provided numbers
  - "subtract": Subtract subsequent numbers from the first
  - "multiply": Multiply all numbers together
  - "divide": Divide first number by second (exactly 2 numbers required)

*numbers (float): Variable number of numeric arguments

EXAMPLES
--------
calculator("add", 1, 2, 3, 4)        → 10
calculator("subtract", 100, 10, 5)   → 85
calculator("multiply", 2, 3, 4)      → 24
calculator("divide", 10, 2)          → 5.0

ERROR HANDLING
--------------
- Invalid operations raise ValueError
- Division by zero raises ZeroDivisionError
- Wrong argument count for division raises ValueError
- Missing arguments raise ValueError

SERVER CONFIGURATION
--------------------
- Host: 0.0.0.0 (all interfaces)
- Port: 8050
- Transport: Server-Sent Events (SSE)
- Name: Calculator

DEVELOPMENT
-----------
The server uses the FastMCP framework to create MCP-compatible tools that can be
used by AI models to perform calculations. The @mcp.tool() decorator registers
functions as available tools in the MCP protocol.