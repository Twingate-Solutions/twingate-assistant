# MongoDB Access with Twingate

## Summary
Twingate secures access to both MongoDB Atlas and self-hosted MongoDB by routing traffic through Connectors and restricting database/admin access to Connector IP addresses. Supports Atlas IP Access Lists, PrivateLink/Private Service Connect, and self-hosted firewall rules.

## Key Information
- Atlas uses TCP port **27017** for connections and UDP port **53** for DNS
- Atlas Admin Console (`cloud.mongodb.com`) IP restrictions are separate from database IP allow lists and must be enabled at the **organization** level
- PrivateLink (AWS/Azure) and Private Service Connect (GCP) eliminate need for public IP allowlisting in Atlas
- Two connection string formats have different requirements: `mongodb+srv://` needs DNS (port 53) + TCP 27017; `mongodb://` needs direct host reachability

## Prerequisites
- Twingate Remote Network with deployed Connector(s)
- MongoDB Atlas project/cluster OR self-hosted MongoDB server
- For Atlas: Connector **public** IP addresses for IP Access List
- For self-hosted: Connector **private** IP address for firewall rules

## Step-by-Step

### Atlas Database Access
1. Create Twingate Resource for `*.mongodb.net`, TCP port 27017, UDP port 53
2. In Atlas → **Network Access**, add each Connector's public IP to IP Access List
3. Connect via `mongosh` with Twingate Client running

### Atlas Admin Console Access
1. In Atlas → **Organization → Settings**, enable "IP Access List for the Atlas UI" (contact MongoDB Support if not visible)
2. Create Twingate Resource for `cloud.mongodb.com`, port 443, same Remote Network as database Connectors
3. Add Connector public IPs to Organization-level IP Access List
4. Verify by accessing `https://cloud.mongodb.com` with Twingate Client active

### Self-Hosted MongoDB
1. Create Twingate Resource with MongoDB server IP/DNS, port 27017
2. Restrict firewall to allow inbound only from Connector **private** IP, OR set `net.bindIp` in `mongod.conf`
3. Connect via `mongosh` through Twingate

## Configuration Values
| Parameter | Value |
|-----------|-------|
| MongoDB TCP port | 27017 |
| DNS port | 53 (UDP) |
| Atlas UI port | 443 (HTTPS) |
| Atlas hostname pattern | `*.mongodb.net` |
| Atlas Admin Console | `cloud.mongodb.com` |
| Self-hosted config file | `mongod.conf` → `net.bindIp` |

## Gotchas
- Atlas UI IP restrictions are **organization-scoped**, not per-project — requires MongoDB Support to enable
- `mongodb+srv://` requires DNS resolution; missing UDP 53 in Resource definition causes failures
- Use **public** Connector IP for Atlas (internet-facing); use **private** Connector IP for self-hosted firewall rules
- PrivateLink/PSC removes need for public IP allowlisting entirely
- Other VPNs running alongside Twingate Client can prevent traffic routing (check Recent Activity for "No Activity")

## Troubleshooting via Recent Activity
- **DNS Failed** → DNS routing/resolution issue (check port 53 in Resource)
- **Connection Failed** → DNS resolved but TCP blocked (check IP allow list or firewall)
- **No Activity** → Client not running, Resource not assigned, or conflicting VPN

## Related Docs
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)
- [MongoDB Private Endpoint Connections](https://www.mongodb.com/docs/atlas/security-private-endpoint/)
- [MongoDB Connection String Reference](https://www.mongodb.com/docs/manual/reference/connection-string/)
- SaaS App Gating Guide (for SSO-based Atlas UI access control)