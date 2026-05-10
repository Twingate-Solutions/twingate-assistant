# Twingate & Customer Data

## Page Title
Twingate & Customer Data

## Summary
Documents what customer data Twingate collects across its three products (Private Access, Identity Firewall, DNS Filtering) and how that data is stored and used. Intended for privacy, legal, and security professionals conducting due diligence. Twingate does not store or inspect encrypted content data traversing its network.

## Key Information

### Three Data Categories (All Products)
- **Services Data**: Control plane data — user details (names/emails), groups, resource definitions, network logs, security policies, access tokens. Stored on Twingate Controller infrastructure (US-based, Google Cloud). Passwords are NOT stored (handled by IdPs).
- **Content Data**: Data plane payloads between Clients and Resources. End-to-end encrypted. **Not stored by Twingate.** Relays route but cannot decrypt traffic.
- **Usage Data**: Diagnostic/statistical data — crash reports, UI interactions, bandwidth, telemetry. Stored same as services data. May be published in anonymized/aggregated form.

### Product-Specific Notes

**Private Access**
- Twingate inspects no payload content; functions like a sealed-mail postal service
- Relays used only when peer-to-peer connection cannot be established

**Identity Firewall (formerly Privileged Access)**
- Requires Private Access subscription
- Session recording logs = content data; captured by Gateway deployed in **customer-controlled infrastructure**
- Twingate has **no access** to session recording logs
- Cannot decrypt session contents due to end-to-end encryption

**DNS Filtering**
- Collects: domain names accessed, timestamp, user identity, device details
- Only applies to users running Twingate Client who aren't excluded by admin
- Storage: US-based infrastructure (Google Cloud)
- Use: service provision, support, improvement only

## Infrastructure & Storage

| Data Type | Stored? | Location |
|-----------|---------|----------|
| Services Data | Yes | US (Google Cloud, multi-region) |
| Content Data | No | N/A (in-transit only) |
| Usage Data | Yes | US (same as services) |
| DNS Logs | Yes | US (Google Cloud) |
| Session Recordings | Customer-controlled | Customer infrastructure |

## Gotchas
- Twingate does **not** store user passwords — authentication delegated to IdPs (Okta, OneLogin, social logins)
- Session recording logs are stored **only** in customer infrastructure; Twingate cannot access them
- Usage data may be published externally if anonymized/de-identified — no opt-out mentioned
- Twingate has a subsidiary in Israel (development focus); vendor/contractor network spans multiple locations with contractual data obligations

## Prerequisites
- Identity Firewall requires an active Private Access subscription
- DNS Filtering requires Twingate Client installed and user not excluded by admin policy

## Related Docs
- [Network Logs](https://www.twingate.com/docs/network-logs)
- [Twingate Relays](https://www.twingate.com/docs/relays)
- [Relay peer-to-peer conditions](https://www.twingate.com/docs/relays)
- [DNS Filtering](https://www.twingate.com/docs/dns-filtering)
- [Vendors list](https://www.twingate.com/docs/vendors)