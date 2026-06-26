# Glossary (AIR-Aligned Ubiquitous Language)

This document defines the shared vocabulary used across APOS.  
It represents the **conceptual mapping between AIR (APOS Intermediate Representation) and system-level constructs**.

---

## Core System Terms

| Term | Definition |
| :--- | :--- |
| **APOS** | Autonomous Project Operating System. A Meta-OS that operationalizes AIR by executing, constraining, persisting, and governing reasoning-driven project lifecycles under Human Director authority. |
| **AIR** | APOS Intermediate Representation. The structured cognitive layer that defines how reasoning is performed via Objective, Assumption, Variable, Inference, Prediction, Validation, and Meta transitions. |
| **Meta-OS** | The system layer that executes AIR. APOS functions as a runtime environment for AIR-based cognition and execution. |
| **Single Worker** | A deterministic execution model in which AIR inference and event processing are strictly sequential to preserve reasoning trace integrity (CoT consistency). |

---

## Governance Terms

| Term | Definition |
| :--- | :--- |
| **Human Director** | The final AIR validation authority responsible for approving high-risk control transitions, meta-layer modifications, and critical system state changes. Not external to AIR, but the terminal governance layer of AIR execution. |
| **HANDSOFIT** | Behavioral governance constraints applied to AIR-derived actions, defining safety, auditability, intervention, and least-privilege execution rules. |
| **ARS** | Meta-governance system defining ownership and authority over AIR artifacts: Accountability, Responsibility, Sovereignty. |
| **Policy Engine** | The deterministic AIR control law system that evaluates all actions before execution using DENY / APPROVAL REQUIRED / ALLOW logic. |

---

## AIR Cognitive Terms

| Term | Definition |
| :--- | :--- |
| **CoT (Chain-of-Thought)** | The internal AIR Inference Trace representing step-by-step reasoning execution. It is not user-facing, but fully preserved within system memory. |
| **Inference (AIR)** | The process of generating structured reasoning paths from Objective and Assumptions toward Actions and Predictions. |
| **Validation (AIR)** | The evaluation of whether predictions and actions align with observed system state (Event history). |
| **Control Variable** | A modifiable parameter derived from AIR inference that influences execution decisions and policy evaluation. |
| **Latent Variable** | Hidden or emergent factors inferred from historical AIR execution patterns and stored in the Knowledge Base. |
| **Meta Layer** | The AIR subsystem responsible for modifying assumptions, structure, and inference rules based on validation feedback. |

---

## Execution & System Terms

| Term | Definition |
| :--- | :--- |
| **Agent** | A runtime execution instance that performs Tasks using a specific Persona within AIR-constrained execution rules. |
| **Persona** | A logical role defining capabilities and behavioral constraints for an Agent. |
| **Task** | A bounded execution unit derived from AIR decomposition of a Goal. |
| **Action** | A proposed execution operation generated from AIR Control Variables and validated by the Policy Engine before execution. |
| **Resource** | Any system asset (files, APIs, models, memory, containers) that can be accessed or modified through Actions. |

---

## Memory & Knowledge Terms

| Term | Definition |
| :--- | :--- |
| **Event** | An immutable record of a validated AIR-derived Action executed in the system. It represents the physical trace of AIR over time. |
| **Event Store** | The append-only system that stores all Events and enables full reconstruction of AIR execution history. |
| **State Projection** | The reconstruction of current system state from Event history (State = Projection(Event Store)). |
| **Working Memory** | The active AIR Inference buffer holding live CoT and intermediate reasoning states. |
| **Project Memory** | The temporal storage layer containing Event history and execution traces of AIR. |
| **Knowledge Base (RAG Layer)** | A compressed representation of historical AIR execution patterns, latent variables, and generalized reasoning structures. |
| **Governance Memory** | The immutable repository of Policies, ADRs, and AIR Meta-layer evolution history. |

---

## Interface & Architecture Terms

| Term | Definition |
| :--- | :--- |
| **Control Plane** | The external interface layer that translates human intent into AIR Control Events. It is transport-agnostic (e.g., Telegram is only an adapter). |
| **Human-in-the-Loop** | The mandatory AIR governance mechanism requiring Human Director intervention for high-risk or irreversible control transitions. |
| **Meta-OS Kernel** | The execution layer of APOS responsible for task execution, agent lifecycle, resource management, and event handling under AIR constraints. |

---

## Core Linguistic Contracts

These are invariant relationships that define APOS consistency:

- **Persona ≠ Agent** → Persona defines role, Agent defines runtime execution
- **State = Projection(Event Store)** → State is derived, not stored
- **Event = AIR Execution Trace** → Every Event originates from validated AIR Action
- **CoT = AIR Inference Trace** → Reasoning is internal and persistent
- **Policy evaluates Action** → No Action bypasses AIR control law layer
- **Human Director = Terminal AIR Validator** → Final authority over critical AIR state transitions
- **Memory = Time-extended AIR cognition** → Knowledge is compressed reasoning history

---

## AIR Meta Insight

APOS vocabulary is not descriptive.

It is **structural alignment between cognition (AIR) and execution (system)**.

This glossary defines not what things mean in language, but:

> how they exist inside the AIR-driven system.