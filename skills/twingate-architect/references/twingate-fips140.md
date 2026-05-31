# Twingate FIPS 140 Compliance

## Summary
Twingate is not FIPS 140 validated and cannot exclusively use FIPS 140-validated cryptographic modules. However, Twingate's transport-layer encapsulation does not decrypt underlying payloads, meaning it does not compromise existing end-to-end FIPS-compliant communications between customer devices.

## Key Information

- **Not FIPS 140 validated** — Twingate holds no FIPS 140-2 or 140-3 certification
- **Compatible, not compliant** — Twingate is considered *compatible* with FIPS 140 communications, not itself compliant
- **No payload decryption** — Twingate encapsulates traffic at the transport layer but cannot decrypt underlying encrypted payloads (e.g., TLS data)
- **Preservation of existing FIPS status** — If endpoint-to-endpoint communication uses FIPS-validated cryptography (e.g., FIPS 140-validated OpenSSL), adding Twingate does not break that compliance posture
- **Why not validated** — FIPS validation process is slow; newer cryptographic module versions with security/bug fixes may be available but not yet validated; Twingate opts for more current (potentially more secure) implementations

## FedRAMP Considerations

- FedRAMP-authorized CSPs **do not automatically require** their vendors to be FedRAMP authorized or exclusively use FIPS 140-validated modules
- CSPs must independently evaluate how Twingate is used within their FedRAMP authorization boundary
- Twingate will provide architectural detail to assist FedRAMP CSPs in their evaluation

## Gotchas

- "FIPS compatible" ≠ "FIPS validated" — Twingate's transport encapsulation layer uses non-validated crypto modules
- FIPS compliance of the *end-to-end* communication depends entirely on the **customer's own application stack**, not Twingate
- If your compliance requirement mandates that **all** cryptographic operations in the data path use FIPS-validated modules (including transport encapsulation), Twingate does not currently satisfy that requirement

## Related Docs

- [FIPS 140-validated OpenSSL library](https://www.openssl.org/docs/fips.html) (external reference)
- Twingate FedRAMP support contact for architectural details