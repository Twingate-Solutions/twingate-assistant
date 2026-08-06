---
source: https://help.twingate.com/articles/2331236562-security-information-for-the-twingate-network
type: help
fetched: 2026-08-06
source_version: 27e1b462018615df84593d7dcc96c057356edd74037542ac052848bbd507c84e
---

# Security Information for the Twingate Network

## Summary
Documents encryption standards used across the Twingate network for compliance and regulatory audit purposes. Covers supported TLS versions and cipher suites. Directs to the Security Center for broader security posture documentation.

## Key Information
- Supports **TLS 1.2 and TLS 1.3**
- Cipher list may change in line with NIST Guidelines
- Full security posture details (People Security, Data Protection, Infrastructure Security, Product Architecture, etc.) available at the [Twingate Security Center](https://www.twingate.com/security)

## Supported Cipher Suites

| Cipher | Key Exchange | Auth | Encryption | MAC |
|--------|-------------|------|------------|-----|
| `TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256` | ECDHE | ECDSA | ChaCha20-Poly1305 | SHA256 |
| `TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256` | ECDHE | RSA | ChaCha20-Poly1305 | SHA256 |
| `TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256` | ECDHE | ECDSA | AES-128-GCM | SHA256 |
| `TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256` | ECDHE | RSA | AES-128-GCM | SHA256 |
| `TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384` | ECDHE | ECDSA | AES-256-GCM | SHA384 |
| `TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384` | ECDHE | RSA | AES-256-GCM | SHA384 |

## Gotchas
- Cipher list is **not static** — subject to change per NIST guideline updates; re-verify before submitting compliance documentation
- This article covers network encryption only; other security domains (vendor management, access control, etc.) are documented separately in the Security Center

## Related Docs
- [Twingate Security Center](https://www.twingate.com/security) — comprehensive security posture documentation
- Contact Twingate Customer Success Manager for security questions not covered here