# 🌍 City Intelligence AI

A multi-tool AI assistant built using FastAPI, LangChain, and Streamlit that can provide real-time information like weather, news, general knowledge, calculations, and current date.

---

## 🚀 Features

* 🌦️ **Weather Information** (via OpenWeather API)
* 📰 **Latest News** (via Tavily Search)
* 🧮 **Calculator Tool** (for mathematical expressions)
* 📚 **Wikipedia Search** (general knowledge queries)
* 📅 **Current Date Tool** (real-time date awareness)
* 🤖 **Smart Agent** (multi-tool reasoning with LangChain)
* 🌐 **FastAPI Backend**
* 🎨 **Streamlit UI**
* 📦 **Dockerized Application**

---

## 🧠 How It Works

User Query → FastAPI → LangChain Agent → Tool Selection → Response

The agent intelligently decides which tool(s) to use based on the query and combines results when needed.

---

## 🛠️ Tech Stack

* Python
* FastAPI
* LangChain
* Streamlit
* Docker
* OpenWeather API
* Tavily API
* Wikipedia Library

---

## 📁 Project Structure

```
.
├── app.py
├── agent.py
├── requirements.txt
├── Dockerfile
├── ui.py
├── tools/
│   ├── weather.py
│   ├── news.py
│   ├── calculator.py
│   ├── wiki.py
│   └── time_tool.py
```

---

## ⚙️ Setup Instructions

### 🔹 1. Clone the Repository

```
git clone https://github.com/ashishjadhav-001/Multi-Tools-Agent-System
cd Multi-Tools-Agent-System
```

---

### 🔹 2. Create `.env` File

```
MISTRAL_API_KEY=your_key
TAVILY_API_KEY=your_key
OPENWEATHER_API_KEY=your_key
```

---

### 🔹 3. Install Dependencies

```
pip install -r requirements.txt
```

---

### 🔹 4. Run Backend

```
uvicorn app:app --reload
```

---

### 🔹 5. Run UI

```
streamlit run ui.py
```

---

## 🐳 Run with Docker

### Build Image

```
docker build -t city-ai .
```

### Run Container

```
docker run --env-file .env -p 8000:8000 city-ai
```

---

## 🌐 API Endpoint

* POST `/chat`

### Example Request

```json
{
  "question": "weather and news of Pune"
}
```

---

## 📌 Example Queries

* "Weather in Mumbai"
* "Latest news of India"
* "2 + 5 * 10"
* "Who is Elon Musk?"
* "What is today’s date?"

---

## 🔒 Security Note

* Do NOT expose your `.env` file
* Always keep API keys private

---

## 🚀 Future Improvements

* Add memory (conversation history)
* Add voice interaction
* Deploy frontend + backend
* Add CI/CD pipeline

---

## 📬 Contact

Built by **Ashish Jadhav**

---

⭐ If you like this project, consider giving it a star!
