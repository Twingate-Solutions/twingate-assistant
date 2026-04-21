## Remotely Accessing a Coworker's Development Server

Use case guide for sharing a developer's personal dev server (on a home or office network) with specific coworkers using Twingate. The developer installs a Connector on their dev server and adds it as a Twingate Resource; coworkers with explicit access can connect without any port forwarding, VPN server, or router changes on the developer's home network.

**Key Information**
- The developer deploys the Connector on the dev server itself (or on the same LAN)
- The dev server is added as a Twingate Resource and access granted only to named coworkers or a specific Group
- No router ports opened, no VPN server needed, no changes to the home network
- Access is narrowly scoped: only the dev server is exposed via Twingate, not the entire home network
- Works whether the dev server is in an office, home, or rented datacenter

**Prerequisites**
- Developer has a Twingate account and the dev server has Docker/Linux available for the Connector
- Coworkers have Twingate Client installed and are added as users in the same Twingate account

**Step-by-Step**
1. Developer: create a Remote Network (e.g. "Dev Server at Home") in Twingate Admin Console
2. Deploy Connector on the dev server (Docker or Linux systemd install)
3. Add the dev server as a Twingate Resource (IP or hostname, specific port if needed)
4. Grant access to the Resource for specific coworkers (individual users or a Group)
5. Coworkers: install Twingate Client, sign in, connect -- the dev server resource appears in their client

**Gotchas**
- If the developer's home internet goes down or the Connector stops, coworkers lose access -- no HA for home Connectors
- Access control is at the Twingate Group/Resource level; the dev server's own SSH/auth controls still apply on top

**Related Docs**
- /docs/connector-deployment
- /docs/resources
- /docs/groups
