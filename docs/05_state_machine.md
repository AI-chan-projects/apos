# 05_state_machine.md

---

## 0. Purpose

This document defines the State Machine model of APOS.

It formalizes how system state is derived from Events through deterministic projection.

State in APOS is not stored.

State is computed.

---

## 1. Core Principle

> State is a projection of the Event Store.

Formally:

State = Projection(Event Store)

There is no independent state mutation outside Event processing.

---

## 2. State Machine Definition

The APOS State Machine is:

- deterministic
- event-driven
- replayable
- immutable-source based

It transforms a sequence of Events into a consistent system state.

---

## 3. State Components

The global system state is composed of:

### 3.1 Project State

- project lifecycle stage
- goal progress
- task completion status

---

### 3.2 Execution State

- active execution slices
- queued actions
- blocked or failed actions

---

### 3.3 Resource State

- external resources (files, APIs, models)
- internal resources (memory, cache, knowledge base)

---

### 3.4 Governance State

- policy evaluation status
- approval pending actions
- human director decisions

---

### 3.5 Memory State

- working memory
- project memory
- knowledge base projections

---

## 4. State Transition Model

State transitions occur only via Events.

### Transition Rule

Event → State Transition Function → New State

No direct mutation is allowed.

---

## 5. Projection Function

The projection function is defined as:

State_t = Projector(State_t-1, Event_t)

Where:

- State_t-1 is previous state snapshot
- Event_t is the incoming event
- State_t is the resulting state

---

## 6. Determinism Rule

Given identical event sequences:

- state reconstruction must always be identical
- no randomness is allowed in projection logic

---

## 7. State Layers

APOS defines hierarchical state layers:

### 7.1 Ephemeral State

- execution slices
- runtime queues
- transient computations

---

### 7.2 Persistent State

- project progress
- resource status
- policy history

---

### 7.3 Derived State

- inferred relationships
- dependency graphs
- aggregated metrics

Derived state is recomputed, not stored.

---

## 8. Event Dependency

State updates depend strictly on Event ordering:

- causal order takes priority
- timestamp order is secondary
- execution slice ordering is authoritative within local scope

---

## 9. Failure State Handling

Failures do not break state consistency.

Failure Events:

- update execution state
- trigger recovery transitions
- may spawn compensatory states

---

## 10. Consistency Model

APOS uses eventual consistency over Event replay:

- state is always reconstructable
- intermediate states may be transient
- final consistency is guaranteed through replay

---

## 11. Replay Semantics

State can be reconstructed by:

Event Store → Sequential Replay → State Projection → Current State

Replay must be deterministic under identical inputs.

---

## 12. AIR Integration

State is directly derived from AIR execution outputs:

- AIR node → Action → Event → State transition

Traceability chain:

AIR → Event → State

---

## 13. Policy Integration

State reflects policy outcomes:

- DENY actions produce no state mutation
- APPROVE actions remain pending until resolved
- ALLOW actions update state immediately after execution

---

## 14. Invariants

- I1: State is always derived from Events
- I2: State cannot be directly modified
- I3: State reconstruction must be deterministic
- I4: Every state change must have an Event origin
- I5: Derived state is never persisted as source of truth

---

## 15. System Role

The State Machine is the interpretive layer between:

- Event history (truth)
- Runtime behavior (execution)
- AIR reasoning (intent)

---

## 16. Design Principle

State is not memory.

State is:

> the current shape of reality reconstructed from history

---

## 17. Final Model

Event Store → Projection Function → State Machine → System State

---

## 18. Core Insight

If Events are APOS reality,

then State is:

> the current snapshot of that reality as interpreted through projection