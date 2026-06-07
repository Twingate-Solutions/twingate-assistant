# Detailed Client Connection Flow

## Page Title
Detailed Client Connection Flow

## Summary
Describes the end-to-end process by which a Twingate Client detects, authorizes, and establishes a secure proxied connection to a Resource. The flow involves the Client, Controller, Relay, and Connector components working together with mutual certificate pinning and cryptographic proof-of-possession. No actual VPN connection is made to remote destinations—only a local tunnel to `127.0.0.1` is established on the device.

## Key Information
- Client intercepts traffic via a local VPN tunnel to `127.0.0.1` (OS-level; not a real VPN)
- Whitelist ACL is signed by Controller, stored on Client, and updated on changes
- Non-matching traffic is bypassed to the device's existing routing table/DNS resolvers
- Network requests for private Resources **do not leave the device** unless user is authorized
- DNS resolution for FQDN-based Resources occurs **at the Connector** (supports private/local DNS)
- Connections use certificate-pinned TLS end-to-end (Client → Relay → Connector)
- Proof-of-possession per [RFC 7800](https://www.rfc-editor.org/rfc/rfc7800) prevents intermediary interference

## Connection Flow Steps

1. **Detect request** — Client's local proxy intercepts traffic matching the signed whitelist ACL by destination address (does not need to be routable from client)
2. **Get Connector authorization** — Client requests token from Controller; response includes:
   - Relay FQDN
   - Hash of Connector ID
   - Digest of Connector's certificate
3. **Establish cert-pinned TLS tunnel** — Client connects to Relay (validated by FQDN cert); Relay verifies Controller-signed token and that target Connector is connected; Client and Connector establish TLS with pinned cert
4. **Present Resource authorization** — Client requests a connection-specific token from Controller (includes Client's public key); Controller returns signed time-bound ACL token with Client's public key; Client signs a TLS-session-derived secret with its private key; both token and signed secret sent to Connector
5. **Connector validates** — Verifies Controller signature, uses Client's public key to validate the TLS session secret (proof-of-possession), confirms ACL entitlement
6. **Proxy traffic** — If Resource is FQDN-based, DNS resolves at Connector; connection forwarded from Client through encrypted tunnel to Resource; source application unaware of proxying

## Gotchas
- The local `127.0.0.1` VPN tunnel may trigger OS-level VPN notifications—this is **not** a VPN to any remote host
- Authorization tokens are **time-bound**; clients must re-obtain tokens for continued access
- Each Client generates its own public/private key pair; this is critical to the proof-of-possession mechanism
- Connection requests are **held** (not dropped or forwarded) until security checks complete—latency expected on first connection to a Resource

## Prerequisites
- At least one Connector registered with the Twingate network
- Client authenticated and registered with the Controller
- Resources configured with access rules in the Admin console

## Related Docs
- Architecture Overview
- Connector Registration Process
- Resources Configuration
- RFC 7800 (Proof-of-Possession Key Semantics for JSON Web Tokens)