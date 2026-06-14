# ADR-002: Human Director Integration

## Status
Accepted

## Context
Human oversight is the foundation of APOS. Without a formal architectural hook, human intervention remains ad-hoc rather than a systemic constraint.

## Decision
Integrate a "Human Director" layer that acts as the primary gatekeeper. High-risk actions must halt until a human-signed event is received.

## Governance Mapping
HANDSOFIT: H, F, D; ARS: Accountability

## Assumptions
- Human Director is available for critical decision loops.

## Invariants
- Final authority remains with the Human Director.

## Alternatives
- Asynchronous notification: Rejected; lacks the "stop-and-wait" mechanism required for critical decisions.

## Consequences
- Positive: Upholds Human Agency and safety.
- Negative: Adds latency to the project lifecycle.

## Future Revisit Conditions
- When automated trust levels allow for autonomous execution of high-risk tasks.

## Date
2026-06-14 