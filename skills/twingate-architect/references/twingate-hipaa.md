# Twingate & HIPAA Compliance

## Summary
Twingate takes the position that it is not a HIPAA business associate under the "conduit exception," as it only routes encrypted traffic without accessing, storing, or decrypting PHI. BAAs are generally unnecessary, though Twingate will review them under specific conditions for qualifying customers.

## Key Information
- Twingate qualifies for the **conduit exception** under HIPAA (per DHHS Omnibus Rule commentary)
- Relays only transport encrypted traffic — no decryption, no content inspection, no storage
- Traffic contact duration is measured in **fractions of a second**
- Peer-to-peer connections bypass Twingate relays entirely; relays are fallback only
- Conduit exception applies to **subcontractors of business associates** as well as direct business associates
- No PHI is involved in user/resource access authorization or admin console operations

## Prerequisites for BAA Review
- Annual contract **above $75,000**
- Customer must accept two conditions:
  1. BAA applies only to the extent HIPAA actually governs Twingate's services
  2. BAA liability is tied to the limitation of liability in the main services agreement

## Twingate's Legal Position
| Aspect | Detail |
|--------|--------|
| Classification | Not a business associate |
| Basis | Conduit exception (DHHS Omnibus Rule) |
| PHI exposure | Transient relay routing only, end-to-end encrypted |
| Storage | None — relays do not store traffic |
| Decryption | None — content is not inspected |

## Gotchas
- Signing a BAA may **incorrectly imply** Twingate is a business associate — Twingate actively discourages this
- BAA review is subject to **legal resource prioritization**; only available for large contracts
- The conduit exception argument depends on Twingate's relay behavior — any architectural change could affect this analysis
- PHI *could* theoretically transit relays (as fallback), but this is transient and encrypted

## Contact
Reach account manager for BAA/HIPAA questions.

## Related Docs
- [Twingate Security](https://www.twingate.com/docs/security) — security measures protecting customer data
- DHHS commentary on the Omnibus Rule (external)
- DHHS subcontractor clarification (external)