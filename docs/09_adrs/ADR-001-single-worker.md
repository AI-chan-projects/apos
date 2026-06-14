# ADR-001: Single Worker Architecture

## Status
Accepted

## Context
APOS requires a stable environment to manage project lifecycles. Distributed workers introduce high complexity in state synchronization, event ordering, and dependency management.

## Decision
Adopt a "Single Worker" architecture. All project lifecycles, persona interactions, and state transitions are processed sequentially by a single core worker.

## Governance Mapping
HANDSOFIT: S (Safety First)

## Assumptions
- Single MacBook/local environment.
- Sequential event processing is sufficient for current project scale.

## Invariants
- Single sequence of event processing.

## Alternatives
- Distributed Actor Runtime: Rejected due to complexity in guaranteeing strict event ordering at this stage.

## Consequences
- Positive: Deterministic behavior, simplified state management, no race conditions.
- Negative: Limited horizontal scalability.

## Future Revisit Conditions
- When multi-node execution is required.
- When project concurrency creates significant performance bottlenecks.
- When resource scheduling demands distributed execution.

## Date
2026-06-14 