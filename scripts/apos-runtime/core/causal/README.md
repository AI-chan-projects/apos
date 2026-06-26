전체 구조

[FAILURE EVENT]
      ↓
[EVENT CORRELATION]
      ↓
[CAUSAL CHAIN BUILD]
      ↓
[ROOT CAUSE RANKING]
      ↓
[EXPLANATION OUTPUT]

“왜 이 일이 일어났는가”를 구조적으로 증명하는 단계

이건 디버깅이 아니라:

시스템 내부 인과관계를 역추적하는 사고 엔진

⸻

🧠 APOS Causal Graph Engine (v0.1)

📁 추가 구조

core/causal/
    causal_graph_builder.py
    causal_trace_engine.py
    event_causality_resolver.py
    causality_types.py
ui/causal/
    causal_viewer.py
    causal_router.py

⸻

🧭 0. 목적

Causal Graph Engine의 목적:

Event를 “시간 순서”가 아니라
원인 → 결과 관계 그래프로 재구성

⸻

🧠 1. 핵심 개념

1. Event ≠ 단순 기록

기존:

Event = log

이제:

Event = causal node (원인 구조 포함)

⸻

2. Causal Edge

A → B
(A caused B)

⸻

3. Causal Chain

AIR 생성
   ↓
TaskGraph 생성
   ↓
DAG Scheduling
   ↓
Node blocked
   ↓
Approval request