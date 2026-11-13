---
source: https://help.twingate.com/articles/2331236562-security-information-for-the-twingate-network
type: help
fetched: 2026-11-13
source_version: d08820c349b61b02948e0be87dafc38f84e259e85a09e70500b8a9a34821032d
trust: official
---

# Page Title
Security Posture & Practices (Security Information for the Twingate Network)

## Summary
This page points to Twingate's Trust Center for security details and lists the TLS versions and cipher suites currently supported on the Twingate network. The list is provided mainly to answer questions from customer regulatory audits. It may change over time in line with NIST guidelines.

## Key Information
- Trust Center covers: People Security, Data Protection & Access Control, Vendor Management, Infrastructure Security, Product Security, and Product Architecture.
- Supported TLS versions: 1.2 and 1.3.
- Supported ciphers (as of the current revision):
  - `TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256`
  - `TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256`
  - `TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`
  - `TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`
  - `TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`
  - `TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`
- All listed suites use ECDHE key exchange (forward secrecy) with AEAD modes (AES-GCM or ChaCha20-Poly1305).
- Last updated: about 1 month before the scrape.

## Prerequisites
None. This is a reference page.

## Step-by-Step
Not applicable.

## Configuration Values
No env vars, CLI flags, or API parameters. The cipher list above is the only configuration-relevant data; it describes what Twingate supports and is not something to configure.

## Gotchas
- The cipher list is not fixed. It can change to follow NIST guidelines, so check the live page before citing it in audit documentation.
- TLS 1.0 and 1.1 are not listed as supported.
- Firewalls, proxies, or TLS inspection devices that restrict ciphers must allow at least one of the suites above, or connections may fail.
- Questions not covered by the Trust Center or this page should go to your Twingate Customer Success Manager.

## Related Docs
- Twingate Trust Center (the page links to it but gives no URL in the scraped text)
- Contact your Customer Success Manager for additional security questions