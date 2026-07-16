# Enterprise Internal Service Desk

## Overview

Enterprise Internal Service Desk is a simple Multi-Agent LLM system that demonstrates Retrieval-Augmented Generation (RAG) for enterprise internal services.

This project was developed as the Final Project for the Enterprise AI course.

---

## Problem Statement

Employees often struggle to find internal SOP information because documents are scattered across different departments.

This system demonstrates how a Multi-Agent architecture can automatically route requests to the appropriate department and answer using department-specific knowledge.

---

## Departments

- HR
- IT
- Finance

---

## Architecture

User

↓

Supervisor Agent

↓

Department Agent

↓

RAG

↓

ChromaDB

↓

LLM

↓

Final Response

---

## Technology

- Python
- LangChain
- ChromaDB
- Sentence Transformers
- Ollama
- PyPDF

---

## Project Status

🚧 MVP Development

---

## Folder Structure

app/

docs/

knowledge_base/

tests/

---

## Current Features

- PDF Loader
- Text Chunking
- Embedding
- ChromaDB
- Multi-Agent Routing
- RAG Pipeline

---

## Future Features

- Better Routing
- Web Interface
- More Departments