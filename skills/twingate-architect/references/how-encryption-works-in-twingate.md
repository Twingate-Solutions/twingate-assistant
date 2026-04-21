## Page Title
Encryption in Twingate

## Summary
Describes how Twingate secures all communications between Client, Connector, Relay, and Controller. The two goals are confidentiality (traffic encrypted end-to-end, opaque to Twingate) and authentication (components verify they're talking to legitimate Twingate infrastructure using certificate pinning and signed tokens).

## Key Information
- **Two goals**: Confidentiality (no third party, including Twingate, can decrypt data traffic) and Authentication (components verify each other's identity)
- **TLS-based authentication**: Client validates Relay and Controller using HTTPS/TLS with certificate authorities — same model as browser-to-bank connections
- **Certificate pinning**: Client pins TLS connection to a specific Connector certificate digest (obtained from Controller) — prevents MITM even if CA is compromised
- **Asymmetric encryption** used for key exchange; symmetric encryption used for data transport (standard TLS pattern)
- **Controller-signed tokens**: time-bound tokens issued by Controller authorize Client-to-Connector connections; Connector verifies token was signed by its own Controller
- **Relay opacity**: Relays forward encrypted packets but cannot decrypt content — encryption is established between Client and Connector, not Client and Relay
- **No inbound ports**: encryption scheme works entirely over outbound connections

## Prerequisites
- Familiarity with TLS/HTTPS concepts helpful but not required — the doc explains from first principles

## Step-by-Step
Not applicable — reference/explainer page.

## Configuration Values
None — encryption is built-in and not configurable.

## Gotchas
- The Relay cannot decrypt traffic — this is by design, not a limitation
- Certificate pinning means a Client must get the current Connector cert digest from the Controller before connecting — stale or revoked Connectors will fail auth
- Time-bound tokens mean clock skew between Client and Controller can cause auth failures

## Related Docs
- `/docs/how-twingate-works` — architecture overview with component roles
- `/docs/client-connection-flow` — step-by-step token and TLS tunnel establishment
- `/docs/understanding-relays` — Relay's role in the connection
