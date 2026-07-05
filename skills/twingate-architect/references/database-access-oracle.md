# Oracle Cloud Database Access with Twingate

## Summary
Twingate secures access to Oracle Database (self-managed or OCI-managed) by routing traffic through Connectors, enabling private endpoints and firewall restrictions without public internet exposure. Supports Oracle DB, Autonomous Database, MySQL HeatWave, and NoSQL Database. Private endpoints are strongly recommended over public endpoints.

## Key Information
- Default Oracle DB port: **1521**
- Two deployment paths: OCI-managed databases (Autonomous DB, MySQL HeatWave, NoSQL) and self-managed Oracle DB
- Private endpoint approach eliminates need to allowlist Connector public IPs
- Connectors must be placed inside the same VCN/LAN as the database for private connectivity
- OCI Console access can be gated via Twingate SSO integration

## Prerequisites
- Twingate Remote Network created with one or more Connectors deployed
- Connectors placed inside same VCN (private) or Connector public IPs captured (public fallback)
- Oracle Database instance accessible on port 1521 (or custom port from `listener.ora`)

## Step-by-Step

### OCI-Managed Databases (Autonomous DB / MySQL HeatWave / NoSQL)
1. **Create Twingate Resource** — Use database private IP or FQDN; assign to user groups
2. **Configure network restrictions** — Allow Connector private IPs/VCN CIDR in OCI Network Security Groups or Security Lists
3. **Connect** — Download wallet, configure `sqlnet.ora` `DIRECTORY` to wallet path, set `TNS_ADMIN`, connect via `sqlplus username/password@TNS_NAME`

### Self-Managed Oracle Database
1. **Create Twingate Resource** — Use private IP/FQDN, port 1521; assign to user groups
2. **Configure firewall** — Allow DB port from Connector private IPs only
3. **Configure listener restrictions** (optional) — Add Valid Node Checking to `sqlnet.ora`, reload listener
4. **Connect** — `sqlplus username/password@"//hostname:1521/orclpdb"`

## Configuration Values

### sqlnet.ora (Valid Node Checking)
```
tcp.validnode_checking = YES
tcp.invited_nodes = (CONNECTOR_IP_1, CONNECTOR_IP_2)
```

### Environment Variables (Autonomous DB wallet)
```bash
export TNS_ADMIN=/path/to/wallet
export TNS_NAME=nw0xyz123_high
```

### Listener reload
```bash
lsnrctl reload
```

## Gotchas
- `sqlnet.ora` changes require `lsnrctl reload` to take effect
- Wallet `DIRECTORY` in `sqlnet.ora` must be absolute path
- OCI has no native console IP allowlist — use Twingate SSO for console access gating
- If using public endpoints, allowlist Connector **public** IPs; private endpoints use VCN CIDR instead
- Port mismatches between Resource config and `listener.ora` will silently fail

## Troubleshooting
| Symptom | Check |
|---|---|
| Connection refused | Connector IP in firewall/`tcp.invited_nodes` |
| DNS Failed (Recent Activity) | DNS zone tied to VPC, DNS server reachable from Connector |
| Connection Failed | Route exists Connector→DB, IP allowlists correct, port open both ends |
| No Activity | Client running, has Resource access, no conflicting VPN |

## Related Docs
- [AWS Database Access Guide](https://www.twingate.com/docs/database-access-aws)
- [Azure Database Access Guide](https://www.twingate.com/docs/database-access-azure)
- [GCP Database Access Guide](https://www.twingate.com/docs/database-access-gcp)
- [SaaS App Gating Guide](https://www.twingate.com/docs/saas-app-gating)
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)