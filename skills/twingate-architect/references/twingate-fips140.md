# Twingate & FIPS 140 Compliance

## Summary
Twingate is not FIPS 140-2/140-3 validated and does not exclusively use FIPS-validated cryptographic modules. However, Twingate's transport-layer encapsulation does not decrypt underlying payloads, preserving the FIPS compliance status of end-to-end encrypted communications that pass through it.

## Key Information
- Twingate is **not FIPS 140 validated** (applies to both 140-2 and 140-3)
- Twingate **cannot decrypt** encapsulated payloads (e.g., underlying TLS traffic)
- If endpoint-to-endpoint communication uses FIPS-validated crypto (e.g., FIPS-validated OpenSSL), adding Twingate **does not break** that compliance status
- Twingate adds its own transport-layer encapsulation using non-FIPS-validated modules, but this wraps—not replaces—existing encrypted communications
- Twingate intentionally avoids locking to FIPS-validated modules because validated versions may lag behind security/bug-fix releases

## FIPS Compatibility Model
| Layer | FIPS Status |
|---|---|
| Customer end-to-end communication (e.g., TLS) | Can be FIPS 140-validated |
| Twingate transport encapsulation | Not FIPS-validated |
| Twingate payload visibility | None (cannot decrypt) |

## FedRAMP Considerations
- FedRAMP-authorized CSPs do **not** automatically require vendors to be FedRAMP authorized or use exclusively FIPS-validated modules
- CSPs must evaluate how Twingate integrates with their specific FedRAMP-authorized service to determine applicable requirements
- Twingate will provide technical details to assist FedRAMP CSPs with their evaluation

## Gotchas
- "FIPS compatible" ≠ "FIPS validated" — Twingate makes no claim of validation
- If your compliance requirement mandates that **all** cryptographic operations (including transport routing/encapsulation) use FIPS-validated modules, Twingate does not satisfy that requirement
- FIPS validation lag: newer, potentially more secure module versions may exist but lack formal validation; Twingate uses these newer versions

## Prerequisites
- None specific; this is a compliance guidance document, not a configuration guide

## Related Docs
- [FIPS 140-validated OpenSSL library](https://www.openssl.org/docs/fips.html) (external reference)
- Twingate FedRAMP evaluation — contact Twingate directly for architectural details