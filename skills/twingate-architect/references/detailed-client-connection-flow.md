# Detailed Client Connection Flow

## Page Title
Detailed Client Connection Flow

## Summary
Describes the end-to-end process by which a Twingate Client detects, authorizes, and proxies traffic to a private Resource via a Connector. The flow involves five sequential phases: traffic interception, Controller authorization, TLS tunnel establishment, proof-of-possession validation, and traffic proxying.

## Key Information

- Client establishes a local VPN tunnel to `127.0.0.1` **only** for traffic interception — this is not a remote VPN connection
- Whitelist ACL is signed by the Controller and stored on the Client; updated on registration and subsequent changes
- Non-Resource traffic bypasses Twingate entirely via existing routing table/DNS
- DNS resolution for FQDN-based Resources occurs **at the Connector**, enabling private/local DNS use for off-network clients
- Certificate pinning is enforced end-to-end (Client → Connector) using a digest provided by the Controller
- Proof-of-possession per [RFC 7800](https://www.rfc-editor.org/rfc/rfc7800) prevents intermediary interference

## Prerequisites
- At least one Connector registered with the Twingate network
- At least one Client registered with the Controller
- Resources configured with access rules in the Admin console

## Step-by-Step Connection Flow

1. **Traffic Interception** — Client detects connection to a Resource address in its signed ACL via local transparent proxy; holds the request
2. **Obtain Connector Authorization** — Client requests authorization from Controller; receives:
   - Relay FQDN (for routing + cert validation)
   - Hash of Connector ID (privacy-preserving Connector reference)
   - Digest of Connector's TLS certificate (for pinning)
3. **Establish TLS Tunnel via Relay**:
   - Client connects to Relay; Relay validates Client's Controller-signed token
   - Relay confirms target Connector is connected (matched by Connector ID hash)
   - Client and Connector establish certificate-pinned TLS tunnel
4. **Present Resource Authorization to Connector**:
   - Client sends its public key to Controller; receives signed time-bound token containing ACL + Client public key
   - Client signs a secret derived from the TLS tunnel context
   - Client sends Controller-signed token + Client-signed secret to Connector
   - Connector validates: token issuer matches its registered Controller, Client public key validates the signed secret, TLS session integrity confirmed (RFC 7800)
5. **Proxy Traffic** — Connector forwards connection to Resource; DNS resolved locally at Connector if FQDN-based

## Configuration Values
- No direct env vars or CLI flags described on this page
- ACL whitelist: delivered from Controller, not manually configured on Client

## Gotchas

- The local `127.0.0.1` tunnel may trigger OS-level VPN notifications — this is expected and does not represent an active remote VPN
- Network requests to private Resources **never leave the client device** unless authorization succeeds
- Destination addresses in ACL do **not** need to be routable from the Client host
- Tokens are time-bound; connections require fresh token issuance per resource access attempt
- Connector ID is exposed to the Relay only as a hash — the Relay has no knowledge of the actual Connector identity

## Related Docs
- Architecture Overview
- Connector Registration Process
- Resources configuration
- Admin Console access rules
- RFC 7800 (Proof-of-Possession Key Semantics for JWTs)