# ADR-001: Single Worker Architecture

## Status
Accepted

## Context
APOS requires a stable environment to manage project lifecycles. Distributing tasks across multiple concurrent workers introduces complexity in state synchronization, event ordering, and dependency management.

## Decision
Adopt a "Single Worker" architecture. All project lifecycles, persona interactions, and state transitions are processed sequentially by a single core worker.

## Alternatives
- Multi-worker/Distributed system: Rejected due to high complexity in ensuring strict event ordering and potential state inconsistency during the early development phase.

## Consequences
### Positive
- Ensures deterministic behavior and event ordering.
- Significantly reduces infrastructure complexity and race conditions.
### Negative
- Limits concurrent execution throughput.
- Potential bottleneck if heavy computational tasks are not offloaded to external services.

## Date
2026-06-14