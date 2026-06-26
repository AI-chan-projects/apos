# ADR-005: AIR Memory Architecture (Cognitive Layer System)

---

## Status
Accepted

---

## 0. AIR Context

Memory in APOS is not a storage system.

It is the **cognitive persistence layer of AIR (APOS Intermediate Representation)**.

### Core Principle

> Memory is AIR extended across time.

Memory is responsible for preserving:
- Inference traces (CoT)
- Validation history
- Event sequences
- Latent variable evolution
- Control decisions

---

## Context

APOS requires a memory system capable of supporting:

- long-horizon reasoning (multi-step AIR inference chains)
- iterative validation and correction
- knowledge accumulation across projects
- reproducible reasoning traces

Traditional memory systems separate:

- RAG (retrieval)
- logs (events)
- context windows (working memory)

In AIR-based architecture, this separation breaks consistency between:

> reasoning (CoT) and stored knowledge (RAG/Event/Memory)

---

## Decision

Adopt a **Unified Tiered AIR Memory Architecture**.

---

## Memory Layers (AIR-Aligned)

### 1. Working Memory (AIR Inference Buffer)

- Stores active CoT (Chain-of-Thought)
- Holds transient AIR inference state
- Contains:
  - current reasoning steps
  - intermediate hypotheses
  - temporary control variables

> This is the **live execution layer of AIR Inference**

---

### 2. Project Memory (AIR Event Projection Layer)

- Stores all Events from Event Sourcing
- Represents historical AIR execution traces
- Enables reconstruction of:
  - past reasoning paths
  - decision outcomes
  - validation results

> This is the **temporal memory of AIR**

---

### 3. Knowledge Base (AIR Latent Knowledge Layer / RAG)

- Vector + graph-based representation of distilled AIR history
- Contains:
  - latent variables
  - recurring inference patterns
  - generalized reasoning structures

> RAG is not external knowledge.
> It is **compressed AIR experience**

---

### 4. Governance Memory (AIR Meta Constraint Layer)

- Stores:
  - Policies
  - ADRs
  - AIR structural modifications
  - Governance decisions

> This layer defines **how AIR is allowed to evolve**

---

## Governance Mapping

HANDSOFIT:
- N (Non-concealment)
- O (Observability)

ARS:
- S (Sovereignty)

---

## Assumptions

- AIR inference traces (CoT) are persistent and reconstructable
- Knowledge can be safely compressed into latent representations
- Event history is sufficient to reconstruct system state
- Governance artifacts must remain immutable and traceable

---

## Invariants

- I1: All AIR Inference (CoT) must originate in Working Memory
- I2: All completed inference paths must be persisted as Events
- I3: Knowledge Base must be derived only from validated Event history
- I4: Governance Memory must be immutable except via ADR
- I5: No memory layer may bypass AIR validation pipeline
- I6: RAG retrieval must always be traceable back to Event lineage

---

## Alternatives

### Flat context window memory
Rejected due to:
- inability to preserve long-term reasoning structure
- loss of AIR trace continuity

### Independent RAG system (non-integrated)
Rejected due to:
- disconnect between reasoning and retrieval
- hallucination risk without Event grounding

### External knowledge graph only
Rejected due to:
- lack of direct linkage to AIR inference traces

---

## Consequences

### Positive
- Unified reasoning + memory architecture
- Full traceability from CoT → Event → Knowledge
- Strong support for long-term AIR evolution
- Enables learning from structured reasoning history

### Negative
- High system complexity
- Requires strict memory discipline enforcement
- Increased storage and computation requirements

---

## Future Revisit Conditions

This architecture must be revised if:

- AIR inference becomes partially stateless with external reconstruction guarantees
- RAG systems achieve native reasoning integration
- Event storage becomes too large for practical reconstruction without compression loss
- New memory paradigms unify retrieval and reasoning natively

---

## AIR Meta Insight (Critical Design Principle)

Memory is not a subsystem.

It is the **time-extended form of AIR cognition**.

This means:

- CoT = instantaneous AIR reasoning
- Events = recorded AIR actions
- RAG = compressed AIR history
- Governance Memory = constraints on AIR evolution

---

## Date
2026-06-26