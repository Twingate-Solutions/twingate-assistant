# Twingate & FIPS 140 Compliance

## Summary
Twingate is not FIPS 140 validated and does not exclusively use FIPS 140-validated cryptographic modules. However, Twingate's transport-layer encapsulation does not decrypt underlying payloads, preserving the FIPS compliance status of end-to-end encrypted communications between customer devices.

## Key Information
- Applies to both FIPS 140-2 and FIPS 140-3
- Twingate is **not** FIPS 140 validated
- Twingate **cannot** decrypt customer payload data (e.g., underlying TLS traffic)
- If endpoint-to-endpoint communications use FIPS-validated crypto (e.g., FIPS-validated OpenSSL), adding Twingate does not break that compliance
- Twingate wraps communications at the transport layer using non-FIPS-validated modules but does not inspect or decrypt payload content
- Twingate intentionally avoids FIPS-validated modules in some cases because newer (potentially more secure) versions may not yet have completed the lengthy validation process

## FIPS Compatibility Model
| Layer | FIPS Status |
|---|---|
| Customer endpoint-to-endpoint TLS | Can be FIPS 140-validated (unaffected by Twingate) |
| Twingate transport encapsulation | Not FIPS 140-validated |
| Payload decryption by Twingate | Not performed — payload integrity preserved |

## FedRAMP Considerations
- FedRAMP-authorized CSPs do **not** require all vendors to be FedRAMP authorized or use exclusively FIPS-validated modules
- CSPs must evaluate how Twingate integrates with their FedRAMP-authorized service to determine pass-through requirements
- Twingate will provide architecture/service details to assist FedRAMP CSPs in their evaluation

## Gotchas
- Twingate cannot be used as the FIPS-validated cryptographic layer itself — it must sit alongside FIPS-compliant endpoint communications
- "Compatible with FIPS 140" ≠ "FIPS 140 validated" — Twingate makes no claim of validation
- FedRAMP compliance requires individual CSP assessment; Twingate does not provide a blanket FedRAMP authorization benefit

## Prerequisites
- For FIPS compatibility claim to apply: both communicating endpoints must independently use FIPS 140-validated cryptographic modules
- Customer must verify their specific use case qualifies under this model

## Related Docs
- [FIPS 140-validated OpenSSL library](https://www.openssl.org/docs/fips.html) (external reference)
- Twingate FedRAMP evaluation support: contact Twingate directly for architecture documentation