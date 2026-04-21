## Page Title
Twingate & FIPS 140 Compliance

## Summary
Clarifies Twingate's relationship to FIPS 140-2/140-3 validation. Twingate is not FIPS 140 validated and does not exclusively use FIPS-validated cryptographic modules, but its presence in a connection does not disturb the FIPS compliance status of the underlying end-to-end communication, because Twingate cannot decrypt application-layer payloads.

## Key Information
- **Not FIPS validated**: Twingate itself does not have FIPS 140-2 or 140-3 validation, and does not exclusively use FIPS-validated crypto modules
- **Transparent to FIPS compliance**: If endpoints communicate over a FIPS-compliant channel (e.g., TLS with a FIPS-validated OpenSSL library), adding Twingate as the routing/authorization layer does not break that compliance -- Twingate cannot decrypt the underlying payload
- **Why not FIPS validated**: FIPS validation process is slow; newer, more secure crypto versions may not yet be validated; using non-validated but more current crypto is arguably more secure
- **FedRAMP context**: FedRAMP CSPs do not automatically require all vendors to be FedRAMP authorized or use exclusively FIPS-validated crypto; CSPs must evaluate their specific usage of Twingate in their FedRAMP boundary and determine what requirements, if any, apply to Twingate in that context
- Twingate can provide more details on request for FedRAMP boundary evaluation

## Prerequisites
None.

## Step-by-Step
Not applicable.

## Configuration Values
None -- FIPS mode is not configurable in Twingate.

## Gotchas
- "Compatible with FIPS compliance" is not the same as "FIPS validated" -- Twingate is the former, not the latter
- Organizations with strict FIPS requirements should verify with their compliance team whether Twingate's transport layer encapsulation affects their specific compliance posture

## Related Docs
- `/docs/twingate-security` -- general Twingate security architecture
- `/docs/how-encryption-works-in-twingate` -- encryption details
