# Redis Access with Twingate

## Summary
Twingate secures Redis (Enterprise Cloud or self-hosted) by routing traffic through Connectors, enabling IP-based access restrictions without public exposure. Supports Redis Enterprise Cloud (managed via CIDR allowlists), subscription admin console gating, and self-hosted Redis instances.

## Key Information
- Redis Enterprise Cloud uses **public endpoints by default**; CIDR allowlists require **paid plans**
- Self-hosted Redis uses Connector **private IPs** in firewall rules; Cloud uses Connector **public IPs**
- PrivateLink (AWS/Azure) and Private Service Connect (GCP) bypass public IP allowlisting entirely
- Admin console (`app.redislabs.com` / `cloud.redis.io`) has no native IP restriction — use Twingate + SSO
- Default Redis port: `6379`; Redis Cloud port shown in console (e.g., `12345`)

## Prerequisites
- Twingate Remote Network and deployed Connector(s)
- Redis Enterprise Cloud instance (paid plan for CIDR allowlist) OR self-hosted Redis server
- Connector public IPs (for Cloud) or private IPs (for self-hosted)

## Step-by-Step

### Redis Enterprise Cloud — Database Access
1. Create Twingate Resource with Redis Cloud hostname and port (from Cloud console)
2. Record Connector public IP addresses
3. In Redis Cloud console: **Security → CIDR allow list** → add Connector IPs as `/32` entries
4. Connect: `redis-cli -h <host> -p <port> -a <password>`

### Redis Enterprise Cloud — Admin Console
1. Create Twingate Resource for `app.redislabs.com` or `cloud.redis.io`, port `443`, same Remote Network
2. Restrict Resource access to authorized users/groups only
3. Users must run Twingate Client to reach the admin console

### Self-Hosted Redis
1. Create Twingate Resource targeting server IP/hostname and port `6379`
2. Add Connector **private IPs** to firewall/security group rules
3. Harden `redis.conf`: set `protected-mode yes`, configure `bind`, set `requirepass`

## Configuration Values
| Setting | Value |
|---|---|
| Default Redis port | `6379` |
| Admin console domains | `app.redislabs.com`, `cloud.redis.io` |
| Admin console port | `443` |
| CIDR notation for single IP | `1.2.3.4/32` |

## Gotchas
- **Cloud vs. self-hosted IP type**: Cloud requires Connector *public* IPs; self-hosted uses Connector *private* IPs
- **Paid plan required** for CIDR allowlists on Redis Enterprise Cloud
- PrivateLink removes need for IP allowlisting but requires provider-specific setup
- If another VPN is active, it may hijack connections (check "No Activity" in Recent Activity logs)
- `DNS Failed` in Recent Activity = Connector can't resolve hostname; check DNS zone is tied to VPC

## Troubleshooting
- **Access denied** → Verify Connector IPs in CIDR allowlist or firewall
- **Auth error** → Check `requirepass` config and credentials
- **Port mismatch** → Match Twingate Resource port to actual Redis port
- **Timeouts** → Verify Connectors are online; check firewall rules on both ends
- Use **Admin Console → Recent Activity** to diagnose DNS Failed, Connection Failed, or No Activity states

## Related Docs
- [MongoDB Access Guide](https://www.twingate.com/docs/database-access-mongodb)
- [SaaS App Gating Guide](https://www.twingate.com/docs/saas-app-gating)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)