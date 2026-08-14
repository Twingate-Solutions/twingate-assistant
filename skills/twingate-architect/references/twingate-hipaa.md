---
source: https://www.twingate.com/docs/twingate-hipaa
type: docs
fetched: 2026-08-14
source_version: edcb24bd3fea74647ad360d698ed85f21078c1fcf90cbe442425b7ed407c72ac
---

# Twingate & HIPAA

## Summary
Twingate's position is that it does not qualify as a HIPAA "business associate" due to the conduit exception, as it only routes encrypted traffic without accessing, storing, or processing PHI. Twingate discourages BAA execution but will review customer-provided BAAs under specific conditions for qualifying accounts.

## Key Information
- Twingate does **not** consider itself a business associate under HIPAA
- Relies on the **conduit exception** (per DHHS Omnibus Rule commentary): acts as a transmission service only
- Traffic through relays is **end-to-end encrypted** — Twingate cannot decrypt or inspect contents
- Relays do **not store** traffic; data is transient (contact measured in fractions of a second)
- **Peer-to-peer connections** (when available) bypass Twingate relays entirely — no Twingate infrastructure touches the traffic
- Relays are only a fallback when direct P2P connections cannot be established
- Conduit exception applies to **subcontractors of business associates** as well (per DHHS clarification)

## What Twingate Does vs. Does Not Touch
| Function | PHI Involved? |
|---|---|
| Admin console (user/resource access management) | No |
| Auth/authorization decisions | No |
| Traffic relay (fallback routing) | Possible transit only — encrypted, not stored |
| Peer-to-peer connections | No Twingate infrastructure involved |

## BAA Policy
- Twingate **prefers not to sign BAAs** — having one implies business associate status, which is inaccurate
- Will **review customer-provided BAAs** with two requirements:
  1. BAA applies only to the extent HIPAA actually applies to Twingate services
  2. Liability under BAA is tied to the main services agreement's limitation of liability provisions
- BAA review only available for **annual plans above $75,000**

## Gotchas
- Signing a BAA could create incorrect legal implications for both parties
- The conduit exception requires that Twingate not have "routine access" to PHI — Twingate's relay architecture satisfies this
- PHI may theoretically transit relays only when P2P connections are unavailable; even then, it is encrypted and not inspected

## Contact
- Reach your **account manager** for BAA or HIPAA-related questions

## Related Docs
- [Twingate Security Overview](https://www.twingate.com/docs/security)
- DHHS Omnibus Rule commentary (conduit exception)
- DHHS clarification on subcontractor conduit exception