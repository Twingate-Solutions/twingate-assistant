# Twingate & HIPAA

## Summary
Twingate takes the position that it is not a HIPAA "business associate" and therefore a BAA is generally unnecessary. This position is based on the HIPAA "conduit exception," as Twingate only routes encrypted traffic without accessing or storing PHI content. Twingate will review customer BAAs under specific conditions for larger accounts.

## Key Information
- Twingate classifies itself as a **conduit**, not a business associate, under HIPAA
- Traffic through Twingate relays is **end-to-end encrypted** — Twingate does not decrypt or inspect content
- Relays **do not store traffic** — data is transient (contact duration measured in fractions of a second)
- Twingate **prefers not to sign BAAs** as it may incorrectly imply business associate status
- The conduit exception applies to **subcontractors of business associates** as well (per DHHS clarification)
- Many connections use **peer-to-peer** routing, meaning traffic never touches Twingate relays at all; relays are fallback only

## Legal Basis
- **Conduit exception**: Derived from DHHS commentary on the HIPAA Omnibus Rule
- Applies to entities transporting data without processing or storing it (e.g., ISPs, postal services)
- DHHS confirmed conduit exception extends to subcontractors of business associates

## BAA Review Conditions
If a BAA is required by your compliance team, Twingate will review (not originate) it with these requirements:
1. BAA scope limited to services where HIPAA **actually applies** to Twingate
2. BAA liability tied to **limitation of liability** provisions in the main services agreement
3. Only available for **annual plans above $75,000**

## Gotchas
- Twingate will not sign a BAA without the two conditions above being met
- Signing a BAA could create incorrect legal impressions about Twingate's role — Twingate actively discourages it
- The conduit position does **not** reduce Twingate's security commitments — security practices apply regardless of HIPAA applicability
- PHI contact only theoretically occurs when a user sends/receives PHI to a protected resource via a relay (not peer-to-peer)

## Prerequisites
- Annual contract above $75,000 required for BAA review
- Contact your **account manager** for BAA or HIPAA-related questions

## Related Docs
- [Twingate Security](https://www.twingate.com/docs/security) — details on security measures
- [DHHS Omnibus Rule Commentary](https://www.hhs.gov) — conduit exception legal basis
- [DHHS subcontractor clarification](https://www.hhs.gov) — conduit exception for business associate subcontractors