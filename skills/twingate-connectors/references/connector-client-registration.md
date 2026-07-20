# Connector & Client Registration

## Page Title
Connector & Client Registration

## Summary
Connectors and Clients must register with the Twingate Controller before encrypted traffic can flow to Resources. Connectors use pre-generated deployment tokens; Clients use identity provider authentication via OpenID Connect. Both receive signed ACLs and Relay connection details upon successful registration.

## Key Information

**Connector Registration:**
- Only admin users can deploy Connectors via Admin console
- Each Connector gets two unique, non-reusable authentication tokens embedded in its startup command
- Admin must re-authenticate before receiving the setup command (additional security gate)
- Upon successful auth, Controller returns a signed, time-expiring message containing:
  - Whitelist ACL (Resources the Connector may forward to)
  - FQDN(s) of one or more Relays
  - Signed tokens authorizing Connector→Relay connection
- Connector validates Controller response authenticity before connecting to Relays
- Relay validates token was signed by its associated Controller; token includes hash of Connector ID (no name/location/address leaked)
- Connector periodically reports to Controller:
  - Connected Relay set (for redundancy/availability tracking)
  - Digest of its current TLS certificate (enables certificate pinning for Clients)
- Heartbeat signal sent continuously to Controller

**Client Registration:**
- Triggered after end-user authenticates with configured IdP or social identity
- Follows standard OpenID Authentication flow
- Controller verifies user email matches an active, configured user in the network
- Controller issues:
  - Tokens expiring within the IdP-provided expiration period (honors IdP token expiry policy)
  - Signed whitelist ACL specifying accessible Resources and which Connector serves each
- After registration, Client listens for network connections matching Resource addresses in ACL

## Prerequisites
- Admin console access (for Connector deployment)
- Configured identity provider or social identity for Client authentication
- Active user account with verified email in Twingate network

## Step-by-Step

**Connector:**
1. Admin deploys Connector via Admin console (re-auth required)
2. Connector starts, authenticates to Controller with embedded tokens
3. Controller responds with signed message (ACL, Relay FQDNs, Relay auth tokens)
4. Connector validates Controller response
5. Connector connects to Relay(s) using Controller-issued tokens
6. Connector begins periodic reporting + heartbeat to Controller

**Client:**
1. Client contacts Controller to initiate auth
2. Controller returns IdP URI
3. User authenticates with IdP; receives redirect with time-expiring access token
4. Controller verifies user identity against active users
5. Controller issues scoped tokens + signed Resource ACL
6. Client begins intercepting matching Resource connection requests

## Gotchas
- Connector tokens are **single-use and non-reusable**; losing them requires generating new ones
- Client token expiry is **controlled by the IdP**, not Twingate; re-auth requires going back to IdP
- Relay never sees TLS certificate pinning information — that exchange is strictly Controller↔Client
- Connector ACL is enforced as a **second check** (Connector independently validates Client connections)

## Related Docs
- Connector Deployment
- Client Connection Flow
- OpenID Authentication
- Admin Console / Admin Users