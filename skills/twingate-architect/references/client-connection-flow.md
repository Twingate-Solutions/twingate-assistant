# Client Connection Flow

## Page Title
Client Connection Flow

## Summary
Describes the end-to-end process by which a Twingate Client detects, authorizes, and proxies traffic to a private Resource. The flow involves local traffic interception, two-phase Controller authorization, certificate-pinned TLS tunneling via a Relay to a Connector, and final proxied forwarding to the Resource.

## Key Information
- Client establishes a local VPN tunnel to `127.0.0.1` **only** for traffic interception — this is not a remote VPN connection
- ACL whitelist is signed by the Controller and stored locally on the Client
- Two separate Controller authorization requests occur per connection: one to locate the Connector, one to prove Resource access rights
- TLS tunnel is certificate-pinned using a Connector certificate digest provided by the Controller
- DNS resolution for FQDN-based Resources occurs **at the Connector** (enables private/local DNS)
- Traffic not matching the whitelist ACL is bypassed to the host's existing routing table
- Proof-of-possession (RFC 7800) protects against MITM attacks on the TLS tunnel

## Prerequisites
- At least one Connector registered with the Twingate network
- At least one Client registered with the Twingate network
- Resources defined and access rules configured in the Admin Console
- User authenticated with the Client

## Step-by-Step: Connection Flow

1. **Intercept**: Client detects outbound connection request matching whitelist ACL via local transparent proxy; holds request
2. **Authorize (Phase 1)**: Client requests authorization token from Controller for the target Resource; receives Relay FQDN and Connector certificate digest
3. **Establish tunnel**: Client connects to Relay (mutual TLS verification); Relay proxies to Connector; Client pins TLS session using certificate digest
4. **Authorize (Phase 2)**: Client requests a second Controller-signed ACL token (bound to Client's public key); presents to Connector for verification
5. **Verify**: Connector validates token chain and proof-of-possession per RFC 7800
6. **Proxy**: Connector resolves DNS (if FQDN Resource) locally and forwards proxied traffic to Resource

## Configuration Values
- Port restrictions configurable via Admin Console (optional)
- No client-side configuration parameters documented on this page

## Gotchas
- The local `127.0.0.1` tunnel **will trigger OS-level VPN notifications** — this is expected and does not indicate a remote VPN connection
- Network requests for private Resources **will not leave the Client device** if the user lacks authorization (held by proxy indefinitely)
- Destination addresses in the ACL do **not** need to be routable from the Client host
- Both TCP and UDP are supported regardless of port/protocol (unless admin restricts ports)

## Related Docs
- Architecture Overview
- Connectors
- Resources
- Port Restrictions (Admin Console)
- RFC 7800 (Proof-of-Possession Key Semantics for JWTs)