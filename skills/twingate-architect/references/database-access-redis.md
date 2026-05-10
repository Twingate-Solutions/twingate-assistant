# Redis Access with Twingate

## Summary
Twingate secures Redis access (Enterprise Cloud or self-hosted) by routing traffic through Connectors, enabling IP restrictions without public exposure. For Redis Enterprise Cloud, Connector public IPs are allowlisted; for self-hosted Redis, Connector private IPs are used in firewall rules.

## Key Information
- Redis Enterprise Cloud uses public endpoints by default; paid plans support CIDR allowlists
- Admin console (`app.redislabs.com` / `cloud.redis.io`) has no native IP allowlist — gate via Twingate + SSO
- PrivateLink (AWS/Azure) and Private Service Connect (GCP) eliminate need for public IP allowlisting
- Default Redis port: `6379`; Redis Cloud port varies per instance (shown in console)

## Prerequisites
- Twingate Remote Network and Connector deployed
- Self-hosted: Connector inside same VPC/LAN as Redis server (use private IPs)
- Redis Enterprise Cloud: Connector public IPs recorded for allowlisting
- Paid Redis Cloud plan for CIDR allowlist feature

## Step-by-Step

### Redis Enterprise Cloud — Database Access
1. Create Twingate Resource → Redis Cloud hostname + port (e.g., `redis-12345.c15.us-east-1-4.ec2.redns.redis-cloud.com:12345`)
2. Redis Cloud Console → **Security → CIDR allow list** → add each Connector public IP in CIDR notation (e.g., `1.2.3.4/32`)
3. Connect: `redis-cli -h <host> -p <port> -a <password>`

### Redis Enterprise Cloud — Admin Console Access
1. Create Twingate Resource → `app.redislabs.com` or `cloud.redis.io`, port `443`
2. Restrict Resource access to authorized users/groups only
3. Users must run Twingate Client to reach admin console

### Self-Hosted Redis
1. Create Twingate Resource → server IP/hostname + port `6379`
2. Restrict inbound via firewall/security groups to Connector **private** IPs
3. Harden `redis.conf`: `protected-mode yes`, `bind <interface>`, `requirepass <strong-password>`

## Configuration Values
| Setting | Value |
|---|---|
| Default Redis port | `6379` |
| Admin console port | `443` |
| CIDR notation format | `1.2.3.4/32` |
| Admin console URLs | `app.redislabs.com`, `cloud.redis.io` |

## Gotchas
- CIDR allowlist requires a **paid** Redis Cloud plan
- Use Connector **public** IPs for Redis Cloud, **private** IPs for self-hosted
- PrivateLink/PSC removes need for IP allowlisting but requires additional cloud setup
- Admin console has no native IP restriction — Twingate is the only network-level control
- Other VPNs running simultaneously can hijack connections (check "No Activity" in Recent Activity)

## Troubleshooting
| Symptom | Check |
|---|---|
| Access denied | Connector IPs in CIDR allowlist/firewall |
| Auth error | `requirepass` config and credentials |
| Port mismatch | Resource port matches Redis instance port |
| DNS Failed | Hostname resolvable from Connector; DNS server accessible |
| Connection Failed | Route exists Connector→DB; firewall allows port both ends |
| No Activity | Client running; no conflicting VPN; user has Resource access |

## Related Docs
- SaaS App Gating Guide
- Connector Best Practices
- Security Policies Guide
- Redis Private Endpoints documentation
- Twingate Troubleshooting Guide