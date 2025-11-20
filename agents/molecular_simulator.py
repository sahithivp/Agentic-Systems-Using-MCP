from fastmcp import Client

async def molecular_simulator(molecule: str, protein: str):
    client = Client("http://127.0.0.1:8000/mcp")  # assuming MCP runs there
    async with client:
        # Basic server interaction
        await client.ping()
        
        # # List available operations
        # tools = await client.list_tools()
        # resources = await client.list_resources()
        # prompts = await client.list_prompts()
        
        # Execute operations
        result = await client.call_tool("add",{"a": 5, "b": 7})
        return result
    # result = await client.call_tool(name="running")
    # return result["result"]
