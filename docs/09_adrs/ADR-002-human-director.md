# ADR-002: Human Director Integration

## Status
Accepted

## Context
APOS mandates that humans remain the ultimate authority. Without a formal architectural hook, human intervention becomes an ad-hoc process rather than a systemic constraint.

## Decision
Integrate a "Human Director" layer that acts as the primary gatekeeper for high-risk actions. All state transitions flagged as "Requires Approval" must halt until a human-signed event is received.

## Alternatives
- Purely asynchronous notification: Rejected as it doesn't guarantee a "stop-and-wait" mechanism for critical decisions.

## Consequences
### Positive
- Enforces the Governance principle of "Human Agency".
- Provides a clear boundary between AI autonomy and human accountability.
### Negative
- Increases latency in the project lifecycle due to waiting for human input.

## Date
2026-06-14