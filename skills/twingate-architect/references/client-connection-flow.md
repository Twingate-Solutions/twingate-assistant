## Page Title
Client Connection Flow

## Summary
Step-by-step walkthrough of how the Twingate Client establishes an authenticated, encrypted connection to a Resource. Five sequential phases: ACL interception, Controller token request, cert-pinned TLS tunnel via Relay, Connector-side ACL verification with proof-of-possession, and final traffic proxying with Connector-side DNS resolution.

## Key Information
- **Phase 1 — Intercept**: Client establishes a local VPN tunnel to `127.0.0.1` to intercept traffic destined for Resources in its signed whitelist ACL; non-matching traffic bypasses Twingate unchanged
- **Phase 2 — Controller token**: Client requests a time-bound signed token from the Controller; token contains Relay FQDN and Connector certificate digest for TLS pinning
- **Phase 3 — TLS tunnel**: Client connects to Relay (validates Relay's public cert); Relay validates Controller-signed Client token; Relay connects Client to Connector; Client pins TLS to Connector cert digest from Phase 2
- **Phase 4 — ACL presentation**: Client makes second Controller request for a user-specific signed ACL; presents ACL to Connector; Connector verifies it was signed by the same Controller; RFC 7800 proof-of-possession check protects against MITM
- **Phase 5 — Proxy**: Connector resolves FQDN via local private DNS (if Resource is FQDN-based); forwards proxied connection to Resource; source application is unaware of the proxy
- Non-matching traffic (not in ACL) bypasses Twingate — pure split-tunnel behavior

## Prerequisites
- At least one Connector registered and one Client authenticated with the network

## Step-by-Step
(See summary above — phases are sequential and mandatory)

## Configuration Values
None on this page — all token and cert mechanics are automatic.

## Gotchas
- The local `127.0.0.1` tunnel causes some OS-level "VPN connected" notifications — Twingate is not a VPN, no remote VPN connection is established
- Two separate Controller round-trips are required per new Resource connection — clock skew or Controller unavailability causes auth failure
- DNS for FQDN resources is resolved by the Connector, not the Client — Client never learns the Resource's real private IP

## Related Docs
- `/docs/how-twingate-works` — component roles and ACL flow
- `/docs/how-dns-works-with-twingate` — DNS interception details
- `/docs/how-encryption-works-in-twingate` — TLS and certificate pinning details
- `/docs/detailed-client-connection-flow` — lower-level packet-by-packet walkthrough
