# 21_control_plane_spec.md

---

## 0. Purpose

This document defines the Control Plane specification of APOS.

It formalizes the interface layer through which Human Director interacts with AIR-based system execution.

The Control Plane is a protocol layer, not a UI implementation.

---

## 1. Core Principle

> The Control Plane is a message-driven interface that translates human intent into AIR Control Events.

It is fully decoupled from:

- AIR reasoning layer
- Execution runtime
- Event store implementation
- UI transport mechanisms

---

## 2. Control Plane Architecture

The Control Plane operates as a translation layer:

Human Input → Control Command → AIR Control Event → Event Store → System Reaction

---

## 3. Control Command Model

All human interactions are expressed as Control Commands.

### 3.1 Command Structure

Each Control Command contains:

- command_id
- source_channel
- command_type
- payload
- timestamp
- authentication context

---

### 3.2 Command Types

#### 1. ApprovalCommand
- approves pending Actions
- used for APPROVE policy resolution

#### 2. RejectionCommand
- rejects pending Actions
- cancels execution pipeline

#### 3. OverrideCommand
- force-modifies governance decisions
- requires elevated authorization

#### 4. QueryCommand
- requests system state or AIR insights
- read-only operation

#### 5. ControlVariableCommand
- modifies AIR control parameters
- affects inference behavior

---

## 4. AIR Control Event Mapping

Every Control Command is transformed into a Control Event:

Control Command → Control Event → Event Store

### 4.1 Control Event Structure

- control_event_id
- command_id
- event_type
- target_scope (AIR / Action / Policy / Runtime)
- payload
- validation_status

---

## 5. Control Event Types

### 5.1 Approval Event
Represents Human Director approval of an Action.

### 5.2 Rejection Event
Represents explicit denial of execution continuation.

### 5.3 Override Event
Represents forced modification of system behavior.

### 5.4 Query Event
Represents read-only system interrogation.

### 5.5 Control Update Event
Represents modification of AIR control variables.

---

## 6. Transport Layer Abstraction

The Control Plane is transport-agnostic.

Supported adapters include:

- Telegram Bot API (initial implementation)
- HTTP API Gateway
- CLI interface
- Future Web UI
- Event bus subscribers

Each adapter must implement:

> Command → Control Event translation contract

---

## 7. Telegram Adapter Specification (Reference Implementation)

Telegram acts as a thin adapter:

Telegram Message → Command Parser → Control Event Generator

Constraints:

- no direct system mutation
- all messages must pass validation layer
- authentication required for state-changing commands

---

## 8. Validation Layer

Before a Control Event is committed:

1. Authenticate sender (Human Director identity)
2. Validate command schema
3. Check authorization level
4. Map to valid AIR scope
5. Attach audit metadata

If validation fails:

- event is rejected
- failure is recorded as Control Failure Event

---

## 9. AIR Integration Model

Control Plane modifies AIR only through controlled events:

- modifies control variables
- triggers AIR re-evaluation cycles
- activates approval resolution paths

Control Plane cannot directly execute Actions.

---

## 10. Runtime Interaction Model

Control Events influence runtime behavior indirectly:

Control Event → Event Store → State Projection → Scheduler Reaction

Examples:

- Approval Event → Action moves to Ready Queue
- Rejection Event → Action is discarded
- Override Event → Policy evaluation re-run
- Control Variable Event → AIR inference updates

---

## 11. Security Model

### 11.1 Authorization Levels

- Level 0: Read-only queries
- Level 1: Approval/Rejection
- Level 2: Control variable modification
- Level 3: System override (restricted)

---

### 11.2 Authentication Requirements

All state-modifying commands require:

- Human Director identity verification
- signed request token (or equivalent)
- audit trail generation

---

## 12. Event Consistency Model

All Control Events must satisfy:

- immutability after commit
- full traceability to command origin
- deterministic replay behavior

---

## 13. Failure Handling

Failure cases include:

- invalid command schema
- unauthorized access
- mapping failure to AIR scope
- transport layer failure

All failures generate:

- ControlFailureEvent

No silent failure is allowed.

---

## 14. Multi-Channel Abstraction Model

All channels converge into a single interface:

Channel Input → Adapter → Unified Control Command → Control Event

No channel has privileged access.

---

## 15. Invariants

- I1: Control Plane cannot directly mutate system state
- I2: All commands must be converted into Control Events
- I3: All Control Events are persisted in Event Store
- I4: AIR modification occurs only through Control Events
- I5: Transport layer is fully replaceable
- I6: Authorization is mandatory for state-changing commands

---

## 16. System Role

The Control Plane is:

- the boundary between Human Director and APOS
- the translation layer between intent and structured system control
- the governance entry point of the entire architecture

---

## 17. Design Principle

The Control Plane does not execute.

It translates human intent into governed system events.

---

## 18. Final Model

Human Input → Control Command → Validation → Control Event → Event Store → System Reaction

---

## 19. Core Insight

If AIR is cognition,

and Execution is behavior,

then Control Plane is:

> the governed interface where human intent enters the system as structured control reality