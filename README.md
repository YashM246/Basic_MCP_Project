MCP Demo - Complete Learning Repository
=======================================

This repository provides a comprehensive learning path for Model Context Protocol (MCP)
implementation, organized into two distinct parts:

**Part 1: Basic MCP Implementation and Mechanics** (Current Directory)
- Demonstrates fundamental MCP concepts without LLM integration
- Shows client-server communication and transport mechanisms
- Provides hands-on experience with MCP tool registration and invocation

**Part 2: LLM Integration** (`2_MCP_OpenAI_Integration/`)
- Connects MCP tools to actual AI models
- Real-world implementation with OpenAI/Claude integration
- Production-ready patterns and best practices

This first part provides a simple calculator tool that demonstrates the core MCP concepts
of tool registration, client-server communication, and transport mechanisms.

FEATURES
--------
- Basic calculator supporting add, subtract, multiply, and divide operations
- Takes exactly two numbers as input for all operations
- Comprehensive error handling for invalid operations and division by zero
- Two transport mechanisms demonstration (stdio and SSE)

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

This demo demonstrates two of the three MCP transport mechanisms:

**STDIO (Standard Input/Output):**
- Communication through stdin/stdout pipes
- Client launches server as subprocess on the same system
- Simpler setup - no manual server startup required
- Best for local development and testing
- Use case: Tools and resources are on the same local machine
- Process-to-process communication within same system

**SSE (Server-Sent Events):**
- HTTP-based communication over network
- Server runs independently on specified host/port
- Requires manual server startup before client connection
- Good for distributed systems and remote tool access
- Allows multiple clients to connect to same server instance
- Use case: Tools and resources are on external/remote servers

**Note on Streamable HTTP**: Since this demo was recorded, MCP has introduced a third transport mechanism called Streamable HTTP, which is now the recommended approach for production environments. While not demonstrated in this basic example, it provides enhanced reliability and production readiness compared to SSE.

Transport Selection Guide:
- **STDIO**: Local development and testing (demonstrated here)
- **SSE**: Basic network communication and learning (demonstrated here)
- **Streamable HTTP**: Production deployments (not included in this demo)

FUNDAMENTAL MCP CONCEPTS
------------------------
This demo illustrates core MCP principles:
1. **Tool Registration**: How servers expose functionality via @mcp.tool()
2. **Client Discovery**: How clients find and list available tools
3. **Tool Invocation**: How clients call server tools with parameters
4. **Transport Abstraction**: How MCP works over different communication methods

**Note**: This is Part 1 - foundational MCP mechanics. For actual LLM integration where AI models automatically discover and call these tools based on user requests, see Part 2 in the `2_MCP_OpenAI_Integration/` directory.

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

**Learning Path:**
1. **Complete Part 1** (Current): Understand MCP fundamentals and transport mechanisms
2. **Proceed to Part 2** (`2_MCP_OpenAI_Integration/`): See actual LLM integration with OpenAI/Claude
3. **Production Considerations**: Authentication, error handling, logging, tool chaining

This foundation demonstrates how MCP enables structured communication between clients and servers. Part 2 shows how AI models can automatically discover and use these tools in real conversations.