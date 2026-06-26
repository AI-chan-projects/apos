# ADR-003: Event Sourcing

---

## Status
Accepted

---

## 0. AIR Context

Event Sourcing in APOS is the **temporal persistence layer of AIR (APOS Intermediate Representation)**.

### AIR Layers mapped to Event Sourcing

- Inference → produces Action candidates
- Control → determines execution intent
- Validation → determines event validity
- Meta → evolves system based on event history

### Core Principle

> Events are the physical trace of AIR execution over time.

---

## Context

Traditional snapshot-based state systems obscure:

- reasoning paths (AIR Inference traces)
- decision history
- validation outcomes
- control flow evolution

In AIR-based systems, this loss is unacceptable because:

> The reasoning process is as important as the final state.

Therefore, system state must be fully reconstructable from historical AIR execution traces.

---

## Decision

Adopt **Event Sourcing as the canonical persistence model for APOS**.

### Definition

Each Event represents:

> A validated transition from AIR-derived Action into system-relevant state change.

---

## Governance Mapping

HANDSOFIT:
- A (Auditability)
- O (Observability)
- N (Non-concealment)

---

## Assumptions

- AIR execution produces traceable, discrete state transitions
- Event volume is manageable through archiving and compression strategies
- AIR inference paths must remain reconstructable indefinitely

---

## Invariants

- I1: Events are immutable and append-only
- I2: Every Event must originate from a validated AIR-derived Action
- I3: State is derived solely from Event projection (State = Projection(Event Store))
- I4: No Event exists without an associated AIR Inference Trace (CoT)
- I5: Event ordering must preserve AIR execution order
- I6: Events cannot be rewritten, only appended or superseded via Meta Events

---

## Alternatives

### CRUD snapshot model
Rejected due to:
- Loss of AIR inference traceability
- Inability to reconstruct reasoning paths
- Weak validation history linkage

### Partial event logging (non-exhaustive)
Rejected due to:
- Broken AIR → Event trace continuity
- Incomplete validation reconstruction

---

## Consequences

### Positive
- Full AIR reasoning traceability (Inference → Action → Event)
- Enables time-travel debugging of reasoning processes
- Supports Meta-layer learning from historical AIR behavior
- Strong auditability of system decisions

### Negative
- Increased storage requirements
- Higher complexity in state reconstruction
- Requires event compaction/archival strategy

---

## Future Revisit Conditions

This architecture may be revisited if:

- Event volume exceeds scalable storage architecture
- Distributed event ordering can be guaranteed more efficiently
- AIR inference becomes partially stateless with guaranteed reconstruction

---

## AIR Meta Insight (Critical Understanding)

Event Sourcing is not a persistence strategy.

It is the **physical memory layer of AIR execution**.

It ensures:

- AIR reasoning is never lost
- Decisions are always reconstructable
- System evolution is fully observable over time

---

## Date
2026-06-26