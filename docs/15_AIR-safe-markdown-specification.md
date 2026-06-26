# 15: AIR-safe Markdown Specification

---

## Purpose

This document defines the writing rules for APOS Markdown documents to ensure compatibility with AIR (APOS Intermediate Representation).

The objective is to separate cognition, structure, and presentation, preventing formatting from altering system meaning.

---

## Principles

- AIR is the source of truth.
- Markdown is a presentation layer.
- Documents must preserve AIR semantics regardless of rendering.
- Representation must never change reasoning.

---

## Writing Rules

### One Concept per Document

Each document should describe one primary concept.

Large topics should be divided into linked documents instead of nested sections.

---

### One Representation per Section

A section should contain only one representation style.

Avoid mixing:

- conceptual explanation
- executable pseudocode
- JSON
- YAML
- implementation details

If multiple representations are needed, place them in separate documents and link to them.

---

### Avoid Nested Code Blocks

Do not place fenced code blocks inside other fenced code blocks.

If an example requires code fences, either:

- escape the fences appropriately, or
- move the example into a separate document and reference it.

---

### Externalize Complex Structures

Large schemas, execution flows, DSL definitions, and configuration files should exist as independent artifacts.

Examples:

- air_flow.yaml
- policy.dsl
- execution_graph.md

Documents should reference these artifacts instead of embedding them.

---

### Preserve Structural Independence

AIR defines the logical structure.

Markdown only visualizes that structure.

Changing document formatting must never change the meaning of AIR.

---

## Recommended Layering

AIR (Reasoning)

↓

APOS (Execution)

↓

Governance / Policy

↓

Memory / Event Store

↓

Markdown Documentation

↓

External Artifacts

---

## Design Philosophy

Documents exist to communicate ideas.

AIR exists to define ideas.

Markdown must remain a thin presentation layer over AIR.

---

## Summary

An AIR-safe document should:

- describe one concept
- use one representation style per section
- avoid nested formatting structures
- reference complex artifacts instead of embedding them
- preserve AIR semantics independently of Markdown