# Detailed Client Connection Flow

## Page Title
Detailed Client Connection Flow

## Summary
Describes the end-to-end process by which a Twingate Client establishes a secure, authenticated connection to a Resource via a Connector. The flow involves traffic interception, multi-step authorization from the Controller, certificate-pinned TLS tunneling through a Relay, and cryptographic proof-of-possession before any private traffic is forwarded.

## Key Information
- Client establishes a local VPN tunnel to `127.0.0.1` solely to intercept/proxy traffic — this is **not** a remote VPN connection
- Non-Resource traffic bypasses Twingate entirely via the existing routing table
- Network requests for private Resources **do not leave the client device** unless the user is authorized
- DNS resolution for FQDN-based Resources happens **at the Connector**, enabling private/local DNS resolution for off-network users
- Proof-of-possession per [RFC 7800](https://datatracker.ietf.org/doc/html/rfc7800) prevents MITM attacks on the TLS session
- Each Client generates its own public/private key pair used for token binding

## Connection Flow Steps

1. **Intercept**: Client detects connection request matching whitelist ACL (Controller-signed, stored locally)
2. **Get Connector info**: Client requests authorization from Controller → receives Relay FQDN, hashed Connector ID, Connector cert digest
3. **Relay validation**: Client connects to Relay; Relay verifies Controller-signed token and that target Connector is connected
4. **TLS tunnel**: Client and Connector establish cert-pinned TLS tunnel (pinned against digest from Controller)
5. **Resource authorization**: Client requests connection-specific token from Controller, including Client public key
6. **Proof-of-possession**: Client signs a TLS-session-derived secret with its private key; sends both Controller token and signed secret to Connector
7. **Connector verification**: Connector validates Controller signature, uses Client public key from token to verify session secret
8. **Proxy traffic**: Connection request forwarded to Resource; DNS resolved locally at Connector if FQDN-based

## Configuration Values
- Whitelist ACL: signed by Controller, delivered on registration and on updates
- Authorization tokens: time-bound, bound to Client public key, signed by Controller
- Relay FQDN: used for both routing and TLS certificate validation

## Gotchas
- The local `127.0.0.1` tunnel may trigger OS-level VPN notifications — this is expected and does not indicate a remote VPN connection
- Destination address in connection request does **not** need to be routable from the Client device
- Connector cert pinning digest comes from Controller — if Connector cert changes without Controller update, connection will fail
- TCP and UDP are proxied regardless of port or protocol

## Prerequisites
- At least one Connector registered with the network
- At least one Client registered with the Controller
- Resources defined with access rules in Admin console
- Controller reachable by both Client and Connector

## Related Docs
- Architecture Overview
- Connector Registration Process
- Resources Configuration
- Admin Console Access Rules