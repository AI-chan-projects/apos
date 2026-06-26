# 22_air_compiler_spec.md

---

## 0. Purpose

This document defines the AIR Compiler Specification of APOS.

It formalizes how structured human input (Markdown DSL) is transformed into AIR (APOS Intermediate Representation), and subsequently into executable system behavior.

The compiler is the bridge between:

- human language
- structured cognition (AIR)
- system execution (Actions + Events)

---

## 1. Core Principle

> The AIR Compiler is a deterministic transformation system, not a semantic interpreter.

It does not “understand” text.

It transforms structure into structured cognition.

---

## 2. Compilation Pipeline

The compilation process follows a strict staged pipeline:

Markdown DSL  
→ Lexical Parsing  
→ Structural Classification  
→ Schema Mapping  
→ AIR Node Construction  
→ Inference Graph Assembly  
→ Policy Context Attachment  
→ AIR Output Graph

---

## 3. Input Model (Markdown DSL)

The compiler accepts structured Markdown with constrained semantics.

Supported sections:

- Goal
- Constraints
- Task
- Actions
- Workflow
- Policy

Each section maps to a deterministic AIR construct.

---

## 4. Output Model (AIR Graph)

The output of compilation is an AIR Graph:

- Objective Node
- Assumption Layer
- Variable Space
- Inference Layer (CoT)
- Prediction Layer
- Validation Layer
- Meta Layer

All nodes are connected via dependency edges.

---

## 5. Compilation Stages

### 5.1 Lexical Parsing

Markdown is tokenized into:

- section headers
- bullet structures
- key-value pairs
- ordered sequences

No semantic inference occurs at this stage.

---

### 5.2 Structural Classification

Parsed tokens are classified into AIR-relevant categories:

- Intent blocks
- Constraint blocks
- Execution blocks
- Policy blocks

---

### 5.3 Schema Mapping

Each Markdown section is mapped to an AIR node type:

- Goal → Objective
- Constraints → Assumptions + PolicyHints
- Task → TaskNode
- Actions → ActionCandidates
- Workflow → ExecutionGraph
- Policy → PolicyLayer

---

### 5.4 AIR Node Construction

Structured data is transformed into AIR nodes:

- Objective Node
- Assumption Node
- Variable Nodes
- Inference Graph Node
- Validation Node
- Meta Node

---

### 5.5 Inference Graph Assembly

AIR nodes are connected into a directed reasoning graph:

- dependency edges
- causality edges
- execution precedence edges

This forms the internal CoT structure of AIR.

---

### 5.6 Policy Context Attachment

Each AIR node is annotated with:

- risk_score (initial estimate)
- policy constraints
- evaluation scope
- governance flags

This ensures execution safety alignment.

---

## 6. CoT (Inference Layer) Handling

The Inference Layer (CoT) is:

- internally preserved
- graph-structured
- not exposed as raw text output

CoT is represented as:

- inference nodes
- transformation edges
- decision branches

---

## 7. Determinism Rule

Given identical input Markdown:

- AIR output must always be identical
- node structure must be reproducible
- graph edges must be deterministic

No randomness is allowed in compilation.

---

## 8. Error Handling Model

Compilation failures occur when:

- schema is invalid
- section mapping is ambiguous
- required fields are missing

Failure behavior:

- emit CompilationFailureEvent
- generate minimal safe AIR graph
- mark nodes as uncertain=true

---

## 9. Ambiguity Resolution

If input is ambiguous:

1. generate lowest-safe AIR representation
2. mark uncertainty flags
3. defer refinement to Meta Layer
4. continue compilation (no hard stop unless critical)

---

## 10. AIR Graph Structure

AIR output is structured as:

- Objective Layer
- Assumption Layer
- Variable Space
- Inference Graph (CoT)
- Prediction Layer
- Validation Layer
- Meta Layer

All layers are connected via directed edges.

---

## 11. Policy Engine Integration

Compiler attaches policy metadata:

- risk_score estimation
- approval requirements
- constraint propagation
- execution eligibility hints

Policy Engine is not executed during compilation.

It is annotated.

---

## 12. Output Contract

The compiler outputs:

AIR Graph Object containing:

- nodes
- edges
- metadata
- policy annotations
- trace identifiers

---

## 13. AIR Traceability

Every AIR node must include:

- origin_markdown_section
- compilation_step_id
- dependency references

This ensures full traceability from text → cognition.

---

## 14. System Role

The AIR Compiler is:

- the cognitive bootstrap layer of APOS
- the transformation engine from human intent to structured reasoning
- the origin point of all executable system behavior

---

## 15. Design Principle

The compiler does not interpret meaning.

It enforces structure.

---

## 16. Final Model

Markdown DSL → Compiler → AIR Graph → Action Protocol → Execution Runtime → Event Store

---

## 17. Core Insight

If AIR is cognition,

then the compiler is:

> the mechanism that turns human language into structured thought inside APOS