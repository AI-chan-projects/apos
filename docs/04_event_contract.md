# 04_event_contract.md

---

## 0. Purpose

This document defines the Event Contract model of APOS.

It establishes the canonical definition of an Event as the atomic unit of system truth.

All system behavior in APOS is ultimately expressed as an immutable sequence of Events.

---

## 1. Core Definition

An Event is:

> an immutable record of a state transition or completed action within APOS.

Events are the only source of truth for system state reconstruction.

---

## 2. Event Properties

Every Event must contain the following fields:

### 2.1 Identity

- event_id: unique identifier
- timestamp: logical execution time
- source: originating subsystem (AIR / Runtime / Policy Engine)

---

### 2.2 Causality

- parent_event_id: optional reference to causally prior event
- causation_type: direct | derived | compensatory

---

### 2.3 Action Linkage

- action_id: associated execution unit
- action_type: type of operation performed

---

### 2.4 State Delta

- state_changes: explicit description of system mutation
- resource_targets: affected resources

---

### 2.5 Policy Trace

- policy_decision: DENY | ALLOW | APPROVE
- risk_score: numeric value [0.0 - 1.0]
- policy_context: evaluation metadata

---

### 2.6 AIR Traceability

- air_node_id: originating AIR node
- inference_hash: optional compressed reasoning reference
- execution_slice_id: runtime execution unit reference

---

## 3. Event Types

APOS defines four primary event categories:

### 3.1 Action Event
Represents successful execution of an action.

### 3.2 Failure Event
Represents failed or partially completed execution.

### 3.3 Policy Event
Represents policy evaluation outcomes (DENY / APPROVE / ALLOW decisions).

### 3.4 System Event
Represents internal system state transitions (scheduler, memory, runtime).

---

## 4. Event Lifecycle

Events follow a strict lifecycle:

### Step 1: Generation
Created by Runtime or Policy Engine

### Step 2: Validation
Ensures schema integrity and policy compliance

### Step 3: Commitment
Persisted to Event Store (immutable append-only log)

### Step 4: Projection
Used to reconstruct system state

---

## 5. Immutability Contract

Once committed:

- Events cannot be modified
- Events cannot be deleted
- Events cannot be reordered

Any correction must be expressed as a new compensatory Event.

---

## 6. Causality Model

Events form a directed causal graph:

- each event may reference previous events
- causality is explicit, not inferred
- no hidden state transitions are allowed

---

## 7. Event Ordering Model

Ordering is defined by:

- logical timestamp
- dependency resolution
- execution slice order

Total ordering is not required globally, but required per causal chain.

---

## 8. Event Store Contract

The Event Store guarantees:

- append-only storage
- deterministic replay
- full state reconstruction
- auditability of all transitions

---

## 9. Failure Representation

Failures are first-class Events.

A failure event must include:

- failure_type
- root_cause (if known)
- recovery_action (if applicable)

Failures do not break system flow; they extend the event chain.

---

## 10. Replay Semantics

System state is reconstructed via:

Event Store → Replay → State Projection → Current State

Replay must produce identical state under identical conditions.

---

## 11. AIR Integration

Each Event must trace back to AIR:

- air_node_id (mandatory)
- inference context (optional)
- execution graph reference (if applicable)

This ensures full cognitive traceability.

---

## 12. Policy Integration

Every Event must contain policy metadata:

- decision (DENY / ALLOW / APPROVE)
- risk_score
- policy evaluation source

Policy decisions are immutable once recorded.

---

## 13. System Invariants

- I1: All system state originates from Events
- I2: Events are immutable and append-only
- I3: Every Action produces at least one Event
- I4: Every Event must be traceable to AIR or system origin
- I5: Policy decisions are permanently recorded
- I6: No hidden state transitions are allowed

---

## 14. Design Principle

Events are not logs.

They are:

> the physical reality layer of APOS

---

## 15. Final Model

Event =

- Identity
- Causality
- Action Link
- State Delta
- Policy Trace
- AIR Trace

---

## 16. Core Insight

If AIR is cognition,

and Actions are behavior,

then Events are:

> reality itself inside APOS