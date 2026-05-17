# Twingate Customer Data Handling

## Page Title
Twingate & Customer Data

## Summary
Documents what customer data Twingate collects across its three products (Private Access, Identity Firewall, DNS Filtering). Intended for privacy, legal, and security professionals. Twingate acts as a routing layer—it does not inspect or store connection payload data.

## Key Information

**Three Data Categories (all products):**
- **Services Data**: Control plane data—user details (names, emails), groups, resource definitions, network logs, access tokens, security policies. Stored on Twingate Controller infrastructure (US, Google Cloud). No passwords stored.
- **Content Data**: Actual payload data between Client and Resource. End-to-end encrypted; Twingate cannot decrypt or read it. **Not stored.**
- **Usage Data**: Telemetry, crash reports, bandwidth stats, UI interactions. Stored same as Services Data. May be published in anonymized/aggregated form.

**Product-Specific Notes:**
- **Identity Firewall**: Session recording logs (captured by customer-deployed Gateways) are Content Data. Twingate has no access to these logs; cannot decrypt sessions.
- **DNS Filtering**: Logs domain names accessed by users, including timestamp, user identity, and device details. Only applies to users running Twingate Client and not excluded by admin.

## Storage Locations
- Services Data, Usage Data, DNS Filtering logs: US-based servers (Google Cloud and others)
- Content Data: Not stored anywhere by Twingate
- Session recordings: Customer-controlled infrastructure only

## Architecture Components
| Operated by Twingate | Operated by Customer |
|---|---|
| Controllers, Relays, Admin Console | Clients, Resources, Connectors, Gateways |

## Gotchas
- Relays may route encrypted traffic when peer-to-peer connection cannot be established, but still cannot see content (end-to-end encrypted)
- Twingate does **not** store user passwords—authentication delegated to IdPs (Okta, OneLogin, social logins)
- Identity Firewall requires a Private Access subscription
- DNS Filtering only logs users running the Twingate Client and not admin-excluded
- Twingate has a subsidiary in Israel (development); uses third-party vendors globally with contractual data obligations

## Related Docs
- [Network Logs](https://www.twingate.com/docs/network-logs)
- [Relays](https://www.twingate.com/docs/relays)
- [DNS Filtering](https://www.twingate.com/docs/dns-filtering)
- [Vendors list](https://www.twingate.com/docs/vendors)
- Certain technical conditions for relay usage (peer-to-peer fallback)