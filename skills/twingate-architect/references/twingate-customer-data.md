# Twingate & Customer Data

## Page Title
Twingate & Customer Data

## Summary
Documents the three categories of customer data Twingate collects across its Private Access, Identity Firewall, and DNS Filtering products. Intended for privacy, legal, and security teams evaluating data handling practices. Twingate does not inspect encrypted content data and does not store user passwords.

## Key Information

### Data Categories (All Products)

| Category | Stored | Inspectable by Twingate |
|----------|--------|------------------------|
| **Services Data** | Yes – US servers (Google Cloud) | Yes |
| **Content Data** | No | No (E2E encrypted) |
| **Usage Data** | Yes – same as Services Data | Yes (anonymized for publishing) |

### Services Data Includes
- User names, email addresses, group memberships
- Resource definitions, remote network names, security policies
- Network logs, access tokens, configuration data
- Support request content
- **Does NOT include passwords** (auth delegated to IdPs: Okta, OneLogin, social)

### Content Data
- Actual payloads between Client ↔ Resource (files, commands, media)
- End-to-end encrypted; Relays cannot decrypt even when relaying traffic
- Never stored by Twingate

### Usage Data
- Crash reports, UI interactions, bandwidth stats, telemetry
- May be published in anonymized/de-identified aggregate form

## Product-Specific Notes

### Identity Firewall
- Requires Private Access subscription
- **Session Recording**: Captured by Gateway components deployed in **customer-controlled infrastructure** — Twingate has zero access to these logs
- E2E encryption prevents Twingate from decrypting session content independently

### DNS Filtering
- Logs: domain names accessed, timestamp, user identity, device details
- Only collected from users running Twingate Client (excludable by admin)
- Stored on US infrastructure (Google Cloud)
- Used only for service operation/improvement

## Infrastructure & Storage
- **Controller** (Twingate-operated): Stores Services/Usage Data; US-based, mirrored for resiliency
- **Relay** (Twingate-operated): Routes encrypted traffic; stores nothing
- **Connector/Gateway/Client** (Customer-operated): Customer controls these components
- Twingate HQ: United States; development subsidiary in Israel

## Gotchas
- Relays *can* be used as routing hops if P2P fails — but still cannot see encrypted payload
- Session recording logs exist only in customer infrastructure; Twingate cannot access them even for support
- DNS Filtering logging is admin-configurable; specific users can be excluded
- Usage data may be published publicly in aggregate form — review if data minimization is a concern

## Related Docs
- [Network Logs](https://www.twingate.com/docs/network-logs)
- [Relay documentation](https://www.twingate.com/docs/relays)
- [DNS Filtering](https://www.twingate.com/docs/dns-filtering)
- [Vendor list](https://www.twingate.com/docs/vendors)
- Certain technical conditions for Relay fallback (linked inline in source)