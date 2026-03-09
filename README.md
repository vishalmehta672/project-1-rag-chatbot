# AI Knowledge Base Chatbot (RAG)

## Project Overview

This project implements a **Retrieval-Augmented Generation (RAG) system** that allows users to ask questions about documents.

Users can upload PDF files and query the knowledge inside them through an API. The system retrieves relevant document chunks using semantic search and generates answers using an LLM.

This project was built as part of a **Generative AI engineering learning journey** focusing on production-style system design.

---

# Key Features

Document upload API

Document ingestion pipeline

Semantic search using vector embeddings

Context-aware question answering

LLM integration

Caching for faster responses

Logging and debugging support

Containerized application using Docker

Basic testing using pytest

---

# System Architecture

Document Ingestion Pipeline

PDF Document
↓
Text Extraction
↓
Text Chunking (with overlap)
↓
Embedding Generation
↓
Vector Storage

Query Pipeline

User Question
↓
Embedding Generation
↓
Vector Similarity Search
↓
Retrieve Relevant Chunks
↓
Prompt Construction
↓
LLM Response Generation
↓
Return Answer

---

# Technology Stack

Backend Framework
FastAPI

Language
Python

Embedding Model
Sentence Transformers

Vector Database
Qdrant

LLM Provider
OpenAI

Containerization
Docker

Testing
Pytest

---

# Project Structure

project-1-rag-chatbot

app
 api
 services
 utils

data
uploads
tests

docs
commands.md

main.py
requirements.txt
Dockerfile
README.md

---

# Development Progress

## Day 1 — Environment Setup

Created project structure.

Set up Python environment and installed required dependencies.

Configured FastAPI server for API development.

Tested embedding generation to ensure models load correctly.

Outcome:
Project foundation and environment ready.

---

## Day 2 — Document Ingestion Pipeline

Implemented PDF document loading.

Extracted text content from documents.

Created text chunking logic to split documents into manageable sections.

Generated embeddings for each chunk.

Stored embeddings in the vector database.

Outcome:
Documents converted into searchable vector knowledge.

---

## Day 3 — Query and Retrieval System

Implemented semantic search.

Converted user questions into embeddings.

Retrieved relevant document chunks using vector similarity.

Connected retrieval results with LLM to generate answers.

Created API endpoint for question answering.

Outcome:
System can answer questions based on uploaded documents.

---

## Day 4 — RAG Quality Improvements

Improved chunking strategy by adding chunk overlap.

Enhanced retrieval strategy by increasing top-k search results.

Introduced structured prompts to reduce hallucinations.

Added logging for debugging and system transparency.

Outcome:
Improved reliability and accuracy of generated answers.

---

## Day 5 — API-Based Document Upload

Implemented document upload endpoint.

Connected uploaded files to the ingestion pipeline.

Converted ingestion script into reusable service.

Improved project structure and service organization.

Outcome:
System can now ingest documents dynamically via API.

---

## Day 6 — Production Improvements

Implemented response caching to reduce repeated LLM calls.

Added unit tests using pytest.

Containerized the application using Docker.

Prepared the system for deployment.

Outcome:
Project is production-ready and easier to deploy.

---

# API Endpoints

Upload Document

Used to upload and ingest PDF documents into the knowledge base.

Ask Question

Used to query the knowledge base and receive AI-generated answers.

---

# Learning Outcomes

Through this project the following concepts were implemented:

Retrieval-Augmented Generation (RAG)

Vector embeddings

Vector similarity search

Semantic document retrieval

Prompt engineering

AI service architecture

API development with FastAPI

Containerization with Docker

Testing with pytest

---

# Future Improvements

LangChain integration

Streaming responses

Better document metadata support

Cloud deployment

Multi-document knowledge bases

---

# Author

Vishal Mehta

Generative AI Engineering Learning Journey
