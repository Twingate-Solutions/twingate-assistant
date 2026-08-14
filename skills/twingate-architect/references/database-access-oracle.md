---
source: https://www.twingate.com/docs/database-access-oracle
type: docs
fetched: 2026-08-14
source_version: bb0f6269f2fb185332ac1ccd3dec88afbd8020f6ab21c6860fbd0afa5c125f06
---

# Oracle Cloud Database Access with Twingate

## Summary
Twingate secures access to Oracle Database (on-prem, OCI VMs, Autonomous Database, MySQL HeatWave, NoSQL) by routing traffic through Connectors, eliminating public internet exposure. Best practice is to use private endpoints with Connectors deployed inside the same VCN/subnet. Supports both OCI-managed and self-managed Oracle Database deployments.

## Key Information
- Default Oracle DB port: **1521** (configurable via `listener.ora`)
- Connector placement inside same VCN eliminates need to allowlist public IPs
- Two endpoint strategies: private endpoint (recommended) or public endpoint with IP allowlisting
- OCI Console access can be gated via SSO/SaaS App Gating (no native OCI IP allowlist)

## Prerequisites
- Twingate Remote Network created with Connector(s) deployed
- Connector placed **inside the VCN/LAN** for private endpoint use
- Oracle Database instance accessible (port 1521 default)
- For Autonomous DB: wallet file downloaded for client authentication

## Step-by-Step

### OCI Managed Databases (Autonomous DB / MySQL HeatWave / NoSQL)
1. Add Twingate Resource using database private IP or FQDN
2. Configure OCI Network Security Groups to allow traffic from Connector private IPs or VCN CIDR
3. Download wallet → unzip → update `sqlnet.ora` `DIRECTORY` to absolute wallet path
4. Set env vars and connect:

### Self-Managed Oracle Database
1. Add Twingate Resource with private IP/FQDN and port 1521
2. Configure firewall/Security List to allow DB port from Connector private IPs
3. (Optional) Configure `sqlnet.ora` Valid Node Checking, then reload listener

## Configuration Values

### Environment Variables
```bash
export TNS_ADMIN=/Users/<User>/Downloads/Wallet
export TNS_NAME=nw0xyz123_high
```

### sqlnet.ora (Valid Node Checking)
```
tcp.validnode_checking = YES
tcp.invited_nodes = (1.2.3.4, 1.2.3.5)  # Connector IPs
METHOD_DATA = (DIRECTORY="/Users/<User>/Downloads/Wallet")
```

### Connection Commands
```bash
# Autonomous DB
sqlplus username/password@TNS_NAME

# Self-managed Oracle
sqlplus username/password@"//hostname.oraclevcn.com:1521/orclpdb"

# Reload listener after sqlnet.ora changes
lsnrctl reload
```

## Gotchas
- `sqlnet.ora` changes require `lsnrctl reload` to take effect — connections won't update automatically
- Port mismatches between `listener.ora` and Twingate Resource definition cause silent failures
- Other VPNs running simultaneously can hijack connections (shows as "No Activity" in console)
- OCI has no native console IP allowlist — must use SSO/SaaS App Gating workaround
- Public endpoint fallback requires capturing Connector **public** IPs (not private) for allowlisting

## Troubleshooting
| Symptom | Cause | Fix |
|---|---|---|
| Connection refused | Connector IP not in firewall/`tcp.invited_nodes` | Update allowlist, reload listener |
| DNS Failed | Hostname unresolvable from Connector | Tie DNS zone to VPC or add DNS as Resource |
| Connection Failed | No route Connector→DB | Check firewall rules, IP allowlists, security groups |
| No Activity | Client not sending to Connector | Check Client running, Resource access granted, no VPN conflict |

## Related Docs
- [AWS Database Access Guide](https://www.twingate.com/docs/database-access-aws)
- [Azure Database Access Guide](https://www.twingate.com/docs/database-access-azure)
- [GCP Database Access Guide](https://www.twingate.com/docs/database-access-gcp)
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)