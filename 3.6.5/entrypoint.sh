#!/bin/bash
set -e

python --version
pip --version

# Setting the Python path
export PYTHONPATH=/home/site/wwwroot/antenv/lib/python3.6/site-packages

# calling gunicorn
echo "Starting the gunicorn server"
GUNICORN_CMD_ARGS="--bind=0.0.0.0" gunicorn application:app