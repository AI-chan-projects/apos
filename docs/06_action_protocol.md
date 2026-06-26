# 06_action_protocol.md

---

## 0. Purpose

This document defines the Action Protocol of APOS.

It formalizes how AIR-generated intent becomes executable behavior in the real system.

The Action Protocol is the boundary between:

- reasoning (AIR)
- reality (Execution + Events)

---

## 1. Core Principle

> Actions are the executable representation of AIR decisions.

An Action is not execution itself.

An Action is a *proposal for execution* subject to policy validation.

---

## 2. Action Definition

An Action is defined as:

- a structured execution intent
- derived from AIR inference
- validated by Policy Engine
- committed via Event generation

---

## 3. Action Lifecycle

### Step 1: AIR Generation

AIR produces:

- objective-aligned decision
- inferred variables
- candidate operations

---

### Step 2: Action Construction

AIR output is transformed into Action objects:

- action_type
- target resource
- parameters
- execution constraints

---

### Step 3: Policy Evaluation

Action is evaluated by Policy Engine:

- DENY → rejected immediately
- APPROVE → paused awaiting Human Director
- ALLOW → eligible for execution

---

### Step 4: Scheduling

Approved Actions are placed into Execution Queue:

- ready queue
- blocked queue
- deferred queue

---

### Step 5: Execution

Runtime system executes Action:

- deterministic execution
- single-worker sequential processing
- controlled resource access

---

### Step 6: Event Emission

Execution produces Events:

- success event
- failure event
- partial completion event

---

## 4. Action Structure

Each Action contains:

### 4.1 Identity

- action_id
- origin_air_node_id

---

### 4.2 Intent

- action_type
- objective alignment reference

---

### 4.3 Target

- resource_id
- resource type

---

### 4.4 Parameters

- structured input data
- execution configuration

---

### 4.5 Constraints

- policy constraints
- execution limits
- safety bounds

---

### 4.6 Risk Metadata

- risk_score
- policy evaluation result

---

## 5. Execution Model

APOS uses deterministic single-worker execution:

- one Action at a time
- strict ordering
- no concurrent mutation of shared state

---

## 6. Scheduling Model

Actions are categorized into queues:

### 6.1 Ready Queue
- approved for execution

### 6.2 Blocked Queue
- waiting for dependencies

### 6.3 Approval Queue
- waiting for Human Director

### 6.4 Failed Queue
- retry or compensation required

---

## 7. Failure Handling

Failures are first-class outcomes:

- Action Failure → Failure Event
- Retry logic → new Action
- Compensation → compensatory Action

No silent failures are allowed.

---

## 8. Action → Event Mapping

Every Action MUST produce at least one Event:

- ActionStartedEvent
- ActionCompletedEvent
- ActionFailedEvent

Events are the only permanent record of execution.

---

## 9. AIR Integration

Action is a direct projection of AIR nodes:

AIR Node → Action Candidate → Policy Evaluation → Execution

Traceability must be preserved:

- air_node_id must always be attached

---

## 10. Policy Binding

No Action can bypass Policy Engine.

Decision outcomes:

- DENY → Action is discarded
- APPROVE → Action is paused
- ALLOW → Action enters execution pipeline

---

## 11. Human Director Interaction

For APPROVE Actions:

- execution is paused
- approval event required
- Action resumes only after explicit decision

---

## 12. Invariants

- I1: All Actions originate from AIR
- I2: All Actions are policy-evaluated before execution
- I3: All Actions produce Events
- I4: No Action executes without explicit scheduling
- I5: Human Director can override APPROVE state
- I6: Execution is strictly sequential per worker

---

## 13. System Role

The Action Protocol is the execution bridge between:

- AIR (reasoning layer)
- Runtime (execution layer)
- Event Store (reality layer)

---

## 14. Design Principle

Actions are not commands.

Actions are:

> constrained hypotheses of execution validated before becoming reality

---

## 15. Final Model

AIR → Action → Policy Engine → Scheduler → Runtime → Event Store

---

## 16. Core Insight

If AIR is thought,

and Events are reality,

then Actions are:

> the fragile boundary where thought attempts to become real