# MongoDB Access with Twingate

## Summary
Twingate secures access to MongoDB Atlas (managed) and self-hosted MongoDB by routing traffic through Connectors and enforcing network access controls. For Atlas, Connector public IPs must be whitelisted in Atlas's IP Access List; for self-hosted, firewall rules restrict access to Connector private IPs.

## Key Information
- MongoDB default port: TCP **27017**; DNS resolution requires UDP **53**
- Two connection string formats with different network requirements: `mongodb+srv://` (DNS SRV-based) vs `mongodb://` (direct host/port)
- Atlas IP Access Lists apply separately to **database access** (project level) and **Admin UI access** (organization level)
- PrivateLink (AWS/Azure) or Private Service Connect (GCP) eliminates need for public IP whitelisting in Atlas

## Prerequisites
- Twingate Remote Network created with Connector(s) deployed
- MongoDB Atlas project/cluster **or** self-hosted MongoDB instance
- Public IP addresses of Connectors (for Atlas IP Access List)
- Private IP addresses of Connectors (for self-hosted firewall rules)

## Step-by-Step

### MongoDB Atlas: Database Access
1. Create Twingate Resource for Atlas cluster hostname (e.g., `*.mongodb.net`), ports TCP 27017 + UDP 53
2. Note Connector public IP addresses
3. In Atlas Console → **Network Access** → **Add IP Address** → add each Connector public IP
4. Connect via `mongosh "mongodb+srv://cluster0.abc123.mongodb.net/mydatabase" --username <user> --password <pass>`

### MongoDB Atlas: Admin UI Access
1. In Atlas **Organization → Settings**, enable **IP Access List for Atlas UI** (contact MongoDB Support if not visible)
2. Create Twingate Resource for `cloud.mongodb.com`, port 443, same Remote Network as database Connectors
3. Add Connector public IPs to Organization-level IP Access List
4. Verify access loads only with Twingate Client running

### Self-Hosted MongoDB
1. Create Twingate Resource with server IP/DNS, port 27017
2. Restrict server firewall to allow inbound only from Connector **private IP** (or configure `net.bindIp` in `mongod.conf`)
3. Connect via `mongosh` with Twingate Client running

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Default MongoDB port | TCP 27017 |
| DNS port | UDP 53 |
| Atlas Admin UI | `cloud.mongodb.com:443` |
| `mongod.conf` binding | `net.bindIp` |

## Gotchas
- `mongodb+srv://` requires DNS (port 53) access in addition to TCP 27017 — Resource must include both
- Atlas database IP Access List and Atlas UI IP Access List are **separate** — both need Connector IPs added
- Use Connector **public** IP for Atlas IP Access List; use Connector **private** IP for self-hosted firewall rules
- Another VPN running alongside Twingate may intercept traffic — check **Recent Activity** for "No Activity" events
- Mismatched connection string type (`srv` vs direct) is a common failure cause

## Troubleshooting via Twingate Admin Console
- **DNS Failed** → Connector cannot resolve hostname
- **Connection Failed** → DNS resolved but database unreachable (firewall/IP list issue)
- **No Activity** → Client not running, Resource not configured, or VPN conflict

## Related Docs
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)
- [MongoDB Private Endpoint Connections](https://www.mongodb.com/docs/atlas/security-private-endpoint/)
- [MongoDB Connection String Reference](https://www.mongodb.com/docs/manual/reference/connection-string/)
- SaaS App Gating Guide (for SSO-based control of Atlas UI)
- Connector Best Practices