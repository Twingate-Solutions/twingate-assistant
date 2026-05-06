# Twingate & FIPS 140 Compliance

## Summary
Twingate is not FIPS 140 validated and cannot exclusively use FIPS 140-validated cryptographic modules. However, Twingate's transport-layer encapsulation does not decrypt underlying payloads, preserving the FIPS compliance status of end-to-end communications that use FIPS-validated cryptography.

## Key Information
- Twingate is **not FIPS 140-2 or 140-3 validated**
- Twingate **cannot exclusively use** FIPS 140-validated cryptographic modules
- Twingate operates at the **transport layer** — it encapsulates but does **not decrypt** application payloads
- If two endpoints communicate using FIPS-validated cryptography (e.g., TLS via FIPS-validated OpenSSL), adding Twingate does **not break** that FIPS compliance
- Twingate is considered **compatible** with FIPS 140-compliant communications, not disruptive to them

## Why Twingate Doesn't Use FIPS-Validated Modules
- FIPS validation process is lengthy; newer cryptographic module versions with security/bug fixes may not yet be validated
- More recent (unvalidated) modules may actually be more secure than older validated versions

## FedRAMP Considerations
- FedRAMP-authorized CSPs do **not necessarily** require vendors to be FedRAMP authorized or exclusively use FIPS 140-validated modules
- CSPs must independently evaluate how Twingate integrates with their FedRAMP-authorized service
- Twingate will provide detailed technical information to help FedRAMP CSPs assess requirements on request

## Gotchas
- "Compatible with FIPS 140" ≠ "FIPS 140 validated" — Twingate makes no validation claim
- The FIPS compatibility argument depends on the **underlying application** using FIPS-validated crypto; Twingate itself does not provide that
- FedRAMP CSPs cannot assume Twingate satisfies their FIPS obligations without their own assessment

## Configuration Values
None — no specific configuration flags or parameters for FIPS mode; Twingate does not offer a FIPS-mode toggle.

## Related Docs
- [FIPS 140-validated OpenSSL library](https://www.openssl.org/) (external reference)
- Twingate FedRAMP/compliance contacts for detailed architecture review