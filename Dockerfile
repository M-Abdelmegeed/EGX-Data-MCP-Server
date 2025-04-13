FROM python:3.11-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY egx.py main.py precious_metals.py tools.py pyproject.toml ./

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Command to run when container starts
CMD ["python", "main.py"]