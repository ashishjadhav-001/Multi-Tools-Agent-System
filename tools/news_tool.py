from dotenv import load_dotenv
load_dotenv()
import os
from tavily import TavilyClient
from langchain.tools import tool

tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def get_news(city: str) -> list:
    """Get latest news about a given city"""
    
    try:
        response = tavily_client.search(
            query=f"latest news of {city}",
            max_results=3
        )

        return response.get("results", [])

    except Exception as e:
        return [{"error": str(e)}]