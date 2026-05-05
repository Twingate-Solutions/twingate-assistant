## Connector & Client Registration

Technical deep-dive on how Connectors and Clients authenticate and register with the Twingate Controller before any Resource traffic flows.

**Connector Registration Flow:**
1. Admin generates a Connector in the Admin Console (requires re-authentication as a security measure)
2. Connector starts and presents its unique, one-time-use tokens to the Controller
3. Controller validates tokens and responds with a signed, time-expiring message containing:
   - Whitelist ACL of Resources the Connector is allowed to forward to
   - FQDNs of one or more Relays to connect to
   - Signed tokens authorizing connection to those Relays
4. Connector validates the Controller response
5. Connector connects to the Relay(s) using the Controller-signed tokens (Relay validates token was signed by its associated Controller; uses a hash of Connector ID — no name/IP leaked)
6. Connector periodically reports to Controller: which Relays it is connected to, and the digest of its current TLS certificate (enables certificate pinning for Client connections)
7. Connector sends ongoing heartbeat to Controller for availability tracking

**Client Registration Flow:**
1. Client connects to Controller to initiate auth
2. Controller returns URI for the configured IdP (or social identity)
3. User authenticates with the IdP; receives a redirect with a time-expiring access token (standard OpenID flow)
4. Controller verifies user email matches an active configured user
5. If authorized, Controller issues:
   - Tokens that expire within the IdP's token expiry window (Controller does not extend IdP expiry)
   - Signed whitelist ACL listing Resources the user can access and which Connector serves each one
6. Client listens for connections matching Resource addresses in the ACL and initiates the Client Connection Flow on a match

**Related Docs:**
- /docs/client-connection-flow -- What happens after registration when a Resource is accessed
- /docs/how-twingate-works -- Architecture overview
- /docs/understanding-relays -- Relay role in the connection
