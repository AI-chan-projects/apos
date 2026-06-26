# 29_system_usage_and_human_workflow_spec.md

---

## 0. Purpose

This document defines how a Human Director interacts with APOS as a cognitive-operational system.

It formalizes the practical usage patterns of:

- AIR creation
- project lifecycle management
- Control Plane interaction
- decision loops
- system feedback interpretation

This is the human-facing operational model of APOS.

---

## 1. Core Principle

> APOS is not operated by commands. It is operated by structured intent.

Human interaction is not procedural control, but cognitive structuring.

---

## 2. Human Role Definition

### 2.1 Human Director

The Human Director is responsible for:

- defining Goals
- providing strategic intent
- approving high-risk Actions
- resolving system ambiguities
- overriding governance decisions when necessary

The Human Director does not execute tasks directly.

---

## 3. Primary Interaction Loop

APOS operates through a continuous cognitive loop:

Human Intent → AIR Definition → System Execution → Event Feedback → Human Review → AIR Update

This loop is the fundamental interaction cycle.

---

## 4. AIR Usage Model

### 4.1 When AIR is created

AIR is created when:

- a new Goal is defined
- system behavior needs structured decomposition
- uncertainty requires explicit modeling
- execution planning is required

---

### 4.2 AIR granularity rules

AIR should be:

- high-level for strategic intent
- detailed only where decision complexity exists
- minimal where Policy Engine suffices

---

### 4.3 Human vs System reasoning boundary

- Human: defines Objective and constraints
- System: performs inference, prediction, validation
- Human: resolves ambiguity and final approval

---

## 5. Project Lifecycle Usage

### 5.1 Project creation

A project begins when:

- a Goal is declared
- AIR is constructed
- system initializes execution graph

---

### 5.2 Stage progression

Projects progress through stages:

- planning
- execution
- validation
- completion

Stage transitions are driven by Event outcomes, not manual switching.

---

### 5.3 Completion condition

A project is complete when:

- Goal conditions are satisfied
- all critical Actions are resolved
- Event Store confirms final state

---

## 6. Control Plane Usage

### 6.1 Interaction model

Human Director interacts via Control Plane using:

- Approval commands
- Rejection commands
- Override commands
- Query commands

---

### 6.2 Approval workflow

1. system proposes Action
2. Policy Engine evaluates risk
3. Action enters pending state
4. Human approves or rejects via Control Plane
5. Event is recorded

---

### 6.3 Emergency interaction

Human Director may:

- halt system execution
- force safe mode
- trigger rollback
- suspend all Actions

---

## 7. Decision Loop Model

Decisions are not single events but loops:

1. AIR proposes structure
2. Policy evaluates constraints
3. Kernel executes eligible Actions
4. Events are recorded
5. Human reviews outcomes
6. AIR is updated

This loop continuously refines system behavior.

---

## 8. Cognitive Load Distribution

APOS divides cognitive responsibility:

### 8.1 Human handles

- goal definition
- ambiguity resolution
- strategic judgment
- final approval decisions

---

### 8.2 System handles

- inference generation (AIR)
- execution scheduling (Kernel)
- policy enforcement
- trace generation
- memory accumulation

---

### 8.3 Shared responsibility

- interpretation of outcomes
- evolution of AIR structure
- refinement of system behavior

---

## 9. Feedback Interpretation Model

System outputs are interpreted as:

- Events → factual history
- Trace → causal explanation
- Metrics → performance signals
- AIR → reasoning structure

Human Director uses these to adjust intent.

---

## 10. Error Handling in Human Workflow

When ambiguity occurs:

1. system marks AIR node as uncertain
2. Control Plane requests human input
3. Human resolves or defers
4. system resumes execution

No silent ambiguity is allowed.

---

## 11. Iterative Refinement Model

APOS is used iteratively:

- each project improves AIR structure
- each failure refines Policy rules
- each execution improves Kernel scheduling
- each interaction improves human-system alignment

---

## 12. Human-System Boundary Principle

> Humans define meaning. Systems execute structure.

APOS strictly enforces this separation.

---

## 13. Invariants

- I1: Human Director retains final authority
- I2: System cannot override human intent
- I3: All actions must originate from AIR or Control Plane input
- I4: Execution is always event-driven
- I5: Human interaction is always mediated through structured interfaces
- I6: No implicit system behavior is allowed outside defined loops

---

## 14. System Role

This layer defines:

- how APOS is actually used
- how cognition is distributed
- how control flows between human and system

---

## 15. Design Principle

APOS is not a tool operated by humans.

It is a shared cognitive system where:

> humans define intent, and the system materializes it through structured execution

---

## 16. Final Model

Human Intent → AIR → Policy → Execution → Event → Trace → Human Feedback → AIR Update

---

## 17. Core Insight

If AIR defines structured thinking,

and Kernel defines structured execution,

then Human Workflow defines:

> how thinking and execution become a continuous shared cognitive loop between human and system