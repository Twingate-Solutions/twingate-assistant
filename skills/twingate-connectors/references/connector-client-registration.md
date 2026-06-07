# Connector & Client Registration

## Page Title
Connector & Client Registration

## Summary
Connectors and Clients must register with the Twingate Controller before encrypted traffic can flow to Resources. Connectors use pre-generated deployment tokens; Clients use OIDC-based identity provider authentication. Both receive signed ACLs and Relay routing information upon successful registration.

## Key Information

**Connector Registration:**
- Deployed only by admin users via Admin console (headless Docker container)
- Uses two unique, single-use authentication tokens embedded in the deployment command
- Admin must re-authenticate before receiving the setup command
- Upon successful auth, Controller returns: whitelist ACL, Relay FQDN(s), and signed Relay authorization tokens
- Connector validates Controller response authenticity before connecting to Relays
- Connector periodically reports to Controller: connected Relay(s) and TLS certificate digest (enables certificate pinning for Client connections)
- Sends ongoing heartbeat to Controller for availability/redundancy tracking

**Client Registration:**
- Triggered after end-user authenticates with configured IdP or social identity
- Uses standard OpenID Connect (OIDC) flow
- Controller verifies user email matches an active, configured user in the Twingate network
- Controller issues tokens that expire per the identity authority's expiration policy — renewal requires re-authentication with the IdP
- Client receives signed whitelist ACL specifying accessible Resources and which Connector serves each

## Prerequisites
- Admin user account (for Connector deployment)
- Configured identity provider or social identity (for Client registration)
- Active user account in Twingate network with verified email address

## Step-by-Step

**Connector:**
1. Admin deploys Connector via Admin console (triggers re-authentication)
2. Connector starts and authenticates to Controller using embedded tokens
3. Controller returns signed message with ACL, Relay FQDNs, and Relay auth tokens
4. Connector validates Controller response
5. Connector connects to Relay(s) using Controller-issued tokens
6. Connector begins reporting heartbeat, connected Relays, and TLS cert digest to Controller

**Client:**
1. Client connects to Controller to initiate auth
2. Controller returns IdP URI
3. User authenticates with IdP; receives redirect with time-expiring access token
4. Controller verifies user identity matches active network user
5. Controller issues scoped tokens and signed whitelist ACL
6. Client listens for connections matching ACL Resource addresses

## Configuration Values
- Connector deployment tokens: auto-generated per Connector, embedded in setup command (not reusable)
- Token expiry: inherited from IdP token expiration for Client sessions

## Gotchas
- Connector tokens are **single-use and Connector-specific** — cannot be reused or shared
- Client token expiry is **controlled by the IdP**, not Twingate — changing expiry requires IdP configuration
- The Relay never has access to TLS certificate digest information (only Controller and Client)
- Connector ID is hashed in Relay tokens — Relay learns nothing about Connector name, location, or network address

## Related Docs
- Connector Deployment
- Client Connection Flow
- OpenID Authentication
- Admin Console (user management)