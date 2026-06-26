# 18_AIR-execution-semantics.md

---

## 0. Purpose

This document defines the execution semantics of AIR within APOS.

It specifies how AIR is transformed into deterministic runtime behavior through:

- action scheduling
- concurrency control
- failure handling
- consistency guarantees

AIR does not execute directly. It is compiled into execution traces.

---

## 1. Core Execution Model

AIR produces:

- Action Candidates
- Execution Graph (DAG)
- Policy-Annotated Nodes

Execution is performed by a Single Worker Runtime Scheduler.

---

## Execution Flow

AIR  
→ Execution Graph  
→ Scheduler  
→ Action Runtime  
→ Event Store  

---

## 2. Action Scheduling Semantics

---

## 2.1 Scheduling Principle

Execution follows a deterministic DAG traversal under policy constraints.

---

## 2.2 Scheduling Rules

### Rule 1: Dependency-First Execution

An action is eligible for execution only if:

- all parent nodes are completed
- required state dependencies are satisfied

---

### Rule 2: Policy Gate Before Scheduling

No action enters the execution queue without passing the Policy Engine.

Policy validation occurs before scheduling, not during execution.

---

### Rule 3: Priority Model

Scheduling priority is determined by:

- Goal criticality
- Dependency depth in the execution graph
- Policy risk level
- Human Director overrides

---

## 2.3 Scheduling Queues

The scheduler maintains three logical queues:

- Ready Queue: executable actions
- Blocked Queue: waiting on dependencies
- Rejected Queue: policy-denied actions

---

## 3. Concurrency Model

---

## 3.1 Fundamental Constraint

APOS enforces a single-worker execution model internally.

Concurrency is achieved through controlled interleaving, not parallel execution.

---

## 3.2 Execution Unit

The atomic unit of concurrency is the Execution Slice.

An Execution Slice represents:

- a single action step
- a single state transition
- a single event emission boundary

---

## 3.3 Interleaving Strategy

The scheduler may interleave execution across:

- tasks
- projects
- stages

However, interleaving is only allowed at execution slice boundaries.

---

## 3.4 Concurrency Constraints

Two actions must never:

- modify the same resource state simultaneously
- violate DAG ordering constraints
- bypass dependency resolution rules

---

## 3.5 Resulting Model

Concurrency is modeled as deterministic time-slicing over a single execution lane.

---

## 4. Failure Model

---

## 4.1 Failure as First-Class Entity

Failures are not exceptions.

They are structured events in the system.

---

## 4.2 Failure Types

### 1. Policy Failure
- Action rejected before execution
- No state mutation occurs

### 2. Execution Failure
- Action started but did not complete successfully
- Partial effects may exist

### 3. Resource Failure
- External dependency failure
- API, filesystem, or model unavailability

### 4. Logical Failure
- AIR inconsistency or invalid inference
- incorrect assumptions or contradictions

---

## 4.3 Failure Handling Pipeline

Failure is processed as:

Failure → Event Emission → State Update → Recovery Decision → Meta Feedback

---

## 4.4 Recovery Strategies

### Retry
Re-execution with identical parameters under deterministic conditions.

### Compensation
Execution of inverse or corrective actions where applicable.

### Abort Branch
Termination of a specific execution branch in the DAG.

### Degraded Execution
Continuation with reduced capability or fallback paths.

---

## 4.5 Failure Containment Rule

Failures must be:

- isolated within execution boundaries
- explicitly recorded as events
- prevented from silently mutating global state

---

## 5. Consistency Model

---

## 5.1 Event Sourcing Consistency

All system states are derived from immutable event history.

State is never directly mutated.

---

## 5.2 AIR-State Consistency Rule

System state is defined as:

State = Projection(Event Store)

---

## 6. Determinism Model

Given identical:

- Markdown input
- AIR structure
- Policy state
- Event history

The system must produce identical execution traces.

---

## 7. Meta Feedback Loop

Execution outcomes feed back into:

- AIR Meta Layer
- inference refinement
- scheduling optimization
- policy evolution proposals

---

## 8. System Summary

---

## Execution Stack

- AIR: cognitive structure
- Execution Graph: planned actions
- Scheduler: deterministic interpreter
- Runtime: execution engine
- Event Store: system truth ledger

---

## 9. Core Insight

AIR is not executed directly.

It is compiled into deterministic execution traces governed by policy and event sourcing.

---

## 10. Final Model

Execution semantics consist of:

- scheduling rules
- concurrency constraints
- failure handling
- consistency guarantees

Together they define how cognition becomes execution in APOS.