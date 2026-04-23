from langchain_core.tools import tool
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Arithmetic Server")

@tool
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

@tool
def subtract(a: float, b: float) -> float:
    """Subtract second number from first."""
    return a - b

@tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b

@tool
def divide(a: float, b: float) -> float:
    """Divide first number by second."""
    if b == 0:
        return "Error: Division by zero"
    return a / b

@tool
def power(a: float, b: float) -> float:
    """Raise a to the power of b."""
    return a ** b

@tool
def modulus(a: float, b: float) -> float:
    """Get remainder of division."""
    return a % b

mcp.add_tool(add)
mcp.add_tool(subtract)
mcp.add_tool(multiply)
mcp.add_tool(divide)
mcp.add_tool(power)
mcp.add_tool(modulus)

if __name__ == "__main__":
    mcp.run()