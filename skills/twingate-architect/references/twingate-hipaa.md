# Twingate & HIPAA Compliance

## Summary
Twingate takes the position it is not a HIPAA business associate due to the "conduit exception" — it routes encrypted traffic without accessing, decrypting, or storing PHI content. Twingate generally avoids signing BAAs but will review customer-provided BAAs under specific conditions for qualifying accounts.

## Key Information
- Twingate's role is access control and encrypted traffic routing — no PHI processing occurs
- Traffic through relays is end-to-end encrypted; Twingate does not decrypt or inspect content
- Relay contact with data is transient (fractions of a second); no traffic is stored
- Peer-to-peer connections (when available) bypass Twingate relays entirely — relays are fallback only
- Conduit exception applies to both covered entities and business associates' subcontractors per DHHS guidance

## HIPAA Conduit Exception Basis
- Twingate relays function as transmission infrastructure (similar to ISPs or postal service)
- No "routine access" to PHI — only incidental contact during traffic routing
- DHHS Omnibus Rule commentary supports this classification
- Same conduit exception logic applies when Twingate acts as a subcontractor to a business associate

## BAA Policy
- **Preferred position:** No BAA (avoids incorrect implication of business associate status)
- **If required:** Twingate will review customer-provided BAAs with two mandatory conditions:
  1. BAA scope limited to where HIPAA actually applies to Twingate services
  2. BAA liability tied to limitation of liability provisions in the main services agreement
- **Eligibility threshold:** Annual plans above **$75,000** only

## Gotchas
- Twingate will not sign BAAs as standard practice — requires justification from compliance teams
- Having a BAA in place may incorrectly imply Twingate handles PHI as a business associate
- BAA review is resource-constrained; only available for qualifying contract size
- P2P connections mean some traffic never touches Twingate infrastructure at all — further weakening the business associate argument

## Contact
Reach out to your **account manager** for BAA, HIPAA, or compliance questions.

## Related Docs
- [Twingate Security Overview](https://www.twingate.com/docs/security)
- DHHS Omnibus Rule commentary (conduit exception)
- DHHS clarification on subcontractor conduit exception