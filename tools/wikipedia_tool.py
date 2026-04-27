from langchain.tools import tool
import wikipedia

@tool
def wikipedia_search(query: str) -> str:
    """Search Wikipedia and return a short summary"""

    try:
        # 🔥 Fix: auto-suggest enabled
        summary = wikipedia.summary(query, sentences=2, auto_suggest=True)
        return f"📚 Wikipedia:\n{summary}"

    except wikipedia.exceptions.DisambiguationError as e:
        # pick first option automatically
        try:
            summary = wikipedia.summary(e.options[0], sentences=2)
            return f"📚 Wikipedia:\n{summary}"
        except:
            return f"⚠️ Multiple results found: {e.options[:3]}"

    except wikipedia.exceptions.PageError:
        return "❌ No Wikipedia page found. Try a more specific query."

    except Exception as e:
        return f"❌ Wikipedia error: {str(e)}"