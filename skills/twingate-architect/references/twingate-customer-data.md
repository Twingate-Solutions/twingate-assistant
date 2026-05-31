# Twingate Customer Data Handling Reference

## Page Title
Twingate & Customer Data

## Summary
Documents what customer data Twingate collects across its Private Access, Identity Firewall, and DNS Filtering products. Intended for privacy, legal, and security professionals. Clarifies data storage locations, retention, and use policies.

## Key Information

### Three Data Categories (All Products)
- **Services Data**: Control plane data — user names/emails, groups, resource definitions, network logs, access tokens, security policies. Stored on Twingate Controller infrastructure (US-based, Google Cloud). Used for service delivery and support. **Passwords not stored** (delegated to IdPs).
- **Content Data**: Data plane payloads between Clients and Resources. **Not stored by Twingate.** End-to-end encrypted; Relays route but cannot decrypt traffic.
- **Usage Data**: Telemetry, crash reports, bandwidth stats, UI interactions. Same storage as services data. May be published in anonymized/aggregated form.

### Per-Product Notes
- **Private Access**: Standard three-category model. Relays facilitate routing but store no traffic.
- **Identity Firewall**: Same three categories. Session recording logs = content data. Gateways deployed in **customer infrastructure** — Twingate has no access to session recordings.
- **DNS Filtering**: Logs domain names accessed, timestamps, user identity, device details. Only collected for users running Twingate Client who aren't admin-excluded. Stored in US infrastructure.

## Storage Locations
- All services and usage data: US servers (Google Cloud and other vendors)
- Content data: Not stored
- DNS Filtering logs: US servers

## Prerequisites
- Identity Firewall requires an active Private Access subscription
- DNS Filtering data collection requires Twingate Client installed and user not excluded by admin

## Gotchas
- Twingate **cannot** decrypt content data even when acting as a Relay — end-to-end encryption prevents this
- Session recording in Identity Firewall is captured by **customer-deployed Gateways**, not Twingate — Twingate has zero access
- DNS Filtering logs are only generated for users **actively running the Client** and not excluded by admin policy
- Peer-to-peer connections may fall back to Relay routing under certain network conditions — encrypted data still passes through but remains unreadable to Twingate
- Usage data may be published publicly if anonymized/de-identified

## Related Docs
- [Network Logs](https://www.twingate.com/docs/) (referenced for services data)
- [Relays documentation](https://www.twingate.com/docs/) (peer-to-peer connection conditions)
- [DNS Filtering](https://www.twingate.com/docs/dns-filtering)
- [Twingate Vendors list](https://www.twingate.com/docs/)