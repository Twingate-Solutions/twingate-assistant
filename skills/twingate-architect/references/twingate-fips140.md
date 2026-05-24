# Twingate FIPS 140 Compliance

## Summary
Twingate is not FIPS 140 validated and cannot exclusively use FIPS 140-validated cryptographic modules. However, Twingate's transport-layer encapsulation does not decrypt underlying payloads, so it does not compromise end-to-end FIPS-compliant communications between endpoints.

## Key Information
- **Not FIPS 140 validated** — Twingate holds no FIPS 140-2 or 140-3 validation
- **Cannot guarantee exclusive use** of FIPS-validated crypto modules internally
- **Does not break existing FIPS compliance** — if two endpoints communicate via FIPS-validated crypto (e.g., TLS using FIPS-validated OpenSSL), adding Twingate does not disturb that status
- Twingate operates at the **transport layer** (encapsulation/routing), and **cannot decrypt** the underlying encrypted payloads
- FIPS validation process lag means Twingate may use newer, unvalidated-but-potentially-more-secure crypto module versions
- "FIPS 140" references apply equally to FIPS 140-2 and FIPS 140-3

## FedRAMP Considerations
- FedRAMP-authorized CSPs are **not required** to use only FedRAMP-authorized vendors
- FedRAMP authorization does not automatically require vendors to implement exclusively FIPS 140-validated modules
- CSPs must evaluate their own usage of Twingate to determine what FedRAMP/FIPS requirements apply
- Twingate will provide architecture/service details to assist FedRAMP CSPs in their evaluation (contact Twingate directly)

## Gotchas
- Twingate's transport encapsulation layer itself does **not** use FIPS-validated crypto — only the underlying application-layer communications can be FIPS-compliant
- FIPS compatibility claim is **conditional**: only valid if the endpoint-to-endpoint communication was already FIPS-compliant before Twingate was introduced
- FedRAMP CSPs cannot assume Twingate covers their FIPS obligations — they must perform their own scoping assessment

## Use Case Summary

| Scenario | FIPS Impact |
|----------|-------------|
| FIPS-compliant app-to-resource TLS + Twingate routing | No FIPS impact |
| Relying on Twingate itself for FIPS-validated crypto | Not supported |
| FedRAMP authorization requiring FIPS 140 | Requires independent CSP assessment |

## Related Docs
- [FIPS 140-validated OpenSSL library](https://www.openssl.org/docs/fips.html) (external reference)
- Twingate FedRAMP inquiries: contact Twingate directly for architecture documentation