#!/bin/sh

gunicorn main:app --bind 0.0.0.0:$API_PORT --workers $API_WORKERS --worker-class uvicorn.workers.UvicornWorker