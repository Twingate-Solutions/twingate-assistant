---
source: https://www.twingate.com/docs/how-twingate-works
type: docs
fetched: 2026-08-14
source_version: 1eb0d28eee485e94afee416b2ab0adec5d57844b96ce93e4b263f57867a725fd
---

# How Twingate Works

## Summary
Twingate uses four components (Controller, Client, Connector, Relay) where no single component can independently authorize traffic flow. Authorization requires confirmation from multiple components, with user authentication delegated to a third-party IdP. Users access Resources via local FQDNs/IPs without needing network topology knowledge.

## Key Information

- **No single point of authorization**: Traffic decisions require intersection of Client ACL + Connector ACL
- **Controller**: Hosted multi-tenant service; only component that never touches data flow
- **Client**: Installed on user devices; handles routing, auth proxy, DNS proxying, TLS tunneling
- **Connector**: Deployed behind private network firewall; verifies Client connections, resolves DNS locally
- **Relay**: Equivalent to TURN server; stores no data; used as fallback when peer-to-peer fails
- **P2P preferred**: Twingate attempts peer-to-peer Client↔Connector first; Relay is backup
- **Connector ID**: Anonymized hash-based ID; only identifying info shared with Clients

## Architecture Flow

- Controller stores config, issues signed ACLs to Clients, registers/authenticates Connectors
- Connector authenticates with Controller → receives Connector ACL → maintains outbound connection to Relay(s)
- Client detects connection to protected Resource → gets signed user ACL from Controller → establishes certificate-pinned TLS tunnel via Relay to Connector
- Connector verifies: TLS tunnel integrity + Client signature + Client ACL claim validity
- Traffic forwarded only if destination exists in **both** Client ACL and Connector ACL (intersection)

## Component Responsibilities

| Component | Hosted By | Touches Data |
|-----------|-----------|--------------|
| Controller | Twingate (multi-tenant) | No |
| Client | User device | Yes (proxy) |
| Connector | Customer network | Yes (forwards) |
| Relay | Twingate | No |

## Security Design

- **ACL double-check**: Resource must be in both Client ACL (user entitlement) and Connector ACL (network destination authorization)
- **Signed ACLs**: Controller signs Client ACL; Connector verifies signature to prevent tampering
- **Certificate pinning**: TLS tunnel pinned to specific Connector via signed connection token
- **Connector registration**: Requires one-time Controller authorization; registered with anonymous hash ID
- **DNS privacy**: DNS lookups for protected Resources resolved locally on Remote network by Connector

## Gotchas

- Connectors **cannot** be deployed without one-time authorization from Controller
- Relay never terminates data-carrying connections — it only brokers the Client↔Connector tunnel establishment
- DNS requests for protected Resources are forwarded to the Connector for local resolution (not resolved on user's network)
- Applications on user devices appear to connect directly to Resources (transparent proxy — no app config needed)
- Connector ID shared with Clients contains no private network information

## Related Docs
- Connector deployment guide
- Client installation guide
- Relay documentation
- Identity Provider configuration
- Admin console / access management