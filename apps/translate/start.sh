#/bin/bash

gunicorn api:app -w ${NUM_WORKERS:-1} -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT