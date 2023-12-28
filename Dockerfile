# Dockerfile
FROM python:3.8

ARG CHAR_INPUT
ENV CHAR_INPUT=${CHAR_INPUT}

WORKDIR /app

COPY . .

CMD ["python", "task1.py"]
