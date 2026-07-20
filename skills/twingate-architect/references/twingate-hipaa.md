# Twingate & HIPAA

## Summary
Twingate's position is that it does not qualify as a HIPAA "business associate" due to the conduit exception, meaning a BAA is generally unnecessary. Twingate relays only transiently pass end-to-end encrypted traffic without decrypting or storing it. BAA review is available under specific conditions for larger enterprise contracts.

## Key Information
- Twingate's admin console manages access control — no PHI involved in auth/authorization processes
- Traffic through Twingate relays is **end-to-end encrypted**; Twingate does not decrypt or inspect content
- Relays **do not store traffic** — data is transient (contact duration measured in fractions of a second)
- Twingate supports **peer-to-peer connections** where traffic never touches Twingate relay infrastructure at all; relays are fallback only
- The conduit exception applies equally to subcontractors of business associates per DHHS guidance

## Conduit Exception Basis
- Twingate does not require "access on a routine basis" to any PHI
- Functionally equivalent to a postal service or ISP — transports data without processing or storing it
- DHHS Omnibus Rule commentary explicitly covers this scenario
- Applies to both covered entities and their business associates (and subcontractors thereof)

## BAA Policy
| Condition | Detail |
|-----------|--------|
| Twingate preference | Not to sign BAAs (avoids incorrect implication of business associate status) |
| BAA available | Yes, for customer-form BAAs only |
| Minimum contract threshold | Annual plans **above $75,000** |
| Required BAA terms | (1) Applies only where HIPAA actually applies to Twingate services; (2) Liability tied to limitation of liability provisions in main services agreement |

## Gotchas
- Signing a BAA could create incorrect legal implications that HIPAA governs Twingate's services — Twingate considers this undesirable for both parties
- BAA review is resource-constrained; only available for high-value annual contracts
- Peer-to-peer connections mean PHI may never touch Twingate infrastructure at all — relay contact is not guaranteed

## Prerequisites
- For BAA review: annual contract exceeding $75,000
- Contact assigned account manager for BAA requests or compliance questions

## Related Docs
- [Twingate Security](https://www.twingate.com/docs/security) — security measures in place regardless of HIPAA applicability
- DHHS Omnibus Rule commentary (external) — conduit exception guidance
- DHHS subcontractor clarification (external) — conduit exception for business associate subcontractors