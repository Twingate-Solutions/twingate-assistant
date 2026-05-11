# MongoDB Access with Twingate

## Summary
Twingate secures access to MongoDB Atlas (managed) and self-hosted MongoDB instances by routing traffic through Connectors and enforcing network access controls. Atlas requires Connector public IPs in its IP Access List; self-hosted deployments use private IPs with firewall rules.

## Key Information
- MongoDB default port: TCP **27017**; DNS requires UDP **53**
- Atlas uses TLS by default on port 27017
- Two connection string formats have different network requirements (`mongodb://` vs `mongodb+srv://`)
- Atlas Admin Console (`cloud.mongodb.com`) IP access lists are configured at the **organization** level, separate from project-level database access lists
- PrivateLink (AWS/Azure) and Private Service Connect (GCP) eliminate need for public IP allowlisting

## Prerequisites
- Twingate Remote Network created with Connector(s) deployed
- MongoDB Atlas project/cluster **or** self-hosted MongoDB server
- For Atlas: Connector **public IPs** needed for IP Access List
- For self-hosted: Connector **private IP** preferred for firewall rules

## Step-by-Step

### Atlas Database Access
1. Create Twingate Resource for `*.mongodb.net`, TCP port 27017, UDP port 53
2. Add Connector public IP(s) to Atlas **Network Access → IP Access List**
3. Connect via `mongosh` with Twingate Client running

### Atlas Admin Console Access
1. Enable IP Access List for Atlas UI via **Organization → Settings** (may require MongoDB Support)
2. Create Twingate Resource for `cloud.mongodb.com`, port 443
3. Add Connector public IPs to **Organization → Settings → IP Access List**

### Self-Hosted MongoDB
1. Create Twingate Resource with server IP/DNS, port 27017
2. Restrict firewall to allow inbound only from Connector's **private IP**, or set `net.bindIp` in `mongod.conf`
3. Connect via `mongosh` through Twingate Client

## Configuration Values
| Parameter | Value |
|-----------|-------|
| MongoDB TCP port | `27017` |
| Atlas UI port | `443` |
| DNS port | `53` (UDP) |
| Atlas Resource pattern | `*.mongodb.net` |
| Admin Console Resource | `cloud.mongodb.com` |
| mongod.conf binding | `net.bindIp` |

## Gotchas
- **`mongodb+srv://`** requires DNS SRV resolution — Resource must allow port 53; **`mongodb://`** requires each hostname/IP to be directly reachable
- Connector **public IPs** required for Atlas (not private); **private IPs** preferred for self-hosted
- Atlas UI IP Access List is **organization-scoped**, not project-scoped — must be enabled by MongoDB Support if not visible
- Another VPN running alongside Twingate Client may cause "No Activity" in logs

## Troubleshooting
| Twingate Activity Log | Meaning |
|-----------------------|---------|
| DNS Failed | Connector cannot resolve hostname |
| Connection Failed | DNS resolved, but database unreachable (firewall/IP list) |
| No Activity | Client not running, Resource missing, or VPN conflict |

## Related Docs
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)
- [SaaS App Gating Guide](https://www.twingate.com/docs/saas-app-gating)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [MongoDB Private Endpoint Connections](https://www.mongodb.com/docs/atlas/security-private-endpoint/)
- [MongoDB Connection String Docs](https://www.mongodb.com/docs/manual/reference/connection-string/)