# MongoDB Access with Twingate

## Summary
Twingate routes traffic securely to MongoDB Atlas (managed) or self-hosted MongoDB instances while enforcing network access controls. For Atlas, Twingate Connector public IPs are added to Atlas IP Access Lists; for self-hosted, firewall rules restrict access to the Connector's private IP.

## Key Information
- Atlas uses TCP port **27017** (direct connections) and UDP port **53** (DNS)
- Atlas Admin Console (`cloud.mongodb.com`) uses port **443**
- Two Atlas deployment modes: public IP allowlisting or PrivateLink (AWS/Azure/GCP)
- Admin Console IP restrictions are organization-level, separate from project-level database access lists
- Self-hosted MongoDB can restrict via OS firewall or `net.bindIp` in `mongod.conf`

## Prerequisites
- Twingate Remote Network and at least one deployed Connector
- MongoDB Atlas project/cluster or self-hosted MongoDB server
- Connector placed inside same network as DB (self-hosted) or secure egress location (Atlas)

## Step-by-Step

### Atlas Database Access
1. Create Twingate Resource for `*.mongodb.net`, TCP 27017 + UDP 53
2. Note Connector public IP(s) from Admin Console → Remote Network → Connectors
3. In Atlas → Network Access → Add IP Address, add each Connector public IP
4. Connect: `mongosh "mongodb+srv://cluster0.abc123.mongodb.net/mydatabase" --username <u> --password <p>`

### Atlas Admin Console Access
1. Enable IP Access List for Atlas UI via Organization → Settings (may require MongoDB Support)
2. Create Twingate Resource for `cloud.mongodb.com`, port 443
3. Add Connector public IP(s) to Organization → Settings → IP Access List

### Self-Hosted MongoDB
1. Create Twingate Resource with server IP/DNS, port 27017
2. Restrict firewall inbound to Connector's **private IP** only
3. Optionally set `net.bindIp` in `mongod.conf` to limit listening interfaces
4. Connect via `mongosh` with Twingate Client running

## Configuration Values
| Parameter | Value |
|-----------|-------|
| MongoDB direct port | TCP 27017 |
| DNS port | UDP 53 |
| Atlas UI port | TCP 443 |
| Atlas UI hostname | `cloud.mongodb.com` |
| Atlas cluster wildcard | `*.mongodb.net` |
| Self-hosted config file | `mongod.conf` → `net.bindIp` |

## Gotchas
- **`mongodb+srv://` vs `mongodb://`**: SRV format requires DNS resolution (port 53); direct format requires each hostname reachable individually — mismatches are a common failure cause
- Use Connector **public IP** for Atlas IP Access List; use **private IP** for self-hosted firewall rules
- Atlas UI IP restrictions are **organization-level** only — must be explicitly enabled by MongoDB Support if not visible
- PrivateLink/Private Service Connect eliminates need for public IP allowlisting entirely
- Another VPN running alongside Twingate Client can cause "No Activity" in Recent Activity logs

## Troubleshooting via Recent Activity
| Status | Cause |
|--------|-------|
| DNS Failed | Connector cannot resolve hostname |
| Connection Failed | DNS resolved but DB unreachable (firewall/IP list) |
| No Activity | Client not running, Resource missing, or VPN conflict |

## Related Docs
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)
- [MongoDB Private Endpoint Connections](https://www.mongodb.com/docs/atlas/security-private-endpoint/)
- [MongoDB Connection String Reference](https://www.mongodb.com/docs/manual/reference/connection-string/)
- Redis Access Guide, Snowflake Access Guide, SaaS App Gating Guide (Twingate docs)