# Use the official Python image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies required for xmlsec
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    pkg-config \
    libxml2-dev \
    libxmlsec1-dev \
    libxmlsec1-openssl \
    libpython3.11-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install pipenv or use requirements.txt if available
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . .

# Command to run the app
CMD ["gunicorn", "employee.wsgi:application", "--bind", "0.0.0.0:8000"]
