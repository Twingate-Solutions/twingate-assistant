# MongoDB Access with Twingate

## Summary
Twingate secures access to MongoDB Atlas and self-hosted MongoDB by routing traffic through Connectors and enforcing network access controls. Atlas deployments require adding Connector public IPs to Atlas IP Access Lists; self-hosted deployments use firewall rules or `bindIp` configuration. Both database and Atlas Admin Console access can be secured.

## Key Information
- Atlas uses TLS on TCP port **27017** by default; DNS requires UDP port **53**
- Atlas Admin Console (`cloud.mongodb.com`) IP access lists are configured at the **organization level**, separate from project-level database access lists
- PrivateLink (AWS/Azure) and Private Service Connect (GCP) eliminate need for public IP allowlisting in Atlas
- Two connection string formats have different network requirements: `mongodb+srv://` (needs DNS/SRV) vs `mongodb://` (direct host connection)

## Prerequisites
- Twingate Remote Network created with one or more Connectors deployed
- Connectors placed inside same network as database (self-hosted) or secure egress location (Atlas)
- MongoDB Atlas project/cluster or self-hosted MongoDB server

## Step-by-Step

### MongoDB Atlas: Database Access
1. Create Twingate Resource for cluster host (e.g., `*.mongodb.net`), TCP port 27017, UDP port 53
2. Note Connector public IP addresses
3. In Atlas console → **Network Access** → **Add IP Address** → add each Connector public IP
4. Connect: `mongosh "mongodb+srv://cluster0.abc123.mongodb.net/mydatabase" --username <user> --password <pass>`

### MongoDB Atlas: Admin Console Access
1. In Atlas → **Organization → Settings**, enable IP Access List for Atlas UI (may require MongoDB Support)
2. Create Twingate Resource for `cloud.mongodb.com`, port 443, same Remote Network as database Connectors
3. Add Connector public IPs to **Organization → Settings → IP Access List**
4. Verify: run Twingate Client, access `https://cloud.mongodb.com`

### Self-Hosted MongoDB
1. Create Twingate Resource with server IP/DNS name, port 27017
2. Restrict inbound firewall to Connector **private IP** only
3. Optionally configure `net.bindIp` in `mongod.conf` to limit listening interfaces
4. Connect via `mongosh` through Twingate Client

## Configuration Values
| Parameter | Value |
|-----------|-------|
| MongoDB TCP port | `27017` |
| DNS port | UDP `53` |
| Atlas UI port | `443` |
| Atlas UI hostname | `cloud.mongodb.com` |
| Atlas IP Access List scope | Organization-level (UI) / Project-level (DB) |

## Gotchas
- **Use public IPs** for Atlas IP Access List; use **private IPs** for self-hosted firewall rules
- `mongodb+srv://` requires DNS resolution — Twingate Resource must allow port 53, not just 27017
- Mismatches between connection string type and Resource definition are a common failure cause
- Atlas UI IP access lists must be explicitly enabled by MongoDB Support if not visible
- SRV-based discovery may resolve to multiple cluster node hostnames — ensure all are reachable

## Troubleshooting
| Symptom | Cause |
|---------|-------|
| Connection refused | Connector IP not in Atlas allowlist or firewall blocking |
| Auth error | Wrong credentials or missing TLS |
| DNS Failed (Activity log) | DNS routing/resolution issue |
| Connection Failed (Activity log) | DNS OK but firewall/IP allowlist blocking |
| No Activity | Client not running, Resource missing, or conflicting VPN |

## Related Docs
- [MongoDB Private Endpoint Connections](https://www.mongodb.com/docs/atlas/security-private-endpoint/)
- [MongoDB Connection String Reference](https://www.mongodb.com/docs/manual/reference/connection-string/)
- Twingate: Redis Access Guide, Snowflake Access Guide, SaaS App Gating Guide, Connector Best Practices