# PROJECT RULES

## Project Overview

Project ini merupakan implementasi sederhana (MVP) dari Enterprise Internal Service Desk menggunakan pendekatan Multi-Agent LLM dengan Retrieval-Augmented Generation (RAG).

Tujuan utama project adalah memenuhi kebutuhan Final Project mata kuliah, bukan membangun produk enterprise yang siap digunakan di dunia nyata.

---

# Core Principles

- Keep It Simple (KISS)
- You Aren't Gonna Need It (YAGNI)
- Minimum Viable Product (MVP)
- Readability over Complexity
- Modular Code
- Reproducible Environment

---

# Project Scope

Project hanya memiliki:

- 1 Supervisor Agent
- 3 Specialist Agents
    - HR Agent
    - IT Agent
    - Finance Agent

Setiap agent memiliki knowledge sendiri berupa dokumen SOP.

---

# Technology Stack

Programming Language

- Python 3.11

Framework

- LangChain

Vector Database

- ChromaDB

Embedding

- Sentence Transformers

LLM

- LM Studio (OpenAI Compatible API)

Document Loader

- PyPDF

---

# Features Included

✓ Load PDF SOP

✓ Text Chunking

✓ Embedding

✓ Vector Database

✓ Retrieval

✓ Multi-Agent Routing

✓ LLM Answer Generation

✓ Basic Evaluation

---

# Features NOT Included

❌ Authentication

❌ Login System

❌ User Management

❌ SQL Database

❌ REST API

❌ Web Dashboard

❌ Docker

❌ Kubernetes

❌ Redis

❌ Celery

❌ RabbitMQ

❌ Graph RAG

❌ Agent Memory

❌ Reflection Agent

❌ Planning Agent

❌ Tool Calling

❌ Voice Interface

---

# Coding Guidelines

- Function should do one thing.
- Keep files small.
- Avoid duplicate code.
- Prefer composition over inheritance.
- Avoid premature optimization.
- Avoid unnecessary abstraction.
- Use meaningful naming.
- Every module should have a single responsibility.

---

# AI Coding Rules

When generating code:

- Always choose the simplest implementation.
- Do not add features outside the roadmap.
- Do not introduce new dependencies unless necessary.
- Do not create unnecessary design patterns.
- Avoid over-engineering.
- Focus on readability and maintainability.

---

# Definition of Done

Project is considered complete when:

1. User asks a question.
2. Supervisor Agent routes to correct department.
3. Agent retrieves information from its own Vector Database.
4. LLM generates answer based on retrieved context.
5. System can be evaluated using predefined metrics.