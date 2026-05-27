# Twingate & Customer Data

## Summary
Documents what customer data Twingate collects across its three products (Private Access, Identity Firewall, DNS Filtering) and how that data is stored/used. Intended for privacy, legal, and security review. Twingate does not store or inspect encrypted content data transiting its network.

## Key Information

### Three Data Categories (All Products)
| Category | Description | Stored? | Location |
|----------|-------------|---------|----------|
| **Services Data** | User details, groups, resource definitions, network logs, config, access tokens | Yes | US (GCP) |
| **Content Data** | Actual payloads between Client and Resource (E2E encrypted) | **No** | N/A |
| **Usage Data** | Crash reports, telemetry, bandwidth stats, UI interactions | Yes | US (GCP) |

### Per-Product Specifics
- **Private Access**: Control plane handles auth/authz; data plane uses Relays for routing only; Relays see no unencrypted content
- **Identity Firewall**: Adds session recording via Gateway (customer-deployed, customer-controlled); Twingate **cannot** access session logs; requires Private Access subscription
- **DNS Filtering**: Logs domain names + timestamp + user identity + device details for users running Twingate Client (unless excluded by admin)

## Architecture Notes
- **Twingate-operated**: Controllers, Relays, Admin Console (cloud)
- **Customer-operated**: Clients, Resources, Connectors, Gateways (Identity Firewall)
- Passwords not stored — auth delegated to IdPs (Okta, OneLogin, social logins)
- Infrastructure: United States; mirrors for resiliency; some Google Cloud

## Gotchas
- Relays may relay encrypted traffic when peer-to-peer connection fails — Relays still cannot decrypt content
- Session recording logs (Identity Firewall) are content data but stored **only** in customer infrastructure, not Twingate's
- DNS Filtering data **is** stored by Twingate (unlike content data) — domain names, user identity, device info
- Usage data may be **published in anonymized/aggregated form** without customer consent
- Twingate has a development subsidiary in Israel and uses third-party vendors globally

## Related Docs
- [Network Logs](https://www.twingate.com/docs) — referenced for services data examples
- [Relays](https://www.twingate.com/docs) — peer-to-peer connection conditions
- [DNS Filtering](https://www.twingate.com/docs/dns-filtering)
- [Vendors list](https://www.twingate.com/docs) — third-party processors