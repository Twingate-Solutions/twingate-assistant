# Oracle Cloud Database Access with Twingate

## Summary
Configure Twingate to provide secure private access to Oracle Database (self-managed or OCI-managed services like Autonomous Database, MySQL HeatWave, NoSQL). Traffic routes through Connectors deployed inside the same VCN/LAN, avoiding public internet exposure. Supports both private endpoint (recommended) and public endpoint (fallback) configurations.

## Key Information
- Default Oracle DB port: **1521** (or as defined in `listener.ora`)
- Connector placement: inside same VCN/subnet as database for private endpoint access
- Supports: Oracle DB on-prem/VM, Autonomous Database, MySQL HeatWave, NoSQL Database
- Private endpoints eliminate need to allowlist Connector public IPs

## Prerequisites
- Twingate Remote Network created with Connector(s) deployed
- Connector placed **inside the same VCN** for private endpoint access
- Oracle Database instance accessible on port 1521 (or custom port)
- Connector private or public IP addresses noted for firewall rules

## Step-by-Step

### OCI Managed Databases (Autonomous DB, HeatWave, NoSQL)
1. Add Twingate Resource using database private IP or FQDN
2. Restrict OCI Network Security Groups/firewall to Connector private IPs (or VCN CIDR)
3. For Autonomous DB: download wallet, configure `sqlnet.ora` `DIRECTORY` path, set `TNS_ADMIN` env var, connect via `sqlplus`

### Self-Managed Oracle Database
1. Add Twingate Resource with private IP/FQDN and port 1521
2. Configure firewall/Security List to allow DB port from Connector IPs only
3. (Optional) Configure `sqlnet.ora` Valid Node Checking with Connector IPs, reload listener
4. Connect via `sqlplus username/password@"//hostname:1521/orclpdb"`

## Configuration Values

### sqlnet.ora (Valid Node Checking)
```
tcp.validnode_checking = YES
tcp.invited_nodes = (1.2.3.4, 1.2.3.5)  # Connector IPs
```

### Wallet/Autonomous DB Environment
```bash
export TNS_ADMIN=/Users/<User>/Downloads/Wallet
export TNS_NAME=nw0xyz123_high
sqlplus username/password@TNS_NAME
```

### Listener Reload
```bash
lsnrctl reload
```

## Gotchas
- `sqlnet.ora` changes require `lsnrctl reload` to take effect — connections won't update automatically
- **No Activity** in Twingate logs = Client never sent traffic to Connector (check Client is running, no conflicting VPN)
- **DNS Failed** = Connector can't resolve hostname; ensure DNS zone is tied to VPC and reachable from Connector
- **Connection Failed** = Connector reached destination but was blocked; verify IP allowlists and firewall rules on both sides
- OCI Console has no native IP allowlist — use Twingate SSO/SaaS App Gating instead
- Port mismatch between Resource config and actual listener port is a common failure point

## Related Docs
- [AWS Database Access Guide](https://www.twingate.com/docs/database-access-aws)
- [Azure Database Access Guide](https://www.twingate.com/docs/database-access-azure)
- [GCP Database Access Guide](https://www.twingate.com/docs/database-access-gcp)
- [SaaS App Gating Guide](https://www.twingate.com/docs/saas-app-gating)
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)
- [Oracle Private Endpoints in OCI](https://docs.oracle.com/en-us/iaas/Content/Database/Tasks/adbprivateaccess.htm)