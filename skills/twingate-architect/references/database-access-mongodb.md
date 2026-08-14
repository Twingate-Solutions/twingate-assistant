---
source: https://www.twingate.com/docs/database-access-mongodb
type: docs
fetched: 2026-08-14
source_version: 095437782e2a19fa01317ee99375102884ea03f2202f2cb4df7b69f6b2077f8c
---

# MongoDB Access with Twingate

## Summary
Configure Twingate to secure access to MongoDB Atlas (managed) or self-hosted MongoDB instances. Twingate enforces network access controls by routing traffic through Connectors whose IP addresses are allowlisted in MongoDB's access controls.

## Key Information
- Supports MongoDB Atlas (SRV and direct connections) and self-hosted MongoDB
- Atlas uses TLS on TCP port 27017; DNS resolution requires UDP port 53
- Atlas UI (`cloud.mongodb.com`) access control is separate from database project IP allowlists
- PrivateLink (AWS/Azure) or Private Service Connect (GCP) eliminates need to use public Connector IPs with Atlas

## Prerequisites
- Twingate Remote Network created with Connector(s) deployed
- MongoDB Atlas project/cluster or self-hosted MongoDB server
- For Atlas: Connector **public** IPs for IP Access List (unless using PrivateLink)
- For self-hosted: Connector **private** IPs for firewall rules

## Step-by-Step

### Atlas Database Access
1. Create Twingate Resource: `*.mongodb.net`, TCP 27017 + UDP 53
2. Add Connector public IPs to Atlas **Network Access → IP Access List**
3. Connect via `mongosh` with Twingate Client running

### Atlas Admin Console Access
1. Enable IP Access List for Atlas UI (Organization → Settings; may require MongoDB Support)
2. Create Twingate Resource: `cloud.mongodb.com`, port 443
3. Add Connector public IPs to Organization → Settings → IP Access List

### Self-Hosted MongoDB
1. Create Twingate Resource: server IP/hostname, port 27017
2. Restrict firewall to allow inbound only from Connector **private** IP, OR set `net.bindIp` in `mongod.conf`
3. Connect via `mongosh` through Twingate Client

## Configuration Values
| Parameter | Value |
|-----------|-------|
| MongoDB TCP port | 27017 |
| DNS port | UDP 53 |
| Atlas UI port | TCP 443 |
| Atlas hostname pattern | `*.mongodb.net` |
| Atlas UI hostname | `cloud.mongodb.com` |
| mongod config key | `net.bindIp` |

## Gotchas
- **`mongodb+srv://` vs `mongodb://`**: SRV format requires DNS (port 53) in addition to TCP 27017; direct format requires each host to be explicitly reachable
- Atlas UI IP Access List is **organization-level**, separate from per-project database IP allowlists
- Use Connector **public** IP for Atlas (internet-facing); use Connector **private** IP for self-hosted firewalls
- PrivateLink removes need for public IP allowlisting entirely
- Other VPNs running alongside Twingate Client can block traffic (check Recent Activity for "No Activity")

## Troubleshooting via Admin Console
- **DNS Failed**: Connector cannot resolve hostname → check DNS routing
- **Connection Failed**: DNS resolved but TCP blocked → check firewall/IP allowlist
- **No Activity**: Client not routing traffic → check Client is running, Resource exists, no conflicting VPN

## Related Docs
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)
- [MongoDB Private Endpoint Connections](https://www.mongodb.com/docs/atlas/security-private-endpoint/)
- [MongoDB Connection String Reference](https://www.mongodb.com/docs/manual/reference/connection-string/)
- Redis Access Guide, Snowflake Access Guide, SaaS App Gating Guide, Connector Best Practices