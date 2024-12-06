FROM python:3.11-alpine

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# Install build tools and dependencies
RUN apk add --no-cache gcc musl-dev libffi-dev

# (Optional) Set working directory
WORKDIR /app

# Copy your application code (if you have it)
COPY . /app

# Install pip dependencies
RUN pip install --upgrade pip setuptools wheel

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip3 install cryptography

# Command to run your application (example)
# CMD ["python", "main.py"]
ENTRYPOINT ["python", "main.py"]
