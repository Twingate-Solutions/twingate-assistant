# MongoDB Access with Twingate

## Summary
Twingate routes traffic securely to MongoDB Atlas (managed) or self-hosted MongoDB instances while enforcing network access controls. For Atlas, Connector public IPs are allowlisted; for self-hosted, firewall rules restrict access to the Connector's private IP. Admin console access to `cloud.mongodb.com` can also be restricted via Twingate.

## Key Information
- MongoDB Atlas uses TLS on TCP port **27017** by default; DNS requires UDP port **53**
- Atlas IP Access List controls which IPs can connect to clusters — Connector public IPs must be added
- Atlas UI IP Access List (org-level) is separate from project/database IP lists; must be enabled via MongoDB Support
- PrivateLink (AWS/Azure) or Private Service Connect (GCP) eliminates need for public IP allowlisting in Atlas
- Self-hosted: use Connector **private IP** in firewall rules; use public IP only when required

## Prerequisites
- Twingate Remote Network created with Connector(s) deployed
- Connectors placed inside same network as database (self-hosted) or in secure egress location (Atlas)
- MongoDB Atlas project/cluster or self-hosted MongoDB server
- Public IP of each Connector (found in Admin Console → Remote Network → Connectors → Public IP)

## Step-by-Step

### Atlas Database Access
1. Create Twingate Resource for cluster hostname (e.g., `*.mongodb.net`), TCP port 27017, UDP port 53
2. In Atlas → Network Access, add each Connector's **public IP** to the IP Access List
3. Connect via `mongosh` with Twingate Client running

### Atlas Admin Console Access
1. In Atlas Organization → Settings, enable **IP Access List for the Atlas UI** (contact MongoDB Support if not visible)
2. Create Twingate Resource for `cloud.mongodb.com`, port 443, using same Remote Network
3. Add Connector public IPs to Organization → Settings → IP Access List
4. Verify access via Twingate Client

### Self-Hosted MongoDB
1. Create Twingate Resource with MongoDB server IP/hostname, port 27017
2. Restrict server firewall to allow inbound only from Connector's **private IP**, or configure `net.bindIp` in `mongod.conf`
3. Connect via `mongosh` through Twingate Client

## Configuration Values
| Parameter | Value |
|-----------|-------|
| MongoDB default port | TCP 27017 |
| DNS port | UDP 53 |
| Atlas UI resource | `cloud.mongodb.com:443` |
| Atlas connection (SRV) | `mongodb+srv://` |
| Atlas connection (direct) | `mongodb://` with `--port 27017` |

## Gotchas
- `mongodb+srv://` requires DNS SRV resolution — Twingate Resource must allow port 53, not just 27017
- `mongodb://` requires each hostname/IP in the URI to be reachable from the Connector
- Atlas UI IP Access List is **org-level** and separate from per-project database IP lists
- Atlas UI IP Access List must be explicitly enabled by contacting MongoDB Support
- Connector **public** IP required for Atlas allowlist; **private** IP preferred for self-hosted firewall rules

## Troubleshooting
- **Connection refused**: Connector IP not in Atlas Access List or firewall/bindIp blocking
- **DNS Failed** (Recent Activity): Connector cannot resolve hostname
- **Connection Failed** (Recent Activity): DNS resolved but TCP connection blocked
- **No Activity**: Client not running, Resource not assigned, or conflicting VPN

## Related Docs
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)
- [MongoDB Private Endpoint Connections](https://www.mongodb.com/docs/atlas/security-private-endpoint/)
- [MongoDB Connection String Docs](https://www.mongodb.com/docs/manual/reference/connection-string/)
- Twingate: Redis Access Guide, Snowflake Access Guide, SaaS App Gating Guide