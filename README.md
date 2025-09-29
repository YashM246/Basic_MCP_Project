MCP Demo - Basic Calculator Server
===================================

This project demonstrates the fundamental concepts of Model Context Protocol (MCP)
server implementation using FastMCP. This is a foundational example showing how MCP
servers and clients communicate - **no LLM integration is included yet**.

This example provides a simple calculator tool that demonstrates the core MCP concepts
of tool registration, client-server communication, and different transport methods.

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

3. Configure the server transport in basic_mcp_server.py:
   - Set transport = "stdio" for stdio communication
   - Set transport = "sse" for Server-Sent Events communication

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

RUNNING THE APPLICATION
-----------------------

STDIO Transport (client-stdio.py):
1. Simply run the client:
   python client-stdio.py

The client automatically starts the server as a subprocess and handles all communication.

SSE Transport (client-sse.py):
1. First, start the server manually:
   python basic_mcp_server.py

2. Then run the client in a separate terminal:
   python client-sse.py

TRANSPORT METHODS
-----------------

STDIO (Standard Input/Output):
- Communication through stdin/stdout pipes
- Client launches server as subprocess on the same system
- Simpler setup - no manual server startup required
- Best for local development and testing
- Use case: Tools and resources are on the same local machine
- Process-to-process communication within same system

SSE (Server-Sent Events):
- HTTP-based communication over network
- Server runs independently on specified host/port
- Requires manual server startup before client connection
- Better for distributed systems and remote tool access
- Allows multiple clients to connect to same server instance
- Use case: Tools and resources are on external/remote servers
- Network-based communication across different systems

Why the difference?
- STDIO: Direct process communication for local tools (same machine)
- SSE: Network communication for remote tools (different machines/services)

FUNDAMENTAL MCP CONCEPTS
------------------------
This demo illustrates core MCP principles:
1. **Tool Registration**: How servers expose functionality via @mcp.tool()
2. **Client Discovery**: How clients find and list available tools
3. **Tool Invocation**: How clients call server tools with parameters
4. **Transport Abstraction**: How MCP works over different communication methods

**Note**: This is a basic MCP foundation. Real-world usage involves LLM integration
where the AI model would discover and call these tools automatically based on user
requests, rather than manual client calls as shown here.

SERVER CONFIGURATION
--------------------
- Host: 0.0.0.0 (all interfaces)
- Port: 8050 (for SSE transport)
- Transport: Configurable (stdio/sse)
- Name: Calculator

DEVELOPMENT NOTES
-----------------
This implementation uses the FastMCP framework to demonstrate MCP fundamentals:

- **@mcp.tool() decorator**: Registers Python functions as MCP tools
- **Transport abstraction**: Same tool works over stdio and SSE
- **Client-server pattern**: Clean separation of tool provider and consumer
- **JSON-RPC communication**: MCP uses structured messaging protocol

**Next Steps for Production Use:**
1. **LLM Integration**: Connect to AI models (Claude, GPT, etc.) that can automatically discover and use these tools
2. **Authentication**: Add security for remote tool access
3. **Error Handling**: Implement comprehensive error recovery
4. **Logging**: Add detailed operation logging
5. **Tool Chaining**: Enable tools to call other tools

This foundation demonstrates how MCP enables AI models to interact with external
tools and services in a standardized way.