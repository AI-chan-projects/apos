# ADR-007: Policy Engine (AIR Control Law Layer)

---

## Status
Accepted

---

## 0. AIR Context

The Policy Engine is the **physical constraint layer of AIR (APOS Intermediate Representation)**.

If AIR defines *thought and decision generation*, then:

> The Policy Engine defines what AIR is allowed to become in reality.

It operates as the **control law system between AIR and execution**.

---

## Context

In AIR-based systems, reasoning alone is insufficient to guarantee:

- safety
- correctness
- governance compliance
- deterministic execution

Without a strict enforcement layer, AIR-generated actions may:

- violate governance constraints
- bypass Human Director authority
- create unsafe state transitions

Therefore, a deterministic enforcement layer is required between:

> AIR Control Variables → System Execution

---

## Decision

Implement a **deterministic, non-bypassable Policy Engine** that governs all AIR-derived Actions.

---

## Policy Engine Definition

The Policy Engine evaluates all AIR-derived Actions before execution.

### Evaluation Input:
- AIR Inference output (CoT trace)
- Control Variables
- Target Resources
- Current System State (Event Projection)
- Governance Context

---

## Policy Evaluation Order (Deterministic Constraint)

All Actions must pass through the following ordered gates:

### 1. DENY (Hard Constraint Layer)
- Absolute prohibition rules
- Overrides all other logic
- Immediately blocks execution

### 2. APPROVAL REQUIRED (Human Director Gate)
- Requires Human Director intervention
- Converts Action into Stop-and-Wait AIR state
- Blocks execution until explicit approval Event

### 3. ALLOW (Execution Permit)
- Action is valid under AIR + Governance constraints
- May proceed to execution layer

---

## Governance Mapping

HANDSOFIT:
- S (Safety First)
- F (Formal Approval)
- I (Improvement Control)
- T (Task Privilege)

---

## Assumptions

- Policies can be expressed as a deterministic DSL
- AIR inference outputs are structured and traceable
- All Actions originate from validated AIR reasoning paths
- Governance rules are globally consistent across system state

---

## Invariants

- I1: No Action may bypass Policy Engine evaluation
- I2: Policy evaluation order is strictly deterministic
- I3: DENY overrides all other evaluation results
- I4: APPROVAL REQUIRED must trigger execution halt
- I5: All policy decisions must be logged as Events
- I6: Policy Engine must be independent of AIR inference logic
- I7: Policies must be versioned and auditable

---

## Alternatives

### Inline conditional checks inside execution layer
Rejected due to:
- inconsistent enforcement
- lack of global governance visibility
- fragmented rule updates

### AI-based dynamic policy evaluation
Rejected due to:
- non-deterministic governance decisions
- inability to guarantee safety constraints
- loss of auditability

---

## Consequences

### Positive
- Strong enforcement of AIR execution constraints
- Centralized governance control point
- Deterministic safety and approval flow
- Clear separation between reasoning and enforcement

### Negative
- Increased system rigidity
- Requires careful DSL design
- Potential bottleneck in high-throughput systems

---

## Future Revisit Conditions

This architecture must be revisited if:

- AI-based formal verification systems guarantee policy correctness
- Policy evaluation can be proven deterministic under probabilistic models
- Governance shifts toward distributed decision-making systems
- AIR inference and policy evaluation merge into unified formal system

---

## AIR Meta Insight (Critical Design Principle)

The Policy Engine is not a filter.

It is the **physical law layer of AIR execution**.

In APOS:

- AIR generates possibilities
- Policy Engine defines permissible reality
- Execution layer materializes approved states
- Event Store records the resulting truth

---

## Date
2026-06-26