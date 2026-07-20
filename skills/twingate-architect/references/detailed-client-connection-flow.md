# Detailed Client Connection Flow

## Page Title
Detailed Client Connection Flow

## Summary
Describes the end-to-end process by which a Twingate Client establishes a secure, authorized connection to a Resource via a Connector. The flow involves ACL interception, Controller-issued tokens, Relay-facilitated TLS tunneling, and mutual cryptographic verification before any traffic is proxied.

## Key Information
- Client establishes a local VPN tunnel to `127.0.0.1` solely to intercept traffic — **not** a remote VPN connection
- Whitelist ACL is signed by Controller, stored on Client; only matching destinations are intercepted
- Non-matching traffic bypasses Twingate entirely (uses existing routing table/DNS)
- TCP and UDP traffic proxied transparently, regardless of port or protocol
- DNS for FQDN-based Resources resolves **at the Connector** (enables private/local DNS)
- Each Client generates its own public/private key pair used for proof-of-possession

## Connection Flow (5 Steps)

### 1. Detect Resource Request
- Local tunnel intercepts destination addresses matching signed whitelist ACL
- Intercepted connections are **held** until authorization completes — traffic never leaves device unless user is authorized

### 2. Obtain Controller Authorization
Controller returns:
- Relay FQDN (for connection + cert validation)
- Hash of Connector ID (sent to Relay without exposing Connector identity)
- Digest of Connector's certificate (enables TLS cert pinning)

### 3. Establish Cert-Pinned TLS to Connector via Relay
- Client connects to Relay, validates Relay cert against FQDN
- Relay verifies Client's Controller-signed token
- Relay verifies requested Connector (by hash) is connected
- Client and Connector negotiate TLS tunnel; Connector cert digest must match Controller-provided digest

### 4. Present Controller-Signed Authorization to Connector
- Client requests connection-specific token from Controller, including Client's public key
- Controller returns signed, time-bound token with ACL + Client public key
- Client signs a secret derived from the TLS tunnel context
- Client sends token + signed secret to Connector over TLS
- Connector validates:
  - Token signed by same Controller it registered with
  - Client public key (from token) validates Client-signed secret
  - No intermediary interference (proof-of-possession per [RFC 7800](https://www.rfc-editor.org/rfc/rfc7800))

### 5. Proxy Traffic to Resource
- FQDN Resources: DNS query forwarded to Connector, resolved locally at Connector
- Traffic forwarded from Client → Connector → Resource
- Application is unaware of proxying; connection negotiation (including encryption) happens normally end-to-end

## Configuration Values
None (this is architectural documentation, no env vars or CLI flags)

## Gotchas
- The local `127.0.0.1` VPN tunnel will trigger OS-level VPN notifications — this is expected and does **not** mean a remote VPN is active
- Resource addresses do **not** need to be routable from the Client device (routing happens at Connector)
- Tokens are **time-bound** — connections require fresh tokens; stale tokens will fail authorization
- Private DNS works for remote/off-network users because DNS resolves at the Connector, not the Client

## Prerequisites
- At least one Connector registered with the Twingate network
- Twingate Client installed and authenticated
- Resources configured in Admin console with access rules assigned

## Related Docs
- Architecture Overview
- Connector Registration Process
- Resources configuration
- RFC 7800 (proof-of-possession key semantics)