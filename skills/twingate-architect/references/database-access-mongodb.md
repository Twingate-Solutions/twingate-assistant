# MongoDB Access with Twingate

## Summary
Twingate secures access to both MongoDB Atlas (managed) and self-hosted MongoDB by routing traffic through Connectors and enforcing IP-based access controls. Atlas clusters restrict connections via IP Access Lists, requiring Connector public IPs to be allowlisted. Self-hosted instances use firewall rules or `bindIp` configuration instead.

## Key Information
- Atlas uses TLS on TCP port **27017** for database connections; DNS on UDP port **53** required for `mongodb+srv://` URIs
- Atlas Admin UI (`cloud.mongodb.com`) secured separately via Organization-level IP Access List on port **443**
- PrivateLink (AWS/Azure) or Private Service Connect (GCP) eliminates need to allowlist public Connector IPs for Atlas
- Use Connector **private IP** for self-hosted firewall rules; **public IP** only when required (e.g., Atlas IP Access List)

## Prerequisites
- Twingate Remote Network created with one or more Connectors deployed
- MongoDB Atlas project/cluster OR self-hosted MongoDB server
- Connector public IP addresses (for Atlas) or private IPs (for self-hosted)

## Step-by-Step

### Atlas Database Access
1. Create Twingate Resource for `*.mongodb.net`, TCP port `27017`, UDP port `53`
2. In Atlas → **Network Access** → **Add IP Address**: add each Connector public IP
3. Connect via `mongosh "mongodb+srv://cluster0.abc123.mongodb.net/mydatabase" --username <user> --password <pass>`

### Atlas Admin UI Access
1. In Atlas → **Organization → Settings**, enable IP Access List for Atlas UI (contact MongoDB Support if not visible)
2. Create Twingate Resource for `cloud.mongodb.com`, port `443`, same Remote Network as database Connectors
3. Add Connector public IPs to the Organization-level IP Access List
4. Verify: run Twingate Client, browse to `https://cloud.mongodb.com`

### Self-Hosted MongoDB
1. Create Twingate Resource with server IP/hostname, port `27017`
2. Restrict server firewall to allow inbound only from Connector **private IP**, OR set `net.bindIp` in `mongod.conf`
3. Connect via `mongosh` with Twingate Client running

## Configuration Values
| Parameter | Value |
|-----------|-------|
| MongoDB default port | TCP `27017` |
| DNS port | UDP `53` |
| Atlas Admin UI | `cloud.mongodb.com`, port `443` |
| Atlas Resource pattern | `*.mongodb.net` |
| Self-hosted bindIp config | `net.bindIp` in `mongod.conf` |

## Gotchas
- `mongodb+srv://` requires DNS (port 53) access in addition to TCP 27017 — missing DNS in Resource definition is a common failure
- Atlas database IP Access List and Atlas UI IP Access List are **separate** — securing one does not secure the other
- Atlas UI IP Access List is **org-level**, not project-level; must be enabled by MongoDB Support if not visible
- Another VPN running alongside Twingate Client can cause "No Activity" errors

## Troubleshooting Reference
| Symptom | Likely Cause |
|---------|-------------|
| `DNS Failed` in Recent Activity | Connector can't resolve hostname; check DNS routing |
| `Connection Failed` in Recent Activity | DNS works but TCP blocked; check firewall/IP allowlist |
| `No Activity` | Client not running, Resource not assigned, or conflicting VPN |
| Connection refused | Connector IP missing from Atlas IP Access List |
| Auth error | Wrong credentials or missing TLS configuration |

## Related Docs
- [SaaS App Gating Guide](https://www.twingate.com/docs/saas-app-gating)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)
- [MongoDB Private Endpoint Connections](https://www.mongodb.com/docs/atlas/security-private-endpoint/)
- [MongoDB Connection String Docs](https://www.mongodb.com/docs/manual/reference/connection-string/)