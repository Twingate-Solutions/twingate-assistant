# Redis Access with Twingate

## Summary
Twingate secures Redis access (Enterprise Cloud or self-hosted) by routing traffic through Connectors, eliminating public exposure. For Redis Cloud, Connector public IPs are allowlisted; for self-hosted Redis, Connector private IPs are used in firewall rules. PrivateLink/Private Service Connect provides fully private connectivity on major cloud providers.

## Key Information
- Default Redis port: **6379** (self-hosted); Redis Cloud uses custom ports shown in console
- Redis Cloud CIDR allowlist requires **paid plans**
- Redis Cloud admin console (`app.redislabs.com` / `cloud.redis.io`) has no native IP allowlist — gate with Twingate + SSO instead
- PrivateLink (AWS/Azure) and Private Service Connect (GCP) eliminate need for public IP allowlisting

## Prerequisites
- Twingate Remote Network created with Connector(s) deployed
- For Redis Cloud: Connector **public IPs** captured for allowlisting
- For self-hosted: Connectors placed in **same VPC/LAN** as Redis server; use **private IPs** in firewall rules
- Redis Enterprise Cloud instance or self-hosted Redis server

## Step-by-Step

### Redis Enterprise Cloud (Database)
1. Create Twingate Resource → hostname from Redis Cloud console, set correct port
2. In Redis Cloud console: **Security → CIDR allow list** → add Connector public IPs as `/32` entries
3. Connect: `redis-cli -h <host> -p <port> -a <password>`

### Redis Enterprise Cloud (Admin Console)
1. Create Twingate Resource for `app.redislabs.com` or `cloud.redis.io`, port **443**
2. Restrict Resource access to authorized users/groups only
3. Users must be connected to Twingate to reach the console

### Self-Hosted Redis
1. Create Twingate Resource targeting server IP/hostname and port (default 6379)
2. Restrict inbound traffic to Connector **private IPs** via firewall/security groups
3. Harden `redis.conf`: set `protected-mode yes`, configure `bind`, set `requirepass`

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Default Redis port | `6379` |
| Redis Cloud admin port | `443` |
| CIDR notation format | `1.2.3.4/32` |
| redis.conf hardening | `protected-mode yes`, `bind <interface>`, `requirepass <password>` |

## Gotchas
- **Only paid Redis Cloud plans** support CIDR allowlists
- Redis Cloud admin console has **no native IP restriction** — Twingate + SSO is the only gating mechanism
- If using PrivateLink, no public IP allowlisting needed — skip CIDR allowlist step
- Self-hosted: use **private** IPs in rules; only use public IPs if Connector reaches server over internet
- Other VPNs running simultaneously may hijack connections (check "No Activity" in Recent Activity)

## Troubleshooting
| Symptom | Check |
|---------|-------|
| Access denied | Connector IPs in allowlist/firewall |
| Auth error | `requirepass` config, credentials |
| Port mismatch | Resource port matches Redis instance |
| DNS Failed | DNS zone tied to VPC, DNS server accessible from Connector |
| Connection Failed | Route exists, IP allowlists correct, firewall allows port |
| No Activity | Client running, Resource access granted, no conflicting VPN |

## Related Docs
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)
- [SaaS App Gating Guide](https://www.twingate.com/docs/saas-app-gating)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- Redis [Private Endpoints documentation](https://redis.io/docs/latest/operate/rc/security/private-service-connect/)