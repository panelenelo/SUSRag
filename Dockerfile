FROM python:3.12-alpine AS builder
WORKDIR /app
ENV UV_LINK_MODE=copy \
    UV_COMPILE_BYTECODE=1 \
    UV_TOOL_BIN_DIR=/usr/local/bin 
RUN apk add --no-cache gcc musl-dev linux-headers
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project
COPY . /app
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked
RUN apk del gcc musl-dev linux-headers

FROM python:3.12-alpine
WORKDIR /app
COPY --from=builder /app /app

EXPOSE 5000
ENTRYPOINT []
CMD ["uv", "run", "main.py"]