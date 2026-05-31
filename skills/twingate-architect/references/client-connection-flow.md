# Client Connection Flow

## Page Title
Client Connection Flow

## Summary
Describes the end-to-end process by which a Twingate Client detects, authorizes, and proxies traffic to a private Resource via a Connector. The flow involves multiple cryptographic verification steps between Client, Controller, Relay, and Connector before any private traffic leaves the client device.

## Key Information
- Client establishes a local VPN tunnel to `127.0.0.1` solely for traffic interception — this is **not** a VPN to any remote destination
- Whitelist ACL is signed by Controller and stored locally on Client; updated on registration and subsequent changes
- All intercepted Resource requests are **held** by the transparent proxy until authorization completes — no traffic leaves the device until the user is verified
- Supports transparent proxying of **any TCP or UDP traffic** regardless of port or protocol
- Non-Resource traffic is bypassed through the host device's existing routing table
- DNS resolution for FQDN-based Resources occurs **at the Connector**, enabling private/local DNS resolution for off-network users

## Prerequisites
- At least one Connector deployed and registered
- At least one Client registered with the Twingate network
- Resources configured with access rules in the Admin Console
- Users assigned access policies by an admin

## Connection Flow (Step-by-Step)

1. **Intercept**: Client detects connection request matching whitelist ACL via local transparent proxy; holds the request
2. **First Auth (Client → Controller)**: Client requests authorization token containing Relay FQDN and Connector certificate digest
3. **Relay Handshake**: Client validates Relay's FQDN-based certificate; Relay validates Client's Controller-signed token
4. **TLS Tunnel**: Client establishes certificate-pinned end-to-end TLS tunnel to Connector using digest from step 2
5. **Second Auth (Client → Controller)**: Client obtains a signed ACL token bound to its public key
6. **Connector Verification**: Connector validates the ACL token originated from the same Controller; Client and Connector perform proof-of-possession (RFC 7800) to confirm tunnel integrity
7. **Traffic Proxy**: Connector forwards held connection to Resource; DNS resolved locally at Connector if Resource is FQDN-based

## Configuration Values
- Port restrictions configurable via Admin Console (optional)
- No client-side configuration parameters exposed in this flow — managed by Controller policy

## Gotchas
- The local `127.0.0.1` tunnel may trigger OS-level VPN notifications — this is expected and does not represent a remote VPN connection
- Destination address does **not** need to be routable from the Client device
- Two separate Controller authorization requests occur per connection (one for Relay/Connector info, one for signed ACL)
- MITM protection uses RFC 7800 proof-of-possession in addition to certificate pinning

## Related Docs
- Architecture Overview
- Connectors
- Resources
- Admin Console / Access Rules
- Port Restrictions