# Project 1 — AI Knowledge Base Chatbot (RAG)

## Overview

This project builds an **AI-powered knowledge base chatbot** that can answer questions from uploaded documents (PDFs).

The system uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant information from documents and generate accurate responses using a Large Language Model.

The project is designed as part of a **6-month AI Engineer learning journey** and follows a **production-style architecture similar to real AI systems used in companies**.

---

# Project Goals

* Learn how **RAG systems work**
* Build a **document ingestion pipeline**
* Generate **embeddings**
* Store embeddings in a **vector database**
* Retrieve relevant document chunks
* Use an LLM to generate answers
* Build an **API service using FastAPI**

---

# High-Level Architecture

Document
↓
Text Extraction
↓
Text Chunking
↓
Embeddings Generation
↓
Vector Database (Qdrant)
↓
Semantic Search
↓
LLM Answer Generation
↓
API Response

---

# Technology Stack

Backend

* Python
* FastAPI

AI / NLP

* Sentence Transformers
* OpenAI API

Vector Database

* Qdrant

Document Processing

* PyPDF

Infrastructure

* Docker

---

# Project Structure

project-1-rag-chatbot

app
 api
 services
 utils

data
tests

main.py
requirements.txt
README.md

---

# Environment Setup

## 1. Install Python

Python version used in this project:

Python 3.11

Recommended tool for version management:

pyenv

---

## 2. Create Virtual Environment

Create a project virtual environment and activate it before installing dependencies.

This ensures dependencies remain isolated for the project.

---

## 3. Install Required Python Libraries

Install the required libraries for:

* API development
* embeddings generation
* PDF processing
* vector database client

The main libraries used are:

FastAPI
Uvicorn
Sentence Transformers
PyPDF
Qdrant Client
OpenAI

---

## 4. Run Vector Database

The project uses **Qdrant** as the vector database.

Run Qdrant locally using Docker.

Once started, Qdrant will run on port **6333**.

This database stores document embeddings and enables semantic search.

---

# Day 1 — Project Foundation

Objectives:

* Create the project structure
* Install dependencies
* Set up the FastAPI application
* Test embedding generation

Tasks completed:

1. Created the project folder and directory structure.
2. Installed all required Python libraries.
3. Set up a FastAPI server.
4. Tested embedding generation using Sentence Transformers.

Outcome:

We confirmed that embeddings can be generated successfully.

This means text can now be converted into vectors.

---

# Day 2 — Document Ingestion Pipeline

Objective:

Build the pipeline that converts documents into searchable knowledge.

Pipeline steps:

PDF Document
↓
Extract text
↓
Split text into smaller chunks
↓
Generate embeddings for each chunk
↓
Store embeddings in the vector database

Tasks completed:

1. Implemented PDF text extraction.
2. Implemented text chunking logic.
3. Generated embeddings for each chunk.
4. Stored embeddings and chunk metadata in Qdrant.

Outcome:

Documents are now stored as **vectorized knowledge** inside the vector database.

This allows semantic search later.

---

# Day 3 — Query and Retrieval System

Objective:

Allow users to ask questions and retrieve relevant document information.

Query pipeline:

User Question
↓
Convert question into embedding
↓
Search vector database
↓
Retrieve most relevant chunks
↓
Send retrieved context to LLM
↓
Generate answer
↓
Return response via API

Tasks completed:

1. Implemented semantic search using Qdrant.
2. Retrieved the most relevant document chunks.
3. Built a query pipeline combining retrieval and LLM generation.
4. Created an API endpoint to accept user questions.

Outcome:

The system can now answer questions based on uploaded documents.

This completes the **core RAG workflow**.

---

# Current System Workflow

Document Ingestion:

PDF
↓
Text Extraction
↓
Text Chunking
↓
Embeddings Generation
↓
Vector Storage

Query Processing:

User Question
↓
Embedding Generation
↓
Vector Search
↓
Retrieve Context
↓
LLM Response

---

# Next Steps (Day 4)

Next improvements will focus on making the system **closer to production quality**.

Planned enhancements:

* Improved text chunking strategy
* Better prompt engineering
* Query optimization
* Logging and debugging
* Testing setup
* Code structure improvements

---

# Learning Outcomes So Far

By Day 3 the following concepts have been implemented:

* RAG architecture
* Embeddings generation
* Vector databases
* Semantic search
* LLM integration
* FastAPI backend service
* Document ingestion pipelines

---

# Author

Vishal Mehta
AI Engineer Learning Journey
