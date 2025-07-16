FROM python:3.11-slim-bookworm

WORKDIR /app

# Install system dependencies required by some Python packages (e.g., cryptography)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy project configuration file to leverage Docker cache
COPY pyproject.toml ./

# Install Python dependencies from pyproject.toml
# This command installs the project itself and its declared dependencies.
RUN pip install --no-cache-dir .

# Install httpx which is used by the application but not declared as a primary dependency in pyproject.toml
# This is necessary because auth.py, github_client.py, and openai_client.py all use httpx.
RUN pip install --no-cache-dir "httpx>=0.25.0,<1.0.0"

# Copy the application source code
COPY app.py auth.py github_client.py openai_client.py ./

# Expose the port the application listens on.
# The application reads the PORT environment variable, defaulting to 8000.
EXPOSE 8000

# Command to run the application using Uvicorn.
# The `if __name__ == "__main__":` block in app.py handles the Uvicorn server startup.
CMD ["python", "app.py"]