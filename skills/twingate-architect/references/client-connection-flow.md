# Client Connection Flow

## Page Title
Client Connection Flow

## Summary
Describes the 5-step process by which a Twingate Client intercepts network requests, authenticates with the Controller, and establishes a secure proxied connection to a Resource via a Connector. The Client uses a local VPN tunnel (to localhost only) for traffic interception, not for remote connectivity. All authorization is time-bound and cryptographically verified.

## Key Information
- Client stores a Controller-signed whitelist ACL; only matching traffic is intercepted
- Non-matching traffic bypasses Twingate entirely via the host's existing routing table
- Local tunnel is to `127.0.0.1` only — no remote VPN connection is made
- DNS resolution for FQDN-based Resources happens **at the Connector**, enabling private/local DNS
- TLS certificate pinning uses a Connector certificate digest provided by the Controller
- Proof-of-possession (RFC 7800) protects against MITM attacks on the TLS tunnel

## Connection Flow (5 Steps)

1. **Detect resource request** — Client intercepts TCP/UDP traffic matching whitelist ACL via local transparent proxy; holds connection pending auth
2. **Obtain Connector authorization token** — Client requests time-bound token from Controller; response includes Relay FQDN and Connector certificate digest
3. **Establish cert-pinned TLS to Connector** — Via Relay: Client validates Relay's public cert; Relay validates Controller-signed token; Client↔Connector TLS tunnel established and pinned to digest
4. **Present Controller-signed ACL to Connector** — Second Controller request returns signed ACL with Client's public key; Connector verifies shared Controller trust + proof-of-possession
5. **Proxy traffic** — Connector forwards connection to Resource; if FQDN-based, DNS resolved locally at Connector

## Prerequisites
- At least one Connector registered on the network
- At least one Client registered on the network
- Resources configured with access rules in Admin Console
- User authenticated with Client (triggers ACL delivery)

## Configuration Values
- Port restrictions: configurable per Resource in Admin Console (optional)
- No specific env vars or CLI flags documented on this page

## Gotchas
- The OS may display a VPN notification when Client starts — this is the `127.0.0.1` tunnel only, **not** a remote VPN
- Private Resource traffic is **held at the Client** until authorization completes — requests never leave the device if the user is unauthorized
- UDP traffic is supported (not just TCP)
- Non-ACL traffic proceeds normally; Client does not affect general internet traffic

## Related Docs
- Architecture Overview
- Connector setup
- Port restrictions (Admin Console)
- RFC 7800 (proof-of-possession for JWTs)