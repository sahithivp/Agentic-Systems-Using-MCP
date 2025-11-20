# # mcp_server.py
# from fastmcp import MCPTool, MCPServer
# import subprocess

# server = MCPServer(name="molecular-simulator")

# @server.tool()
# def run_docking_simulation(molecule: str, protein: str):
#     """
#     Simulates molecular docking between molecule and protein using a Python script or API.
#     """
#     try:
#         # Placeholder for your real docking logic
#         result = f"Simulated docking: Molecule {molecule} shows 82% binding affinity with Protein {protein}."
#         return {"result": result}
#     except Exception as e:
#         return {"error": str(e)}

# if __name__ == "__main__":
#     server.run()


# server.py
from fastmcp import FastMCP
import asyncio
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


mcp = FastMCP("Demo 🚀")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=8000, path="/mcp")