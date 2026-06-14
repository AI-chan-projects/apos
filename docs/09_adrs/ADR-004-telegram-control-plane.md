# ADR-004: Telegram Control Plane

## Status
Accepted (Transitional)

## Context
The Human Director needs a persistent, mobile-ready, real-time interface for oversight.

## Decision
Use the Telegram Bot API as the primary Control Plane interface for alerts and approval workflows.

## Strategic Limitation
Telegram is an implementation convenience and not a permanent dependency.

## Governance Mapping
HANDSOFIT: D (Direct Intervention), O (Observability)

## Assumptions
- External messaging service reliability is acceptable for MVP.

## Invariants
- Approval commands must be validated through the internal Event Bus.

## Alternatives
- Custom Web Dashboard: Rejected due to maintenance overhead and mobile notification limitations.

## Consequences
- Positive: Instant reachability, native rich UI.
- Negative: Dependency on 3rd party, token security risks.

## Future Revisit Conditions
- When moving toward a native event-bus based UI/Dashboard.

## Date
2026-06-14 