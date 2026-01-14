# Configuration Setup
    FROM python:3.12-slim AS builder
    WORKDIR /app

    # Install Dependencies
    COPY requirements.txt .
    COPY dev-requirements.txt .
    RUN pip install --no-cache-dir -r dev-requirements.txt
    RUN pip install --no-cache-dir -r requirements.txt

    # Copy in the code
    COPY . .
