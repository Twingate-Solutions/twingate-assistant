# Twingate & HIPAA

## Summary
Twingate takes the position that it is not a HIPAA "business associate" and therefore a BAA is generally unnecessary. This is based on the "conduit exception" — Twingate only routes encrypted traffic without accessing, storing, or inspecting PHI content. Twingate will review customer BAAs under specific conditions for large accounts.

## Key Information
- Twingate's role: access control + encrypted traffic routing only
- Relays pass traffic without decrypting or storing it (transient, sub-second contact)
- Peer-to-peer connections bypass relays entirely; relays are fallback only
- End-to-end encryption means Twingate cannot read traffic contents
- No PHI involved in admin console operations (user/resource management, auth/authz)

## Twingate's Legal Position
- Qualifies for **conduit exception** under DHHS Omnibus Rule commentary
- Analogous to ISPs/postal services: transport only, no processing or storage
- Conduit exception applies to **subcontractors of business associates** as well (per DHHS clarification)
- Signing a BAA could incorrectly imply Twingate is a business associate

## BAA Review Conditions
If compliance team requires a BAA, Twingate will review with these requirements:
1. BAA applies **only to the extent HIPAA actually applies** to Twingate services
2. Liability tied back to **limitation of liability provisions** in the main services agreement
3. Only available for **annual plans above $75,000**

## Gotchas
- Twingate **does not proactively offer** BAAs and prefers not to sign them
- Most network traffic never touches Twingate infrastructure (P2P connections)
- When relays are used, contact duration is measured in fractions of a second
- No BAA review for accounts below $75,000/year threshold
- PHI-handling responsibility remains with the covered entity/business associate — Twingate is the conduit

## Prerequisites
- For BAA review: annual contract above $75,000
- Contact your account manager for BAA inquiries

## Related Docs
- [Twingate Security](https://www.twingate.com/docs/security) — security measures overview
- DHHS Omnibus Rule commentary (conduit exception definition)
- DHHS clarification on subcontractor conduit exception

## Contact
Reach out to your **account manager** for BAA, HIPAA, or compliance questions.