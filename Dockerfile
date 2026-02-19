FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose port 80 instead of 8501
EXPOSE 80

# Run Streamlit on port 80 and bind to 0.0.0.0
CMD ["streamlit", "run", "app.py", "--server.port=80", "--server.address=0.0.0.0"]
