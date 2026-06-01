# MongoDB Access with Twingate

## Summary
Configure Twingate to secure access to MongoDB Atlas (managed) or self-hosted MongoDB instances. Twingate routes traffic through Connectors, which are allowlisted in MongoDB's network access controls. Covers database access, Atlas Admin Console access, and self-hosted deployments.

## Key Information
- MongoDB Atlas uses IP Access Lists to restrict connections; Connector public IPs must be allowlisted
- Default MongoDB port: TCP 27017; DNS requires UDP 53
- Atlas Admin UI (`cloud.mongodb.com`) has a separate IP Access List at the Organization level (must be enabled by MongoDB Support)
- PrivateLink (AWS/Azure) or Private Service Connect (GCP) enables fully private connectivity without public IP allowlisting
- Self-hosted: use Connector **private IP** in firewall rules; Atlas: use Connector **public IP** in IP Access List

## Prerequisites
- Twingate Remote Network created with Connectors deployed
- Connectors placed inside same network as self-hosted DB, or in egress location for Atlas
- MongoDB Atlas project/cluster or self-hosted MongoDB server
- For Atlas Admin UI restriction: contact MongoDB Support to enable org-level IP Access List

## Step-by-Step

### MongoDB Atlas — Database Access
1. Create Twingate Resource for Atlas cluster hostname (e.g., `*.mongodb.net`), TCP 27017 + UDP 53
2. Note Connector public IPs (Admin Console → Remote Network → Connectors → Public IP)
3. In Atlas: **Network Access → Add IP Address** → add each Connector public IP
4. Connect: `mongosh "mongodb+srv://cluster0.abc123.mongodb.net/mydatabase" --username <user> --password <pass>`

### MongoDB Atlas — Admin Console Access
1. In Atlas: **Organization → Settings** → enable IP Access List for Atlas UI (contact support if missing)
2. Create Twingate Resource: `cloud.mongodb.com`, port 443, same Remote Network as DB Connectors
3. Add Connector public IPs to **Organization → Settings → IP Access List**
4. Verify: run Twingate Client, access `https://cloud.mongodb.com`

### Self-Hosted MongoDB
1. Create Twingate Resource with server IP/DNS, port 27017
2. Restrict server firewall to allow inbound only from Connector **private IP**
3. Optionally set `net.bindIp` in `mongod.conf` to limit listening interfaces
4. Connect via `mongosh` with Twingate Client running

## Configuration Values
| Setting | Value |
|---|---|
| MongoDB default port | TCP 27017 |
| DNS port | UDP 53 |
| Atlas Admin UI host | `cloud.mongodb.com` |
| Atlas Admin UI port | 443 |
| Atlas connection (SRV) | `mongodb+srv://` |
| Atlas connection (direct) | `mongodb://` + `--port 27017` |

## Gotchas
- `mongodb+srv://` requires DNS (UDP 53) access in addition to TCP 27017; Resource must allow both
- `mongodb://` vs `mongodb+srv://` mismatch is a common connection failure cause
- Atlas Admin UI IP Access List is **separate** from per-project database IP Access Lists
- For Atlas, always use Connector **public IP** (not private) in IP Access Lists
- For self-hosted, prefer Connector **private IP** in firewall rules

## Troubleshooting
- **Connection refused**: Connector IP not in Atlas IP Access List or firewall blocking
- **DNS Failed** (Recent Activity): Connector cannot resolve hostname
- **Connection Failed** (Recent Activity): DNS resolved but DB unreachable (firewall/routing)
- **No Activity**: Client not running, Resource not assigned, or conflicting VPN

## Related Docs
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)
- [MongoDB Private Endpoint Connections](https://www.mongodb.com/docs/atlas/security-private-endpoint/)
- [MongoDB Connection String Docs](https://www.mongodb.com/docs/manual/reference/connection-string/)
- Redis Access Guide, Snowflake Access Guide, SaaS App Gating Guide, Connector Best Practices