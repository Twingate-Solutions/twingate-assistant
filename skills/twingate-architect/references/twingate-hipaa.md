# Twingate & HIPAA

## Summary
Twingate provides guidance for HIPAA-regulated customers on why it considers itself exempt from BAA requirements under the HIPAA "conduit exception." Twingate acts as a traffic relay, not a data processor, and does not decrypt or store PHI in transit. BAAs are discouraged but can be reviewed under specific conditions for qualifying customers.

## Key Information
- Twingate's position: it is **not a business associate** under HIPAA
- Qualifies under the **conduit exception** (similar to ISPs or postal services)
- Traffic through relays is **end-to-end encrypted**; Twingate cannot decrypt or inspect contents
- Relays **do not store traffic** — data is transient (contact measured in fractions of a second)
- **Peer-to-peer connections** bypass Twingate relays entirely; relays are fallback only
- Conduit exception applies equally to **subcontractors of business associates** per DHHS clarification

## Prerequisites
- N/A (informational/legal page)

## BAA Process (If Required)
1. Contact your Twingate account manager
2. Twingate will review customer-provided BAA (not their own form)
3. Must meet requirements:
   - BAA scope limited to extent HIPAA **actually applies** to Twingate services
   - Liability tied to limitation of liability in main services agreement
4. BAA review only available for **annual plans above $75,000**

## Configuration Values
- None applicable

## Gotchas
- Twingate **will not proactively sign BAAs** — doing so implies business associate status they consider inaccurate
- BAA review is **customer-form only**; Twingate does not provide their own BAA template
- Review is **not available for contracts under $75,000/year**
- Having a BAA in place may create incorrect compliance expectations about HIPAA applicability

## Related Docs
- [Twingate Security](https://www.twingate.com/docs/security) — security measures overview
- DHHS Omnibus Rule commentary (conduit exception)
- Contact: Account manager for BAA/HIPAA questions