# MongoDB Access with Twingate

## Summary
Twingate secures access to both MongoDB Atlas and self-hosted MongoDB by routing traffic through Connectors and enforcing IP-based access controls. Atlas deployments require adding Connector public IPs to the Atlas IP Access List; self-hosted deployments use firewall rules or `net.bindIp` to restrict access to Connector private IPs.

## Key Information
- Atlas uses TLS on TCP port **27017** for database connections and UDP port **53** for DNS
- Atlas Admin Console (`cloud.mongodb.com`) requires port **443** and a separate IP Access List at the **organization** level
- PrivateLink (AWS/Azure) and Private Service Connect (GCP) eliminate need for public IP allowlisting in Atlas
- Two connection string formats have different network requirements (`mongodb+srv://` needs DNS; `mongodb://` needs direct host access)

## Prerequisites
- Twingate Remote Network and Connector deployed
- Connectors placed inside same network as DB (self-hosted) or in secure egress location (Atlas)
- MongoDB Atlas project/cluster or self-hosted MongoDB server
- Connector public IPs noted for Atlas; private IPs for self-hosted firewall rules

## Step-by-Step

### MongoDB Atlas – Database Access
1. Create Twingate Resource for `*.mongodb.net`, TCP port 27017 + UDP port 53
2. Note Connector public IP addresses
3. In Atlas → **Network Access** → **Add IP Address** → add each Connector public IP
4. Connect via `mongosh "mongodb+srv://cluster0.abc123.mongodb.net/mydatabase" --username <user> --password <pass>`

### MongoDB Atlas – Admin Console Access
1. Enable **IP Access List for Atlas UI** in Organization → Settings (contact MongoDB Support if not visible)
2. Create Twingate Resource for `cloud.mongodb.com`, port 443, same Remote Network
3. Add Connector public IPs to Organization → Settings → IP Access List
4. Verify access loads only with Twingate Client running

### Self-Hosted MongoDB
1. Create Twingate Resource with server IP/DNS, port 27017
2. Restrict firewall to allow only Connector **private IP**, OR set `net.bindIp` in `mongod.conf`
3. Connect via `mongosh` through Twingate Client

## Configuration Values
| Parameter | Value |
|-----------|-------|
| MongoDB TCP port | `27017` |
| DNS port | `53` (UDP) |
| Atlas Admin UI port | `443` |
| Atlas Admin UI host | `cloud.mongodb.com` |
| Atlas wildcard resource | `*.mongodb.net` |
| mongod.conf directive | `net.bindIp` |

## Gotchas
- **`mongodb+srv://` vs `mongodb://`**: SRV format requires DNS (port 53) in Resource definition; direct format requires each hostname individually reachable
- Atlas database IP Access List and Atlas UI IP Access List are **separate**—securing the DB does not secure the admin console
- Use Connector **public IP** for Atlas (cloud service); use Connector **private IP** for self-hosted firewall rules
- Organization-level UI IP Access Lists must be enabled by MongoDB Support if not visible

## Troubleshooting
| Error | Likely Cause |
|-------|-------------|
| Connection refused | Connector IP not in Atlas Access List or firewall blocking self-hosted |
| Authentication error | Wrong credentials or missing TLS |
| Timeouts | Connector offline or blocked by security groups |
| DNS Failed (Activity log) | DNS routing/access issue |
| Connection Failed (Activity log) | IP allow list or firewall issue |
| No Activity (Activity log) | Client not running or Resource misconfigured |

## Related Docs
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)
- [MongoDB Private Endpoint Connections](https://www.mongodb.com/docs/atlas/security-private-endpoint/)
- [MongoDB Connection String Reference](https://www.mongodb.com/docs/manual/reference/connection-string/)
- Redis Access Guide, Snowflake Access Guide, SaaS App Gating Guide, Connector Best Practices