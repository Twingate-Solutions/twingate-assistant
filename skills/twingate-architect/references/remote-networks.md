## Remote Networks

Remote Networks are logical containers that group Resources together. All Connectors within a Remote Network must be able to reach all Resources defined in that network. At least one active Connector is required before Resources become accessible.

**Key Information:**
- A Remote Network corresponds to a physical network, VPC, or logical access boundary
- Connectors within the same Remote Network provide interchangeable, load-balanced access
- At least one Connector required; two or more recommended for HA and load balancing
- Load balancing across Connectors is automatic -- no manual configuration needed
- A single Connector typically handles traffic for hundreds of users depending on usage patterns
- All Connectors in the same Remote Network must share the same network routing and access rules

**Prerequisites:**
- Twingate account
- At least one host reachable to the target Resources where a Connector can be deployed

**Gotchas:**
- If all Connectors in a Remote Network go offline, all Resources in that network become inaccessible
- Connectors within the same Remote Network are assumed interchangeable -- routing rule divergence between them causes inconsistent behavior
- A Remote Network with Resources but no active Connector silently denies all access

**Related Docs:**
- /docs/connector -- Connector deployment and management
- /docs/resources -- Defining Resources within Remote Networks
- /docs/remote-network-best-practices -- HA and operational guidelines
