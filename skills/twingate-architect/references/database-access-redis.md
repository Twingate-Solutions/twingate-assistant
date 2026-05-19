# Redis Access with Twingate

## Summary
Secure Redis connections (Enterprise Cloud or self-hosted) by routing traffic through Twingate Connectors, enabling IP restrictions without public exposure. Supports Redis Enterprise Cloud CIDR allow lists, PrivateLink/Private Service Connect for fully private connectivity, and self-hosted Redis via firewall rules.

## Key Information
- Redis Enterprise Cloud uses **public endpoints by default**; paid plans support CIDR allow lists
- Connector **public IPs** used for Redis Cloud; **private IPs** used for self-hosted Redis
- Default Redis port: `6379`; Redis Cloud port varies (shown in console)
- Admin console (`app.redislabs.com` / `cloud.redis.io`) has no native IP allow list — gate via Twingate + SSO

## Prerequisites
- Twingate Remote Network created with Connector(s) deployed
- For self-hosted: Connectors inside same VPC/LAN as Redis server
- For Redis Cloud: Connector public IPs recorded for allow listing
- Redis Enterprise Cloud paid plan (for CIDR allow list feature)

## Step-by-Step

### Redis Enterprise Cloud Database
1. Create Twingate Resource → Redis Cloud hostname + port (from Cloud console)
2. In Redis Cloud console: **Security → CIDR allow list** → add Connector public IPs as `/32` entries
3. Connect: `redis-cli -h <host> -p <port> -a <password>`

### Redis Enterprise Cloud Admin Console
1. Create Twingate Resource for `app.redislabs.com` or `cloud.redis.io`, port `443`
2. Restrict Resource access to authorized users/groups only
3. Users must run Twingate Client to access subscription console

### Self-Hosted Redis
1. Create Twingate Resource → server IP/hostname + port `6379`
2. Add Connector **private IPs** to firewall/security group rules
3. Harden `redis.conf`: set `protected-mode yes`, configure `bind`, set `requirepass`

## Configuration Values
| Setting | Value |
|---|---|
| Default Redis port | `6379` |
| Admin console domains | `app.redislabs.com`, `cloud.redis.io` |
| Admin console port | `443` |
| CIDR notation for single IP | `1.2.3.4/32` |
| redis.conf hardening | `protected-mode yes`, `bind <interface>`, `requirepass <password>` |

## Gotchas
- PrivateLink/Private Service Connect eliminates need for public IP allowlisting but requires AWS/Azure/GCP setup in Redis Cloud
- Use **public IPs** for Redis Cloud allow lists; use **private IPs** for self-hosted firewall rules — mixing these is a common error
- No native IP restriction on Redis Cloud admin console; must use Twingate + optional SSO
- If another VPN is active, it may intercept traffic before Twingate (check Recent Activity → "No Activity")
- DNS failures indicate Connector cannot resolve hostname — verify DNS zone is accessible from Connector

## Troubleshooting Reference
| Symptom | Check |
|---|---|
| Access denied | Connector IP in CIDR allow list |
| Auth error | `requirepass` config + credentials |
| Port mismatch | Resource port matches Redis instance |
| DNS Failed | DNS reachable from Connector, hostname resolves |
| Connection Failed | Route exists, firewall allows port both sides |
| No Activity | Client running, Resource access granted, no conflicting VPN |

## Related Docs
- SaaS App Gating Guide
- Connector Best Practices
- Security Policies Guide
- Redis Private Endpoints documentation
- Twingate Troubleshooting Guide