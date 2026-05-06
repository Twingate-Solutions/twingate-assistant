# Twingate & HIPAA

## Summary
Twingate takes the position that it is not a HIPAA "business associate" and therefore does not require a BAA, citing the "conduit exception" under DHHS Omnibus Rule guidance. Twingate relays only transiently route end-to-end encrypted traffic without decrypting or storing it. BAA review is available under specific conditions for larger contracts.

## Key Information
- Twingate qualifies for the **conduit exception**: acts as a transmission service only, not a data processor or storer
- PHI traffic through Twingate relays is **end-to-end encrypted** — Twingate cannot decrypt or inspect contents
- Relays **do not store traffic** — data contact is transient (fractions of a second)
- **Peer-to-peer connections** are preferred; relays are fallback only, meaning PHI may never touch Twingate infrastructure at all
- Conduit exception applies to both covered entities and **subcontractors of business associates** per DHHS clarification
- No PHI is involved in Twingate's core functions: user/resource access management, authentication, authorization

## Prerequisites
- N/A — this is a compliance position document, not a setup guide

## Configuration Values
- None applicable

## BAA Review Conditions
If a BAA is required by your compliance team:
1. BAA scope limited to extent HIPAA **actually applies** to Twingate services
2. Liability under BAA tied to **limitation of liability** in the main services agreement
3. Only available for **annual plans above $75,000**
4. Contact your account manager to initiate

## Gotchas
- Twingate **prefers not to sign BAAs** — doing so could incorrectly imply business associate status
- The conduit exception does **not** mean Twingate has weaker security — security measures apply regardless of HIPAA applicability
- Twingate reviews **your standard form BAA** only (does not provide its own form)
- Legal review is resource-constrained; BAA review is not available for smaller contracts

## Related Docs
- [Twingate Security](https://www.twingate.com/docs/security) — security measures overview
- DHHS Omnibus Rule commentary (external) — conduit exception definition
- DHHS subcontractor clarification (external) — conduit exception for business associate subcontractors