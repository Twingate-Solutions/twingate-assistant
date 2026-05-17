# Connector & Client Registration

## Page Title
Connector & Client Registration

## Summary
Connectors and Clients must register with the Twingate Controller before encrypted traffic can flow to Resources. Connectors use pre-generated tokens from the Admin console; Clients use OIDC-based identity provider authentication. Both receive signed ACLs and Relay routing information upon successful registration.

## Key Information

**Connector Registration:**
- Deployed only by admin users via Admin console
- Uses two one-time, non-reusable authentication tokens embedded in the deployment command
- Admin must re-authenticate before receiving the setup command
- Upon successful auth, Controller returns: whitelist ACL, Relay FQDNs, and signed tokens to authorize Relay connections
- Connector validates Controller response authenticity before connecting to Relay
- Relay authorization token includes a hash of Connector ID (no name/location/address leaked)
- Connector periodically reports to Controller: connected Relay(s) and current TLS certificate digest (enables TLS certificate pinning for Clients)
- Connector sends ongoing heartbeat to Controller for availability tracking in redundancy scenarios

**Client Registration:**
- Triggered after end-user authenticates with configured IdP or social identity
- Follows standard OpenID Connect (OIDC) flow
- Controller verifies user's verified email matches an active, configured user
- Upon success, Controller issues: expiring tokens (tied to IdP token expiry) and a signed whitelist ACL
- ACL specifies accessible Resources (by address) and which Connector serves each Resource
- Token renewal requires re-authentication with the IdP — Controller does not extend expiry independently
- Client listens for network connections matching ACL Resource addresses and initiates Client Connection Flow on match

## Prerequisites
- Admin console access (for Connector deployment)
- Configured identity provider or social identity (for Client registration)
- Active, configured user account in Twingate network

## Step-by-Step

**Connector:**
1. Admin re-authenticates in Admin console
2. Admin deploys Connector with generated token pair
3. Connector authenticates to Controller with tokens
4. Controller returns signed message (ACL, Relay FQDNs, Relay auth tokens)
5. Connector validates Controller response
6. Connector connects to Relay(s) using Controller-issued tokens
7. Connector reports Relay connections and TLS cert digest to Controller periodically

**Client:**
1. Client connects to Controller to initiate auth
2. Controller returns IdP URI
3. User authenticates with IdP; receives redirect with time-expiring access token
4. Controller verifies token and matches user to active account
5. Controller issues expiring tokens and signed ACL
6. Client configures local listener for matching Resource addresses

## Gotchas
- Connector tokens are **single-use only** — cannot be reused if deployment fails
- Client token expiry is controlled by the IdP, not Twingate — reauthentication policy must be set at the IdP level
- Relay never sees TLS certificate pinning information; that exchange is Controller↔Connector only
- TLS connections from Clients go **directly to Connector**, not through Relay

## Related Docs
- Connector Deployment
- Client Connection Flow
- OpenID Authentication
- Admin Users documentation