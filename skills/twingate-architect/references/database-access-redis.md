# Redis Access with Twingate

## Summary
Twingate secures Redis access (Redis Enterprise Cloud or self-hosted) by routing traffic through Connectors, enabling IP-based restrictions without public exposure. For cloud deployments, Connector public IPs are allowlisted in Redis Cloud; for self-hosted, Connector private IPs are used in firewall rules. PrivateLink/Private Service Connect eliminates public IP allowlisting entirely on AWS/Azure/GCP.

## Key Information
- Redis Enterprise Cloud databases require **paid plans** for CIDR allow list support
- Redis Cloud admin console (`app.redislabs.com` / `cloud.redis.io`) has no native IP allowlist — gate via Twingate + SSO
- Self-hosted Redis default port: `6379`
- PrivateLink (AWS/Azure) and Private Service Connect (GCP) supported for fully private connectivity

## Prerequisites
- Twingate Remote Network and Connector deployed
- Redis Enterprise Cloud (paid plan) or self-hosted Redis instance
- For cloud: Connector **public IP addresses**
- For self-hosted: Connector **private IP addresses** (Connector in same VPC/LAN)

## Step-by-Step

### Redis Enterprise Cloud — Database Access
1. Create Twingate Resource with Redis Cloud hostname and port (e.g., `redis-12345.c15.us-east-1-4.ec2.redns.redis-cloud.com`, port `12345`)
2. Record Connector public IP(s)
3. In Redis Cloud console → **Security → CIDR allow list** → add each Connector IP as `/32`
4. Connect: `redis-cli -h <host> -p <port> -a <password>`

### Redis Enterprise Cloud — Admin Console Access
1. Create Twingate Resource for `app.redislabs.com` or `cloud.redis.io`, port `443`
2. Use same Remote Network as database Connectors
3. Restrict Resource access to authorized users/groups only
4. Users must run Twingate Client to reach the console

### Self-Hosted Redis
1. Create Twingate Resource targeting server IP/hostname and port `6379`
2. Restrict inbound traffic to Connector **private IPs** via firewall/security groups
3. Harden `redis.conf`: `protected-mode yes`, `bind <interface>`, `requirepass <strong-password>`

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Default Redis port | `6379` |
| Admin console HTTPS port | `443` |
| CIDR notation for single IP | `1.2.3.4/32` |
| Redis Cloud admin URLs | `app.redislabs.com`, `cloud.redis.io` |

## Gotchas
- **CIDR allowlist requires paid Redis Cloud plan** — not available on free tier
- Self-hosted: use **private IPs** in firewall rules; only use public IPs if Connector reaches server over internet
- PrivateLink removes need to allowlist Connector public IPs — access restricted automatically by private network
- Admin console access: combine Twingate with SSO (SaaS App Gating) for identity-based control
- Other active VPNs may hijack connections (check "No Activity" in Recent Activity logs)

## Troubleshooting
| Symptom | Check |
|---------|-------|
| Access denied | Connector IPs in CIDR allowlist/firewall |
| Auth error | `requirepass` config and credentials |
| Port mismatch | Resource port matches Redis instance |
| DNS Failed | Hostname resolvable from Connector; DNS server accessible |
| Connection Failed | Route exists Connector→DB; firewall allows port both ends |
| No Activity | Client running; Resource access granted; no conflicting VPN |

## Related Docs
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)
- [SaaS App Gating Guide](https://www.twingate.com/docs/saas-app-gating)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [MongoDB Access Guide](https://www.twingate.com/docs/database-access-mongodb)
- [Redis Private Endpoints Documentation