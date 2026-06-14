# ADR-004: Telegram Control Plane

## Status
Accepted

## Context
The Human Director needs a persistent, mobile-first, and real-time interface to oversee the APOS system.

## Decision
Utilize Telegram Bot API as the primary Control Plane interface for alerts, monitoring, and approval workflows.

## Alternatives
- Custom Web Dashboard: Rejected due to high maintenance overhead and lack of real-time push notification efficiency on mobile.

## Consequences
### Positive
- Instant reachability on all devices.
- Rich interactive UI elements (buttons, menus) are natively supported.
### Negative
- Dependency on a third-party messaging platform.
- Security concerns regarding bot token management.

## Date
2026-06-14