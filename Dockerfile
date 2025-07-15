FROM python:3.11-slim-bookworm

WORKDIR /app

# Install system dependencies required for Python packages like 'cryptography'.
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file and install Python dependencies.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application source code into the container.
COPY app.py .
COPY auth.py .
COPY github_client.py .
COPY openai_client.py .

# Expose the port the FastAPI application will listen on.
EXPOSE 8088

# Command to run the application using uvicorn, as specified in app.py.
# The app.py script itself handles reading the PORT environment variable.
CMD ["python", "app.py"]