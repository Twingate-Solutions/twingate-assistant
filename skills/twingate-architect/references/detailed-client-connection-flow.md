# Detailed Client Connection Flow

## Page Title
Detailed Client Connection Flow

## Summary
Describes the end-to-end process by which a Twingate Client intercepts network requests, obtains authorization from the Controller, establishes a certificate-pinned TLS tunnel through a Relay to a Connector, and proxies traffic to private Resources. The flow ensures no private traffic leaves the client device unless the user is explicitly authorized.

## Key Information
- Client establishes a local VPN tunnel to `127.0.0.1` **only** for traffic interception — this is not a remote VPN connection
- Non-matching traffic (not in whitelist ACL) bypasses Twingate entirely via existing routing table
- DNS resolution for FQDN-based Resources occurs **at the Connector**, enabling private/local DNS usage for off-network users
- Certificate pinning is enforced end-to-end: Client pins the Connector's certificate digest provided by the Controller
- Every Client generates its own public/private key pair used for proof-of-possession validation
- Implements RFC 7800 proof-of-possession to prevent intermediary tampering

## Connection Flow Steps

1. **Detect resource request** — Client intercepts TCP/UDP connections matching whitelist ACL (signed by Controller); holds request until auth completes
2. **Obtain Connector authorization** — Client requests token from Controller; receives: Relay FQDN, hashed Connector ID, Connector certificate digest
3. **Connect to Relay** — Client connects to Relay, validates Relay TLS cert against FQDN; Relay verifies Controller-signed token and confirms Connector is connected
4. **Establish certificate-pinned TLS tunnel** — Client-Connector TLS tunnel negotiated; pinned against Connector cert digest from step 2
5. **Present Controller-signed auth to Connector** — Client fetches connection-specific token (includes Client public key) from Controller; signs a TLS-session-derived secret; sends both to Connector over tunnel
6. **Connector validates** — Verifies Controller signature, uses embedded Client public key to validate signed secret (proof-of-possession)
7. **Proxy traffic** — FQDN DNS resolved at Connector; connection forwarded to Resource; source application unaware of proxying

## Configuration Values
- Whitelist ACL: signed by Controller, delivered at Client registration and on updates
- Authorization tokens: time-bound, connection-specific, bound to Client public key
- Connector identification at Relay: SHA hash of Connector ID (not raw ID)

## Gotchas
- The local `127.0.0.1` tunnel may trigger OS-level VPN notifications — this is expected and does not represent a remote VPN connection
- Private Resource traffic is held at the Client until all auth steps complete; it **never leaves the device** if authorization fails
- Relay only brokers the connection setup — it cannot inspect traffic due to certificate pinning between Client and Connector
- Connector cert digest is provided by Controller, not discovered at connection time — Controller is the trust anchor

## Prerequisites
- At least one Connector registered with the Twingate network
- Client registered and authenticated with the Controller
- Resources configured with access rules in Admin console

## Related Docs
- Architecture Overview
- Connector Registration Process
- Resource Configuration
- RFC 7800 (Proof-of-Possession Key Semantics for JWTs)