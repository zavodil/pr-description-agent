FROM python:3.11-slim-bookworm

WORKDIR /app

# Copy pyproject.toml for dependency installation
COPY pyproject.toml ./

# Install build dependencies and project dependencies from pyproject.toml
# Note: The provided pyproject.toml lists 'requests' as a dependency, but the code
# explicitly uses 'httpx.AsyncClient'. 'httpx' is also listed in the dev dependencies.
# To ensure the application runs correctly, 'httpx' is explicitly installed.
RUN pip install --no-cache-dir setuptools wheel && \
    pip install --no-cache-dir . && \
    pip install --no-cache-dir httpx

# Copy the application source code
COPY app.py ./
COPY auth.py ./
COPY github_client.py ./
COPY openai_client.py ./

# Expose the port the application listens on
EXPOSE 8000

# Create a non-root user and switch to it for security best practices
RUN adduser --system --group appuser
USER appuser

# Command to run the application using Uvicorn
# The port is read from the PORT environment variable in app.py, defaulting to 8000.
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]