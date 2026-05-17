# Twingate FIPS 140 Compliance

## Summary
Twingate is not FIPS 140 validated and cannot exclusively use FIPS 140-validated cryptographic modules. However, Twingate's transport-layer encapsulation does not decrypt underlying payloads, so existing FIPS-compliant end-to-end communications between devices remain unaffected by Twingate's presence.

## Key Information
- **Not FIPS 140 validated** — Twingate holds no FIPS 140-2 or 140-3 validation
- **Cannot enforce FIPS-only crypto** — no mode to restrict to FIPS-validated modules
- **Transport-layer encapsulation only** — Twingate wraps traffic at the transport layer but cannot decrypt application payloads (e.g., underlying TLS data)
- **FIPS integrity preserved** — if endpoints communicate using FIPS-validated crypto (e.g., FIPS-validated OpenSSL TLS), adding Twingate does not break that compliance status
- **Why no FIPS validation**: FIPS validation process is slow; newer crypto module versions with security/bug fixes may exist before validation completes — Twingate prioritizes using more current (potentially more secure) modules

## FedRAMP Considerations
- FedRAMP-authorized CSPs **do not automatically require** their vendors to be FedRAMP authorized or use exclusively FIPS-validated modules
- FedRAMP CSPs must individually evaluate how Twingate fits within their specific FedRAMP authorization scope
- Twingate will provide architectural details to assist FedRAMP CSPs in their evaluation

## Gotchas
- "FIPS compatible" ≠ "FIPS validated" — Twingate's positioning is compatibility (non-interference), not certification
- Twingate's own encapsulation tunnel uses **non-FIPS-validated crypto** — only the inner application-layer communications retain FIPS status
- Organizations requiring that **every cryptographic operation** in the data path use FIPS-validated modules will find Twingate non-compliant by that strict definition
- FIPS 140-2 and FIPS 140-3 are treated identically in Twingate's documentation/policy

## Related Docs
- [FIPS 140-validated OpenSSL library](https://www.openssl.org/docs/fips.html) (external reference)
- Twingate Security documentation
- Twingate FedRAMP support contact for CSP-specific evaluation