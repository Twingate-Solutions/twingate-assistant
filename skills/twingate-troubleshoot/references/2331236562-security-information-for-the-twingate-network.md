---
source: https://help.twingate.com/articles/2331236562-security-information-for-the-twingate-network
type: help
fetched: 2026-10-04
source_version: 8bf0e924f3a27e80067b80f1781d1194622141756d42f5ef3110184b4ea15492
trust: official
---

# Security Information for the Twingate Network

## Summary
Documents Twingate's encryption configuration for compliance and regulatory audit purposes. Covers supported TLS versions and cipher suites used across the Twingate network.

## Key Information

- Twingate supports **TLS 1.2 and TLS 1.3**
- Cipher list may change over time in alignment with NIST Guidelines
- Full security posture details (People Security, Data Protection, Vendor Management, Infrastructure Security, Product Security, Product Architecture) are covered in the [Twingate Security Center](https://www.twingate.com/security)

## Supported Cipher Suites

| Cipher | TLS Version |
|--------|-------------|
| `TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256` | 1.2/1.3 |
| `TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256` | 1.2/1.3 |
| `TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256` | 1.2/1.3 |
| `TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256` | 1.2/1.3 |
| `TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384` | 1.2/1.3 |
| `TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384` | 1.2/1.3 |

All cipher suites use **ECDHE** (Ephemeral Elliptic Curve Diffie-Hellman) for key exchange, providing forward secrecy.

## Gotchas

- This cipher list is **not static** — it evolves with NIST guidelines; verify current state before including in compliance documentation
- For audit use, confirm the list is still current at time of submission by contacting your Customer Success Manager

## Support Escalation

For security questions not covered here or in the Security Center, contact your **Twingate Customer Success Manager**.

## Related Docs

- [Twingate Security Center](https://www.twingate.com/security)
- Twingate Help: General network and connector configuration articles