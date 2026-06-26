# 17_APOS-compiler-architecture.md

---

## 0. Purpose

This architecture defines how APOS transforms Markdown DSL into executable runtime behavior through AIR (APOS Intermediate Representation).

It establishes the full compilation pipeline:

Markdown DSL → AIR → Execution Graph → Runtime Actions → Event Store

This is the core cognitive execution pipeline of APOS.

---

## 1. High-Level Pipeline

Markdown DSL  
↓  
DSL Parser Layer  
↓  
AIR Compiler (Cognitive IR Builder)  
↓  
Policy Binding Layer  
↓  
Execution Planner (Action Graph Builder)  
↓  
Runtime Executor  
↓  
Event Store  
↓  
Memory + Meta Learning Loop  

---

## 2. System Layers

APOS Compiler is structured into five sequential layers.

---

## 2.1 DSL Parsing Layer (Syntax → Structure)

### Responsibility

Convert Markdown DSL into structured semantic blocks.

### Output Structure

- sections
- metadata
- hierarchy
- raw intent blocks

### Principle

No reasoning occurs in this layer.  
Only structural decomposition is performed.

---

## 2.2 AIR Compiler Layer (Structure → Cognition)

### Responsibility

Transform structured DSL into AIR cognitive representation.

### Subcomponents

#### Intent Extractor
Maps:
- Goal → Objective
- Task → TaskNode

#### Assumption Builder
Maps:
- Constraints → Assumptions

#### Variable Mapper
Extracts:
- control variables
- latent variables

#### Inference Scaffold Builder
Constructs:
- reasoning structure (CoT internal representation)
- dependency skeleton

---

### Output

AIR object containing:

- objective
- assumptions
- variables
- inference graph
- task decomposition

---

## 2.3 Policy Binding Layer (Constraint Injection)

### Responsibility

Attach governance rules to AIR nodes.

### Inputs

- AIR graph
- Global Policy Engine

### Output

Protected AIR object with policy context attached to all nodes.

### Rule

No AIR node exists without policy evaluation context.

---

## 2.4 Execution Planner (AIR → Action Graph)

### Responsibility

Convert AIR structures into executable action plans.

### Mapping Logic

| AIR Element | Execution Element |
|-------------|------------------|
| Objective | Goal State |
| TaskNode | Job |
| Inference Graph | Execution Path |
| Variables | Runtime Parameters |

### Output

Directed Acyclic Graph (DAG) of executable actions.

---

## 2.5 Runtime Executor (Action → Reality)

### Responsibility

Execute actions under strict policy constraints and system governance.

### Execution Flow

1. Action Request generated
2. Policy Engine validation
3. If denied, reject and log event
4. If approved, execute action
5. Emit immutable event to Event Store

---

## 3. Action Runtime Model

Each action is represented as a structured runtime entity:

- type
- parameters
- execution context
- policy status
- execution state

Actions are the atomic units of execution in APOS.

---

## 4. Event Loop Integration

Every action execution produces an immutable event.

These events:

- update system state
- feed into memory systems
- contribute to future AIR refinement

---

## 5. Meta Feedback Loop (Learning System)

Execution results are continuously fed back into the system:

Execution Result  
↓  
Event Store  
↓  
Memory Aggregation  
↓  
AIR Meta Layer Update  
↓  
Compiler Optimization Loop  

This enables system-level learning over time.

---

## 6. Key Design Principles

---

### 6.1 Separation of Concerns

- Markdown DSL defines intent
- AIR defines cognition
- Execution Graph defines planning
- Runtime defines reality

---

### 6.2 Determinism Principle

Given identical inputs and state:

Markdown → AIR → Execution Graph → Runtime behavior must be deterministic.

---

### 6.3 Policy Non-bypass Rule

No system layer may bypass the Policy Engine.

This includes AIR and execution planning layers.

---

### 6.4 Traceability Rule

Every execution must be traceable through:

Markdown → AIR → Action → Event

---

## 7. Compiler Architecture Summary

Markdown DSL  
↓  
DSL Parser  
↓  
AIR Compiler  
↓  
Policy Binding  
↓  
Execution Planner  
↓  
Runtime Executor  
↓  
Event Store  
↓  
Memory + Learning Loop  

---

## 8. Core Insight

APOS is not an agent framework.

It is a compiled cognitive operating system where:

- language becomes structure
- structure becomes reasoning
- reasoning becomes execution
- execution becomes history

---

## 9. Final Model

- Language Layer: Markdown DSL
- Cognition Layer: AIR
- Constraint Layer: Policy Engine
- Planning Layer: Execution Graph
- Runtime Layer: System Execution
- Memory Layer: Event Store

---

## 10. Closing Principle

APOS does not simulate intelligence.

It compiles intelligence into executable structure.