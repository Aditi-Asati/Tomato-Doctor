FROM python:3.11.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

COPY streamlit-requirements.txt .
RUN pip3 install -r streamlit-requirements.txt

COPY fastapi-requirements.txt .
RUN pip3 install -r fastapi-requirements.txt

COPY . .

ENV STREAMLIT_GLOBAL_DEVELOPMENT_MODE=false

EXPOSE 8501
EXPOSE 8000

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

CMD ["sh", "-c", "streamlit run /app/web/main.py --server.port=8501 --server.address=0.0.0.0 & uvicorn api.api:app --host 0.0.0.0 --port 8000"]
