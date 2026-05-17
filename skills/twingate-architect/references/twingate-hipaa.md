# Twingate & HIPAA

## Summary
Twingate provides guidance for HIPAA-regulated customers on why a Business Associate Agreement (BAA) is generally unnecessary. Twingate operates as a network conduit—routing encrypted traffic without accessing, storing, or decrypting PHI—qualifying for the HIPAA "conduit exception." Twingate will review BAAs only under specific conditions for qualifying contracts.

## Key Information
- Twingate's position: It is **not a business associate** under HIPAA due to the conduit exception
- Traffic through Twingate relays is **end-to-end encrypted**; Twingate does not decrypt or inspect content
- Relays do **not store traffic**; data contact is transient (fractions of a second)
- Twingate **prefers not to sign BAAs** as doing so implies business associate status incorrectly
- Conduit exception applies to both covered entities and business associates (per DHHS Omnibus Rule commentary)
- Peer-to-peer connections bypass Twingate relays entirely; relays are fallback only

## What Twingate Touches (and Doesn't)
| Function | PHI Involved? |
|---|---|
| Admin console (access policy management) | No |
| Authentication/authorization | No |
| Traffic relay routing | Transient, encrypted, unread |
| Traffic storage | Never |

## BAA Review Conditions
If a BAA is required by your compliance team, Twingate will review with these requirements:
1. BAA scope limited to extent HIPAA **actually applies** to Twingate services
2. Liability tied to **limitation of liability** provisions in the main services agreement
3. **Annual contract must exceed $75,000** to receive BAA review

## Gotchas
- Signing a BAA can create incorrect legal impressions about Twingate's role—Twingate actively discourages it
- Conduit exception applies to subcontractors of business associates, not just first-tier relationships (per DHHS clarification)
- P2P connections mean PHI may **never touch Twingate infrastructure at all**; relay contact is not guaranteed

## Prerequisites
- Must be on an **annual plan above $75,000** to request BAA review
- Contact your **account manager** for BAA or HIPAA questions

## Related Docs
- [Twingate Security](https://www.twingate.com/docs/security) — security measures overview
- DHHS Omnibus Rule commentary (conduit exception definition)
- DHHS subcontractor BAA guidance