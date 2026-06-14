# ADR-005: Memory Architecture

## Status
Accepted

## Context
Agents must manage transient execution data and accumulated project knowledge to perform long-term tasks effectively.

## Decision
Implement a tiered memory architecture: Working, Project, Knowledge Base, and Governance Memory.

## Governance Mapping
HANDSOFIT: N (Transparent Learning); ARS: Sovereignty

## Assumptions
- RAG-based knowledge distillation is feasible for current context needs.

## Invariants
- Governance Memory (Policies/ADRs) must be synchronized across agent restarts.

## Alternatives
- Flat context window: Rejected; does not scale for multi-week projects.

## Consequences
- Positive: Enables long-term knowledge retention and "organizational memory".
- Negative: Complexity in managing vector databases.

## Future Revisit Conditions
- When the knowledge base exceeds latency/cost requirements for real-time retrieval.

## Date
2026-06-14 