## Cloaking strongDM with Twingate

Removes the publicly exposed TCP port required by strongDM gateways by routing strongDM traffic through Twingate. The strongDM gateway's advertised host is changed to its internal IP/hostname, which is added as a private Twingate Resource. No inbound firewall ports need to be open.

**Key Information**
- strongDM default proxy port: 5000 (can be restricted per Resource in Twingate)
- The Connector must be on the same private subnet as the strongDM gateway
- Change strongDM's "advertised host" in the strongDM Admin UI to the internal hostname or IP address
- After cloaking, the gateway has no publicly resolvable hostname or open inbound ports

**Step-by-Step**
1. Deploy a Twingate Connector on the same private subnet as the strongDM gateway
2. In Twingate Admin Console, add the strongDM gateway's internal hostname or IP as a Resource; restrict to port 5000 (or the configured proxy port)
3. In strongDM Admin UI, change the gateway's "advertised host" to the internal hostname or IP

**Testing**
- Verify access is blocked when Twingate Client is not connected
- Verify access works when Twingate Client is connected

**Related Docs**
- /docs/cloak-your-bastion-server
- /docs/resources
- /docs/connector-placement-best-practices
