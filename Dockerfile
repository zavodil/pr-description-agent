FROM python:3.11-slim-bookworm

WORKDIR /app

# Install system dependencies required for some Python packages (e.g., cryptography)
# These are common for Debian-based Python images.
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the working directory
COPY requirements.txt .

# Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY . .

# Expose the port the application listens on
EXPOSE 8088

# Command to run the application
# The app.py script handles the PORT environment variable internally
CMD ["python", "app.py"]