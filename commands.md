# Development Commands

This file contains useful commands used during development.

---

# Environment Setup

Create virtual environment

python -m venv venv

Activate virtual environment (Mac/Linux)

source venv/bin/activate

---

# Install Dependencies

Install project libraries

pip install fastapi uvicorn sentence-transformers pypdf qdrant-client openai

---

# Run Vector Database

Start Qdrant using Docker

docker run -p 6333:6333 qdrant/qdrant

---

# Run FastAPI Server

Start development server

uvicorn main:app --reload

API documentation

http://127.0.0.1:8000/docs

---

# Test Document Ingestion

Run ingestion script

python test_ingest.py

---

# Git Commands

Initialize repository

git init

Add files

git add .

Commit changes

git commit -m "initial project setup"

Push to GitHub

git push origin main

---

# Useful Docker Commands

List running containers

docker ps

Stop container

docker stop <container_id>

Remove container

docker rm <container_id>
