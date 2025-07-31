FROM python:3.11-slim-bookworm

WORKDIR /app

# Install system dependencies required for building Python packages like cryptography
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libssl-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port the application listens on
EXPOSE 8000

# Command to run the application using Uvicorn
# Use ${PORT:-8000} to allow runtime override of the port, defaulting to 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "${PORT:-8000}"]