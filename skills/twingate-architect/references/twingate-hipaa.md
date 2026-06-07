# Twingate & HIPAA

## Summary
Twingate provides network access control and traffic routing but does not process or store PHI, qualifying for the HIPAA "conduit exception." Twingate's position is that it is not a business associate under HIPAA and prefers not to sign BAAs. BAA review is available for enterprise customers meeting spend thresholds.

## Key Information
- Twingate acts as a **conduit** (like an ISP or postal service), routing encrypted traffic without decrypting or storing contents
- Traffic through relays is **end-to-end encrypted**; Twingate cannot inspect contents
- Relays do **not store traffic** — data is transient (sub-second contact duration)
- Twingate **supports peer-to-peer connections**, meaning traffic may not even touch Twingate relays at all
- Relays are only used as fallback when P2P connections cannot be established
- DHHS conduit exception applies to **subcontractors of business associates** as well

## Prerequisites
- N/A (compliance/legal reference page, not implementation)

## Configuration Values
- None applicable

## BAA Review Conditions
If compliance team requires a BAA:
1. BAA applies **only to the extent HIPAA actually applies** to Twingate services
2. Liability under BAA is **tied to limitation of liability** in the main services agreement
3. BAA review only available for **annual plans above $75,000**
4. Contact your **account manager** to initiate

## Gotchas
- Signing a BAA could incorrectly imply Twingate is a business associate — Twingate considers this potentially undesirable for both parties
- PHI may only contact Twingate infrastructure when a user device transmits PHI to/from a protected resource via a relay (not P2P path)
- Twingate's non-HIPAA-applicability stance does **not reduce** their security commitments

## Legal Basis
- DHHS Omnibus Rule commentary — conduit exception
- Applies equally to subcontractors of business associates per DHHS clarification

## Related Docs
- [Twingate Security](https://www.twingate.com/docs/security) — security measures overview
- Contact: Account manager for BAA/HIPAA questions