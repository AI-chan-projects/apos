# Domain Model: APOS

This model defines the core entities, relationships, and invariants within the Autonomous Project Operating System (APOS) using Domain-Driven Design (DDD) principles.

## 0. AIR Integration Principle

APOS domain entities are executed through a structured reasoning layer called **AIR (APOS Intermediate Representation)**.

AIR is not a domain entity.
It is the **reasoning substrate** that all domain entities are interpreted through.

All planning, execution, validation, and learning operations must be traceable to AIR structures.

---

## 1. Core Entities

### 1.1 Planning & Governance
* **Human Director**: The ultimate authority responsible for setting Goals and providing final approval for high-risk Actions.
* **Goal**: A human-defined desired outcome that drives project planning, task generation, and success evaluation.
* **Project**: The top-level orchestrator representing a specific lifecycle.
* **Stage**: A discrete lifecycle phase of a Project that determines active Personas, available actions, and transition rules.

---

### 1.2 Execution & Orchestration
* **Task**: A bounded unit of work generated from AIR decomposition of a Goal.
* **Persona**: A logical role with defined responsibilities and **Capabilities**.
* **Capability**: A granular permission or skill that determines which Actions a Persona (or Agent) can perform.
* **Agent**: A runtime instance that assumes a specific Persona to perform Tasks.
* **Action**: An executable operation proposed by an Agent, derived from AIR Control Variables, subject to Policy evaluation.
* **Resource**: A managed asset (e.g., files, repositories, models, APIs, containers, memories) accessed or modified by Actions and mapped to AIR Observable or Control variables.

---

### 1.3 State, Persistence & Policy
* **Policy**: A set of rules enforced by the Policy Engine that governs behavior (Can: Persona + Action + Resource).
* **Event**: An immutable record of any state change or validated AIR execution outcome.
* **Event Store**: The append-only persistence layer that stores immutable events and enables state reconstruction.
* **State**: The current projection derived solely from Event history and AIR validation results.

---

### 1.4 Memory Architecture
* **Working Memory**: Transient context for current AIR reasoning and task execution.
* **Project Memory**: Persistent store for project events, AIR traces, and task outcomes.
* **Knowledge Base**: Vector + graph-based system storing derived Latent Variables and historical AIR patterns.
* **Governance Memory**: Repository for Policies, ADRs, and Meta-layer modifications of AIR structure.

---

## 2. Entity Relationships

1. **Human Director** defines the **Goal**.
2. **Goal** is transformed into an **AIR representation (Objective Layer)**.
3. **AIR decomposition** drives the **Project** structure.
4. **Project** manages the current **Stage**.
5. **Stage** decomposes AIR into **Tasks (Inference + Planning output)**.
6. **Tasks** are assigned to a **Persona** and executed by an **Agent**.
7. **Agent** proposes an **Action**, mapped from AIR Control Variables.
8. **Action** is validated by **Policy Evaluation** (`Can(Persona, Action, Resource)`), constrained by AIR Assumptions.
9. Validated **Action** results in an **Event**, which is interpreted as AIR Validation output.
10. **State** is updated via projection of Events and AIR validation history.

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

### AIR-Extended Invariants

* **I9**: Every Task must be traceable to at least one AIR Objective decomposition.
* **I10**: Every Action must map to at least one AIR Control Variable.
* **I11**: Every Event must contribute to AIR Validation or Meta-layer update.
* **I12**: No Action is valid unless it is reachable via an AIR Inference path.
* **I13**: Meta-layer modifications require explicit validation failure, drift detection, or Human Director override.

---

## 4. Ubiquitous Language Summary

* **Persona vs. Agent**:
  A **Persona** is the "what/who" (logical role/template),
  while an **Agent** is the "how" (runtime instance/executor).

  This decoupling allows swapping underlying models without changing the Persona definition.

---

## 5. AIR Clarification

AIR is the canonical reasoning layer of APOS:

- It defines how Goals are interpreted
- It structures how Tasks are derived
- It constrains how Actions are validated
- It governs how learning occurs through Meta updates

AIR is not optional.
It is the **required intermediate representation for all system behavior**.