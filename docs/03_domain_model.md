# Domain Model: APOS

This model defines the core entities, relationships, and invariants within the Autonomous Project Operating System (APOS) using Domain-Driven Design (DDD) principles.

## 1. Core Entities

### 1.1 Planning & Governance
* **Human Director**: The ultimate authority responsible for setting Goals and providing final approval for high-risk Actions.
* **Goal**: A human-defined desired outcome that drives project planning, task generation, and success evaluation.
* **Project**: The top-level orchestrator representing a specific lifecycle.
* **Stage**: A discrete lifecycle phase of a Project that determines active Personas, available actions, and transition rules.

### 1.2 Execution & Orchestration
* **Task**: A bounded unit of work generated from a Goal and executed by an Agent.
* **Persona**: A logical role with defined responsibilities and **Capabilities**.
* **Capability**: A granular permission or skill that determines which Actions a Persona (or Agent) can perform.
* **Agent**: A runtime instance that assumes a specific Persona to perform Tasks.
* **Action**: An executable operation proposed by an Agent, subject to Policy evaluation before execution.
* **Resource**: A managed asset (e.g., files, repositories, models, APIs, containers, memories) accessed or modified by Actions.

### 1.3 State, Persistence & Policy
* **Policy**: A set of rules enforced by the Policy Engine that governs behavior (Can: Persona + Action + Resource).
* **Event**: An immutable record of any state change or action within the system.
* **Event Store**: The append-only persistence layer that stores immutable events and enables state reconstruction.
* **State**: The current projection derived solely from Event history.

### 1.4 Memory Architecture
* **Working Memory**: Transient context for current task execution.
* **Project Memory**: Persistent store for project events and task outcomes.
* **Knowledge Base**: Vector-based RAG for long-term knowledge distillation.
* **Governance Memory**: Repository for ADRs, Policies, and Approval histories.

---

## 2. Entity Relationships
1. **Human Director** defines the **Goal**.
2. **Goal** drives the **Project**.
3. **Project** manages the current **Stage**.
4. **Stage** decomposes the **Goal** into **Tasks**.
5. **Tasks** are assigned to a **Persona** (with **Capabilities**) and executed by an **Agent**.
6. **Agent** proposes an **Action** targeting a **Resource**.
7. **Action** is validated by **Policy Evaluation** (`Can(Persona, Action, Resource)`).
8. Validated **Action** results in an **Event**, stored in the **Event Store**.
9. **State** is updated via **State Projection** and recorded in **Memory**.

---

## 3. Domain Invariants
* **I1**: A Goal must belong to exactly one Project.
* **I2**: An Agent assumes exactly one active Persona at a time.
* **I3**: Every Action must be evaluated by a Policy before execution.
* **I4**: Every committed Event is immutable and append-only.
* **I5**: State is derived solely from the Event Store (State = Projection(Event Store)).
* **I6**: Every high-risk Action requires Human Director approval.
* **I7**: A Persona may own multiple Capabilities.
* **I8**: Actions always operate on defined Resources.

---

## 4. Ubiquitous Language Summary
* **Persona vs. Agent**: A **Persona** is the "what/who" (logical role/template), while an **Agent** is the "how" (runtime instance/executor). This decoupling allows swapping underlying models without changing the Persona definition.