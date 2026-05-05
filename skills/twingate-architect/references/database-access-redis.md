# Redis Access with Twingate

## Summary
Secure Redis access (Enterprise Cloud or self-hosted) by routing traffic through Twingate Connectors, enabling IP allowlisting or private endpoint restrictions without public exposure. Supports Redis Enterprise Cloud database access, admin console gating, and self-hosted Redis instances.

## Key Information
- Redis Enterprise Cloud uses public endpoints by default; paid plans support CIDR allow lists
- Connector **public IPs** used for Redis Cloud allowlisting; Connector **private IPs** used for self-hosted firewall rules
- PrivateLink (AWS/Azure) or Private Service Connect (GCP) eliminates need for public IP allowlisting
- Admin console (`app.redislabs.com` / `cloud.redis.io`) has no native IP restriction — gate via Twingate + SSO

## Prerequisites
- Twingate Remote Network and deployed Connector(s)
- Redis Enterprise Cloud (paid plan for CIDR allow list) or self-hosted Redis instance
- Connector public IPs (for Cloud) or private IPs (for self-hosted) recorded before configuration

## Step-by-Step

### Redis Enterprise Cloud — Database Access
1. Create Twingate Resource: hostname (e.g., `redis-12345.c15.us-east-1-4.ec2.redns.redis-cloud.com`), port from Redis Cloud console
2. In Redis Cloud console → database → **Security → CIDR allow list** → add each Connector public IP as `/32`
3. Connect: `redis-cli -h <host> -p <port> -a <password>`

### Redis Enterprise Cloud — Admin Console Access
1. Create Twingate Resource: `app.redislabs.com` or `cloud.redis.io`, port `443`
2. Restrict Resource access to authorized users/groups only
3. Users must run Twingate Client to reach the console

### Self-Hosted Redis
1. Create Twingate Resource targeting server IP/hostname and port `6379`
2. Add Connector **private IPs** to firewall/security group inbound rules
3. Harden `redis.conf`: `protected-mode yes`, `bind <interface>`, `requirepass <strong-password>`

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Default Redis port | `6379` |
| Redis Cloud admin console | `app.redislabs.com` or `cloud.redis.io` |
| Admin console port | `443` |
| CIDR notation for single IP | `1.2.3.4/32` |

## Gotchas
- **Cloud vs. self-hosted IPs**: Cloud requires Connector *public* IPs; self-hosted uses *private* IPs — mixing these breaks connectivity
- PrivateLink/PSC removes need for public IP allowlisting entirely — preferred for AWS/Azure/GCP deployments
- Redis Cloud admin console has **no native IP restriction** — must use Twingate (+ optionally SSO) to gate it
- `No Activity` in Recent Activity means the Client isn't routing traffic — check for conflicting VPNs

## Troubleshooting
| Symptom | Fix |
|---------|-----|
| Access denied | Verify Connector IPs in CIDR allow list or firewall |
| Authentication error | Check `requirepass` config and credentials |
| Port mismatch | Match Resource port to Redis instance port |
| DNS Failed | Check DNS zone/VPC binding, DNS server reachable from Connector |
| Connection Failed | Verify route exists Connector→database, check security group rules |
| No Activity | Confirm Client running, Resource access granted, no VPN conflict |

## Related Docs
- [SaaS App Gating Guide](https://www.twingate.com/docs/saas-app-gating)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [Redis Private Endpoints Documentation](https://redis.io/docs)
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)