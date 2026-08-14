---
source: https://www.twingate.com/docs/twingate-fips140
type: docs
fetched: 2026-08-14
source_version: e94ddfd712afc7afd714a7b2eeca90a4f0373757eefb54b94b4107f751acb963
---

# Twingate & FIPS 140 Compliance

## Summary
Twingate is not FIPS 140 validated and cannot exclusively use FIPS 140-validated cryptographic modules. However, Twingate's presence does not compromise end-to-end FIPS-compliant communications between endpoints, as it cannot decrypt underlying encrypted payloads.

## Key Information
- **Not FIPS 140 validated** — Twingate holds no FIPS 140-2 or 140-3 validation
- **Cannot exclusively use** FIPS 140-validated cryptographic modules
- Twingate operates at the **transport layer encapsulation** level — it routes/authorizes connections but does not decrypt application payloads
- If two endpoints communicate via FIPS-compliant encryption (e.g., TLS using FIPS 140-validated OpenSSL), adding Twingate **does not break** that compliance status
- Twingate's own encapsulation layer uses non-FIPS-validated crypto modules
- Non-validated modules may actually incorporate more recent security fixes than validated ones (validation process is slow)

## FIPS 140 Compatibility Model
```
[Client App (FIPS TLS)] --> [Twingate (non-FIPS transport encapsulation)] --> [Resource (FIPS TLS)]
                          ↑
              Cannot see/decrypt TLS payload
              End-to-end FIPS status preserved
```

## FedRAMP Considerations
- FedRAMP-authorized CSPs are **not required** to use only FedRAMP-authorized vendors
- FedRAMP-authorized CSPs are **not required** to use only vendors with exclusively FIPS 140-validated modules
- CSPs must evaluate their own specific FedRAMP requirements and determine what obligations, if any, pass through to Twingate
- Twingate will provide architecture/service details to assist FedRAMP CSPs in their evaluation

## Gotchas
- "FIPS 140 compliant" and "FIPS 140 validated" are distinct — Twingate is neither, but is **compatible** with compliant deployments
- References to "FIPS 140" in this doc cover both FIPS 140-2 and 140-3
- FIPS compatibility claim only holds if **both endpoints** use FIPS-validated crypto independently of Twingate
- Twingate does not self-certify as FedRAMP authorized

## Prerequisites
- None — informational/compliance guidance only

## Configuration Values
- None — no configuration flags or environment variables relevant to FIPS mode

## Related Docs
- [FIPS 140-validated OpenSSL library](https://www.openssl.org/docs/fips.html) (external reference)
- Twingate FedRAMP contact: reach out to Twingate directly for architecture details