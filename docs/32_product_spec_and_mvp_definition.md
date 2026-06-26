# 32_product_spec_and_mvp_definition.md
---
## 0. Purpose
This document defines the Product Specification and MVP scope of APOS.
It translates the full APOS system into a minimal, buildable, and testable product.
The goal is not completeness.
The goal is **first working cognitive system loop**.
---
## 1. Core Principle
> A system is only valuable when it can execute a complete cognitive loop in reality.
MVP must prove:
- AIR can represent intent
- Kernel can execute safely
- Policy can govern actions
- Events can record truth
- Control Plane can receive human input
---
## 2. MVP Definition
The APOS MVP is defined as:
> A single-worker system that takes structured human intent, transforms it into AIR, executes it safely, and records all outcomes as immutable events.
---
## 3. MVP Core Loop

Human Intent
→ Control Plane
→ AIR Compiler
→ AIR Runtime
→ Policy Engine
→ Kernel Execution
→ Event Store
→ Trace Output
→ Human Feedback

---
## 4. MVP Scope (INCLUDED)
### 4.1 AIR System (Minimal)
- Objective definition
- Assumption handling
- simple inference structure
- basic validation layer
No full Meta-Layer evolution required.
---
### 4.2 Compiler (Minimal DSL)
Supports:
- Goal definition
- Task decomposition
- Action list generation
- basic workflow ordering
No advanced graph optimization required.
---
### 4.3 Kernel (Minimal Execution Engine)
Must support:
- single-worker execution loop
- sequential action execution
- event emission
- failure handling
No parallelism allowed.
---
### 4.4 Policy Engine (Rule-Based)
Must support:
- DENY / ALLOW / APPROVE
- simple risk scoring
- human approval gating
No AI-based policy inference required.
---
### 4.5 Event Store (Append-only)
Must support:
- event append
- event retrieval
- replay of system state
No distributed consensus required.
---
### 4.6 Control Plane (Telegram-based)
Must support:
- command input
- approval workflow
- status query
- emergency stop
---
### 4.7 Trace System
Must support:
- action → event mapping
- causal chain reconstruction
- execution history view
---
## 5. MVP Scope (EXCLUDED)
The following are explicitly NOT part of MVP:
- AIR Meta Layer evolution engine
- distributed kernel architecture
- multi-worker execution
- advanced memory compression
- AI-based policy learning
- multi-modal control interfaces
- large-scale observability stack
---
## 6. Success Criteria
MVP is successful if:
- A human can define a Goal via Control Plane
- System generates AIR representation
- Actions are executed deterministically
- All actions are governed by Policy Engine
- All outcomes are stored as Events
- Execution can be replayed exactly
---
## 7. Minimal Architecture

Control Plane
→ AIR Compiler
→ Policy Engine
→ Kernel
→ Event Store
→ Trace Viewer

---
## 8. Product Boundary Definition
APOS MVP is NOT:
- an autonomous AGI system
- a multi-agent swarm system
- a distributed AI platform
APOS MVP IS:
> a deterministic human-guided cognitive execution loop
---
## 9. Human Role in MVP
Human Director:
- defines Goals
- resolves ambiguities
- approves high-risk actions
- validates system output
System does NOT replace human judgment.
---
## 10. Risk Model
MVP is constrained by:
- single-worker execution safety
- strict policy enforcement
- immutable event logging
Risk is managed through:
- deterministic execution
- human approval gating
- failure-safe kernel design
---
## 11. Deployment Assumption
MVP assumes:
- single container deployment
- local or lightweight server environment
- external Telegram integration
- minimal storage backend
---
## 12. Evolution Path After MVP
Once MVP is stable:
- AIR Meta Layer expansion
- distributed execution
- memory compression systems
- adaptive policy learning
- multi-instance APOS federation
---
## 13. Design Principle
MVP is not a simplified APOS.
It is the **first observable instance of APOS cognition in execution form**.
---
## 14. Final Model
Human Intent → AIR → Policy → Kernel → Events → Trace → Human Feedback
---
## 15. Core Insight
If APOS is a cognitive operating system,
then MVP is:
> the smallest possible system where cognition becomes executable reality under human governance