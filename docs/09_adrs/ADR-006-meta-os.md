# ADR-006: Meta-OS Definition (APOS as AIR-Integrated Operating System)

---

## Status
Accepted

---

## 0. AIR Context

APOS is not a replacement for AIR (APOS Intermediate Representation).

It is the **operating system that executes, constrains, and evolves AIR over time**.

### Core Relationship

- AIR = Cognitive Reasoning Layer
- APOS = System Execution Layer for AIR

APOS provides:
- execution environment for AIR inference
- governance enforcement over AIR actions
- memory persistence of AIR traces
- orchestration of AIR-driven projects

---

## Context

Modern AI systems typically separate:

- reasoning (model logic)
- execution (system runtime)
- memory (storage)
- governance (policy layer)

This separation leads to fragmentation:

> reasoning cannot directly control execution or memory evolution

APOS solves this by integrating AIR as the central cognitive substrate of the system.

---

## Decision

Define APOS as a **Meta-Operating System that natively executes AIR-based systems**.

---

## APOS Architectural Model

### 1. AIR (Cognitive Layer)
- Inference (CoT)
- Prediction
- Control variable generation
- Validation logic

---

### 2. APOS Kernel (Execution Layer)
Responsible for:
- Task execution
- Agent lifecycle management
- Resource allocation
- Event handling

---

### 3. Governance Layer
- HANDSOFIT constraints
- ARS ownership model
- Human Director override system
- Policy Engine enforcement

---

### 4. Memory Layer
- Event Store (temporal truth)
- RAG Knowledge Base (compressed AIR history)
- Working Memory (live AIR inference)
- Governance Memory (system evolution rules)

---

## Architectural Principle

- Applications run on APOS as AIR-driven Projects
- Projects are orchestrated via AIR inference + execution loop
- All system behavior must be traceable to AIR reasoning paths
- Governance constrains AIR execution, not replaces it

---

## Governance Mapping

ARS:
- A (Accountability)
- R (Responsibility)
- S (Sovereignty)

---

## Assumptions

- AIR is the canonical reasoning system for all APOS operations
- System execution must be traceable to AIR inference paths
- Governance must operate without breaking AIR determinism
- Kernel-layer execution is deterministic and event-sourced

---

## Invariants

- I1: All APOS operations must originate from AIR inference or governance triggers
- I2: No execution occurs without AIR-derived intent or Human Director override
- I3: Memory is always a projection of AIR execution history
- I4: Governance cannot bypass AIR execution traceability
- I5: APOS kernel must remain deterministic under single-worker execution model

---

## Alternatives

### Pure AIR system (no OS layer)
Rejected due to:
- lack of execution control
- absence of resource management
- no persistent system orchestration

### Traditional OS + AI plugin model
Rejected due to:
- AIR disconnected from execution layer
- weak governance integration
- fragmented memory systems

---

## Consequences

### Positive
- Unified cognitive + execution architecture
- Strong traceability from reasoning to system state
- Enables full lifecycle project orchestration
- Supports scalable AIR-driven automation systems

### Negative
- High system complexity
- Tight coupling between reasoning and execution layers
- Requires strict discipline in AIR trace preservation

---

## Future Revisit Conditions

This architecture may be revised if:

- AIR becomes a standardized external reasoning protocol
- OS-level AI orchestration frameworks emerge
- Execution environments support native reasoning integration
- Governance can be safely externalized without system coupling

---

## AIR Meta Insight (Critical Design Principle)

APOS is not above AIR.

APOS is the **execution substrate that makes AIR operational in the real world**.

In other words:

> AIR thinks  
> APOS acts  
> Governance constrains  
> Memory remembers  

---

## Date
2026-06-26