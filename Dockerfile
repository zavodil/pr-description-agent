FROM python:3.8-slim-bullseye

WORKDIR /app

# Install system dependencies required for some Python packages (e.g., cryptography)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libssl-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency files first to leverage Docker cache
COPY requirements.txt .
COPY pyproject.toml .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port the application listens on
EXPOSE 8000

# Command to run the application
# The app.py script handles reading the PORT environment variable and defaults to 8000
CMD ["python", "app.py"]