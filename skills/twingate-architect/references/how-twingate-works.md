## Page Title
How Twingate Works

## Summary
Detailed technical overview of Twingate's four-component architecture: Controller, Client, Connector, and Relay. No single component can unilaterally authorize access — authorization is always multi-party. Connectors make outbound-only connections; no inbound ports required.

## Key Information
- **Controller**: cloud-hosted control plane; stores config, authenticates Connectors, issues signed ACLs to Clients, delegates user auth to IdP; never touches data flow
- **Client**: installed on user device; handles authentication, holds signed user ACL, intercepts traffic to protected resources, proxies DNS and TCP/UDP, establishes certificate-pinned TLS tunnel to Connector
- **Connector**: deployed behind firewall in private network; outbound connections only to Controller and Relay; verifies Client ACL signature on every inbound connection; performs local DNS resolution for FQDN resources
- **Relay**: TURN-equivalent; stores only anonymized hash-based Connector IDs; never terminates data connections; used as fallback when P2P is unavailable
- ACL double-check: traffic is only forwarded if destination falls in the intersection of both the Client ACL and Connector ACL
- Connector registered with anonymized hash-generated unique ID — the only identifying info shared with Clients
- Users access resources via FQDN or IP local to the remote network — no knowledge of network topology required

## Prerequisites
None — reference/overview page.

## Step-by-Step
Not applicable.

## Configuration Values
None on this page.

## Gotchas
- The Controller never handles data flow — it only orchestrates auth and issues signed tokens
- Connector ACL intersection with Client ACL is a second authorization check — misconfigured Connector ACLs can block legitimate access even if the user has permissions
- Certificate pinning on the TLS tunnel means connections are tied to a specific Connector ID, not just any endpoint

## Related Docs
- `/docs/architecture` — architecture overview
- `/docs/how-dns-works-with-twingate` — DNS interception mechanics
- `/docs/client-connection-flow` — step-by-step connection walkthrough
- `/docs/understanding-relays` — Relay infrastructure detail
- `/docs/peer-to-peer-communication-in-twingate` — P2P connection detail
