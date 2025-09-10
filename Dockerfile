From python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir requirements.txt

COPY . .

env PORT=5000

CMD ["gunicorn", "--bind", "0.0.0:5000", "app:app"]
