from fastmcp import Client

async def molecular_simulator(molecule: str, protein: str):
    client = Client("http://127.0.0.1:8000/mcp")  # assuming MCP runs there
    async with client:
        await client.ping()
        
        result = await client.call_tool(
            "run_docking_simulation",
            {
                "molecule": molecule,
                "protein": protein
            }
        )
        return result.content
