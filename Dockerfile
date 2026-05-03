FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Expose both ports
EXPOSE 8000
EXPOSE 8501

# Run both FastAPI and Streamlit
CMD sh -c "uvicorn app:app --host 0.0.0.0 --port 8000 & streamlit run ui.py --server.address 0.0.0.0 --server.port 8501"