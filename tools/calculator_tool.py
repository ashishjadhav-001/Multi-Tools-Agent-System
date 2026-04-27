import math
from langchain.tools import tool

@tool
def calculator(expression: str) -> str:
    """Evaluate basic math expressions safely"""
    
    allowed_names = {"__builtins__": {}, "math": math}
    
    try:
        result = eval(expression, allowed_names)
        return f"🧮 Result: {result}"
    
    except Exception as e:
        return f"❌ Error: {str(e)}"