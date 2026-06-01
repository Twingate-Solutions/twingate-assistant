# Connector & Client Registration

## Page Title
Connector & Client Registration

## Summary
Connectors and Clients must register with the Twingate Controller before network traffic can flow. Connectors use pre-generated tokens from the Admin console; Clients use OpenID Connect via a configured identity provider. Both receive signed ACLs and Relay connection details upon successful registration.

## Key Information

### Connector Registration
- Only admin users can deploy Connectors via Admin console
- Two unique, non-reusable authentication tokens are generated per Connector and embedded in the startup/deployment command
- Admin must re-authenticate before receiving the setup command (additional security step)
- Connectors run headless in Docker containers behind the Remote network firewall

**Registration sequence:**
1. Connector authenticates to Controller with startup tokens
2. Controller returns signed, time-expiring message containing:
   - Whitelist ACL (Resources the Connector may forward to)
   - FQDN(s) of one or more Relays
   - Controller-signed tokens authorizing Relay connections
3. Connector validates Controller response authenticity
4. Connector connects to Relay(s) using Controller-issued tokens; Relay validates token was signed by its associated Controller (token includes hash of Connector ID—no name/location/IP exposed)
5. Connector periodically reports to Controller:
   - Connected Relay set (for Client routing)
   - TLS certificate digest (enables certificate pinning for direct Client→Connector connections)
6. Connector sends ongoing heartbeat for redundancy/availability signaling

### Client Registration
- Triggered after successful user authentication with IdP or social identity
- Follows standard OpenID Connect flow

**Registration sequence:**
1. Client contacts Controller to initiate auth request
2. Controller returns IdP URI or social sign-in page
3. User authenticates; receives redirect to Controller endpoint with time-expiring access token
4. Controller verifies user email matches an active, configured user
5. On match, Controller issues:
   - Tokens expiring within the IdP's original token expiration period (no extension—reauthentication policy follows IdP policy)
   - Signed whitelist ACL specifying accessible Resources (by address) and which Connector serves each
6. Client listens for network connections matching ACL Resource addresses and initiates Client Connection Flow on match

## Prerequisites
- Admin console access (for Connector deployment)
- Configured identity provider or social identity (for Client registration)
- Active, configured user account in Twingate network

## Configuration Values
- Connector startup command contains two embedded auth tokens (generated at deploy time, single-use)
- Token expiration follows IdP-issued expiration period exactly

## Gotchas
- Connector tokens cannot be reused—if lost, a new Connector must be generated
- Relay never receives Client TLS certificate digest; only the Connector and Controller handle that data
- Controller token expiry is bound to IdP token expiry—renewing requires IdP reauthentication; cannot be extended independently

## Related Docs
- [Connector Deployment](https://www.twingate.com/docs/connector)
- Client Connection Flow (referenced in page, follow-on doc)
- OpenID Authentication flow