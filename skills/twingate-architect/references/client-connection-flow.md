# Client Connection Flow

## Page Title
Client Connection Flow

## Summary
Describes the 5-step process by which a Twingate Client intercepts, authorizes, and proxies traffic to private Resources. The Client establishes a local VPN tunnel to localhost solely for traffic interception, then uses the Controller, Relay, and Connector to build a certificate-pinned TLS tunnel before forwarding traffic. Non-Resource traffic bypasses Twingate entirely.

## Key Information
- Client receives a **signed whitelist ACL** from the Controller at registration and on updates
- A local tunnel to `127.0.0.1` intercepts Resource-bound traffic; this is **not** a remote VPN connection
- Non-matching traffic is **bypassed** through the existing OS routing table
- DNS for FQDN-based Resources resolves **at the Connector** (enables private/local DNS for remote users)
- Certificate pinning uses a **Connector certificate digest** delivered by the Controller
- MITM protection uses **proof-of-possession per RFC 7800** between Client and Connector
- Intercepted Resource connections are **held locally** until authorization completes — traffic cannot leave the device without authorization

## Connection Flow Steps

1. **Detect Resource request** — Client's transparent proxy intercepts TCP/UDP traffic matching the signed whitelist ACL by destination address
2. **Obtain Connector authorization** — Client requests a time-bound token from the Controller; response includes Relay FQDN and Connector certificate digest
3. **Establish certificate-pinned TLS to Connector** — Client connects via Relay (Relay verifies Controller-signed token; Client validates Relay FQDN cert); Client and Connector then build direct end-to-end TLS tunnel pinned to Connector cert digest
4. **Present Controller-signed ACL to Connector** — Client fetches a second token (signed ACL bound to user's public key); Connector verifies shared Controller trust + proof-of-possession
5. **Proxy traffic** — DNS forwarded to Connector if Resource is FQDN-based; connection forwarded to Resource using Connector's local network address; application is unaware of proxying

## Configuration Values
- Port restrictions configurable via Admin Console (optional, applies to proxied Resource traffic)
- No environment variables or CLI flags documented on this page

## Gotchas
- The `127.0.0.1` local tunnel triggers OS-level VPN notifications — this is expected and does **not** indicate a remote VPN connection
- Destination addresses for Resources **do not** need to be routable from the Client host device
- DNS resolution occurs at the Connector, not the Client — private DNS infrastructure works transparently for off-network users
- Both authorization tokens are **time-bound**; the flow requires two separate Controller requests per connection setup

## Prerequisites
- At least one Connector deployed and registered
- At least one Client registered with the Twingate network
- Resources configured with access rules in the Admin Console

## Related Docs
- Architecture Overview
- Resource configuration / port restrictions (Admin Console)
- RFC 7800 (proof-of-possession for JWTs)