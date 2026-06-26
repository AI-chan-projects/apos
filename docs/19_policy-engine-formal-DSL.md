# 19_policy-engine-formal-DSL.md
---
## 0. Purpose
This document defines the formal Policy Engine DSL used in APOS to evaluate and govern all Actions derived from AIR.
It standardizes:
- DENY (hard block)
- ALLOW (direct execution)
- APPROVE (human-in-the-loop gate)
- Risk scoring model
- Rule composition and resolution logic
The Policy Engine is the execution constraint layer of APOS.
---
## 1. Core Decision Model
Each Action is resolved into exactly one decision:
| Decision | Meaning |
|----------|--------|
| DENY | Execution is forbidden |
| ALLOW | Execution proceeds immediately |
| APPROVE | Human Director approval required before execution |
---
## 2. Policy Rule Structure
A policy rule is defined as:
```yaml
policy:
  id: string
  priority: integer
  match:
    action_type: string | regex
    resource: string | pattern
    context: optional conditions
  condition:
    risk_score: expression
    constraints: list
  decision: DENY | ALLOW | APPROVE
  reason: string
```
⸻

## 3. Policy Evaluation Pipeline

Policy evaluation follows a deterministic pipeline:

1. Action received from Execution Planner
2. Rule matching
3. Risk scoring
4. Constraint evaluation
5. Decision resolution

⸻

## 4. Rule Matching Semantics

A rule applies if:

* action_type matches
* resource matches
* context conditions are satisfied

Multiple matching rules are allowed.

⸻

## 5. Risk Scoring Model

⸻

## 5.1 Risk Score Definition

RiskScore is a normalized value:

RiskScore ∈ [0.0, 1.0]

* 0.0 → no risk
* 1.0 → system-critical risk

⸻

## 5.2 Risk Components

RiskScore is computed from weighted components:

* Resource Sensitivity
* Irreversibility
* External Dependency
* Governance Sensitivity

⸻

## 5.3 Conceptual Formula

RiskScore =
w1 * ResourceSensitivity +
w2 * Irreversibility +
w3 * ExternalDependency +
w4 * GovernanceSensitivity

⸻

## 6. Default Decision Logic

If no policy rule matches:

* RiskScore < 0.3 → ALLOW
* 0.3 ≤ RiskScore < 0.7 → APPROVE
* RiskScore ≥ 0.7 → DENY

⸻

## 7. Rule Resolution Order

Rules are resolved by:

1. Priority (highest first)
2. Specificity of match
3. Risk overrides

⸻

## 8. Override Hierarchy

Decision precedence:

DENY > APPROVE > ALLOW

* DENY always overrides other decisions
* APPROVE overrides ALLOW when both apply

⸻

## 9. Human Director Integration

When decision is APPROVE:

* Execution is paused
* Approval event is required

Approval event format:

approval:
  action_id: string
  director_id: string
  decision: approve | reject
  timestamp: datetime

⸻

## 10. Policy Context Binding

Each evaluated Action produces:

PolicyContext:
evaluated: true
risk_score: float
decision: DENY | ALLOW | APPROVE
source: policy_engine_v0.1

⸻

## 11. Safety Guarantees

⸻

## 11.1 Non-Bypass Rule

No component may bypass the Policy Engine:

* AIR cannot override policies
* Execution Planner cannot skip evaluation
* Runtime cannot ignore decisions

⸻

## 11.2 Determinism Rule

Given identical inputs and policy state:

Action + Policy → deterministic decision

⸻

## 12. Failure Modes

## 12.1 Rule Conflict

Resolved via priority and specificity.

## 12.2 Missing Rule

Fallback to risk-based default evaluation.

## 12.3 Engine Failure

Fails safe:

Default decision = DENY

⸻

## 13. System Role of Policy Engine

The Policy Engine is not a filter.

It is the deterministic constraint system that shapes AIR into executable behavior.

⸻

## 14. Final Model

Action
→ Rule Matching
→ Risk Evaluation
→ Decision Engine
→ { DENY | ALLOW | APPROVE }
→ Execution Gate