## Remotely Access a NAS Device with Twingate

Use case guide for accessing a NAS device remotely without port forwarding or dynamic DNS. A Twingate Connector is deployed on a device in the same local network (or on the NAS itself if supported), the NAS is added as a Resource, and authorized users connect via the Twingate Client using the NAS's private IP address.

**Key Information**
- No port forwarding, no dynamic DNS, no public IP exposure needed
- The NAS is accessed via its private IP address (same as when locally connected)
- Connector can be installed on the NAS itself (Synology supported) or on another device in the same LAN
- Access control via Twingate Groups -- restrict to specific users if needed
- Synology DSM 6.x and DSM 7.x have dedicated Connector deployment guides

**Step-by-Step**
1. Create a Remote Network in Admin Console (e.g. "Home Network")
2. Add the NAS's private IP (e.g. `192.168.1.50`) as a Twingate Resource on that Remote Network
3. Add a Connector to the Remote Network and click Provision
4. Install the Connector on the NAS or another device in the same LAN; verify it goes online
5. Connect with Twingate Client and access the NAS using its private IP address

**Gotchas**
- If the Connector is not on the same LAN as the NAS, the Connector must have L3 routing to reach the NAS IP
- Dynamic ISP IP addresses are irrelevant with Twingate -- the Connector uses outbound connections only

**Related Docs**
- /docs/synology-dsm-6
- /docs/synology-dsm-7
- /docs/connector-deployment
- /docs/resources
