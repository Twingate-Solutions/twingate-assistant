# Client Connection Flow

## Page Title
Client Connection Flow

## Summary
Describes the end-to-end process by which a Twingate Client intercepts network requests, obtains authorization from the Controller, establishes a certificate-pinned TLS tunnel via a Relay to a Connector, and proxies traffic to private Resources. No traffic leaves the client device unless the user is authorized.

## Key Information
- Client maintains a Controller-signed whitelist ACL locally; only matching traffic is intercepted
- Local VPN tunnel to `127.0.0.1` is used for interception only — not a remote VPN connection
- Non-matching traffic bypasses Twingate via the host's existing routing table
- DNS for FQDN-based Resources resolves at the Connector (enables private/local DNS)
- Proof-of-possession per RFC 7800 protects against MITM attacks on the TLS tunnel
- TCP and UDP traffic proxied transparently regardless of port/protocol (port restrictions configurable via Admin Console)

## Connection Flow Steps

1. **Detect request** — Client intercepts connection requests matching its whitelist ACL via local transparent proxy; holds connection pending authorization
2. **Obtain Connector authorization** — Client requests token from Controller; response includes Relay FQDN and Connector certificate digest
3. **Establish cert-pinned TLS tunnel** — Client connects through Relay (mutual identity verification), then establishes end-to-end TLS to Connector pinned to the certificate digest from step 2
4. **Present signed ACL to Connector** — Client obtains second Controller-signed token (bound to client public key + user ACL); Connector verifies it matches its own Controller; proof-of-possession (RFC 7800) confirms tunnel integrity
5. **Proxy traffic** — Connector forwards connection to Resource; if FQDN-based, DNS resolves locally at Connector; source application is unaware of proxying

## Configuration Values
- Port restrictions: configurable in Admin Console (optional)
- Local intercept address: `127.0.0.1` (fixed)

## Gotchas
- The local VPN tunnel to `localhost` may trigger OS-level VPN notifications — this is expected and does not represent a remote VPN connection
- Intercepted connections to private Resources are **held** at the client until auth completes; slow Controller responses will delay connection establishment
- DNS resolution occurs at the Connector, not the client — ensure Connector has access to required DNS servers for private Resources
- Tokens are time-bound; clock skew between components could cause auth failures

## Prerequisites
- At least one Connector registered and connected
- At least one Client authenticated with the Controller
- Resources configured with access rules in Admin Console

## Related Docs
- Architecture Overview
- Resources configuration
- Connector setup
- Port restrictions (Admin Console)
- RFC 7800 (proof-of-possession key semantics for JWTs)