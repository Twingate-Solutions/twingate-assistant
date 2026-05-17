# MongoDB Access with Twingate

## Summary
Twingate secures access to MongoDB Atlas (managed) and self-hosted MongoDB by routing traffic through Connectors and enforcing network access controls. Atlas deployments require adding Connector public IPs to Atlas IP Access Lists; self-hosted deployments use firewall rules or `bindIp` restrictions.

## Key Information
- Atlas uses TLS on TCP port **27017** by default; DNS requires UDP port **53**
- Atlas UI (`cloud.mongodb.com`) IP Access Lists are separate from database project IP allow lists and must be enabled at the **organization** level via MongoDB Support
- PrivateLink (AWS/Azure) and Private Service Connect (GCP) eliminate the need for public IP allowlisting in Atlas
- Two connection string formats have different network requirements (see below)

## Prerequisites
- Twingate Remote Network and at least one deployed Connector
- MongoDB Atlas project/cluster or self-hosted MongoDB instance
- Connector placed inside same network as DB (self-hosted) or secure egress location (Atlas)

## Step-by-Step

### Atlas: Securing Databases
1. Create Twingate Resource for `*.mongodb.net`, TCP port `27017`, UDP port `53`
2. Note Connector **public** IP addresses
3. In Atlas → **Network Access** → **Add IP Address**: add each Connector public IP
4. Connect: `mongosh "mongodb+srv://cluster0.abc123.mongodb.net/mydatabase" --username <u> --password <p>`

### Atlas: Securing Admin Console
1. In Atlas → **Organization → Settings**, request IP Access List for Atlas UI from MongoDB Support if not visible
2. Create Twingate Resource: `cloud.mongodb.com`, port `443`, same Remote Network as DB Connectors
3. Add Connector public IPs to **Organization → Settings → IP Access List**
4. Verify: run Twingate Client, access `https://cloud.mongodb.com`

### Self-Hosted MongoDB
1. Create Twingate Resource with server IP/DNS, port `27017`
2. Restrict firewall to allow inbound only from Connector **private** IP, OR set `net.bindIp` in `mongod.conf`
3. Connect via `mongosh` with Twingate Client running

## Configuration Values
| Setting | Value |
|---|---|
| MongoDB TCP port | `27017` |
| DNS port | UDP `53` |
| Atlas UI | `cloud.mongodb.com:443` |
| Atlas wildcard resource | `*.mongodb.net` |
| Self-hosted config file | `mongod.conf` → `net.bindIp` |

## Gotchas
- **`mongodb+srv://` vs `mongodb://`**: SRV format requires DNS resolution (port 53) in addition to TCP 27017; direct format requires each hostname to be explicitly reachable — mismatches are a common failure cause
- Atlas UI IP Access Lists are **org-level**, not project-level; requires MongoDB Support to enable
- Use Connector **private** IP for self-hosted firewall rules; use **public** IP only when required (e.g., Atlas IP Access List)
- With PrivateLink/Private Service Connect, public IP allowlisting in Atlas is unnecessary
- Other VPNs running alongside Twingate Client can cause "No Activity" in logs

## Troubleshooting via Twingate Admin Console → Recent Activity
- **DNS Failed**: Connector cannot resolve hostname
- **Connection Failed**: DNS resolved but DB unreachable (firewall/IP allow list issue)
- **No Activity**: Client not running, Resource missing, or conflicting VPN

## Related Docs
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)
- [SaaS App Gating Guide](https://www.twingate.com/docs/saas-app-gating)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [MongoDB Connection String Docs](https://www.mongodb.com/docs/manual/reference/connection-string/)
- [MongoDB Private Endpoint Connections](https://www.mongodb.com/docs/atlas/security-private-endpoint/)