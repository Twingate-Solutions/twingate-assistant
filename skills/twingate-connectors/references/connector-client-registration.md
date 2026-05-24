# Connector & Client Registration

## Summary
Connectors and Clients must register with the Twingate Controller before encrypted traffic can flow to Remote network Resources. Connectors use pre-generated tokens from the Admin console; Clients use OpenID Connect flow via a configured identity provider. Both processes result in signed ACLs and Relay connection details issued by the Controller.

## Key Information

**Connector Registration:**
- Deployed only by admin users via Admin console; runs in headless Docker containers
- Uses two unique, non-reusable authentication tokens embedded in the startup command
- Admin must re-authenticate before receiving the setup command (additional security step)
- On startup, Connector receives: whitelist ACL, Relay FQDN(s), and Controller-signed tokens
- Periodically reports to Controller: connected Relay set + current TLS certificate digest (enables certificate pinning for Client→Connector connections)
- Sends ongoing heartbeat to Controller for availability/redundancy tracking
- Relay never receives TLS certificate digest — only shared between Connector and Controller

**Client Registration:**
- Triggered after end-user authenticates with configured IdP or social identity
- Uses standard OpenID Connect (OIDC) flow; redirect includes time-expiring access token
- Controller verifies user's email matches an active configured user
- On success, Client receives: Controller tokens (expiry tied to IdP token expiry) + signed whitelist ACL
- ACL specifies accessible Resource addresses and which Connector serves each Resource
- Client listens for connections matching ACL Resource addresses, then initiates Client Connection Flow

## Prerequisites
- Admin console access (for Connector deployment)
- Configured identity provider or social identity (for Client registration)
- Active, configured user account in Twingate network (email must match)

## Registration Flow Summary

**Connector:**
1. Authenticate to Controller with startup tokens
2. Receive signed message: ACL + Relay FQDNs + Relay auth tokens
3. Validate Controller response authenticity
4. Connect to Relay(s) using Controller-issued tokens
5. Periodically report Relay connections + cert digest to Controller

**Client:**
1. Connect to Controller to initiate auth request
2. Receive IdP/social login URI
3. Authenticate with IdP; receive redirect with access token
4. Controller validates user identity against configured users
5. Receive Controller tokens + signed ACL
6. Listen for connections matching ACL Resources

## Gotchas
- Connector tokens are **single-use only** — cannot be reused if deployment fails
- Client token expiry is **controlled by IdP token expiry**, not Twingate — re-auth requires going back through the IdP
- Connector ID hash is included in Relay auth tokens to prevent leaking Connector name/location/network address
- Connectors act as a **second enforcement layer** on connections — only forward to ACL-whitelisted Resources

## Related Docs
- Connector Deployment
- Client Connection Flow
- OpenID Authentication
- Admin Console / Admin Users