# Redis Access with Twingate

## Summary
Twingate secures Redis access (Enterprise Cloud or self-hosted) by routing traffic through Connectors, enabling IP restriction without public exposure. Supports Redis Enterprise Cloud CIDR allowlisting, admin console gating, and self-hosted firewall-based access control. PrivateLink/Private Service Connect eliminates public IP allowlisting for cloud deployments.

## Key Information
- Redis Enterprise Cloud databases use public endpoints by default; CIDR allowlisting requires a **paid plan**
- Admin console (`app.redislabs.com` / `cloud.redis.io`) has no native IP allowlist—use Twingate + SSO instead
- Redis Enterprise Cloud supports PrivateLink (AWS/Azure) and Private Service Connect (GCP) for fully private connectivity
- Self-hosted Redis: use Connector **private IPs** in firewall rules; cloud-managed Redis: use Connector **public IPs** in allowlists

## Prerequisites
- Twingate Remote Network and Connector deployed
- Redis Enterprise Cloud (paid plan for CIDR features) or self-hosted Redis instance
- For PrivateLink: AWS, Azure, or GCP deployment with private endpoint configured

## Step-by-Step

### Redis Enterprise Cloud - Database Access
1. Create Twingate Resource: set hostname (e.g., `redis-12345.c15.us-east-1-4.ec2.redns.redis-cloud.com`) and port (e.g., `12345`)
2. Record Connector public IP addresses
3. In Redis Cloud console → Security → CIDR allow list → add each Connector IP as `/32`
4. Connect: `redis-cli -h <host> -p <port> -a <password>`

### Redis Enterprise Cloud - Admin Console Access
1. Create Twingate Resource for `app.redislabs.com` or `cloud.redis.io`, port `443`
2. Restrict Resource access to authorized users/groups only
3. Verify: connect Twingate Client, then visit console URL

### Self-Hosted Redis
1. Create Twingate Resource targeting server IP/hostname, port `6379` (default)
2. Add Connector **private IPs** to firewall rules/security groups
3. Harden `redis.conf`: set `protected-mode yes`, `bind` to specific interfaces, `requirepass <strong-password>`

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Default Redis port | `6379` |
| Admin console domains | `app.redislabs.com`, `cloud.redis.io` |
| Admin console port | `443` |
| CIDR notation format | `1.2.3.4/32` |

## Gotchas
- **Cloud vs. self-hosted IP type**: Cloud-managed Redis needs Connector **public IPs**; self-hosted needs **private IPs**
- PrivateLink removes need for public IP allowlisting entirely—preferred approach for AWS/Azure/GCP
- Admin console has no native IP restriction; Twingate + SSO is the only gating mechanism
- Multiple Connectors: all Connector IPs must be added to the allowlist

## Troubleshooting
| Symptom | Cause | Fix |
|---------|-------|-----|
| Access denied | IP not in allowlist | Add Connector IP to CIDR allow list |
| DNS Failed | Connector can't resolve hostname | Check DNS zone/VPC association |
| Connection Failed | No route to database | Verify firewall rules and IP allowlists |
| No Activity | Client not routing traffic | Ensure Twingate Client running, check for conflicting VPN |

## Related Docs
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)
- [SaaS App Gating Guide](https://www.twingate.com/docs/saas-app-gating)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [MongoDB Access Guide](https://www.twingate.com/docs/database-access-mongodb)