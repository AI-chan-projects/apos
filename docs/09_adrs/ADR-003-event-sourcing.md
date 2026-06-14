# ADR-003: Event Sourcing

## Status
Accepted

## Context
Traditional state snapshots obscure the reasoning behind system changes, hindering auditability and future learning.

## Decision
Adopt Event Sourcing. Every state change is stored as an immutable event in the Event Store.

## Governance Mapping
HANDSOFIT: A (Auditability), O (Observability)

## Assumptions
- Event storage volume is manageable.

## Invariants
- Events are immutable.
- Events are append-only.
- State is a projection of events.

## Alternatives
- CRUD snapshots: Rejected; lacks transparency and audit history.

## Consequences
- Positive: Full auditability, time-travel debugging, enables deep learning from history.
- Negative: Implementation complexity; needs archiving strategies.

## Future Revisit Conditions
- When event throughput exceeds current storage capacity or system latency requirements.

## Date
2026-06-14 