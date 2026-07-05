# Twingate & Customer Data

## Page Title
Twingate & Customer Data

## Summary
Documents the three categories of customer data Twingate processes across its Private Access, Identity Firewall, and DNS Filtering products. Clarifies what Twingate stores, where it's stored, and how it's used. Intended for privacy, legal, and security professionals.

## Key Information

### Three Data Categories

| Category | Stored? | Twingate Access? |
|---|---|---|
| **Services Data** | Yes – US-based Controller infrastructure | Yes |
| **Content Data** | No | No (end-to-end encrypted) |
| **Usage Data** | Yes – same as Services Data | Yes |

- **Services Data**: User names/emails, groups, resource definitions, network names, security policies, network logs, access tokens. No passwords stored (delegated to IdPs like Okta/OneLogin).
- **Content Data**: Actual payload data between Clients and Resources. End-to-end encrypted; Relays route but cannot read it. Never stored by Twingate.
- **Usage Data**: Crash reports, UI interactions, bandwidth stats, telemetry. May be published in anonymized/aggregated form.

### Infrastructure
- Services/Usage data stored on US servers (Google Cloud and others)
- Data mirrored across multiple locations for resiliency

### Product-Specific Notes

**Private Access**: Connectors, Clients, and Resources are customer-operated. Controllers, Relays, and Admin Console are Twingate-operated.

**Identity Firewall**:
- Requires Private Access subscription
- Session recording logs (content data) are captured by **Gateways**, which are **customer-deployed and customer-controlled**
- Twingate has **zero access** to session recording logs
- End-to-end encryption prevents Twingate from decrypting session contents

**DNS Filtering**:
- Logs domain names accessed, timestamps, user identity, device details
- Only applies to users running the Twingate Client who aren't excluded by admin
- Data stored on Twingate US infrastructure
- Used only to provide/maintain/support/improve the service

## Prerequisites
- Identity Firewall requires an active Private Access subscription
- DNS Filtering and session recording require Twingate Client installed on user devices

## Gotchas
- **Relays do not store traffic or network-identifiable information** — peer-to-peer connections fall back to Relay routing only under specific technical conditions
- **Session recording is entirely within customer infrastructure** — Twingate cannot access these logs even for support
- DNS Filtering only logs domains for users **not excluded** by admin policy; admins control scope
- Usage data may be published publicly in anonymized form — no opt-out mechanism mentioned

## Related Docs
- [Network Logs](https://www.twingate.com/docs/network-logs)
- [Relays](https://www.twingate.com/docs/relays)
- [DNS Filtering](https://www.twingate.com/docs/dns-filtering)
- [Vendors list](https://www.twingate.com/docs/vendors)
- Peer-to-peer connection conditions (linked inline in source)