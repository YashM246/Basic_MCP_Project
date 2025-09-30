import os
import json
from mcp.server.fastmcp import FastMCP

# Create an MCP Server
# We are making a server which will basically emulate RAG and act
# as a Knowledge Base
mcp = FastMCP(
    name= "Knowledge Base",
    host= "0.0.0.0",            # Only for SSE Transport (Local Host)
    port = 8050
)

@mcp.tool()
def get_knowledge_base()->str:
    """
        Retrieves the entire knowledge base as a string
    """

    try:
        kb_path = os.path.join(os.path.dirname(__file__), "data", "kb.json")
        with open(kb_path, "r") as f:
            kb_data = json.load(f)

        # Format the kb as a string
        kb_text="Here is the retrieved knowledge base: \n\n"


        if isinstance(kb_data, list):
            for i, item in enumerate(kb_data, 1):
                if isinstance(item, dict):
                    question = item.get("question", "Unknown Question")
                    answer = item.get("answer", "Unknown Answer")
                else:
                    question = f"Item {i}"
                    answer = str(item)

                kb_text += f"Q{i}: {question}\n"
                kb_text += f"A{i}: {answer}\n\n"
        else:
            kb_text += f"Knowledge Base Content: {json.dumps(kb_data, indent=2)}\n\n"

        return kb_text
    
    except FileNotFoundError:
        return "Error: Knowledge base file not found"
    
    except json.JSONDecodeError:
        return "Error: Invalid JSON in knowledge base file"
    
    except Exception as e:
        return f"Error: {str(e)}"


# Run the server
if __name__ == "__main__":
    mcp.run(transport="stdio")