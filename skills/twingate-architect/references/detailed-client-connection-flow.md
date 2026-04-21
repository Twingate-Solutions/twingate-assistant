## Page Title
Detailed Client Connection Flow

## Summary
Low-level walkthrough of the five-phase Twingate Client connection sequence, expanding on the overview doc with specifics on token contents, Relay validation steps, and the proof-of-possession mechanism. Covers exactly what information flows between Controller, Client, Relay, and Connector at each step.

## Key Information
- **Phase 1 — Intercept**: Local tunnel to `127.0.0.1`; Client intercepts traffic matching whitelist ACL; non-matching traffic bypasses via existing routing table
- **Phase 2 — Controller token**: Token contains: (1) Relay FQDN for cert validation, (2) hash of Connector ID (not raw ID — Relay learns only the hash, preserving anonymity), (3) Connector certificate digest for TLS pinning
- **Phase 3 — TLS tunnel establishment**:
  1. Client connects to Relay; validates Relay's FQDN-based public cert
  2. Relay verifies Client's token is signed by a known Controller
  3. Relay verifies Connector (identified by hash) is currently connected
  4. Relay allows Client-Connector peering; TLS tunnel pinned to Connector cert digest
- **Phase 4 — ACL presentation**:
  - Client generates its own public/private key pair; sends public key with second Controller request
  - Controller returns signed ACL + Client's public key (bound together)
  - Client signs a secret derived from the established TLS tunnel state (shared context)
  - Connector validates: Controller signature on ACL, Client public key validates tunnel-derived secret (RFC 7800 proof-of-possession)
- **Phase 5 — Proxy**: FQDN resources have DNS resolved locally at Connector; proxied connection forwarded to Resource; source app unaware of proxy

## Prerequisites
- At least one registered Connector and authenticated Client

## Step-by-Step
Phases are sequential and all required — see Key Information above.

## Configuration Values
None — all cryptographic operations are automatic.

## Gotchas
- Connector ID hash in the Controller token is the same hash the Connector registered with the Relay — mismatch means connection fails at Relay validation
- Proof-of-possession (RFC 7800) means a stolen token cannot be replayed from a different TLS session
- Two Controller round-trips required: one for connection info, one for the user-specific ACL

## Related Docs
- `/docs/client-connection-flow` — summary version of the same flow
- `/docs/how-encryption-works-in-twingate` — TLS and cert pinning details
- `/docs/understanding-relays` — Relay's role in connection establishment
- `/docs/how-dns-works-with-twingate` — DNS resolution at Connector
