# Connector & Client Registration

## Page Title
Connector & Client Registration

## Summary
Connectors and Clients must register with the Twingate Controller before encrypted traffic can flow to Remote network Resources. Connectors use pre-generated deployment tokens; Clients use identity provider authentication via OpenID Connect. Both receive signed, time-expiring ACLs and Relay routing information from the Controller.

## Key Information
- Connector tokens are **one-time use only** — cannot be reused
- Admin must re-authenticate before receiving Connector setup command
- Connector operates headless (Docker container) behind firewall — no interactive auth
- Client token expiry is **inherited from the identity provider's token expiry** — Controller does not set its own expiry
- Connector periodically reports connected Relays and its TLS certificate digest to Controller (enables TLS certificate pinning for Client connections)
- Relay never sees TLS certificate pinning information — only Controller and Client

## Prerequisites
- Admin console access (admin user role required for Connector deployment)
- Configured identity provider (IdP) or social identity for Client authentication
- Docker environment for Connector deployment

## Connector Registration Flow
1. Connector starts with two auth tokens embedded in its startup command
2. Authenticates to Controller using those tokens
3. Controller returns signed, time-expiring message containing:
   - Whitelist ACL (which Resources Connector may forward to)
   - FQDN(s) of Relay(s) to connect to
   - Controller-signed token(s) authorizing Relay connections
4. Connector validates Controller response authenticity
5. Connector connects to Relay(s) using Controller-issued token (token includes hash of Connector ID — no name/location/address leaked)
6. Connector sends periodic heartbeats + reports: active Relay connections, current TLS certificate digest

## Client Registration Flow
1. Client connects to Controller to initiate auth request
2. Controller returns IdP URI (configured IdP or social identity)
3. User authenticates with IdP → receives redirect to Controller endpoint with time-expiring access token (standard OpenID Connect)
4. Controller verifies user's email matches an active configured user
5. Controller issues:
   - Tokens expiring within IdP-provided expiration period
   - Signed whitelist ACL (Resources user can access + which Connector serves each Resource)
6. Client listens for network connections matching ACL Resource addresses → triggers Client Connection Flow

## Configuration Values
| Item | Details |
|------|---------|
| Connector tokens | Two tokens, auto-generated per Connector, single-use |
| Token expiry | Inherited from IdP session expiry (not configurable in Twingate) |
| Connector transport | Docker container, outbound connections only |

## Gotchas
- Connector tokens **cannot be reused** — if lost, a new Connector must be created
- Controller tokens for Clients expire exactly when the IdP token expires — reauthentication requires going back to IdP
- Relay is explicitly **not** party to TLS certificate pinning information
- Connector ACL acts as a **second enforcement layer** — Connector independently validates allowed Resources regardless of Client ACL

## Related Docs
- Connector Deployment
- Client Connection Flow
- OpenID Authentication
- Admin Console / Admin User documentation