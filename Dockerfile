FROM python:3.11-slim-bookworm

WORKDIR /app

COPY pyproject.toml ./

RUN pip install --no-cache-dir . \
    && pip install --no-cache-dir httpx

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]