# Detailed Client Connection Flow

## Page Title
Detailed Client Connection Flow

## Summary
Describes the end-to-end process by which a Twingate Client detects, authorizes, and proxies traffic to a protected Resource via a Connector. The flow involves three distinct authorization steps with the Controller before any private traffic leaves the client device. No traffic reaches a Resource unless the user is explicitly authorized.

## Key Information
- Client establishes a **local VPN tunnel to 127.0.0.1** solely to intercept traffic—this is not a remote VPN connection
- Traffic matching the whitelist ACL is intercepted and held; non-matching traffic bypasses Twingate entirely
- ACL is signed by the Controller and stored locally on the Client
- DNS resolution for FQDN-based Resources occurs **at the Connector** (supports private/internal DNS)
- Certificate pinning is enforced end-to-end (Client → Connector) via digest provided by Controller
- Relay never sees plaintext traffic; it only brokers the Client-Connector tunnel
- Implements proof-of-possession per **RFC 7800** to prevent intermediary interference

## Prerequisites
- At least one Connector registered with the Twingate network
- At least one Client registered and authenticated
- Resources configured in the Admin console with access rules assigned

## Step-by-Step Connection Flow

1. **Intercept** — Client detects connection request matching whitelist ACL via local tunnel; holds the request
2. **Get Connector info** — Client requests authorization from Controller; receives:
   - Relay FQDN
   - Hash of Connector ID
   - Digest of Connector's TLS certificate
3. **Connect to Relay** — Client connects to Relay; Relay validates Controller-signed token and confirms Connector is connected
4. **TLS tunnel** — Client and Connector negotiate certificate-pinned TLS tunnel (verified against digest from step 2)
5. **Resource authorization** — Client requests connection-specific token from Controller (includes Client public key); Controller returns signed, time-bound token with ACL and Client public key
6. **Proof-of-possession** — Client signs a secret derived from the TLS tunnel; sends token + signed secret to Connector
7. **Connector validation** — Connector verifies Controller signature, Client public key, and TLS-derived secret
8. **Proxy traffic** — Connector forwards traffic to Resource; DNS resolved locally at Connector if FQDN-based

## Configuration Values
- No directly configurable parameters in this flow; behavior is governed by Controller-issued ACLs and tokens
- Tokens are **time-bound** (exact TTL not specified in docs)

## Gotchas
- The local tunnel to `127.0.0.1` may trigger OS-level VPN notifications—this is expected and does not indicate a remote VPN connection
- Resource destination addresses do **not** need to be routable from the Client device (only from the Connector)
- Private traffic is **never forwarded** from the client if authorization fails at any step
- Relay sees only the Connector hash, not the Connector ID itself

## Related Docs
- Architecture Overview
- Connector Registration Process
- Resources configuration
- RFC 7800 (proof-of-possession for JWTs)