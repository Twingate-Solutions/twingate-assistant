## Quick Start

Three-step walkthrough to get Twingate operational: create a Remote Network, deploy a Connector, and install the Client. Resources must be added to a Group before users can access them.

**Key Information:**
- Remote Network → Resource → Connector → Client is the setup sequence
- A Resource must be added to at least one Group to be accessible -- creating it alone is not enough
- Connector deployment options vary by environment (Docker, native Linux service, etc.)
- Client download: get.twingate.com
- P2P connections are recommended for bandwidth efficiency and Fair Use Policy compliance

**Prerequisites:**
- Twingate account (free tier available)
- Permissions to deploy Docker or native Linux service on the target Remote Network host

**Step-by-Step:**
1. In Admin Console, click Network → Add next to Remote Networks → select location → name and create
2. Within the Remote Network, click Add Resource → fill in address and label → click Add Resource
3. Assign the Resource to a Group (required; "Everyone" is the default)
4. Click Deploy Connector → select deployment method → run generated script on Connector host
5. Monitor Connector status: both Controller and Relay connections must turn green
6. Visit get.twingate.com, install Client, sign in → access the Resource

**Gotchas:**
- Connector must be on a host that can route to the Resources it serves -- network reachability is not automatic
- A Resource with no Group assigned is inaccessible to all users, even admins

**Related Docs:**
- /docs/remote-networks -- Remote Network configuration details
- /docs/resources -- Resource address formats and options
- /docs/connector -- Connector deployment options
- /docs/local-peer-to-peer-best-practices -- P2P configuration
