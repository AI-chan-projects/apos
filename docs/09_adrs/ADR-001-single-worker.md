# ADR-001: Single Worker Architecture

---

## Status
Accepted

---

## 0. AIR Context

This ADR is grounded in AIR (APOS Intermediate Representation).

### Relevant AIR Layers
- Inference (CoT / reasoning trace)
- Control
- Validation
- Meta

### AIR Dependency
Single Worker architecture ensures that AIR inference traces (Chain-of-Thought) remain:

- Deterministic
- Sequential
- Reconstructable
- Auditable

---

## Context

APOS requires a stable execution environment to manage project lifecycles.

Within AIR-based reasoning systems, concurrent execution introduces a critical issue:

> Non-deterministic Inference Paths

If multiple workers execute AIR transformations concurrently:
- Inference traces diverge
- Control variable ordering becomes ambiguous
- Validation cannot reliably reconstruct reasoning paths

Therefore, reasoning determinism becomes a first-class constraint.

---

## Decision

Adopt a **Single Worker Architecture per APOS instance**.

### Key Principle

> AIR Inference must be executed sequentially within a single deterministic reasoning stream.

### Execution Model

- One worker per APOS instance
- All AIR transformations are executed sequentially
- CoT (Chain-of-Thought) is preserved as the **Inference Trace**
- Parallelism is achieved only via horizontal scaling (multiple isolated instances)

---

## Governance Mapping

HANDSOFIT:
- S (Safety First)
- O (Observability)

---

## Assumptions

- AIR Inference correctness depends on ordered reasoning traces
- CoT is not optional explanation, but a required AIR execution artifact
- Distributed reasoning introduces unacceptable ambiguity in validation
- Container-level isolation is sufficient for scaling

---

## Invariants

- I1: AIR Inference must be strictly sequential within a single instance
- I2: CoT (Inference Trace) must be fully recorded for every Action
- I3: Event ordering must match AIR execution order
- I4: No concurrent modification of AIR state within a single instance

---

## Alternatives

### Multi-worker internal concurrency
Rejected due to:
- Non-deterministic AIR inference paths
- Loss of traceability in CoT
- Broken validation consistency

### Fully distributed shared-state inference
Rejected due to:
- Event ordering ambiguity
- Control variable race conditions
- Governance enforcement complexity

---

## Consequences

### Positive
- Deterministic AIR reasoning
- Fully reconstructable CoT (Inference Trace)
- Simplified governance enforcement
- Strong auditability of reasoning paths

### Negative
- Reduced internal parallelism
- Increased reliance on horizontal scaling
- Potential latency in long inference chains

---

## Future Revisit Conditions

This decision must be revisited if:

- AIR inference becomes partially parallelizable with deterministic guarantees
- New execution models support ordered CoT merging
- Distributed reasoning frameworks achieve strict trace ordering guarantees
- Resource constraints make single-worker execution infeasible

---

## AIR Meta Note (Important Insight)

This ADR establishes a foundational principle:

> In APOS, reasoning determinism is more important than execution concurrency.

CoT is not an optional debugging artifact.

It is the **formalized Inference Layer of AIR**, required for:

- Validation
- Prediction comparison
- Meta-layer updates
- Governance enforcement

---

## Date
2026-06-26