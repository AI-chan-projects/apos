🧭 0. 목적

Time Scrubbing Center는 APOS 실행을 다음처럼 다룬다:

기존

* event stream = 기록

이제

👉 event stream = “조작 가능한 시간 축”

⸻

🧠 1. 핵심 기능

1. Time Scrubbing (핵심)

* slider로 time 이동
* 특정 timestamp로 state 복원

⸻

2. Past View

* 과거 execution replay
* DAG 상태 재구성

⸻

3. Future Projection (semi-deterministic)

* DAG + policy 기반 “가능성 시뮬레이션”