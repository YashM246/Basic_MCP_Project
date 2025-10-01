MCP Demo - Learning Project
=============================

This repository documents my exploration of Model Context Protocol (MCP) implementation.
I built this project to understand how MCP enables AI models to interact with external tools and services.

**Project Structure:**
- **Part 1**: Basic MCP mechanics and transport methods
- **Part 2**: Real LLM integration with OpenAI API

This hands-on project helped me understand MCP fundamentals through building a calculator tool that works with different transport mechanisms.

## Part 1: Basic MCP Implementation

**What I Built:**
- Calculator tool with basic arithmetic operations
- MCP server that exposes the calculator via `@mcp.tool()` decorator
- Two different client implementations demonstrating transport methods

**Key Learning:**
- How MCP servers register and expose tools
- Client-server communication patterns
- Transport mechanisms: stdio vs SSE

**Running the Code:**
```bash
# STDIO Transport - client manages server lifecycle
python client-stdio.py

# SSE Transport - manual server startup required
python basic_mcp_server.py  # Terminal 1
python client-sse.py        # Terminal 2
```

## Part 2: LLM Integration

**What I Built:**
- `MCPOpenAIClient` class that integrates MCP with OpenAI API
- Automatic tool discovery and execution by AI models
- Query processing system where AI decides when to use tools

**Key Learning:**
- How to bridge MCP tools with LLM APIs
- Tool format conversion between MCP and OpenAI schemas
- Managing conversation context with tool results
- Resource cleanup and error handling patterns

**Running the Code:**
```bash
cd 2_MCP_OpenAI_Integration/
# Add OPENAI_API_KEY to .env file
python client.py
```

**What Happens:**
1. AI receives user query + available MCP tools
2. AI automatically decides if tools are needed
3. Tools execute via MCP, results integrated into conversation
4. AI provides natural response using tool results

## Key Differences

| Part 1 | Part 2 |
|--------|--------|
| Manual tool calls | AI decides automatically |
| Learning MCP mechanics | Real AI tool integration |
| Technical demonstration | Natural conversation |

## What I Learned

This project helped me understand:
- MCP's role in extending AI capabilities with external tools
- Different transport mechanisms and their use cases
- How to integrate MCP with popular LLM APIs
- The difference between manual tool calling and AI-driven tool usage
- Resource management in async Python applications