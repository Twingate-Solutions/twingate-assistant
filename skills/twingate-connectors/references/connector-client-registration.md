---
source: https://www.twingate.com/docs/connector-client-registration
type: docs
fetched: 2026-08-14
source_version: 82c73b359c6dbd4f4959de9285a151103cb9a8f7453ac0af969d4300f9898651
---

# Connector & Client Registration

## Page Title
Connector & Client Registration

## Summary
Connectors and Clients must register with the Twingate Controller before encrypted traffic can flow to Remote network Resources. Connectors use pre-generated deployment tokens; Clients use IdP-based OpenID authentication. Both receive signed ACLs and Relay routing info from the Controller upon successful registration.

## Key Information

**Connector Registration:**
- Deployed only by admin users via Admin console; runs headless in Docker
- Uses two unique, non-reusable tokens per Connector embedded in the deployment command
- Admin must re-authenticate before receiving the setup command
- Controller responds with: whitelist ACL, Relay FQDN(s), signed Relay authorization tokens
- Connector validates Controller response authenticity before connecting to Relay
- Relay authorization token includes a hash of Connector ID (no name/location/address leaked)
- Connector periodically reports to Controller: connected Relay(s) + current TLS certificate digest (enables certificate pinning for Client→Connector connections)
- Heartbeat signal maintained for redundancy/availability tracking

**Client Registration:**
- Triggered after end-user authenticates with configured IdP or social identity provider
- Follows standard OpenID Connect flow; redirects include time-expiring access token
- Controller verifies user's verified email matches an active, configured user
- Controller issues tokens scoped to the IdP's expiration period — token renewal requires IdP re-authentication
- Controller issues signed whitelist ACL specifying: accessible Resources (by address) + which Connector serves each Resource
- Client monitors local network for connections matching ACL Resource addresses; matching requests trigger the Client Connection Flow

## Prerequisites
- Admin access to Twingate Admin console (for Connector deployment)
- Configured identity provider or social identity for Client authentication
- Active, configured user record in Twingate network matching user's verified email

## Configuration Values
- Connector deployment tokens: two per Connector, generated at deploy time, single-use
- Token expiry: inherits IdP session expiration for Clients
- TLS certificate digest: reported by Connector to Controller for Client-side certificate pinning

## Gotchas
- Connector tokens **cannot be reused** — regenerate if lost or unused
- Client token expiry is controlled by the upstream IdP, not Twingate — changing session duration requires IdP policy changes
- The Relay never receives the Connector's TLS certificate digest; certificate pinning is Controller-mediated
- Connector acts as a **second enforcement point** for ACLs (first is the Controller/Client ACL)

## Related Docs
- [Connector Deployment](#)
- [Admin Users](#)
- [Client Connection Flow](#)
- [OpenID Authentication](https://openid.net/connect/)