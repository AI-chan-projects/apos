# ADR-004: Control Plane (Telegram Interface Adapter)

---

## Status
Accepted (Transitional)

---

## 0. AIR Context

The Control Plane is the **external interface layer of AIR (APOS Intermediate Representation)**.

It is responsible for translating human input into:

- AIR Control Variable modifications
- Action approvals/rejections
- Governance override signals
- Validation triggers

### Key Principle

> The Control Plane is transport-agnostic; Telegram is only one implementation.

---

## Context

Human Director requires a real-time, mobile-accessible interface to interact with AIR-based system execution.

However, direct coupling between APOS and a single communication platform introduces:

- vendor lock-in risk
- limited extensibility
- architectural rigidity

In AIR-based design, interaction channels must remain decoupled from reasoning and execution layers.

---

## Decision

Adopt a **Control Plane abstraction layer**, initially implemented via Telegram Bot API.

### Control Plane responsibilities:

- Receive Human Director commands
- Translate messages into AIR Control events
- Trigger approval workflows for high-risk Actions
- Stream AIR state updates (Events, Validation, Inference summaries)

---

## Strategic Architecture Principle

> Telegram is not the Control Plane.
> Telegram is an **adapter for the Control Plane interface**.

The actual Control Plane is defined as:

> A message-driven interface that maps human intent → AIR Control Events

---

## Governance Mapping

HANDSOFIT:
- D (Direct Intervention)
- O (Observability)
- F (Formal Approval)

---

## Assumptions

- Human Director requires low-latency interaction with AIR system
- Messaging-based interfaces are sufficient for control and approval workflows
- External API reliability is acceptable for transitional architecture

---

## Invariants

- I1: All Human commands must be validated before affecting AIR state
- I2: Control Plane messages must map to AIR Control Variables or Governance Events
- I3: No external interface may directly modify system state without AIR mediation
- I4: Approval commands must generate immutable Events in Event Store
- I5: Control Plane is replaceable without affecting AIR or Domain layers

---

## Alternatives

### Custom Web Dashboard
Rejected due to:
- higher maintenance cost
- slower iteration cycle
- reduced mobility compared to messaging interface

### Direct CLI control interface
Rejected due to:
- limited accessibility
- poor real-time notification support

### Embedded UI inside APOS core
Rejected due to:
- tight coupling with execution engine
- violation of separation between AIR and interface layers

---

## Consequences

### Positive
- Fast Human Director interaction loop
- Decoupled interface layer (future-proof)
- Easy replacement of transport mechanism
- Supports real-time governance over AIR execution

### Negative
- Dependency on external messaging infrastructure (Telegram)
- Security risks related to bot token management
- Rate limits and platform constraints

---

## Future Revisit Conditions

This architecture must be revisited when:

- A native APOS Control Plane protocol is implemented
- Event-bus based UI systems replace messaging platforms
- Multi-channel control interfaces (Telegram, Web, CLI) are unified under a single abstraction layer
- Security requirements necessitate full self-hosted communication infrastructure

---

## AIR Meta Insight (Critical Design Principle)

The Control Plane is not part of AIR reasoning.

It is the **external projection layer of AIR Control Events**.

It ensures that:

- Human intent is translated into structured AIR inputs
- AIR execution remains decoupled from interface transport
- Governance can operate independently of UI implementation

---

## Date
2026-06-26