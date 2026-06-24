# Twingate & Customer Data

## Page Title
Twingate & Customer Data

## Summary
Documents what customer data Twingate collects across its three products (Private Access, Identity Firewall, DNS Filtering). Intended for privacy, legal, and security professionals. Explains data categories, storage locations, and usage policies.

## Key Information

### Three Data Categories (All Products)
| Category | Stored? | Twingate Can Read? |
|----------|---------|-------------------|
| **Services Data** | Yes – US-based Controller infrastructure | Yes |
| **Content Data** | No | No (end-to-end encrypted) |
| **Usage Data** | Yes – same as Services Data | Yes |

### Services Data
- Includes: usernames, email addresses, groups, resource definitions, network names, security policies, network logs, access tokens
- **Excludes**: user passwords (handled by IdPs: Okta, OneLogin, social logins)
- Storage: Twingate Controller infrastructure, US servers (Google Cloud), mirrored for resiliency

### Content Data
- Actual payload traffic between Clients and Resources
- End-to-end encrypted; Relays route but cannot decrypt
- **Never stored** by Twingate

### Usage Data
- Crash reports, UI interactions, bandwidth stats, telemetry
- May be published in anonymized/aggregated form

## Product-Specific Notes

### Identity Firewall
- Requires Private Access subscription
- Session recording logs = Content Data
- **Gateways deployed in customer infrastructure** – Twingate has no access to session recordings
- Twingate cannot decrypt application sessions

### DNS Filtering
- Logs: domain names accessed, timestamp, user identity, device details
- Only collected from users running Twingate Client who aren't excluded by admin
- Storage: US-based infrastructure (Google Cloud)
- Used only to provide/maintain/support/improve service

## Infrastructure & Data Residency
- **Storage location**: United States
- **Twingate components** (cloud-operated): Controllers, Relays, Admin Console
- **Customer-operated components**: Clients, Resources, Connectors, Identity Firewall Gateways
- Subsidiary in Israel (development focus)
- Third-party vendors subject to contractual data handling requirements

## Gotchas
- Relays may relay encrypted traffic when peer-to-peer connection fails, but still cannot decrypt it
- Session recording is captured by customer-deployed Gateways, not Twingate – admins control this data entirely
- DNS Filtering data collection requires Twingate Client to be running; excluded users are not logged
- Usage data may be published publicly if anonymized – no opt-out mechanism described

## Related Docs
- [Network Logs](https://www.twingate.com/docs/) (referenced inline)
- [Relays documentation](https://www.twingate.com/docs/)
- [DNS Filtering](https://www.twingate.com/docs/dns-filtering)
- [Vendor list](https://www.twingate.com/docs/)
- Certain technical conditions for relay fallback (referenced inline)