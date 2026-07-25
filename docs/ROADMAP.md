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
- [x] Initialize Embedding Model
- [x] Store Vectors in ChromaDB

---

## Phase 4 — Retriever

- [ ] Build Retriever from ChromaDB
- [ ] Retrieve relevant documents
- [ ] Return context

---

## Phase 5 — Tool Layer

Objective:

Implement reusable tools that can be executed by each department agent.

Deliverables:

- [ ] Retrieve Tool
- [ ] Context Validation Tool
- [ ] Response Generation Tool
- [ ] Workflow Action Tool

Output:

Department agents use tools instead of directly accessing the RAG pipeline.

---

## Phase 6 — Department Agents

Implement:

- [ ] HR Agent
- [ ] IT Agent
- [ ] Finance Agent

Each agent should:

- Receive user query
- Execute Retrieve Tool
- Execute Context Validation Tool
- Execute Response Generation Tool
- Execute Workflow Action Tool (if required)

---

## Phase 7 — Supervisor Agent

- [ ] Detect user intent
- [ ] Route request to department agent
- [ ] Return department response

---

Phase 8 — Enterprise Automation

Simulation only.

Implement:

- [ ] Leave Request Workflow
- [ ] IT Ticket Workflow
- [ ] Reimbursement Workflow

Store workflow state using JSON files.

---

## Phase 9 — Evaluation

Evaluate:

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
- Authentication
- SQL Database
- REST API
- Graph RAG
- MCP Tool Server