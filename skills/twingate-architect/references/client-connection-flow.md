---
source: https://www.twingate.com/docs/client-connection-flow
type: docs
fetched: 2026-08-14
source_version: b487b8ac897c19fd04c36c85907f9d4bd4d16a694ca3bc57029503a9ec17ae2a
---

# Client Connection Flow

## Page Title
Client Connection Flow

## Summary
Documents the step-by-step process by which a Twingate Client detects, authorizes, and establishes secure connections to Resources through Connectors. The flow involves local traffic interception, dual Controller authorization token exchanges, certificate-pinned TLS tunneling via a Relay, and transparent proxying to the destination Resource.

## Key Information
- Client establishes a local VPN tunnel to `127.0.0.1` solely to intercept traffic — **not** a remote VPN connection
- Whitelist ACL is signed by the Controller, stored on Client, and updated on registration/changes
- Non-Resource traffic is bypassed to the host device's existing routing table
- DNS resolution for FQDN-based Resources happens at the Connector (enables private/local DNS for off-network users)
- Network requests for private Resources **never leave the Client device** unless the user is authorized
- MITM protection implemented via RFC 7800 proof-of-possession technique

## Prerequisites
- At least one Connector registered with the Twingate network
- At least one Client registered with the Twingate network
- Resources configured in Admin Console with access rules assigned

## Step-by-Step Connection Flow

1. **Detect connection request** — Client's local proxy intercepts traffic matching the Controller-signed whitelist ACL by destination address
2. **Obtain Connector authorization token** — Client requests time-bound token from Controller; response includes Relay FQDN and Connector certificate digest
3. **Establish certificate-pinned TLS tunnel** — Client connects through Relay (mutual identity verification), then establishes end-to-end TLS to Connector pinned to certificate digest
4. **Present Controller-signed ACL** — Client makes second Controller request; receives signed ACL containing Client's public key; Connector verifies shared Controller authority + proof-of-possession
5. **Proxy traffic** — Connection proceeds; DNS forwarded to Connector if Resource is FQDN-based; Connector routes to Resource using local network address

## Configuration Values
- Port restrictions configurable via Admin Console (optional, for TCP/UDP)
- No client-side configuration required for the connection flow itself

## Gotchas
- The `127.0.0.1` local tunnel triggers OS-level VPN notifications — this is expected and does **not** indicate a remote VPN connection
- Destination address in connection request does not need to be routable from the Client host device
- Two separate Controller authorization requests occur per connection (not one) — first for Connector info, second for ACL verification
- Held connections to private Resources add latency while security checks complete before traffic is forwarded

## Related Docs
- Architecture Overview
- Connector documentation
- Resource configuration / port restrictions (Admin Console)
- RFC 7800 (proof-of-possession key semantics for JWTs)