# Twingate & Customer Data

## Page Title
Twingate & Customer Data

## Summary
Documents what customer data Twingate collects across its three products (Private Access, Identity Firewall, DNS Filtering) and how that data is stored and used. Intended for privacy, legal, and security professionals. Twingate does not store or inspect encrypted content data traversing its network.

## Key Information

### Three Data Categories (All Products)
- **Services Data**: Control plane data — user details (names, emails), groups, resource definitions, network logs, access tokens, security policies. Stored on Twingate Controller infrastructure (US-based, Google Cloud). No passwords stored.
- **Content Data**: Actual payload data between Clients and Resources. End-to-end encrypted; Twingate cannot decrypt or store it. Relays route but do not terminate or log connections.
- **Usage Data**: Diagnostic/statistical data — crash reports, UI interactions, bandwidth, telemetry. Stored same as Services Data. May be published in anonymized/aggregated form.

### Product-Specific Notes

**Private Access**
- Clients, Resources, Connectors = customer-controlled
- Controllers, Relays, Admin Console = Twingate-operated
- Relays used for routing only when P2P connection fails

**Identity Firewall (formerly Privileged Access)**
- Requires Private Access subscription
- Adds session recording via **Gateways** deployed in customer infrastructure
- Twingate has zero access to session recording logs (customer-controlled Gateways)
- Session recordings = Content Data
- End-to-end encryption prevents Twingate from decrypting sessions

**DNS Filtering**
- Logs: domain names accessed, timestamp, user identity, device details
- Only collected from users running Twingate Client (unless excluded by admin)
- Storage: US-based Twingate infrastructure (Google Cloud)
- Use: service provision, support, improvement only

## Storage Locations
- All data stored in United States
- Google Cloud used as infrastructure vendor
- Mirrored across multiple locations for resiliency

## Gotchas
- Twingate does **not** store user passwords — authentication delegated to IdPs (Okta, OneLogin, social logins)
- Content data is **never stored** by Twingate, even when Relays route traffic
- DNS Filtering data collection requires: (1) admin enablement, (2) user running Client, (3) user not excluded from filtering
- Identity Firewall session logs are inaccessible to Twingate because Gateways run in customer infrastructure
- Usage data may be published publicly if anonymized/de-identified

## Workforce & Vendors
- HQ: United States; development subsidiary in Israel
- Third-party vendors and contractors used; contractual data handling requirements imposed
- Vendor list available at [twingate.com/docs/vendors](https://www.twingate.com/docs/vendors) (referenced in source)

## Related Docs
- [Network Logs](https://www.twingate.com/docs/network-logs)
- [Relays](https://www.twingate.com/docs/relays)
- [DNS Filtering](https://www.twingate.com/docs/dns-filtering)
- [Certain Technical Conditions (P2P fallback)](https://www.twingate.com/docs/relays)
- Twingate Vendors list