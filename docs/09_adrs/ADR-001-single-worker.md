# ADR-001: Single Worker Architecture

## Status
Accepted

## Context
APOS requires a stable environment to manage project lifecycles. Distributing tasks across multiple concurrent workers within a single process introduces high complexity in state synchronization, event ordering, and dependency management.

## Decision
Adopt a "Single Worker" architecture within each APOS instance. 
Concurrency is achieved through multiple isolated APOS instances (e.g., Docker containers) rather than through multiple workers inside a single instance. This design prioritizes deterministic execution, reduced resource consumption, failure isolation, and simplified governance enforcement.

## Governance Mapping
HANDSOFIT: S (Safety First)

## Assumptions
- Lightweight isolation (Docker/Container) is the preferred scaling mechanism.
- Inter-instance communication (via Event Bus/Broker) is more reliable than intra-instance thread/process synchronization.

## Invariants
- Each APOS instance operates with a single sequential worker.
- Concurrent project execution is managed by horizontal scaling of instances.

## Alternatives
- Internal Multi-threading/Multi-processing: Rejected due to complexity in guaranteeing event ordering and state consistency.

## Consequences
- Positive: Deterministic behavior, simplified state management, robust failure isolation, and easier governance enforcement.
- Negative: Higher overhead in orchestrating multiple containers/instances.

## Future Revisit Conditions
- When container orchestration overhead becomes a bottleneck for resource-constrained environments.
- When shared memory requirements between instances exceed latency budgets.

## Date
2026-06-14