# 02_architecture.md
---
## 0. Purpose
This document defines the overall architecture of APOS (Autonomous Project Operating System).
It integrates all previously defined subsystems into a single coherent system model.
APOS is not an application.
It is a structured cognitive operating system for autonomous project execution under human governance.
---
## 1. System Overview
APOS is composed of five core layers:
### 1.1 Cognitive Layer
- AIR (APOS Intermediate Representation)
- Inference structure
- Assumption modeling
- Prediction and validation
---
### 1.2 Execution Layer
- Actions
- Scheduling system
- Single-worker runtime
- Execution protocol
---
### 1.3 Constraint Layer
- Policy Engine
- Risk scoring
- Approval gating
- Governance enforcement
---
### 1.4 Reality Layer
- Event Store
- Event Contracts
- Immutable execution history
---
### 1.5 Evolution Layer
- Memory Model
- Knowledge Base
- Compression pipeline
- Learning feedback loops
---
## 2. System Flow (End-to-End)
APOS operates as a closed loop:
AIR → Action → Policy Engine → Execution → Event Store → State → Memory → AIR
---
## 3. Core Pipeline Architecture
### Step 1: AIR Generation
Human intent is transformed into structured reasoning.
Outputs:
- Objective
- Assumptions
- Variables
- Inference graph
---
### Step 2: Action Derivation
AIR produces executable candidates.
---
### Step 3: Policy Evaluation
All Actions are evaluated:
- DENY → rejected
- APPROVE → human gating required
- ALLOW → execution permitted
---
### Step 4: Scheduling
Approved Actions enter execution queues.
---
### Step 5: Execution Runtime
Single-worker deterministic execution model:
- sequential processing
- no concurrency conflicts
- strict ordering guarantees
---
### Step 6: Event Emission
Execution produces immutable Events.
---
### Step 7: State Projection
State is reconstructed from Event history.
---
### Step 8: Memory Formation
Events are compressed into memory structures.
---
### Step 9: AIR Feedback Loop
Memory reshapes future AIR reasoning.
---
## 4. Layered System Model
APOS is structured as:

AIR (Cognition)
↓
Action (Intent → Execution Bridge)
↓
Policy Engine (Constraint System)
↓
Runtime (Execution System)
↓
Event Store (Reality Layer)
↓
State Machine (Projection Layer)
↓
Memory Model (Evolution Layer)
↓
AIR (Feedback Loop)

---
## 5. Core Subsystems
### 5.1 AIR
- structured reasoning system
- produces deterministic inference graphs
- does not execute directly
---
### 5.2 Policy Engine
- evaluates all Actions
- enforces governance constraints
- provides deterministic decisions
---
### 5.3 Execution Runtime
- single-worker architecture
- sequential execution model
- deterministic behavior guarantee
---
### 5.4 Event Store
- immutable append-only log
- causal history of all system actions
- source of truth for system state
---
### 5.5 State Machine
- projection of Events
- no direct mutation allowed
- fully replayable system state
---
### 5.6 Memory System
- compressed representation of Event history
- long-term learning mechanism
- feedback loop into AIR
---
## 6. Architectural Invariants
- I1: AIR does not execute actions directly
- I2: All Actions must pass Policy Engine
- I3: All execution results are Events
- I4: State is derived exclusively from Events
- I5: Memory is derived from Events and AIR traces
- I6: No subsystem may bypass Event Store
- I7: Human Director retains ultimate authority
---
## 7. Control Hierarchy
Authority flow:
Human Director
→ Policy Engine
→ Execution Runtime
→ Event Store
→ State Machine
→ Memory System
→ AIR
Human authority is final in all approval-gated transitions.
---
## 8. Failure Model
APOS failure handling is event-based:
- failures are Events
- retries are new Actions
- compensation is explicit execution flow
- no silent failure exists
---
## 9. Consistency Model
APOS uses deterministic replay consistency:
- Event Store is canonical truth
- State is reproducible
- Memory is reconstructable
- AIR is derivable context-aware reasoning layer
---
## 10. Scalability Model
APOS scales horizontally via:
- multiple isolated single-worker instances
- event-driven synchronization
- external event bus coordination
No internal multi-threaded execution is assumed.
---
## 11. System Philosophy
APOS is designed as:
> a cognitive operating system where reasoning, execution, and memory are separated into strict deterministic layers
---
## 12. Final System Definition
APOS =
- AIR (thinking)
- Policy Engine (constraints)
- Action Protocol (execution intent)
- Runtime (execution)
- Event Store (reality)
- State Machine (current world)
- Memory Model (learning loop)
---
## 13. Core Insight
APOS is not automation.
APOS is:
> a closed-loop system that converts human intent into governed, traceable, and evolving operational reality