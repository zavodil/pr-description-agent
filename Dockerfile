FROM python:3.11-slim-bookworm

WORKDIR /app

# Install system dependencies required by Python packages like 'cryptography'
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port the application listens on.
# The application defaults to 8088 if PORT environment variable is not set.
EXPOSE 8088

# Command to run the application using uvicorn, as defined in app.py
CMD ["python", "app.py"]