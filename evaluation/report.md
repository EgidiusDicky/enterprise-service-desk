# Evaluation Report

## Overview

This document defines how the four evaluation metrics — Accuracy, Efficiency, Explainability, and Hallucination — are measured in the Enterprise Service Desk MVP.

---

## Accuracy

**Definition:** The degree to which the system's answer matches the correct information in the knowledge base.

**Evaluation Method:**

- Prepare a set of test queries with known ground-truth answers derived directly from the HR, IT, and Finance SOP documents.
- For each query, run the full pipeline: Supervisor routing → Agent retrieval → LLM response.
- Compare the generated answer against the ground-truth answer.
- Use exact keyword match or substring match for binary scoring (pass/fail).
- Report accuracy as: `(number of correct answers / total queries) × 100%`.

**Why this approach:** The MVP uses a local LLM and simple keyword routing. Complex semantic similarity scoring (e.g., BLEU, ROUGE, BERTScore) would add unnecessary overhead. Exact/substring matching is sufficient to verify that the system retrieves and reproduces the correct SOP content.

---

## Efficiency

**Definition:** The speed and resource cost of processing a single user query end-to-end.

**Evaluation Method:**

- Measure end-to-end latency for each query: time from query submission to answer delivery.
- Break down latency into three stages:
    1. **Routing time** — Supervisor Agent decides the target department.
    2. **Retrieval time** — Vector DB lookup and context extraction.
    3. **Generation time** — LLM produces the final answer.
- Record the total number of tokens consumed per query (input + output).
- Report average latency (in seconds) and average token consumption across all test queries.

**Why this approach:** The system runs entirely on local hardware (LM Studio + ChromaDB). Latency breakdown helps identify bottlenecks (e.g., slow LLM generation vs. fast vector search). Token count tracks cost if the model were served via API.

---

## Explainability

**Definition:** The ability to trace how the system arrived at a given answer.

**Evaluation Method:**

- For every generated answer, log the following artifacts:
    - **Routing decision** — Which department agent was selected and why (keyword match).
    - **Retrieved context** — The exact document chunks returned by the retriever.
    - **Validation result** — Whether the retrieved context passed the validation tool (non-empty check).
    - **LLM prompt** — The full prompt sent to the LLM (context + question).
- A human evaluator reviews the logs and answers:
    - *Can you see which document the answer came from?*
    - *Is the reasoning from context to answer clear?*
- Report the percentage of queries where a human can fully trace the answer back to the source document.

**Why this approach:** The MVP pipeline is already transparent by design (no black-box routing, no agent-to-agent communication). Logging each stage provides full traceability without requiring complex interpretability libraries.

---

## Hallucination

**Definition:** The presence of information in the generated answer that is not supported by the retrieved context.

**Evaluation Method:**

- For each test query, extract all factual claims from the generated answer.
- Cross-check each claim against the retrieved context (the document chunks provided to the LLM).
- A claim is marked as a hallucination if:
    - It contradicts the retrieved context.
    - It introduces information not present in the retrieved context.
    - It invents procedures, policies, or numbers that do not exist in the SOP documents.
- Report hallucination rate as: `(number of hallucinated claims / total claims) × 100%`.
- Additionally, report the percentage of queries that contain *at least one* hallucination.

**Why this approach:** Manual claim extraction and verification is appropriate for an MVP with a small test set. The retrieved context serves as the ground truth — any deviation is a hallucination. This method directly measures whether the LLM stays faithful to the provided documents.

---

## Summary

| Metric | Measurement | Target |
|---|---|---|
| Accuracy | Exact/substring match against ground truth | ≥ 80% |
| Efficiency | End-to-end latency & token consumption | < 30s per query |
| Explainability | Human-traceable answer path | ≥ 90% |
| Hallucination | Claim-level cross-check against context | < 10% |

Targets are baseline expectations for the MVP. These will be refined as the project matures.