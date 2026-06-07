# Twingate & Customer Data

## Page Title
Twingate & Customer Data

## Summary
Documents what customer data Twingate collects across its three products (Private Access, Identity Firewall, DNS Filtering). Intended for privacy, legal, and security professionals. Twingate acts as a routing intermediary for encrypted content—it cannot read payload data.

## Key Information

### Three Data Categories (All Products)
| Category | Stored? | Examples |
|----------|---------|---------|
| **Services Data** | Yes – US servers (GCP) | User names/emails, groups, resource definitions, network logs, access tokens, security policies |
| **Content Data** | **No** | Actual payloads between Client and Resource; end-to-end encrypted |
| **Usage Data** | Yes – same as Services | Crash reports, telemetry, bandwidth stats; may be published anonymized |

### Per-Product Data Notes
- **Private Access**: Control plane handles auth/authz metadata; data plane traffic is E2E encrypted and not stored
- **Identity Firewall**: Session recording logs = Content Data; Gateways are **customer-deployed**—Twingate has no access to session logs; E2E encryption prevents Twingate from decrypting sessions
- **DNS Filtering**: Logs domain names, timestamp, user identity, device info for users running the Client (unless admin-excluded); stored on US infrastructure

## Prerequisites
- Identity Firewall requires a Private Access subscription
- DNS Filtering requires the Twingate Client to be running on user devices

## Configuration Values / Architecture Components

| Component | Operated By | Function |
|-----------|-------------|---------|
| Controller | Twingate (cloud) | Auth/authz coordination, stores Services Data |
| Relay | Twingate (cloud) | Routes encrypted traffic; stores nothing |
| Admin Console | Twingate (cloud) | Customer configuration interface |
| Client | Customer | Installed on end-user devices |
| Connector | Customer | Deployed in customer infrastructure |
| Gateway (Identity Firewall) | Customer | Session recording; no Twingate access |

## Gotchas
- **Passwords not stored**: Auth delegated to IdPs (Okta, OneLogin, social logins)
- **Relays cannot read content**: Even when used for routing (not just P2P brokering), traffic remains E2E encrypted
- **Session recording data is customer-only**: Gateways live in customer infra; Twingate cannot access these logs
- **DNS Filtering scope**: Only applies to users running the Client and not admin-excluded
- **Usage Data may be published**: Anonymized/aggregated stats can be made public
- **Data residency**: All storage is US-based; Twingate has Israeli development subsidiary and uses third-party vendors

## Related Docs
- [Network Logs](https://www.twingate.com/docs/network-logs)
- [Twingate Relays](https://www.twingate.com/docs/relays)
- [Relay connection conditions](https://www.twingate.com/docs/relays#certain-technical-conditions)
- [DNS Filtering](https://www.twingate.com/docs/dns-filtering)
- [Vendors list](https://www.twingate.com/docs/vendors)