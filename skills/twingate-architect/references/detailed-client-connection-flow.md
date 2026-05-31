# Detailed Client Connection Flow

## Page Title
Detailed Client Connection Flow

## Summary
Describes the end-to-end process by which a Twingate Client establishes a secure, authorized connection to a private Resource via a Connector. The flow involves five distinct phases: request detection, authorization, TLS tunnel establishment, token-based proof-of-possession, and traffic proxying.

## Key Information

- Client establishes a local VPN tunnel to `127.0.0.1` **only** for intercepting/detecting Resource traffic — this is NOT a remote VPN connection
- Whitelist ACL is signed by the Controller and stored locally on the Client
- All tokens are time-bound and connection-specific
- Non-Resource traffic is bypassed to the existing routing table/DNS — Client is transparent to other traffic
- DNS resolution for FQDN-based Resources occurs **at the Connector**, enabling private/local DNS usage for off-network users
- Certificate pinning is enforced end-to-end (Client → Connector) using a digest provided by the Controller
- Proof-of-possession implemented per [RFC 7800](https://www.rfc-editor.org/rfc/rfc7800)

## Prerequisites
- At least one Connector registered with the Twingate network
- At least one Client registered with the Twingate network
- Resources configured with access rules in the Admin console

## Step-by-Step Connection Flow

1. **Detect request** — Client's local proxy intercepts TCP/UDP traffic matching the Controller-signed whitelist ACL by destination address
2. **Obtain Connector authorization** — Client requests token from Controller; response includes:
   - Relay FQDN
   - Hash of Connector ID (privacy-preserving)
   - Digest of Connector's TLS certificate (for pinning)
3. **Establish certificate-pinned TLS tunnel** — Client connects to Relay → Relay validates Controller-signed token → Relay confirms Connector is connected → Client and Connector negotiate TLS using pinned certificate
4. **Present Controller-signed authorization** — Client:
   - Requests connection-specific token from Controller (includes Client public key)
   - Receives signed ACL + public key in Controller response
   - Signs a secret derived from the TLS session
   - Sends both the Controller token and signed secret to Connector over the tunnel
5. **Connector validates** — Verifies Controller signature, Client public key, and TLS-session-bound secret (proof-of-possession)
6. **Proxy traffic** — Connection request forwarded; DNS resolved at Connector for FQDN resources; application traffic proxied transparently

## Configuration Values
- No direct env vars or CLI flags documented on this page
- ACL is delivered automatically by Controller on Client registration and on updates

## Gotchas

- The local `127.0.0.1` tunnel may trigger OS-level VPN notifications — this is expected and does **not** indicate a remote VPN connection
- Network requests for private Resources are **held** at the Client until authorization completes — they never leave the device if the user is unauthorized
- Destination address for a Resource does **not** need to be routable from the Client host
- Each Client generates its own public/private key pair — tokens are bound to the Client's private key

## Related Docs
- Architecture Overview
- Connector Registration Process
- Resources configuration (Admin console)
- RFC 7800 (proof-of-possession for JWTs)