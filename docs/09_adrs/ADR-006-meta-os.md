# ADR-006: Meta-OS Definition

## Status
Accepted

## Context
APOS is more than an application; it is an organizational orchestrator.

## Decision
Define APOS as a Meta-OS governing Project Lifecycles, Agent Personas, Memory Systems, Policy/Approval, Resource Allocation, and Event Processing.

## Architectural Principle
- Applications run on APOS.
- Projects are orchestrated by APOS.
- Governance is enforced by APOS.

## Governance Mapping
ARS: Accountability, Responsibility, Sovereignty

## Assumptions
- Modular separation between kernel and application logic is feasible.

## Invariants
- All agent interactions must occur through the APOS interface.

## Alternatives
- Simple Agent Framework: Rejected; fails to convey systemic governance and resource control.

## Consequences
- Positive: Modular, scalable, and clearly defined scope.
- Negative: Risk of over-architecting early on.

## Future Revisit Conditions
- If the system scope shifts from "project management" to "general automation".

## Date
2026-06-14