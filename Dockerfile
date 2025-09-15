FROM python:3.13-slim-bullseye

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y build-essential

RUN pip install --no-cache-dir -r requirements.txt

# garante que o Python sempre veja /app como raiz dos pacotes
ENV PYTHONPATH="/app:${PYTHONPATH}"

EXPOSE 8888