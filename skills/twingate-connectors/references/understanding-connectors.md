---
source: https://www.twingate.com/docs/understanding-connectors
type: docs
fetched: 2026-11-13
source_version: 8a36bc260dde7090a8367c7f09bf834dd10b7f1f37d93b22a1aa4a51fd772068
trust: official
---

# Understanding Connectors

## Summary
Connectors are software-defined proxies deployed inside a private network (cloud or on-prem) that route authorized user traffic to protected Resources. They resemble VPN gateways superficially but differ in security and management behavior. This page gives general conceptual guidance for any environment; environment-specific guides are elsewhere in the docs.

## Key Information
- **Not VPN gateways.** Connectors never let users join the private network. They act as narrow "keyholes" allowing only individual connections to authorized Resources.
- **Never expose to the public internet.** Always place Connectors behind a firewall, inside the private network that hosts the protected Resources.
- **Users never connect to a Connector directly.** Twingate routes users through the appropriate Connector transparently.
- **Multiple Connectors have no downside.** Users are unaware of which Connector handles a connection, so Connectors can mirror your network topology without adding user-facing complexity.
- **Geographic routing.** Traffic can be routed to the nearest Connector. Deploy one per region where services are replicated.
- **Local name/address resolution.** DNS and IP resolution for a Resource happens in the Remote Network where the Connector resides, not on the user's device. Users can use private DNS names and IPs.
- **Automatic clustering.** Connectors in the same Remote Network are clustered automatically for redundancy. Add more to scale with demand.
- **Precise split tunneling.** Only traffic destined for authorized Resources is routed to the relevant Connector. Only Resource traffic on that Remote Network flows through it.
- **No routing changes needed.** Segment networks per best practices and place Connectors in subnets as needed, without modifying network routing for remote access.

## Prerequisites
None stated on this page. A Twingate Remote Network and a private network location for deployment are implied.

## Step-by-Step
Not applicable (conceptual page).

## Configuration Values
None listed on this page.

## Gotchas
- Placing a Connector in a publicly reachable location violates the recommended design.
- Don't treat Connectors as VPN endpoints. Users cannot select or connect to them, and they grant no general network access.
- Resource DNS resolves from the Connector's network, so ensure the Connector can resolve the private names used by Resources.
- Clustering and redundancy apply only within the same Remote Network.

## Related Docs
- Connectors Best Practices guide (including geographic routing)
- Access Control for Staging Environments (use case for separate Connectors per network)
- Environment-specific Connector deployment guides (cloud and on-prem)