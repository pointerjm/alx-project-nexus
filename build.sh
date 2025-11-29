#!/usr/bin/env bash
# Exit immediately if a command fails
set -o errexit

# Project folder
PROJECT_DIR="ecommerce_backend"

echo "🔹 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "🔹 Applying database migrations..."
python $PROJECT_DIR/manage.py migrate --noinput

echo "🔹 Collecting static files..."
python $PROJECT_DIR/manage.py collectstatic --noinput

echo "✅ Build script completed successfully!"
