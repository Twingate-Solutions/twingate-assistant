## Redis Access with Twingate

Twingate routes traffic to Redis Enterprise Cloud and self-hosted Redis through secure Connectors. For Redis Cloud, the Connector's public IP is added to the CIDR allow list (paid plans only); for self-hosted instances, the Connector's private IP is used in firewall rules or `redis.conf` bind settings. Redis Cloud supports PrivateLink (AWS/Azure) and Private Service Connect (GCP) for fully private connectivity.

**Key Information**
- Redis Cloud CIDR allow list requires a paid plan (not available on free tier)
- Resource port: shown in the Redis Cloud console next to the public endpoint (not always 6379)
- Self-hosted default port: 6379
- Admin console (`app.redislabs.com` or `cloud.redis.io`): no native IP allowlist; gate via SSO/SaaS App Gating; Resource port 443
- Redis Cloud supports PrivateLink (AWS/Azure) and PSC (GCP) for eliminating public IP allowlisting
- `redis.conf` hardening: `protected-mode yes`, `bind` to restrict listening interfaces, `requirepass` for password auth

**Prerequisites**
- Remote Network and Connector deployed (inside same VPC/LAN for self-hosted; any secure egress for Redis Cloud)
- Redis Cloud instance (paid plan) or self-hosted Redis server
- Connector public IP (Redis Cloud CIDR allowlist) or private IP (self-hosted firewall)

**Step-by-Step (Redis Cloud)**
1. Create Resource: Redis Cloud hostname (e.g. `redis-12345.c15.us-east-1-4.ec2.redns.redis-cloud.com`), port from Redis Cloud console
2. In Redis Cloud console: Security -> CIDR allow list -> enable and add Connector public IP in `/32` CIDR notation
3. Connect: `redis-cli -h <hostname> -p <port> -a <password>`

**Step-by-Step (Self-hosted)**
1. Create Resource: Redis server IP or hostname, port 6379
2. Restrict inbound to Connector private IP via firewall or security group
3. Optionally configure `redis.conf`: set `bind` to Connector-accessible interface, `requirepass`
4. Connect: `redis-cli -h <host> -p 6379 -a <password>`

**Gotchas**
- Redis Cloud CIDR allow list is only available on paid plans -- free tier cannot restrict by IP
- Redis Cloud port is not always 6379 -- use the port shown in the Redis Cloud console next to the public endpoint
- Admin console (app.redislabs.com / cloud.redis.io) requires a separate Twingate Resource; it has no native IP allowlist

**Related Docs**
- /docs/database-access-guide
- /docs/saas-app-gating
- /docs/connector-best-practices
