# Detailed Client Connection Flow

## Page Title
Detailed Client Connection Flow

## Summary
Describes the end-to-end process by which a Twingate Client establishes a secure, authorized connection to a Resource via a Connector. The flow covers traffic interception, multi-step authorization via the Controller, certificate-pinned TLS tunnel establishment through a Relay, and final proxied traffic forwarding.

## Key Information

- Client creates a local VPN tunnel to `127.0.0.1` **only** for traffic interception—this is NOT a remote VPN
- Whitelist ACL is signed by the Controller and stored locally on the Client
- Non-matching traffic is bypassed to the device's existing routing/DNS (Client is transparent)
- DNS resolution for FQDN-based Resources happens **at the Connector**, enabling private/local DNS for remote users
- TLS certificate pinning is enforced Client→Connector using a certificate digest provided by the Controller
- Each Client generates its own public/private key pair; public key is embedded in Controller-signed tokens
- Proof-of-possession per [RFC 7800](https://www.rfc-editor.org/rfc/rfc7800) prevents intermediary interference

## Prerequisites
- At least one Connector registered with the Twingate network
- At least one Client registered with the Twingate network
- Resources configured in the Admin console with access rules

## Step-by-Step Connection Flow

1. **Detect request** — Client intercepts TCP/UDP connection to a destination matching its Controller-signed whitelist ACL via local transparent proxy
2. **Get Connector authorization** — Client requests authorization from Controller; receives:
   - Relay FQDN
   - Hash of Connector ID (privacy-preserving)
   - Connector certificate digest (for pinning)
3. **Establish certificate-pinned TLS tunnel** — Client connects to Relay:
   - Relay validates Client's Controller-signed token
   - Relay confirms target Connector is connected
   - Client and Connector negotiate TLS; Client pins against provided certificate digest
4. **Present Resource authorization** — Over the established tunnel:
   - Client sends its public key to Controller; receives signed, time-bound ACL token
   - Client signs a secret derived from the TLS tunnel context
   - Client sends both (Controller token + Client-signed secret) to Connector
5. **Connector validates** — Connector verifies:
   - Controller signature on the authorization token
   - Client-signed secret using the public key in the token
   - TLS session integrity (proof-of-possession)
6. **Proxy traffic** — Connector forwards traffic to Resource:
   - FQDN Resources: DNS resolved locally at Connector
   - Application is unaware of proxying

## Configuration Values
None exposed directly in this doc (conceptual flow documentation).

## Gotchas

- The local `127.0.0.1` tunnel may trigger OS-level VPN notifications—this is expected and does not represent a remote VPN connection
- Network requests for private Resources **never leave the Client device** unless the user is authorized; connection is held until all security checks pass
- Resource destination addresses do **not** need to be routable from the Client device
- Tokens are **time-bound**; each connection requires a fresh token from the Controller
- Certificate pinning means a compromised or swapped Connector certificate will block connections

## Related Docs
- Architecture Overview
- Connector Registration Process
- Resources Configuration
- RFC 7800 (Proof-of-Possession Key Semantics for JWTs)