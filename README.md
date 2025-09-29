MCP Demo - Basic Calculator Server
===================================

This project demonstrates a basic Model Context Protocol (MCP) server implementation
using FastMCP that provides a simple calculator tool for AI models.

FEATURES
--------
- Basic calculator supporting add, subtract, multiply, and divide operations
- Takes exactly two numbers as input for all operations
- Comprehensive error handling for invalid operations and division by zero
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
  - "add": Add two numbers (a + b)
  - "subtract": Subtract second number from first (a - b)
  - "multiply": Multiply two numbers (a * b)
  - "divide": Divide first number by second (a / b)

a (float): First number
b (float): Second number

EXAMPLES
--------
calculator("add", 5, 3)        → 8.0
calculator("subtract", 10, 4)  → 6.0
calculator("multiply", 6, 7)   → 42.0
calculator("divide", 15, 3)    → 5.0

ERROR HANDLING
--------------
- Invalid operations raise ValueError
- Division by zero raises ZeroDivisionError

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