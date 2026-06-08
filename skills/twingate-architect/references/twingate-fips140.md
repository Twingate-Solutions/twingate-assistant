# Twingate & FIPS 140 Compliance

## Summary
Twingate is not FIPS 140 validated and cannot exclusively use FIPS 140-validated cryptographic modules. However, Twingate's transport-layer encapsulation does not decrypt underlying payloads, preserving the FIPS compliance status of end-to-end communications that use FIPS-validated modules.

## Key Information

- **Not FIPS 140 validated**: Twingate does not hold FIPS 140-2 or 140-3 validation
- **Does not break FIPS compliance**: If endpoint-to-endpoint communication uses FIPS-validated crypto (e.g., TLS via FIPS-validated OpenSSL), adding Twingate does not disturb that compliance status
- **Transport encapsulation only**: Twingate wraps communications at the transport layer using non-FIPS-validated modules but cannot decrypt application-layer payloads
- **Compatibility model**: Twingate is considered *compatible* with FIPS 140-compliant communications, not itself compliant
- **Why not validated**: FIPS validation process is slow; newer crypto module versions with security/bug fixes often exist before validation completes

## FedRAMP Considerations

- FedRAMP-authorized CSPs do **not** require all vendors to be FedRAMP authorized or exclusively use FIPS-validated modules
- CSPs must independently evaluate how Twingate fits within their FedRAMP authorization boundary
- Twingate will provide architectural detail to assist FedRAMP CSPs in their evaluation

## Gotchas

- "Compatible with FIPS 140" ≠ "FIPS 140 compliant/validated" — Twingate cannot be listed as a FIPS-validated component
- If your compliance requirement mandates **all** components in the data path use FIPS-validated crypto, Twingate does **not** satisfy that requirement
- The FIPS compatibility argument depends on end-to-end encryption being established at the application layer (e.g., TLS); plaintext application traffic would not have equivalent protection at Twingate's encapsulation layer

## Prerequisites

- End-to-end communications must use FIPS 140-validated cryptographic modules independently of Twingate for the compatibility claim to apply
- FedRAMP CSPs should engage Twingate directly for architecture documentation needed for authorization assessment

## Related Docs

- [FIPS 140-validated OpenSSL library](https://www.openssl.org/docs/fips.html) (external reference)
- Twingate security documentation
- FedRAMP authorization guidance