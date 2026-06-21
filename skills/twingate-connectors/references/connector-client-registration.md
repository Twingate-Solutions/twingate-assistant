# Connector & Client Registration

## Page Title
Connector & Client Registration

## Summary
Connectors and Clients must register with the Twingate Controller before encrypted traffic can flow to Remote network Resources. Connectors use pre-generated deployment tokens; Clients authenticate via a configured identity provider using OpenID Connect. Both receive signed ACLs and Relay connection details from the Controller upon successful registration.

## Key Information

**Connector Registration:**
- Only admin users can deploy Connectors via the Admin console
- Two unique, non-reusable tokens are embedded in the deployment command per Connector
- Admin must re-authenticate before receiving the setup command
- Upon startup, Controller responds with: whitelist ACL, Relay FQDN(s), and signed tokens to authorize Relay connections
- Connector validates Controller response authenticity before connecting to Relay
- Relay authorization token includes a hash of Connector ID (no name/location/address leaked)
- Connector periodically reports to Controller: connected Relay set + current TLS certificate digest (enables certificate pinning for Clients)
- Connector sends ongoing heartbeat to Controller for redundancy/availability tracking

**Client Registration:**
- Triggered after end-user authenticates with IdP or social identity
- Uses standard OpenID Connect flow
- Controller verifies user's email matches an active, configured user in the Twingate network
- Controller issues tokens scoped to the identity provider's expiration period (no independent extension)
- Token renewal requires re-authentication with the identity provider
- Client receives a signed whitelist ACL specifying: accessible Resources (by address) + which Connector serves each Resource
- Client listens for network connections matching ACL Resource addresses after registration

## Prerequisites
- Admin account required to deploy Connectors
- Identity provider (IdP) or social identity configured in Twingate network for Client auth
- Users must exist as active, configured members of the Twingate network

## Configuration Values
- Connector deployment tokens: two tokens per Connector, generated at creation, single-use
- Token expiry: tied to IdP-issued token expiration (Controller does not override)
- ACL content: Resource addresses (Clients) + Resource-to-Connector mapping

## Gotchas
- Connector tokens **cannot be reused** — if lost, a new Connector must be generated
- Admin re-authentication is required before obtaining Connector setup command
- Client token expiry is controlled by the IdP, not Twingate — changing session duration requires IdP-side configuration
- The Relay never receives Client TLS certificate pinning information — this stays between Client and Controller/Connector
- Connectors act as a **second enforcement layer** on top of Client ACLs, independently validating allowed Resources

## Related Docs
- Connector Deployment
- Client Connection Flow
- OpenID Authentication
- Admin Console / Admin Users