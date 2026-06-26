# 20_execution_runtime_kernel.md

---

## 0. Purpose

This document defines the Execution Runtime Kernel of APOS.

It is the lowest-level execution layer responsible for turning Actions into deterministic system behavior.

If APOS is an operating system, this kernel is its execution heartbeat.

---

## 1. Core Principle

> The Runtime Kernel executes one atomic step at a time in a deterministic loop.

All system behavior is reduced to a sequence of execution ticks.

There is no parallel execution inside a single APOS instance.

---

## 2. Execution Model Overview

APOS Runtime operates as a continuous loop:

Event Queue → Scheduler → Execution Kernel → Runtime → Event Store

Each iteration of this loop is called an Execution Tick.

---

## 3. Execution Tick Definition

An Execution Tick is a single deterministic unit of system progress.

Each tick performs exactly one of:

- Action execution
- Action scheduling
- Policy resolution handling
- Failure recovery
- State synchronization

---

## 4. Kernel Loop

The runtime kernel operates as:

1. Fetch next Action
2. Validate execution eligibility
3. Apply scheduling rules
4. Execute Action (if allowed)
5. Emit Events
6. Update runtime state
7. Persist to Event Store
8. Update internal queues

Repeat indefinitely.

---

## 5. System Queues

The kernel manages four primary queues:

### 5.1 Ready Queue
Actions approved for execution.

### 5.2 Blocked Queue
Actions waiting for dependencies or external conditions.

### 5.3 Approval Queue
Actions awaiting Human Director decision.

### 5.4 Failed Queue
Actions requiring retry or compensation logic.

---

## 6. Scheduler Logic

The scheduler selects Actions based on:

- priority score
- dependency resolution
- risk evaluation result
- resource availability
- policy state

Selection is deterministic given identical input state.

---

## 7. Execution Semantics

Each Action execution follows strict rules:

- single-thread execution only
- no concurrent mutation of shared state
- deterministic input → output mapping
- all side effects must produce Events

---

## 8. Kernel State Model

The runtime kernel maintains ephemeral state:

- current tick index
- active Action
- queue snapshots
- temporary execution context

This state is not persisted as source of truth.

Only Events are persisted.

---

## 9. Failure Handling Model

Failures are first-class execution outcomes.

### 9.1 Failure Types

- Execution Failure
- Policy Rejection Failure
- Resource Unavailable Failure
- System Constraint Violation

---

### 9.2 Failure Response

When failure occurs:

1. Generate Failure Event
2. Update Failed Queue
3. Optionally schedule compensatory Action
4. Continue execution loop

No failure halts the kernel unless explicitly configured as fatal.

---

## 10. Blocking Model

An Action enters blocked state if:

- dependency Actions not completed
- required Event not present
- external condition unmet

Blocked Actions are re-evaluated each tick.

---

## 11. Approval Model Integration

If Policy Engine returns APPROVE:

- Action is moved to Approval Queue
- Kernel pauses execution of that Action
- Human Director event is required
- Execution resumes only after approval event

---

## 12. Event Emission Contract

Each tick may emit one or more Events:

- ActionStartedEvent
- ActionCompletedEvent
- ActionFailedEvent
- SchedulerEvent
- StateSyncEvent

Events are immediately forwarded to Event Store.

---

## 13. Determinism Guarantee

Given identical:

- Event history
- Action set
- Policy state

The Runtime Kernel must produce:

> identical execution trace

No randomness is allowed inside kernel logic.

---

## 14. Concurrency Model

APOS Runtime enforces:

- single-worker execution
- no parallel action execution
- external horizontal scaling only via multiple APOS instances

Concurrency is a system-level property, not kernel-level.

---

## 15. Recovery Model

On restart:

1. Replay Event Store
2. Reconstruct State Machine
3. Restore queue state
4. Resume Execution Tick loop

Kernel itself is stateless beyond replay reconstruction.

---

## 16. AIR Integration

AIR does not execute directly.

AIR → Action → Scheduler → Kernel Execution

Kernel treats AIR outputs as immutable execution intent inputs.

---

## 17. Policy Integration

Policy Engine is evaluated before execution:

- DENY → Action discarded
- APPROVE → moved to Approval Queue
- ALLOW → executed in kernel loop

Policy decisions are never re-evaluated inside execution step.

---

## 18. System Invariants

- I1: Kernel executes one Action per tick
- I2: All execution side effects must produce Events
- I3: No shared-state mutation outside Event Store
- I4: Kernel is deterministic under identical input state
- I5: No concurrency inside single APOS instance
- I6: Failures do not stop system unless fatal flag is set

---

## 19. System Role

The Execution Runtime Kernel is:

- the physical execution engine of APOS
- the bridge between intent and reality
- the deterministic processor of Actions

---

## 20. Design Principle

The kernel does not decide.

It only executes what has already been decided.

---

## 21. Final Model

AIR → Action → Policy Engine → Scheduler → Execution Kernel → Event Store

---

## 22. Core Insight

If AIR is cognition,

and Policy is constraint,

and Events are reality,

then the Runtime Kernel is:

> the mechanical heartbeat that turns governed intent into irreversible system history