# Connector & Client Registration

## Page Title
Connector & Client Registration

## Summary
Connectors and Clients must register with the Twingate Controller before encrypted traffic can flow to Resources. Connectors use pre-generated tokens for headless authentication; Clients use IdP-based OAuth/OpenID Connect flows. Both receive signed ACLs and Relay information from the Controller upon successful registration.

## Key Information

**Connector Registration:**
- Only admin users can deploy Connectors via Admin console
- Two unique, single-use tokens are generated per Connector at deployment time
- Admin must re-authenticate before receiving the setup command
- Controller responds with: ACL whitelist, Relay FQDN(s), and signed tokens authorizing Relay connections
- Connector validates Controller response authenticity before connecting to Relays
- Relay tokens include a hash of Connector ID (no name/location/network address leaked)
- Connector periodically reports to Controller: connected Relay set + current TLS certificate digest (enables certificate pinning for Client→Connector connections)
- Heartbeat signal sent ongoing for redundancy/availability tracking

**Client Registration:**
- Triggered after end-user authenticates with IdP or social identity provider
- Follows standard OpenID Connect flow
- Controller verifies user email matches an active, configured user in the Twingate network
- Controller issues tokens scoped to the IdP's expiration period — token renewal requires re-authentication with IdP
- Client receives signed ACL specifying accessible Resources and which Connector serves each Resource
- After registration, Client intercepts network connections matching ACL Resource addresses

## Prerequisites
- Admin role required to deploy Connectors
- Identity provider configured in Twingate network (or social identity enabled)
- Users must exist as active, configured accounts in Twingate

## Step-by-Step: Connector Registration
1. Admin deploys Connector via Admin console (triggers re-authentication)
2. Connector starts and presents two auth tokens to Controller
3. Controller validates tokens → returns signed message with ACL, Relay FQDNs, Relay auth tokens
4. Connector validates Controller response signature
5. Connector connects to Relay(s) using Controller-issued tokens
6. Relay validates token was signed by its associated Controller
7. Connector begins periodic reporting (Relay connections + cert digest) and heartbeat

## Step-by-Step: Client Registration
1. Client contacts Controller to initiate auth
2. Controller returns IdP URI or social login URI
3. User authenticates with IdP → redirect to Controller with time-expiring access token
4. Controller validates token and matches user to active account
5. Controller issues scoped tokens (expiry inherited from IdP) + signed Resource ACL
6. Client begins intercepting connections matching ACL addresses → triggers Client Connection Flow

## Configuration Values
- Connector startup command contains two unique authentication tokens (generated per Connector, non-reusable)
- Token expiry: inherited from IdP session expiry for Clients; time-expiring for Connector Controller messages

## Gotchas
- Connector auth tokens **cannot be reused** — generating new tokens requires creating a new Connector deployment
- Client token expiry is controlled by the IdP, not Twingate — changing session policy must be done at the IdP level
- Relay never receives TLS certificate digest information (Client↔Connector TLS is end-to-end)

## Related Docs
- [Connector Deployment](https://www.twingate.com/docs/connector)
- Client Connection Flow (referenced as next topic)
- OpenID Authentication flow