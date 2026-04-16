FROM python:3.11-slim

# Install uv directly from astral's official image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

WORKDIR /project

# Copy dependency files first to leverage Docker layer caching
COPY pyproject.toml uv.lock ./

# Install dependencies into the system python environment
RUN uv pip install --system -r pyproject.toml

# Copy the rest of your application code
COPY ./app ./app

# Command to run your app
CMD ["python", "app/main.py"]
