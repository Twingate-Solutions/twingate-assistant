---
source: https://help.twingate.com/articles/2331236562-security-information-for-the-twingate-network
type: help
fetched: 2026-10-28
source_version: bdbd450174eccc90a884b614993af8476377bdba5e2596b25e68724a652644f9
trust: official
---

# Security Posture & Practices – Twingate Network

## Page Title
Security Information for the Twingate Network

## Summary
Documents Twingate's encryption configuration for compliance and regulatory audit purposes. Covers supported TLS versions and cipher suites in use on the Twingate network. Directs users to the Trust Center for broader security posture documentation.

## Key Information

- **Trust Center** covers: People Security, Data Protection & Access Control, Vendor Management, Infrastructure Security, Product Security, and Product Architecture
- Supported TLS versions: **TLS 1.2** and **TLS 1.3**
- Cipher list may change in alignment with NIST Guidelines

## Supported Cipher Suites

| Cipher | Auth | Key Exchange | Encryption | Hash |
|--------|------|--------------|------------|------|
| `TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256` | ECDSA | ECDHE | ChaCha20-Poly1305 | SHA-256 |
| `TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256` | RSA | ECDHE | ChaCha20-Poly1305 | SHA-256 |
| `TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256` | ECDSA | ECDHE | AES-128-GCM | SHA-256 |
| `TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256` | RSA | ECDHE | AES-128-GCM | SHA-256 |
| `TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384` | ECDSA | ECDHE | AES-256-GCM | SHA-384 |
| `TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384` | RSA | ECDHE | AES-256-GCM | SHA-384 |

## Gotchas

- Cipher list is **not static** — it evolves with NIST guidance; verify current state before submitting to auditors
- This page does not cover full security architecture details; Trust Center is the authoritative source for broader compliance evidence
- For unanswered audit questions, contact your **Twingate Customer Success Manager** directly

## Prerequisites
None — informational reference page only.

## Related Docs
- [Twingate Trust Center](https://trust.twingate.com) — full security posture documentation
- Contact: Twingate Customer Success Manager for gap questions