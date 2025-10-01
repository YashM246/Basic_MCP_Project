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
2. **Proceed to Part 2** (`2_MCP_OpenAI_Integration/`): See actual LLM integration with OpenAI
3. **Production Considerations**: Authentication, error handling, logging, tool chaining

This foundation demonstrates how MCP enables structured communication between clients and servers. Part 2 shows how AI models can automatically discover and use these tools in real conversations.

---

# Part 2: LLM Integration (`2_MCP_OpenAI_Integration/`)

The second part of this repository demonstrates real-world LLM integration where AI models can automatically discover and use MCP tools during conversations.

## PART 2 FEATURES
-----------------
- **MCPOpenAIClient Class**: Integrated client that combines MCP and OpenAI APIs
- **Automatic Tool Discovery**: AI models automatically find available MCP tools
- **Seamless Tool Execution**: Tools are called transparently during conversations
- **Conversation Context**: Tool results are integrated into natural dialogue
- **Production Patterns**: Proper resource management and error handling

## PART 2 ARCHITECTURE
---------------------

### MCPOpenAIClient Class
The core integration class that bridges MCP servers and OpenAI models:

**Key Methods:**
- `connect_to_server()`: Establishes connection to MCP server
- `get_mcp_tools()`: Converts MCP tools to OpenAI tool format
- `process_query()`: Handles complete query processing with tool integration
- `cleanup()`: Manages resource cleanup

### Query Processing Flow
1. **Tool Discovery**: Retrieve available MCP tools
2. **Initial AI Call**: Send user query with available tools to OpenAI
3. **Tool Execution**: If AI chooses to use tools, execute them via MCP
4. **Final Response**: AI formulates response using tool results
5. **Context Management**: Maintain conversation history throughout

## PART 2 SETUP
--------------

### Requirements
```
openai>=1.0.0
mcp
python-dotenv
nest-asyncio
```

### Environment Variables
Create a `.env` file with:
```
OPENAI_API_KEY=your_openai_api_key_here
```

### Running Part 2
1. **Set up environment**:
   ```bash
   cd 2_MCP_OpenAI_Integration/
   pip install -r requirements.txt
   ```

2. **Configure your OpenAI API key** in the `.env` file

3. **Run the integrated client**:
   ```bash
   python client.py
   ```

## PART 2 EXAMPLE USAGE
----------------------

### Basic Query Processing
```python
client = MCPOpenAIClient()
await client.connect_to_server("server.py")

# AI automatically uses tools when needed
response = await client.process_query("What's 25 * 17?")
# AI will automatically call calculator tool and provide result
```

### What Happens Behind the Scenes
1. User asks: "What's 25 * 17?"
2. AI receives query + available calculator tool
3. AI decides to use calculator tool
4. Tool executes: calculator("multiply", 25, 17)
5. AI receives result: 425
6. AI responds: "25 × 17 equals 425"

## KEY DIFFERENCES: PART 1 vs PART 2
------------------------------------

| Aspect | Part 1 (Basic MCP) | Part 2 (LLM Integration) |
|--------|-------------------|--------------------------|
| **Tool Calling** | Manual client calls | AI automatically decides |
| **Discovery** | Explicit tool listing | AI discovers tools dynamically |
| **Integration** | Separate client/server | Unified AI experience |
| **Use Case** | Learning MCP mechanics | Production AI applications |
| **User Experience** | Technical demonstration | Natural conversation |

## PART 2 PRODUCTION CONSIDERATIONS
----------------------------------
- **API Key Security**: Environment variables for sensitive data
- **Error Handling**: Robust error management for tool failures
- **Rate Limiting**: OpenAI API usage management
- **Tool Validation**: Input validation for tool parameters
- **Conversation Memory**: Managing long conversation contexts
- **Multi-tool Workflows**: Handling complex multi-step tool usage

This integration demonstrates the true power of MCP: enabling AI models to seamlessly interact with external tools and services as if they were native capabilities.