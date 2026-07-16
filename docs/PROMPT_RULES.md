# PROMPT RULES

## Purpose

This document defines mandatory instructions for any AI coding assistant working on this repository.

The objective is to build a **Minimum Viable Product (MVP)** for an academic project.

This project prioritizes:

- Simplicity
- Readability
- Maintainability
- Fast implementation

This is **NOT** a production-ready enterprise system.

---

# Project Goal

Build a simple Enterprise Internal Service Desk using:

- Multi-Agent LLM
- Retrieval-Augmented Generation (RAG)
- ChromaDB
- LangChain
- Local LLM (LM Studio)

The objective is to demonstrate the architecture, not to build a commercial product.

---

# General Rules

Always follow:

- KISS (Keep It Simple)
- YAGNI (You Aren't Gonna Need It)
- DRY (Don't Repeat Yourself)

Prefer readable code over clever code.

Avoid unnecessary abstraction.

Avoid unnecessary optimization.

---

# Scope Limitation

Never expand the project outside the roadmap.

The project only contains:

- 1 Supervisor Agent
- 3 Specialist Agents
    - HR
    - IT
    - Finance

Nothing else.

---

# Forbidden Features

Never implement:

- Authentication
- Login
- Registration
- REST API
- FastAPI
- Flask
- Django
- Streamlit
- Web UI
- SQL Database
- PostgreSQL
- MySQL
- Redis
- Docker
- Kubernetes
- RabbitMQ
- Celery
- GraphRAG
- Reflection Agent
- Planning Agent
- Memory Agent
- Multi-step reasoning framework
- Tool Calling
- Function Calling
- Internet Search

Unless explicitly requested by the developer.

---

# Code Style

Prefer:

Small modules

Small classes

Small functions

Single Responsibility

Meaningful naming

Type hints where appropriate

Minimal comments

Self-explanatory code

---

# Project Structure

Never change the folder structure unless instructed.

Current structure:

app/

knowledge_base/

docs/

tests/

Do not create unnecessary folders.

---

# Dependency Rules

Only use dependencies listed in requirements.txt.

Never introduce new packages without explicit approval.

Always prefer the Python standard library whenever possible.

---

# Multi-Agent Rules

There is only one Supervisor Agent.

Supervisor Agent only decides which department should answer.

Supervisor Agent must never answer directly.

Each department agent:

- Owns its own knowledge
- Retrieves context from its own documents
- Generates its own answer

Agents never communicate with each other.

Only the Supervisor communicates with department agents.

---

# Routing Rules

Current routing is intentionally simple.

Use keyword routing.

Do NOT implement semantic routing.

Do NOT implement LLM routing.

Do NOT implement classifier models.

Simple routing is enough for the MVP.

---

# RAG Rules

Each department has:

Own PDF

↓

Own Embedding

↓

Own Chroma Collection

↓

Own Retriever

Never merge all departments into a single knowledge base.

---

# Error Handling

Fail gracefully.

Return clear error messages.

Never crash because:

PDF not found

Vector DB missing

Empty query

Model unavailable

---

# Coding Philosophy

Whenever there are multiple possible implementations:

Always choose:

- fewer files
- fewer classes
- fewer abstractions
- fewer dependencies
- fewer lines of code

The simplest correct solution is always preferred.

---

# Before Writing Code

Before generating any code, always ask yourself:

Does this feature exist in the roadmap?

Does this feature satisfy the MVP?

Can this be implemented more simply?

Am I introducing unnecessary complexity?

If the answer is YES,

DO NOT implement it.

---

# Completion Criteria

The implementation is complete when:

1. User asks a question.

2. Supervisor routes to the correct department.

3. Department retrieves relevant documents.

4. Context is passed to the LLM.

5. LLM generates the answer.

No additional functionality is required.

---

# Developer Communication

Never assume missing requirements.

If a requirement is ambiguous:

Do not invent a complex solution.

Instead:

- choose the simplest reasonable implementation, or
- ask for clarification before making architectural changes.

Architecture decisions must remain consistent with PROJECT_RULES.md and ROADMAP.md.

The AI assistant is expected to act as a software engineer following an existing architecture, not as a software architect redesigning the project.