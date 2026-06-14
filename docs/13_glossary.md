# Glossary

This document defines the common vocabulary (Ubiquitous Language) used throughout the APOS project. It ensures consistency across design, implementation, and governance.

| Term | Definition |
| :--- | :--- |
| **APOS** | Autonomous Project Operating System. A Meta-OS that orchestrates projects, personas, memory, policies, and event-driven execution under human governance. |
| **HANDSOFIT** | The nine operational governance principles that define the behavioral boundaries and responsibilities of AI agents within APOS. |
| **ARS** | Accountability, Responsibility, and Sovereignty; the three meta-governance principles defining ownership, authority, and ultimate control within APOS. |
| **Human Director** | The Human Director who defines project goals, provides approvals, and holds ultimate accountability and authority within APOS. |
| **Persona** | A logical role that defines responsibilities, capabilities, and access rights. It is independent of the underlying Agent implementation. |
| **Agent** | A runtime instance that assumes a Persona and performs Tasks. |
| **Goal** | A human-defined desired outcome that drives project planning, task generation, and success evaluation. |
| **Task** | A bounded unit of work derived from a Goal and executed by an Agent. |
| **Action** | An executable operation proposed by an Agent and subject to Policy evaluation before execution. |
| **Capability** | A granular permission or skill that determines which Actions a Persona or Agent can perform. |
| **Resource** | A managed asset (e.g., files, repositories, models, APIs, containers, memories) accessed or modified by Actions. |
| **Event** | An immutable fact representing a state change or completed Action within the system. |
| **Event Store** | An append-only persistence layer that stores immutable events and enables state reconstruction. |
| **State Projection** | The process of deriving the current State from the Event history stored in the Event Store (State = Projection(Event Store)). |
| **Single Worker** | An architectural principle in which each APOS instance processes events sequentially through one core worker to guarantee deterministic execution and simplified governance. |
| **Human-in-the-Loop** | The governance mechanism that keeps humans involved in approvals, interventions, and high-risk decisions throughout the project lifecycle. |
| **Organizational Learning** | The process of transforming project experiences, failures, and decisions into reusable organizational knowledge. |
| **Meta-OS** | A system-level orchestrator managing agents, memory, and project lifecycles. |

## Core Linguistic Contracts
To ensure system consistency, maintain the following logical relationships:
* **Persona ≠ Agent**: Personas define the "What/Who", Agents define the "How".
* **State = Projection(Event Store)**: State is not stored; it is derived from immutable facts.
* **Event = Immutable Fact**: Once committed, events cannot be deleted or modified.
* **Policy evaluates Action**: All proposed actions are subject to centralized policy validation.
* **Director = Ultimate Accountability**: Every autonomous decision is ultimately traceable to the Human Director's oversight. 