---
source: https://help.twingate.com/articles/2331236562-security-information-for-the-twingate-network
type: help
fetched: 2026-11-01
source_version: 3d89e103abf66f9fa568f54c1d54edd9ddc725830a5584731dddb48a86d65bdf
trust: official
---

# Security Posture & Practices – Twingate Network

## Page Title
Security Information for the Twingate Network

## Summary
Twingate documents its security posture and encryption configuration for customers undergoing regulatory audits. The page specifies supported TLS versions and cipher suites used on the Twingate network. Full security details (people security, data protection, vendor management, infrastructure/product security) are available via Twingate's Trust Center.

## Key Information

- **TLS Versions Supported:** TLS 1.2 and TLS 1.3
- **Supported Cipher Suites:**
  - `TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256`
  - `TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256`
  - `TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`
  - `TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`
  - `TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`
  - `TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`
- All ciphers use **ECDHE** for forward secrecy
- Cipher list subject to change in line with **NIST Guidelines**

## Prerequisites
- None for reference purposes
- Contact your **Twingate Customer Success Manager** for questions not covered here or in the Trust Center

## Configuration Values
No user-configurable parameters. These ciphers are enforced at the Twingate network level and are not selectable by end users or administrators.

## Gotchas
- The cipher/TLS list **will change over time** as NIST guidelines evolve; verify current values with Twingate support for time-sensitive compliance audits
- This page covers network-level encryption only; broader security topics (access control, vendor management, infrastructure) require visiting the Trust Center separately

## Related Docs
- [Twingate Trust Center](https://www.twingate.com/trust) – covers People Security, Data Protection & Access Control, Vendor Management, Infrastructure Security, Product Security, Product Architecture
- Contact your Twingate Customer Success Manager for audit-specific questions