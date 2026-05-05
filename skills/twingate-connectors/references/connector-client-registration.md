# Connector & Client Registration

## Page Title
Connector & Client Registration

## Summary
Connectors and Clients must register with the Twingate Controller before encrypted traffic can flow to Remote network Resources. Connectors use pre-generated deploy tokens; Clients use identity provider authentication via OpenID Connect. Both receive signed ACLs and Relay connection info from the Controller upon successful registration.

## Key Information

**Connector Registration:**
- Only admin users can deploy Connectors via Admin console
- Two unique, single-use authentication tokens are embedded in each Connector's startup command
- Admin must re-authenticate before receiving the setup command
- Upon successful auth, Controller returns a signed, time-expiring message containing:
  - Whitelist ACL (Resources the Connector may forward to)
  - FQDN(s) of one or more Relays
  - Controller-signed tokens authorizing Relay connections
- Connector validates Controller response authenticity before connecting to Relays
- Relay tokens include a hash of the Connector's ID (no name/location/network address leaked)
- Connector periodically reports to Controller:
  - Connected Relay set (for Client routing/redundancy)
  - Current TLS certificate digest (enables certificate pinning for direct Client→Connector TLS)
- Connector sends ongoing heartbeat to Controller

**Client Registration:**
- Triggered after end-user authenticates with configured IdP or social identity
- Follows standard OpenID Connect flow
- Controller verifies user's verified email matches an active, configured user
- Upon match, Controller issues:
  - Tokens expiring within the IdP-issued token expiration period (no extension)
  - Signed whitelist ACL listing accessible Resources and which Connector serves each
- Client listens for network connections matching ACL Resource addresses; matching connections trigger the Client Connection Flow

## Prerequisites
- Admin account to deploy Connectors
- Configured identity provider (or social identity) for Client auth
- Active/configured user records in Twingate network

## Gotchas
- Connector tokens are **single-use and non-reusable** — regenerate if deployment fails
- Client token expiration is **bound to IdP token expiry** — Controller does not extend it; reauthentication must go through the IdP
- The Relay never sees Client TLS certificate pinning data — only the Connector and Controller handle this
- Connector ACL acts as a **second enforcement layer** independent of Client-side ACL checks
- Admin re-authentication is required before receiving Connector setup commands (additional security gate)

## Configuration Values
- No direct env vars or API params documented on this page
- Tokens are auto-generated per-Connector at deploy time via Admin console

## Related Docs
- [Connector Deployment](https://www.twingate.com/docs/connector)
- [Client Connection Flow](https://www.twingate.com/docs/client-connection-flow)
- [OpenID Authentication](https://www.twingate.com/docs/openid)
- Admin Users documentation
- Relay/Controller architecture docs