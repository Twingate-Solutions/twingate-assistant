# Client Connection Flow

## Page Title
Client Connection Flow

## Summary
Describes the end-to-end process by which a Twingate Client detects, authenticates, and proxies traffic to a private Resource through a Connector. The flow involves local traffic interception, dual Controller authorization token exchanges, certificate-pinned TLS tunneling via a Relay, and transparent proxying. No traffic leaves the client device unless the user is authorized.

## Key Information
- Client establishes a local VPN tunnel to `127.0.0.1` solely to intercept traffic destined for Resources in its whitelist ACL — this is **not** a VPN to any remote destination
- Whitelist ACL is Controller-signed and stored locally on the Client
- Intercepted connection requests are **held** until authorization completes — unauthorized requests never leave the device
- Non-Resource traffic is bypassed to the host's existing routing table transparently
- DNS for FQDN-based Resources resolves **at the Connector**, enabling private/local DNS without client-side DNS configuration
- MITM protection uses RFC 7800 proof-of-possession between Client and Connector

## Prerequisites
- At least one Connector registered to the Twingate network
- At least one Client registered to the Twingate network
- Resources configured in the Admin Console with access rules assigned to users

## Step-by-Step Connection Flow

1. **Detect Resource request** — Client intercepts connection matching signed whitelist ACL by destination address (address need not be routable from client)
2. **Obtain Connector authorization token** — Client requests token from Controller; response includes Relay FQDN and Connector certificate digest
3. **Establish cert-pinned TLS tunnel** — Client connects to Relay (validates Relay's public cert); Relay validates Client's Controller-signed token; Client and Connector establish end-to-end TLS pinned to Connector's certificate digest
4. **Present Resource ACL token** — Client makes second Controller request; receives signed ACL containing client's public key; presents to Connector for verification
5. **Proof-of-possession check** — Client and Connector verify TLS tunnel integrity per RFC 7800
6. **Proxy traffic** — DNS (if FQDN Resource) resolves at Connector; proxied connection forwarded to Resource; source application unaware of tunneling

## Configuration Values
- Port restrictions for proxied traffic: configurable via Admin Console
- Supported traffic: any TCP or UDP, any port or protocol (unless restricted)

## Gotchas
- The local `127.0.0.1` tunnel will trigger OS-level VPN notifications — this is expected and does **not** mean a remote VPN is active
- Two separate Controller token requests occur per connection (one for Connector routing info, one for ACL verification)
- Certificate pinning uses a digest from the Controller, not standard PKI — Connector cert must be current in the Controller
- DNS resolution happens at the Connector, not the client — local/private DNS on the remote network works automatically

## Related Docs
- Architecture Overview
- Connectors
- Resources
- Port Restrictions (Admin Console)
- RFC 7800 (proof-of-possession for JWTs)