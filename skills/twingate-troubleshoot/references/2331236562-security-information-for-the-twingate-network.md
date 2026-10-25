---
source: https://help.twingate.com/articles/2331236562-security-information-for-the-twingate-network
type: help
fetched: 2026-10-25
source_version: 0d37c95a358aee6b3844382362c3ae818bf76d51cb96d7b081341e3355e565ff
trust: official
---

# Twingate Security Posture & Practices

## Page Title
Security Information for the Twingate Network

## Summary
Documents Twingate's encryption configuration for compliance and regulatory audit purposes. Covers supported TLS versions and cipher suites. Directs users to the Trust Center for broader security posture documentation.

## Key Information

- Twingate maintains a **Trust Center** covering: People Security, Data Protection & Access Control, Vendor Management, Infrastructure Security, Product Security, and Product Architecture
- Supports **TLS 1.2 and TLS 1.3**
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

All cipher suites use **ECDHE** (forward secrecy) with either **ECDSA** or **RSA** authentication.

## Gotchas

- Cipher list is **not static** — verify current list before including in compliance documentation, as it tracks NIST guidelines
- This page does not cover full security architecture detail; that lives in the Trust Center

## Escalation Path

For security questions not covered here or in the Trust Center, contact your **Twingate Customer Success Manager**.

## Related Docs

- [Twingate Trust Center](https://www.twingate.com/trust) — authoritative source for full security posture
- Twingate Help Center (general)