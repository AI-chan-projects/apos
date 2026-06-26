# ADR-002: Human Director Integration

---

## Status
Accepted

---

## 0. AIR Context

This ADR defines the role of the **Human Director as a first-class participant in the AIR (APOS Intermediate Representation) lifecycle**.

### AIR Layers directly affected
- Objective (Goal definition and reinterpretation)
- Assumptions (validation and correction authority)
- Control (execution approval boundary)
- Validation (final truth arbitration)
- Meta (system-level correction authority)

---

## Context

APOS operates on AIR-based reasoning and execution flows.

Without a formal architectural integration of human authority into AIR, governance becomes external and reactive rather than structural.

This creates a critical risk:

> Human oversight becomes disconnected from the reasoning process itself.

To prevent this, Human Director must be embedded directly into the AIR lifecycle as a governing constraint and override layer.

---

## Decision

Introduce the **Human Director as a mandatory AIR Governance Actor**.

### Core Principle

> The Human Director is the final arbiter of AIR state transitions.

### Execution Model

- AIR may generate:
  - reasoning (Inference)
  - plans (Control mappings)
  - predictions (Prediction layer outputs)

- BUT the following require Human Director confirmation:
  - High-risk Action execution
  - Control variable activation affecting irreversible resources
  - Meta-layer modifications (AIR structure changes)
  - Conflict resolution in Validation failure cases

### Stop-and-Wait Semantics

For critical AIR transitions:

> Execution MUST halt until explicit Human Director decision is received.

This is not asynchronous notification.
This is a **system-level execution barrier**.

---

## Governance Mapping

HANDSOFIT:
- H (Human Agency) → elevated to AIR core constraint
- F (Formal Approval)
- D (Direct Intervention)
- O (Observability)

ARS:
- Accountability → fully mapped to Human Director
- Responsibility → shared execution, final authority centralized
- Sovereignty → Human Director retains ownership of AIR state

---

## Assumptions

- Human cognitive judgment is irreplaceable in ambiguous or high-risk AIR states
- Latent variables and assumptions may be incomplete or biased within AIR
- Automated reasoning systems cannot guarantee global safety alignment

---

## Invariants

- I1: All AIR Meta-layer modifications require Human Director approval
- I2: High-risk Control Actions cannot execute without Human confirmation
- I3: Human Director overrides supersede all AIR-derived decisions
- I4: Validation conflicts default to Human arbitration
- I5: AIR cannot self-modify governance boundaries

---

## Alternatives

### Fully autonomous AIR execution
Rejected due to:
- Loss of human epistemic control
- Risk of unchecked Meta-layer drift
- Governance irreversibility concerns

### Soft approval (notification-based)
Rejected due to:
- Lack of execution halt guarantees
- Risk of implicit system progression without human input

---

## Consequences

### Positive
- Strong human-system coupling within AIR lifecycle
- Explicit control boundaries over reasoning and execution
- Increased safety in meta-level modifications
- Clear accountability structure

### Negative
- Increased latency in decision-heavy workflows
- Human bottleneck in high-complexity systems
- Potential interruption of autonomous reasoning flow

---

## Future Revisit Conditions

This architecture may be revised if:

- Verified AI systems achieve formally proven alignment guarantees
- AIR validation mechanisms achieve human-equivalent judgment reliability
- Meta-layer safety can be guaranteed without external intervention

---

## AIR Meta Insight (Critical Design Principle)

Human Director is not external to AIR.

They are:

> the **final validation and override layer of the AIR system itself**

This ensures that:

- AIR generates reasoning
- Human validates reality alignment
- Governance enforces safety boundaries
- System evolves under controlled human authority

---

## Date
2026-06-26