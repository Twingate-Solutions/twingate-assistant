# Twingate FIPS 140 Compliance

## Summary
Twingate is not FIPS 140-2/140-3 validated and does not exclusively use FIPS-validated cryptographic modules. However, Twingate's transport-layer encapsulation does not decrypt underlying payloads, so existing FIPS-compliant end-to-end communications remain unaffected when routed through Twingate.

## Key Information
- Twingate applies to both FIPS 140-2 and FIPS 140-3 equally
- Twingate acts as an authorization/routing layer only — it cannot decrypt application-layer payloads (e.g., TLS traffic)
- If device-to-resource communication uses FIPS-validated crypto (e.g., FIPS-validated OpenSSL), adding Twingate does not break FIPS compliance of that communication
- Twingate's own transport encapsulation uses non-FIPS-validated modules
- Non-validated does not mean less secure — newer modules may include security fixes not yet through the lengthy validation process

## Prerequisites
- Customers must already have FIPS-compliant endpoints and applications if FIPS compliance is required
- FIPS compliance of the end-to-end communication must be established independently of Twingate

## FIPS Compatibility Model
| Layer | FIPS Status |
|---|---|
| Customer app ↔ resource (e.g., TLS) | Can be FIPS-validated (unaffected by Twingate) |
| Twingate transport encapsulation | Not FIPS-validated |
| Twingate payload access | None — Twingate cannot decrypt payloads |

## FedRAMP Considerations
- FedRAMP-authorized CSPs **do not** require all vendors to be FedRAMP authorized or exclusively use FIPS-validated modules
- CSPs must evaluate how Twingate is used within their FedRAMP-authorized service to determine applicable requirements
- Twingate can provide architecture details to assist FedRAMP CSPs in their evaluation

## Gotchas
- Twingate is **not** FIPS 140 validated — do not represent it as such in compliance documentation
- Twingate cannot be configured to exclusively use FIPS-validated cryptographic modules (no opt-in FIPS mode)
- FIPS compatibility claim is conditional: only applies if the underlying communication is already FIPS-compliant without Twingate in the path
- FedRAMP CSPs must independently determine what obligations, if any, flow down to Twingate for their specific use case

## Related Docs
- [FIPS 140-validated OpenSSL library](https://www.openssl.org/docs/fips.html) (external reference)
- Twingate FedRAMP contact: reach out to Twingate directly for architecture documentation to support FedRAMP assessments