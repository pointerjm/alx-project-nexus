
---

# ✅ **2. deploy.sh**

```bash
#!/bin/bash

echo "📦 Installing dependencies..."
pip install -r requirements.txt

echo "⚙️ Running migrations..."
python manage.py migrate

echo "📂 Collecting static files..."
python manage.py collectstatic --noinput

echo "🚀 Preparing Vercel serverless environment..."
mkdir -p api
cp vercel_wsgi.py api/index.py

echo "✨ Deployment build complete. Push to Vercel to finish deployment."
