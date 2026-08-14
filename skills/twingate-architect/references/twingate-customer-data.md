---
source: https://www.twingate.com/docs/twingate-customer-data
type: docs
fetched: 2026-08-14
source_version: 77eb1cca02a86bc49bf49c1aacbfb6a6a714ac71beb24ff8318780fb41c15179
---

# Twingate & Customer Data

## Page Title
Twingate & Customer Data

## Summary
Documents what customer data Twingate collects across its three products (Private Access, Identity Firewall, DNS Filtering). Intended for privacy, legal, and security professionals. Twingate does not inspect or store content data due to end-to-end encryption.

## Key Information

### Three Data Categories (All Products)

| Category | Stored? | Examples |
|----------|---------|---------|
| **Services Data** | Yes – US servers (GCP) | User names/emails, groups, resource definitions, network logs, access tokens, security policies |
| **Content Data** | No | Encrypted payloads between Clients and Resources |
| **Usage Data** | Yes – same as Services | Crash reports, UI interactions, bandwidth stats, telemetry |

### Per-Product Data Handling

**Private Access**
- Control plane: authentication/authorization coordination → Services Data
- Data plane: end-to-end encrypted traffic via Relays → Content Data (not stored, not inspectable)
- Passwords never stored; auth delegated to IdPs (Okta, OneLogin, social)

**Identity Firewall**
- Same three categories as Private Access
- Session recording logs = Content Data
- Gateways deployed in **customer-controlled infrastructure** → Twingate has zero access to session logs
- Twingate cannot decrypt application sessions

**DNS Filtering**
- Logs: domain names accessed, timestamp, user identity, device details
- Only collected from users running Twingate Client who aren't excluded by admin
- Stored on Twingate US infrastructure (GCP)
- Used only for service operation/improvement

## Storage Location
- All Services and Usage Data: United States (Google Cloud, multi-region for resiliency)
- Content Data: Not stored anywhere

## Gotchas
- Relays assist routing under certain conditions but **cannot read** encrypted content even in relay mode
- DNS Filtering data collection requires Client to be running; excluded users are not logged
- Session recording in Identity Firewall is entirely within customer infrastructure — Twingate has no visibility
- Usage data may be **published in anonymized/aggregated form** without customer consent
- Twingate has a subsidiary in Israel (development focus) and uses third-party vendors — customer data may be handled by contractors in various locations

## Workforce & Vendors
- HQ: United States
- Subsidiary: Israel (development)
- Third-party vendors used; contractual data handling requirements imposed

## Related Docs
- [Network Logs](https://www.twingate.com/docs/network-logs)
- [Relays](https://www.twingate.com/docs/relays)
- [DNS Filtering](https://www.twingate.com/docs/dns-filtering)
- [Vendors list](https://www.twingate.com/docs/vendors)
- Peer-to-peer connection conditions documentation