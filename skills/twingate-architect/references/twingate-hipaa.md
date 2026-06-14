# Twingate & HIPAA Compliance

## Summary
Twingate provides network access control and traffic routing but does not store, decrypt, or process PHI content. Twingate asserts it qualifies for the HIPAA "conduit exception" and is not a business associate, though it will review BAAs under specific conditions.

## Key Information
- Twingate's position: qualifies as a **conduit** (like an ISP), not a business associate under HIPAA
- Traffic through relays is **end-to-end encrypted** — Twingate does not decrypt or inspect content
- Relays do **not store traffic** — data is transient (milliseconds of contact)
- Twingate **prefers not to sign BAAs** as it may imply incorrect regulatory obligations
- Peer-to-peer connections (when available) bypass Twingate relays entirely — zero PHI contact
- Conduit exception applies to both covered entities and subcontractors of business associates per DHHS guidance

## Legal Basis
- **Conduit Exception**: Defined in DHHS commentary on the HIPAA Omnibus Rule
- Applies because Twingate does not require "access on a routine basis" to PHI
- DHHS confirmed conduit exception extends to **subcontractors** of business associates

## BAA Review Conditions
Twingate will review customer-provided BAAs only if:
1. BAA scope is limited to where HIPAA **actually applies** to Twingate services
2. BAA liability is tied to the **limitation of liability** in the main services agreement
3. Customer is on an **annual plan above $75,000**

## Gotchas
- Twingate will not provide its own BAA form — review is of **customer's standard form only**
- Signing a BAA may create misleading compliance implications for both parties
- Relay contact with PHI only occurs when P2P connection is unavailable (fallback scenario)
- BAA review is subject to legal resource prioritization — not guaranteed for all enterprise customers

## Contact
Reach account manager for BAA and HIPAA questions.

## Related Docs
- [Twingate Security](https://www.twingate.com/docs/security) — security controls and measures
- DHHS Omnibus Rule commentary (external)