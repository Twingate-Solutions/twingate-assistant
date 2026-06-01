# Redis Access with Twingate

## Summary
Configure Twingate to provide secure, private access to Redis Enterprise Cloud or self-hosted Redis instances. Twingate routes Redis traffic through Connectors, enabling IP-based access restrictions without public exposure. Supports both CIDR allowlisting and PrivateLink/Private Service Connect for fully private connectivity.

## Key Information
- Redis Enterprise Cloud requires paid plan for CIDR allow list support
- Self-hosted Redis Connectors use **private IPs** in firewall rules; Redis Cloud Connectors use **public IPs** in allow lists
- Admin console (`app.redislabs.com` / `cloud.redis.io`) has no native IP allowlist—gate with Twingate + SSO instead
- PrivateLink (AWS/Azure) and Private Service Connect (GCP) eliminate need for public IP allowlisting entirely
- Default Redis port: `6379`; Redis Cloud port varies per instance

## Prerequisites
- Twingate Remote Network created with Connector(s) deployed
- Redis Enterprise Cloud (paid plan) or self-hosted Redis instance
- Connector public IPs (for Redis Cloud) or private IPs (for self-hosted)

## Step-by-Step

### Redis Enterprise Cloud – Database Access
1. Create Twingate Resource with Redis Cloud hostname and port (from Cloud console)
2. Record Connector public IP addresses
3. In Redis Cloud console → **Security → CIDR allow list** → add each Connector IP as `/32`
4. Connect: `redis-cli -h <host> -p <port> -a <password>`

### Redis Enterprise Cloud – Admin Console Access
1. Create Twingate Resource for `app.redislabs.com` or `cloud.redis.io`, port `443`
2. Use same Remote Network as database Connectors
3. Restrict Resource access to authorized users/groups only
4. Users must run Twingate Client to reach the console

### Self-Hosted Redis
1. Create Twingate Resource targeting server IP/hostname and port `6379`
2. Restrict inbound traffic to Connector **private IPs** via firewall/security groups
3. Harden `redis.conf`: set `protected-mode yes`, configure `bind`, set `requirepass`

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Default Redis port | `6379` |
| Admin console port | `443` |
| CIDR notation for single IP | `1.2.3.4/32` |
| redis.conf hardening | `protected-mode yes`, `bind <interface>`, `requirepass <password>` |

## Gotchas
- **PrivateLink bypasses IP allowlisting**—no need to add Connector public IPs when using private endpoints
- Redis Cloud admin console has **no native IP restriction**—Twingate is the only network-level gate
- Use public IPs for Connector-to-Redis-Cloud paths; use private IPs for self-hosted paths—mixing these is a common misconfiguration
- Verify port in Twingate Resource exactly matches Redis instance port (port mismatch is a frequent issue)

## Troubleshooting
- **Access denied**: Connector IP not in CIDR allow list or firewall rules
- **DNS Failed**: Connector cannot resolve hostname—check DNS zone/VPC binding
- **Connection Failed**: Route or firewall issue between Connector and database
- **No Activity**: Twingate Client not running, no Resource access, or another VPN intercepting traffic

## Related Docs
- [MongoDB Access Guide](https://www.twingate.com/docs/database-access-mongodb)
- [SaaS App Gating Guide](https://www.twingate.com/docs/saas-app-gating)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)