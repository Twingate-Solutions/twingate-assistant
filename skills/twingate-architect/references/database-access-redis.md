# Redis Access with Twingate

## Summary
Twingate secures Redis connections (Redis Enterprise Cloud or self-hosted) by routing traffic through Connectors, enabling IP-based access restrictions without public exposure. Supports Redis Enterprise Cloud database endpoints, the Redis Cloud admin console, and self-hosted Redis instances.

## Key Information
- Redis Enterprise Cloud uses public endpoints by default; paid plans support CIDR allow lists
- Self-hosted Redis uses Connector **private IPs** in firewall rules; Redis Cloud uses Connector **public IPs** in allow lists
- PrivateLink (AWS/Azure) or Private Service Connect (GCP) eliminates need for public IP allowlisting entirely
- Admin console (`app.redislabs.com` / `cloud.redis.io`) has no native IP allow list — gate via Twingate + SSO

## Prerequisites
- Twingate Remote Network with deployed Connector(s)
- Redis Enterprise Cloud instance (paid plan for CIDR allow lists) or self-hosted Redis server
- Connector public IPs (for Redis Cloud) or private IPs (for self-hosted)

## Step-by-Step

### Redis Enterprise Cloud — Database Access
1. Create Twingate Resource: set host to Redis Cloud endpoint (e.g., `redis-12345.c15.us-east-1-4.ec2.redns.redis-cloud.com`) and matching port
2. Record Connector public IP(s)
3. In Redis Cloud console → **Security → CIDR allow list** → add each Connector IP as `/32`
4. Connect: `redis-cli -h <host> -p <port> -a <password>`

### Redis Enterprise Cloud — Admin Console Access
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
| Admin console port | `443` |
| CIDR notation format | `1.2.3.4/32` |
| Redis Cloud domains | `app.redislabs.com`, `cloud.redis.io` |

## Gotchas
- **Public vs. private IPs**: Redis Cloud requires Connector *public* IPs; self-hosted requires Connector *private* IPs
- CIDR allow lists only available on **paid** Redis Enterprise Cloud plans
- Without PrivateLink, all Redis Cloud traffic traverses the public internet via Connector public IPs
- Other VPNs may intercept traffic — disable before testing ("No Activity" in Recent Activity logs)

## Troubleshooting
| Symptom | Check |
|---|---|
| Access denied | Connector IP in CIDR allow list or firewall |
| Authentication error | `requirepass` config and credentials |
| Port mismatch | Twingate Resource port matches Redis port |
| DNS Failed | Connector can resolve hostname; DNS server accessible |
| Connection Failed | Route exists Connector→DB; firewall allows port both directions |
| No Activity | Client running, Resource access granted, no conflicting VPN |

## Related Docs
- MongoDB Access Guide
- Snowflake Access Guide
- SaaS App Gating Guide
- Connector Best Practices
- Twingate Troubleshooting Guide