# ================== IMPORTS ==================
from fastapi import FastAPI, HTTPException
from schemas import Query
from agent import agent
import logging
from datetime import datetime

# ================== APP INIT ==================
app = FastAPI(
    title="City Intelligence Agent API",
    version="1.0.0"
)

# ================== LOGGING ==================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# ================== ROOT ==================
@app.get("/")
def home():
    return {
        "status": "running",
        "message": "City Intelligence Agent API is live 🚀"
    }

# ================== CHAT ENDPOINT ==================
import uuid
@app.post("/chat")
def chat(query: Query):
    try:
        # 🔥 Auto-generate session_id if not provided
        session_id = query.session_id or str(uuid.uuid4())

        result = agent.invoke({
            "messages": [
                {"role": "user", "content": query.question}
            ],
            "session_id": session_id
        })

        return {
            "response": result["messages"][-1].content
        }

    except Exception as e:
        return {"error": str(e)}