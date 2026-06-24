# Twingate FIPS 140 Compliance

## Summary
Twingate is not FIPS 140 validated and cannot exclusively use FIPS 140-validated cryptographic modules. However, Twingate's transport-layer encapsulation does not decrypt underlying payloads, so existing FIPS-compliant end-to-end communications between endpoints remain unaffected by Twingate's presence.

## Key Information

- **Not FIPS 140 validated**: Twingate itself has no FIPS 140-2 or 140-3 validation
- **Transport-layer encapsulation**: Twingate wraps communications at the transport layer using non-FIPS-validated crypto modules
- **Cannot decrypt payloads**: Twingate never decrypts the underlying encrypted data (e.g., TLS payloads), preserving end-to-end FIPS compliance
- **Compatible, not compliant**: If endpoint-to-endpoint communication uses FIPS-validated crypto (e.g., FIPS-validated OpenSSL), adding Twingate does not break that FIPS status
- **Why no FIPS validation**: FIPS validation process is slow; newer crypto module versions with security/bug fixes may not yet be validated but are not necessarily less secure

## FedRAMP Considerations

- FedRAMP-authorized CSPs do **not** automatically require vendors to be FedRAMP authorized or use exclusively FIPS 140-validated modules
- CSPs must independently evaluate how Twingate integrates with their FedRAMP-authorized cloud service
- Twingate will provide architecture/service details to assist FedRAMP CSPs with their evaluation — contact Twingate directly

## Gotchas

- Twingate cannot be used to satisfy a FIPS 140 validation requirement for the network layer itself
- FIPS compliance of end-to-end traffic depends entirely on the **endpoints** using FIPS-validated modules, not Twingate
- FedRAMP authorization is not automatically inherited or implied by using Twingate
- References to "FIPS 140" in Twingate docs cover both FIPS 140-2 and FIPS 140-3

## Related Docs

- [FIPS 140-validated OpenSSL library](https://www.openssl.org/docs/fips.html) (external reference)
- Twingate FedRAMP/compliance contact for CSP-specific guidance