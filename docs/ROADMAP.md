# PROJECT ROADMAP

## Phase 1 — Project Setup

- [ ] Create project structure
- [ ] Create Conda environment
- [ ] Install dependencies
- [ ] Setup Git repository

---

## Phase 2 — Knowledge Base

- [ ] Prepare HR SOP
- [ ] Prepare IT SOP
- [ ] Prepare Finance SOP

---

## Phase 3 — RAG Pipeline

- [x] Load Documents
- [x] Split Documents
- [ ] Initialize Embedding Model
- [ ] Store Vectors in ChromaDB
- [ ] Build Retriever

---

## Phase 4 — Agents

- [ ] HR Agent
- [ ] IT Agent
- [ ] Finance Agent

---

## Phase 5 - Agent Tool Design

Objective:

Design reusable tools that can be executed by each department agent.

Deliverables:

- Retrieve Tool
- Context Validation Tool
- Response Generation Tool

Output:

Each department agent owns a set of tools that can be executed as part of its workflow.

---

## Phase 6 - Department Agent

Implement:

- HR Agent
- IT Agent
- Finance Agent

Each agent should:

- Receive user query
- Execute retrieval tool
- Execute validation tool
- Generate answer

Each agent acts independently.

---

## Phase 7 — Supervisor Agent

- [ ] Simple keyword routing
- [ ] Route user request
- [ ] Call specialist agent

---

## Phase 8 — LLM Response

- [ ] Retrieve context
- [ ] Generate final answer

---

## Phase 9 — Evaluation

- [ ] Accuracy
- [ ] Hallucination
- [ ] Efficiency
- [ ] Explainability

---

## Future Improvements (Outside Scope)

- Semantic Router
- Agent Memory
- Reflection Agent
- Web UI
- API
- Graph RAG