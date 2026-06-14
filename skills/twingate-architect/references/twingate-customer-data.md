# Twingate & Customer Data

## Summary
Documents what customer data Twingate collects across its Private Access, Identity Firewall, and DNS Filtering products. Intended for privacy, legal, and security professionals. Covers data categories, storage locations, and usage policies.

## Key Information

### Three Data Categories (All Products)
- **Services Data**: Control plane data — user details (names, emails), groups, resource definitions, network logs, security policies, access tokens. Stored on Twingate-controlled infrastructure in the US (Google Cloud). Passwords are NOT stored (handled by IdPs like Okta, OneLogin).
- **Content Data**: Data plane payloads between Clients and Resources. End-to-end encrypted; Twingate cannot decrypt. **Not stored by Twingate.** Relays route but cannot read content.
- **Usage Data**: Telemetry, crash reports, bandwidth stats, UI interactions. Stored same locations as Services Data. May be published in anonymized/aggregated form.

### Product-Specific Notes

**Private Access**
- Client installed on end-user devices; Connectors and Relays broker connections
- Relays store no traffic or network-identifiable information

**Identity Firewall (formerly Privileged Access)**
- Requires Private Access subscription
- Session recording logs captured by **customer-deployed Gateways** in customer infrastructure — Twingate has **no access** to these logs
- Twingate cannot decrypt session contents due to E2E encryption

**DNS Filtering**
- Logs: domain names accessed, timestamp, user identity, device details
- Only collected from users running Twingate Client and not excluded by admin
- Stored on Twingate US infrastructure

## Storage Locations
- **US-based servers** (including Google Cloud vendors)
- Data mirrored in multiple locations for resiliency
- Twingate HQ: United States; subsidiary in Israel (development focus)

## Gotchas
- Content data is E2E encrypted — Twingate **cannot** access payload contents even if traffic passes through a Relay
- Session recording in Identity Firewall is entirely within customer-controlled infrastructure; Twingate has zero visibility
- DNS Filtering data collection only applies to users with the Client installed and not excluded by admin policy
- Usage data may be published publicly if anonymized — no customer-identifiable info included

## Configuration Values
- No CLI flags or API parameters defined in this document
- DNS Filtering and session recording must be explicitly enabled by an administrator

## Related Docs
- [Network Logs](https://www.twingate.com/docs) (referenced for Services Data)
- [Relays](https://www.twingate.com/docs) (technical conditions for relay usage)
- [DNS Filtering](https://www.twingate.com/docs/dns-filtering)
- [Twingate Vendors](https://www.twingate.com/docs) (third-party vendor list)