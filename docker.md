# Docker Beginner Guide (For RAG Chatbot Project)

## 1. What is Docker?

Docker allows us to run applications inside **containers**.
A container includes:

* Code
* Python
* Libraries
* Dependencies

So the application runs the **same everywhere**.

Example:

Your system:

Mac → Python → FastAPI → Qdrant → Redis

Docker system:

Container → Python → FastAPI → Qdrant → Redis

---

# 2. What is Docker Compose?

Docker Compose runs **multiple containers together**.

In our project we run:

1. FastAPI App
2. Qdrant Vector Database
3. Redis Cache

All defined in:

```
docker-compose.yml
```

---

# 3. Important Docker Files in Our Project

### Dockerfile

Builds the application container.

Example:

```
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

### docker-compose.yml

Defines services:

```
services:

  app:
    build: .
    ports:
      - "8000:8000"
    depends_on:
      - qdrant
      - redis

  qdrant:
    image: qdrant/qdrant
    ports:
      - "6333:6333"

  redis:
    image: redis:7
    ports:
      - "6379:6379"
```

---

# 4. Basic Docker Commands

## Start containers

```
docker compose up
```

Start in background:

```
docker compose up -d
```

Build containers again:

```
docker compose up --build
```

---

# 5. Stop Containers

```
docker compose down
```

This stops and removes containers.

---

# 6. See Running Containers

```
docker ps
```

Example output:

```
project-1-rag-chatbot-app-1
project-1-rag-chatbot-qdrant-1
project-1-rag-chatbot-redis-1
```

---

# 7. See Logs (Very Important)

View logs:

```
docker compose logs
```

Live logs:

```
docker compose logs -f app
```

Example:

```
INFO: Uvicorn running on http://0.0.0.0:8000
```

---

# 8. Enter a Container

Open terminal inside container:

```
docker exec -it project-1-rag-chatbot-app-1 bash
```

Now you are inside the container.

Example commands:

```
ls
python
```

Exit container:

```
exit
```

---

# 9. Restart Containers

```
docker compose restart
```

Restart only app:

```
docker compose restart app
```

---

# 10. Remove Everything (Clean Reset)

```
docker compose down
docker system prune -a
```

Use carefully.

---

# 11. Check Docker Networks

```
docker network ls
```

Our project network:

```
project-1-rag-chatbot_default
```

This network allows containers to communicate.

Example:

```
app → qdrant
app → redis
```

---

# 12. Test Containers

### FastAPI

```
http://localhost:8000/docs
```

### Qdrant Dashboard

```
http://localhost:6333/dashboard
```

---

# 13. Project Architecture

Our AI system:

```
FastAPI (API)
     │
     ├── Redis (Cache)
     │
     └── Qdrant (Vector Database)
```

All running inside Docker.

---

# 14. Typical Development Workflow

Start system:

```
docker compose up -d --build
```

Check containers:

```
docker ps
```

View logs:

```
docker compose logs -f app
```

Stop system:

```
docker compose down
```

---

# 15. When Something Breaks

Use these commands:

```
docker compose logs app
docker compose logs qdrant
docker compose logs redis
```

Or enter container:

```
docker exec -it project-1-rag-chatbot-app-1 bash
```

---

# Summary

Important commands:

Start project:

```
docker compose up -d --build
```

Check containers:

```
docker ps
```

Logs:

```
docker compose logs -f app
```

Stop containers:

```
docker compose down
```

Enter container:

```
docker exec -it container_name bash
```

---

This is enough Docker knowledge for most backend AI projects.
