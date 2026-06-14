# Redis Access with Twingate

## Summary
Twingate secures Redis access (Enterprise Cloud or self-hosted) by routing traffic through Connectors, enabling IP-based restrictions without public exposure. Supports Redis Enterprise Cloud database endpoints, the Redis Cloud admin console, and self-hosted Redis instances.

## Key Information
- Redis Enterprise Cloud uses public endpoints by default; paid plans support CIDR allow lists
- Admin console (`app.redislabs.com` / `cloud.redis.io`) has no native IP restriction — gate via Twingate Resource + SSO
- Self-hosted Redis uses Connector **private IPs** in firewall rules; Redis Cloud uses Connector **public IPs** in allow lists
- PrivateLink (AWS/Azure) and Private Service Connect (GCP) eliminate need for public IP allowlisting

## Prerequisites
- Twingate Remote Network and deployed Connector(s)
- For self-hosted: Connectors inside same VPC/LAN as Redis server
- For Redis Cloud: Connector public IPs recorded for allow list
- Redis Enterprise Cloud paid plan (for CIDR allow list feature)

## Step-by-Step

### Redis Enterprise Cloud – Database Access
1. Create Twingate Resource: hostname (e.g., `redis-12345.c15.us-east-1-4.ec2.redns.redis-cloud.com`) + port from Redis Cloud console
2. In Redis Cloud console → **Security → CIDR allow list** → add each Connector public IP as `/32`
3. Connect: `redis-cli -h <host> -p <port> -a <password>`

### Redis Enterprise Cloud – Admin Console Access
1. Create Twingate Resource for `app.redislabs.com` or `cloud.redis.io`, port `443`
2. Restrict Resource access to authorized users/groups only
3. Users must run Twingate Client to reach the console

### Self-Hosted Redis
1. Create Twingate Resource targeting server IP/hostname, port `6379` (default)
2. Add Connector **private IPs** to firewall/security group rules
3. Harden `redis.conf`: `protected-mode yes`, `bind <interface>`, `requirepass <strong-password>`

## Configuration Values
| Setting | Value |
|---|---|
| Default Redis port | `6379` |
| Admin console domains | `app.redislabs.com`, `cloud.redis.io` |
| Admin console port | `443` |
| CIDR notation for single IP | `1.2.3.4/32` |
| redis.conf hardening | `protected-mode yes`, `bind`, `requirepass` |

## Gotchas
- Redis Cloud CIDR allow list requires a **paid plan**
- Use Connector **public IPs** for Redis Cloud, **private IPs** for self-hosted — mixing these is a common misconfiguration
- No activity in Twingate logs means the Client isn't sending traffic — check for conflicting VPNs
- DNS failures indicate the Connector can't resolve the hostname; verify DNS zone is tied to VPC

## Troubleshooting
| Symptom | Check |
|---|---|
| Access denied | Connector IP in CIDR allow list/firewall |
| Auth error | `requirepass` config, credentials |
| Port mismatch | Twingate Resource port matches Redis instance |
| DNS Failed | DNS zone/VPC association, DNS server accessible from Connector |
| Connection Failed | Route exists Connector→DB, firewall allows port both ends |
| No Activity | Client running, user has Resource access, no VPN conflict |

## Related Docs
- [MongoDB Access Guide](https://www.twingate.com/docs/database-access-mongodb)
- [SaaS App Gating Guide](https://www.twingate.com/docs/saas-app-gating)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)