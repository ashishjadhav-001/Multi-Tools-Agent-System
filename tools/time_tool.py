from langchain.tools import tool
from datetime import datetime

@tool
def get_current_date() -> str:
    """Get the current date and year"""
    
    now = datetime.now()
    return now.strftime("%Y-%m-%d (Year: %Y)")