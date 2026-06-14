# ADR-003: Event Sourcing

## Status
Accepted

## Context
Traditional CRUD state management makes it difficult to audit decisions and replay history for learning purposes.

## Decision
Use Event Sourcing as the primary pattern for state management. Every state change is stored as an immutable event in the Event Store.

## Alternatives
- Standard relational database snapshots: Rejected because it loses the "why" and "how" behind state changes, which is critical for 6주차 Learning.

## Consequences
### Positive
- Full auditability and traceability of the project history.
- Enables easy "time-travel" debugging and project reconstruction.
### Negative
- Requires more complex implementation than simple state updates.
- Event store can grow very large; requires archiving strategy.

## Date
2026-06-14