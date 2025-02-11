FROM ghcr.io/astral-sh/uv:debian-slim

RUN apt update && apt install -y build-essential git
WORKDIR /app
COPY . /app

RUN uv sync --frozen

ENTRYPOINT ["uv", "run", "python", "/app/backup.py"]
