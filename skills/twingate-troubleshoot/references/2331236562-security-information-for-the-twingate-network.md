---
source: https://help.twingate.com/articles/2331236562-security-information-for-the-twingate-network
type: help
fetched: 2026-09-06
source_version: 19b3631bc511f0639d297702283966eb518c15bb20ff190d4df6f59d0e883ca2
---

# Security Information for the Twingate Network

## Summary
Documents the encryption protocols and cipher suites used across the Twingate network for compliance and regulatory audit purposes. Supports TLS 1.2 and 1.3 with six ECDHE-based cipher suites. Cipher list may change over time in alignment with NIST Guidelines.

## Key Information
- Supported TLS versions: **TLS 1.2** and **TLS 1.3**
- All supported ciphers use ECDHE (Elliptic-curve Diffie-Hellman Ephemeral) key exchange
- Two signature algorithm variants per cipher: ECDSA and RSA
- Three encryption schemes supported: ChaCha20-Poly1305, AES-128-GCM, AES-256-GCM

## Supported Cipher Suites

| Cipher | Key Exchange | Auth | Encryption | Hash |
|--------|-------------|------|------------|------|
| TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256 | ECDHE | ECDSA | ChaCha20-Poly1305 | SHA256 |
| TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256 | ECDHE | RSA | ChaCha20-Poly1305 | SHA256 |
| TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256 | ECDHE | ECDSA | AES-128-GCM | SHA256 |
| TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 | ECDHE | RSA | AES-128-GCM | SHA256 |
| TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384 | ECDHE | ECDSA | AES-256-GCM | SHA384 |
| TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 | ECDHE | RSA | AES-256-GCM | SHA384 |

## Gotchas
- Cipher list is **not static** — will change in line with NIST Guideline updates; verify current list before submitting compliance documentation
- This page covers network-level encryption only; broader security topics (data protection, access control, infrastructure security) are in the Security Center

## Additional Resources
- [Twingate Security Center](https://www.twingate.com/security) — covers People Security, Data Protection & Access Control, Vendor Management, Infrastructure Security, Product Security, Product Architecture
- Contact your **Twingate Customer Success Manager** for security questions not covered here