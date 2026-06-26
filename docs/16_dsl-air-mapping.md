# 16_dsl-air-mapping.md
---
## 0. Purpose
This specification defines how Markdown DSL constructs are transformed into AIR (APOS Intermediate Representation).
It establishes a deterministic mapping between:
- human-authored structured text (Markdown DSL)
- system-level cognitive representation (AIR)
---
## 1. Core Principle
Markdown expresses intent.  
AIR constructs reasoning.
Mapping is NOT semantic interpretation.  
It is structured compilation.
---
## 2. Mapping Pipeline
Markdown DSL  
   ↓  
Syntactic Parsing  
   ↓  
Structural Classification  
   ↓  
AIR Node Construction  
   ↓  
Inference Graph Assembly  
   ↓  
Policy Context Attachment  
   ↓  
AIR Object  
---
## 3. DSL → AIR Core Mapping Rules
---
## 3.1 Goal → Objective Node
### Markdown DSL

## Goal
Build a user behavior analysis system

AIR Output

Objective:
  description: "Build a user behavior analysis system"

⸻

## 3.2 Constraints → Assumption Filter + Policy Hint

Markdown DSL

## Constraints
- No external API calls
- Human approval required for high-risk actions

AIR Output

Assumptions:
  - external_api_access = false
PolicyHints:
  - high_risk_action requires Human Approval

⸻

## 3.3 Task → Decomposed Objective Subgraph

Markdown DSL

## Task: Analyze Logs
- collect data
- preprocess data
- extract patterns

AIR Output

TaskNode:
  name: Analyze Logs
  subgraph:
    - collect_data
    - preprocess_data
    - extract_patterns

⸻

## 3.4 Actions → Execution Candidates

Markdown DSL

## Actions
- fetch(source=database)
- analyze(method=clustering)

AIR Output

ActionCandidates:
  - type: fetch
    params: { source: database }
  - type: analyze
    params: { method: clustering }

⸻

## 3.5 Workflow → Directed Acyclic Execution Graph (DAG)

Markdown DSL

## Workflow
1. Collect Data
2. Train Model
3. Validate Results

AIR Output

ExecutionGraph:
  nodes:
    - Collect Data
    - Train Model
    - Validate Results
  edges:
    - Collect → Train
    - Train → Validate

⸻

## 3.6 Policy Block → Policy Attachment Layer

Markdown DSL

## Policy
- deny: external_write
- require: approval for deletion

AIR Output

PolicyLayer:
  deny:
    - external_write
  require_approval:
    - deletion

⸻

## 4. Structural Binding Rules

⸻

## 4.1 Section Identity Rule

Each Markdown section maps to exactly one AIR node type:

| Markdown Section | AIR Target |
|------------------|------------|
| Goal | Objective |
| Constraints | Assumptions + PolicyHints |
| Task | TaskNode |
| Actions | ActionCandidates |
| Workflow | ExecutionGraph |
| Policy | PolicyLayer |

⸻

## 4.2 No Mixed Mapping Rule

A single Markdown block cannot generate:

* multiple unrelated AIR roots
* ambiguous node types

Each block → one primary AIR construct

⸻

## 4.3 Hierarchical Preservation Rule

Markdown nesting does NOT equal AIR nesting.

Instead:

* structure is inferred
* dependencies are computed

⸻

## 5. Inference Injection Rule

Markdown does NOT define inference.

But AIR MUST generate:

* implicit relationships
* dependency graph
* execution order

This is derived, not authored.

⸻

## 6. Policy Attachment Rule

All AIR nodes are automatically annotated with:

PolicyContext:
  evaluated: true
  source: global_policy_engine

No exception.

⸻

## 7. Ambiguity Handling

If Markdown is ambiguous:

Step 1

Convert to lowest-safe AIR form

Step 2

Mark as:

uncertain: true

Step 3

Push to Meta Layer for refinement

⸻

## 8. AIR Construction Priority

When conflict occurs:

1. Policy constraints override
2. Workflow structure overrides
3. Task structure overrides
4. Goal intent is preserved but adjusted

⸻

## 9. Versioning Rule

This spec is versioned independently from:

* AIR structure
* Markdown DSL syntax
* Policy Engine

Because:

mapping rules evolve faster than core system architecture

⸻

## 10. Design Principle

Markdown DSL is:

a probabilistic human input language

AIR is:

a deterministic execution-ready cognitive graph

Mapping is:

the compiler bridge between the two

⸻

## 11. Summary Model

Markdown DSL → Intent Encoding
AIR → Structured Cognition
Policy → Constraint Filter
Event → Reality Trace
Mapping Spec → Compiler Bridge

⸻

## 12. Final Insight

This mapping layer is the first point where:

human language becomes system-structured cognition.

It is not translation.

It is compilation.