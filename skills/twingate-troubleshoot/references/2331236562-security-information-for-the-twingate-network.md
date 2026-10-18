---
source: https://help.twingate.com/articles/2331236562-security-information-for-the-twingate-network
type: help
fetched: 2026-10-18
source_version: e69958bae03ec5186e31d6befff525521295cf546f72e57e499b78c9c906ead0
trust: official
---

# Twingate Security Posture & Practices

## Page Title
Security Information for the Twingate Network

## Summary
Documents Twingate's encryption configuration for compliance and regulatory audit purposes. Covers supported TLS versions and cipher suites in use on the Twingate network. Directs users to the Trust Center for broader security posture details.

## Key Information
- Primary security documentation lives at the **Twingate Trust Center** (covers People Security, Data Protection & Access Control, Vendor Management, Infrastructure Security, Product Security, Product Architecture)
- Supported TLS versions: **TLS 1.2 and TLS 1.3**
- Cipher list may change in line with **NIST Guidelines**

## Supported Cipher Suites
| Cipher |
|--------|
| `TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256` |
| `TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256` |
| `TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256` |
| `TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256` |
| `TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384` |
| `TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384` |

All suites use **ECDHE** key exchange (forward secrecy). Algorithms include ChaCha20-Poly1305 and AES-GCM (128/256-bit).

## Gotchas
- Cipher list is **not static** — it evolves with NIST guidance; verify current list before embedding in compliance documentation
- This page covers **network-layer encryption only**; broader security controls (access control, vendor management, etc.) are in the Trust Center, not here

## Prerequisites / Contacts
- For questions not covered here or in the Trust Center: contact your **Twingate Customer Success Manager**

## Related Docs
- [Twingate Trust Center](https://www.twingate.com/trust) — authoritative source for full security posture
- NIST TLS Guidelines (external reference for cipher validity)