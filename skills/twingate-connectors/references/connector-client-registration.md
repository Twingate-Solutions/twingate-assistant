# Connector & Client Registration

## Page Title
Connector & Client Registration

## Summary
Connectors and Clients must register with the Twingate Controller before encrypted traffic can flow to Remote network Resources. Connectors use pre-generated deployment tokens; Clients use identity provider (IdP) authentication via OpenID Connect. Both receive signed ACLs and Relay connection details from the Controller upon successful registration.

## Key Information

**Connector Registration:**
- Deployed only by admin users via Admin console
- Uses two unique, single-use authentication tokens embedded in the deployment command
- Admin must re-authenticate before receiving the setup command
- Upon startup, Connector receives from Controller:
  - Signed, time-expiring response
  - Whitelist ACL (Resources the Connector may forward to)
  - FQDN(s) of one or more Relays
  - Controller-signed tokens authorizing Relay connections
- Connector validates Controller response authenticity before connecting to Relays
- Relay authorization token includes a hash of Connector ID (no name/location/network address leaked)
- Connector periodically reports to Controller:
  - Connected Relay set (enables Client routing in redundancy scenarios)
  - Current TLS certificate digest (enables certificate pinning for direct Client→Connector TLS connections)
- Heartbeat signal maintained to Controller continuously

**Client Registration:**
- Triggered after end-user authenticates with configured IdP or social identity
- Follows standard OpenID Connect flow
- Controller verifies user's email matches an active, configured user
- Upon successful auth, Controller issues:
  - Tokens expiring within the IdP-provided expiration period (Controller does not extend or shorten)
  - Signed whitelist ACL mapping Resource addresses → authorized Connectors
- Client listens for network connections matching ACL Resource addresses; matches trigger the Client Connection Flow

## Prerequisites
- Admin user access to deploy Connectors
- Configured identity provider (or social identity) for Client authentication
- Active, configured users in the Twingate network matching verified email addresses

## Configuration Values
- **Connector tokens**: Two unique tokens per Connector, embedded in deployment command (generated per-Connector, non-reusable)
- **Token expiry**: Tied to IdP-issued token expiration; renewal requires IdP re-authentication

## Gotchas
- Connector tokens are single-use and Connector-specific; they cannot be reused or shared
- Client token lifetime is strictly bound to IdP token expiry — Twingate cannot override this policy
- The Relay never receives TLS certificate digest information — only Controller and Client handle certificate pinning
- Users must exist as active/configured in Twingate even if IdP authentication succeeds; IdP auth alone is insufficient

## Related Docs
- Connector Deployment
- Client Connection Flow
- OpenID Authentication
- Admin Console / Admin Users
- Relays and Controllers (architecture)