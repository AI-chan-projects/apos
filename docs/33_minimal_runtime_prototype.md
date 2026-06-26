# 33_minimal_runtime_prototype.md
---
## 0. Purpose
This document defines the Minimal Runtime Prototype (MRP) of APOS.
It is not a full system implementation.
It is the smallest executable slice that proves:
> AIR → Policy → Kernel → Event Store → Human Feedback loop can actually run.
---
## 1. Core Principle
> If it cannot run, it is not a system.
This prototype removes all abstraction layers not required for execution.
---
## 2. Prototype Goal
The goal is to build a working loop that:
1. receives a Goal
2. converts it into a minimal AIR structure
3. generates Actions
4. evaluates them via Policy Engine
5. executes via Kernel
6. stores Events
7. allows human feedback via Control Plane
---
## 3. Minimal System Architecture

[ Human Input ]
↓
[ Control Plane ]
↓
[ Minimal AIR Generator ]
↓
[ Policy Engine ]
↓
[ Kernel Loop ]
↓
[ Event Store ]
↓
[ Feedback Output ]

---
## 4. Minimal Components
### 4.1 Event Store (Core Reality Layer)
The Event Store is the only persistent layer.
#### Responsibilities:
- append events
- retrieve events
- replay events
#### Event Structure:
- id
- timestamp
- type
- payload
- source (AIR / Kernel / Human)
- status
---
### 4.2 Kernel (Single Worker Loop)
The Kernel is a deterministic execution loop.
#### Responsibilities:
- process Action queue sequentially
- execute approved actions
- emit events
- maintain tick cycle
#### Execution Model:

while true:
action = next_action()
decision = policy.evaluate(action)
if decision == ALLOW:
event = execute(action)
store(event)

---
### 4.3 Policy Engine (Minimal Rules)
Rule-based evaluator:
#### Output:
- ALLOW
- DENY
- APPROVE_REQUIRED
#### Inputs:
- action type
- risk level
- context state
#### Rule example:
- file_write → APPROVE_REQUIRED
- read_only → ALLOW
- system_shutdown → DENY unless human override
---
### 4.4 Minimal AIR Generator
This is a simplified cognition layer.
#### Input:
- Goal string
#### Output:
- Objective
- 1–5 Tasks
- Each Task → 1–3 Actions
No inference graph required.
---
### 4.5 Control Plane (Human Interface)
Minimal interface:
- send Goal
- approve action
- reject action
- view status
Implementation can be:
- Telegram bot (preferred)
- CLI fallback
---
## 5. Minimal Data Flow

Human Goal
→ AIR Generator
→ Action List
→ Policy Evaluation
→ Kernel Execution
→ Event Store
→ Human Feedback

---
## 6. Execution Loop Definition
APOS minimal runtime is a single loop:

1. receive input
2. generate AIR
3. create actions
4. evaluate policy
5. execute allowed actions
6. store events
7. wait for feedback
8. repeat

---
## 7. System Constraints
### 7.1 Single Worker Rule
Only one execution loop is allowed per instance.
No concurrency.
No parallel execution.
---
### 7.2 Event Immutability
Once stored:
- events cannot be modified
- events cannot be deleted
---
### 7.3 Policy Enforcement Mandatory
No action may bypass Policy Engine.
---
### 7.4 AIR Simplicity Constraint
No meta-layer required in prototype.
AIR is strictly:
Goal → Tasks → Actions
---
## 8. Failure Model
Failures are explicit events:
- execution_failure
- policy_rejection
- invalid_goal
- kernel_error
No silent failures allowed.
---
## 9. Prototype Success Criteria
The prototype is successful if:
- A user can send a Goal
- System generates Actions
- Policy evaluates each Action
- Kernel executes at least one Action
- Event Store records results
- Human can see and respond
---
## 10. Minimal Technology Assumptions
No strict tech stack required.
Suggested:
- Python or TypeScript
- JSON-based Event Store
- Simple queue for Kernel
- Telegram Bot API or CLI
---
## 11. What This Prototype IS NOT
- not distributed system
- not optimized system
- not scalable architecture
- not full AIR implementation
- not production system
---
## 12. What This Prototype IS
> a single-threaded, event-driven cognitive loop
---
## 13. System Principle
APOS does not begin as a platform.
It begins as a loop.
---
## 14. Final Model
Human → AIR → Policy → Kernel → Events → Human
---
## 15. Core Insight
If APOS is a cognitive operating system,
then this prototype is:
> the first heartbeat of that system in execution form