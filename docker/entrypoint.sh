#!/bin/sh
set -e

echo "Starting Crochet Pattern Manager..."

exec uvicorn main:app \
  --host 0.0.0.0 \
  --port 8296
