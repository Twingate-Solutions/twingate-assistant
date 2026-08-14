---
source: https://www.twingate.com/docs/database-access-redis
type: docs
fetched: 2026-08-14
source_version: 9f37a8760882377ede641d791c88dd95961fc90832ea19db52bdf461bf9bdc4f
---

# Redis Access with Twingate

## Summary
Twingate secures Redis access (Enterprise Cloud or self-hosted) by routing traffic through Connectors, eliminating public exposure. For Redis Cloud, Connector public IPs are allowlisted; for self-hosted Redis, Connector private IPs are used in firewall rules. PrivateLink/Private Service Connect is recommended for fully private cloud connectivity.

## Key Information
- Default Redis port: `6379` (self-hosted); Redis Cloud uses custom ports shown in console
- Redis Enterprise Cloud requires **paid plan** for CIDR allow list support
- Admin console (`app.redislabs.com` / `cloud.redis.io`) has no native IP restriction — gate via Twingate + SSO
- PrivateLink (AWS/Azure) and Private Service Connect (GCP) eliminate need for public IP allowlisting

## Prerequisites
- Twingate Remote Network created with Connector(s) deployed
- For self-hosted: Connectors inside same VPC/LAN as Redis server
- For Redis Cloud: Connector public IP addresses noted
- Redis Enterprise Cloud instance or self-hosted Redis server

## Step-by-Step

### Redis Enterprise Cloud (Database Access)
1. Create Twingate Resource with Redis Cloud hostname and port (e.g., `redis-12345.c15.us-east-1-4.ec2.redns.redis-cloud.com:12345`)
2. In Redis Cloud console: **Security → CIDR allow list** → add each Connector public IP as `/32`
3. Connect: `redis-cli -h <host> -p <port> -a <password>`

### Redis Enterprise Cloud (Admin Console)
1. Create Twingate Resource for `app.redislabs.com` or `cloud.redis.io`, port `443`
2. Restrict Resource access to required users/groups only
3. Users must run Twingate Client to reach console

### Self-Hosted Redis
1. Create Twingate Resource targeting server IP/hostname and port `6379`
2. Firewall: allow inbound only from Connector **private IPs**
3. Harden `redis.conf`: `protected-mode yes`, `bind <interface>`, `requirepass <strong-password>`

## Configuration Values
| Setting | Value |
|---|---|
| Default Redis port | `6379` |
| Redis Cloud admin (old) | `app.redislabs.com` |
| Redis Cloud admin (new) | `cloud.redis.io` |
| Admin console port | `443` |
| CIDR notation for single IP | `1.2.3.4/32` |

## Gotchas
- Self-hosted: use **private IPs** in firewall rules; only use public IPs if Connector reaches server over internet
- Redis Cloud CIDR allow list requires paid plan — free tier cannot restrict by IP
- No native IP restriction on Redis Cloud admin console — must use Twingate (+ optional SSO)
- When using PrivateLink, skip public IP allowlisting — access is automatically restricted to private network

## Troubleshooting
| Symptom | Check |
|---|---|
| Access denied | Connector IP in CIDR allow list / firewall |
| Auth error | `requirepass` config and credentials |
| Port mismatch | Resource port matches Redis instance |
| DNS Failed | Connector can resolve hostname; DNS zone tied to VPC |
| Connection Failed | Route exists Connector→DB; firewall allows port both ends |
| No Activity | Twingate Client running; Resource access granted; no conflicting VPN |

## Related Docs
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)
- [SaaS App Gating Guide](https://www.twingate.com/docs/saas-app-gating)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [Redis Private Endpoints documentation](https://redis.io/docs)