# Base Image - Use Python 3.11 Slim
FROM python:3.11-slim

# Working Directory
WORKDIR /app

# Copy Files
COPY requirements.txt .

# Install Dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of Application Code
COPY . .

# Expose Port
EXPOSE 8000

# Command to start the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]