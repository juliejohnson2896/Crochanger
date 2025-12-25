FROM python:3.12-slim

# Environment
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system deps
RUN apt-get update && apt-get install -y \
    build-essential \
    poppler-utils \
    tesseract-ocr \
    sqlite3 libsqlite3-dev \
    && rm -rf /var/lib/apt/lists/*

# Create app user
ARG PUID=1000
ARG PGID=1000
RUN groupadd -g $PGID appgroup \
    && useradd -u $PUID -g appgroup -m appuser

# App directories
WORKDIR /app
RUN mkdir -p /library /config \
    && chown -R appuser:appgroup /app /library /config

# Install Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY app/ /app/
COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

USER appuser

EXPOSE 8296
ENTRYPOINT ["/entrypoint.sh"]
