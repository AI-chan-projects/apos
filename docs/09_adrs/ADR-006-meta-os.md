# ADR-006: Meta-OS Definition

## Status
Accepted

## Context
APOS is not just an application; it requires a management layer for agents, resources, and project metadata.

## Decision
Define APOS as a "Meta-OS" that encapsulates the management of project lifecycles, persona registration, and resource access policies.

## Alternatives
- Standard Application Framework: Rejected as it doesn't convey the need for resource lifecycle management and systemic governance.

## Consequences
### Positive
- Clearly distinguishes between OS-level management and application-level logic.
- Promotes modular architecture.
### Negative
- Over-architecting risk if the scope is not strictly managed.

## Date
2026-06-14