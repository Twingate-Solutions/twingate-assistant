# Client Connection Flow

## Page Title
Client Connection Flow

## Summary
Describes the 5-step process by which a Twingate Client establishes a secure, authorized connection to a Resource via a Connector. The Client intercepts network requests, obtains time-bound tokens from the Controller, and establishes a certificate-pinned TLS tunnel before proxying traffic.

## Key Information
- Client receives a signed whitelist ACL from the Controller upon registration; only matching traffic is intercepted
- Local VPN tunnel to `127.0.0.1` is used solely for traffic interception — **not** an actual VPN connection to any remote destination
- Non-matching traffic bypasses Twingate entirely via the host's existing routing table
- All tokens are time-bound and signed by the Controller
- DNS resolution for FQDN-based Resources occurs **at the Connector**, enabling private/local DNS for off-network users
- Proof-of-possession (RFC 7800) is used to verify TLS tunnel integrity against MITM attacks

## Prerequisites
- At least one Connector deployed and registered
- At least one Client registered with the Twingate network
- Resources configured in the Admin Console with access rules assigned to users

## Step-by-Step Connection Flow

1. **Detect request** — Client's transparent proxy intercepts traffic matching its Controller-signed whitelist ACL based on destination address
2. **Obtain Connector authorization** — Client requests a time-bound token from the Controller; response includes Relay FQDN and Connector certificate digest
3. **Establish certificate-pinned TLS tunnel** — Client connects through Relay (mutual verification), then establishes end-to-end TLS to Connector, pinned to the certificate digest from step 2
4. **Present signed ACL to Connector** — Client requests a second token from the Controller: a signed, user-specific ACL including the Client's public key; Connector verifies this against its own Controller authorization + proof-of-possession check
5. **Proxy traffic** — Connector forwards traffic to the Resource; if FQDN-based, DNS resolves locally at the Connector

## Configuration Values
- Port restrictions configurable via Admin Console (optional)
- No client-side configuration required for this flow; behavior is driven by Controller-delivered ACL

## Gotchas
- Network requests for private Resources are **held at the Client** and never leave the host device if the user lacks authorization
- The local `127.0.0.1` tunnel may trigger OS-level VPN notifications — this is expected and does not indicate a remote VPN connection
- Two separate Controller authorization requests occur per connection (step 2 and step 4); both must succeed
- Destination address does not need to be routable from the Client host device

## Related Docs
- Architecture Overview
- Connectors
- Resources
- Admin Console / Access Rules
- Port Restrictions configuration
- RFC 7800 (Proof-of-Possession Key Semantics for JWTs)