# ADR-005: Memory Architecture

## Status
Accepted

## Context
APOS agents need a way to manage both transient execution context (Short-term) and accumulated project knowledge (Long-term).

## Decision
Implement a tiered memory architecture: 
1. **Working Memory**: Transient context for current task execution.
2. **Project Memory**: Persistent store for project events and state.
3. **Knowledge Base**: Vector-based RAG for long-term knowledge distillation.

## Alternatives
- Simple long-context window: Rejected because it does not scale for long-running project lifecycles.

## Consequences
### Positive
- Efficient context management for long-term projects.
- Better knowledge retention and retrieval.
### Negative
- Complexity in managing vector database embeddings and synchronization.

## Date
2026-06-14