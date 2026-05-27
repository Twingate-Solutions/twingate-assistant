# Oracle Cloud Database Access with Twingate

## Summary
Twingate enables secure private access to Oracle Database (self-managed or OCI-managed) by routing traffic through Connectors deployed inside your VCN/LAN. Avoids public internet exposure by enforcing private endpoints and firewall restrictions. Supports Autonomous Database, MySQL HeatWave, NoSQL Database, and self-managed Oracle DB.

## Key Information
- Default Oracle DB port: **1521**
- Connector placement: inside same VCN/LAN as database for private endpoint access
- Private endpoints eliminate need to allowlist Connector public IPs
- OCI Console access can be gated via SSO/SaaS App Gating (no native OCI IP allowlist)

## Prerequisites
- Twingate Remote Network created with Connector deployed
- Connector placed inside VCN (private) or Connector public IP captured (public endpoint fallback)
- Oracle Database instance accessible on port 1521 (or custom port from `listener.ora`)

## Step-by-Step

### OCI Managed Databases (Autonomous DB / MySQL HeatWave / NoSQL)
1. Create Twingate Resource using database private IP or FQDN; assign user groups
2. Set OCI Network Security Group/firewall to allow traffic from Connector private IPs or VCN CIDR
3. Download wallet, configure `sqlnet.ora` `DIRECTORY` to wallet path, set `TNS_ADMIN`, connect via `sqlplus username/password@TNS_NAME`

### Self-Managed Oracle Database
1. Create Twingate Resource with private IP/FQDN and port 1521; assign user groups
2. Configure firewall/Security List to allow DB port from Connector private IPs
3. (Optional) Configure `sqlnet.ora` Valid Node Checking, reload listener
4. Connect: `sqlplus username/password@"//host:1521/orclpdb"`

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Default DB port | `1521` |
| `TNS_ADMIN` env var | Path to unzipped wallet directory |
| `sqlnet.ora` DIRECTORY | Absolute path to wallet |
| `tcp.validnode_checking` | `YES` |
| `tcp.invited_nodes` | Connector IP addresses |

**Listener reload command:**
```bash
lsnrctl reload
```

## Gotchas
- `sqlnet.ora` changes require `lsnrctl reload` to take effect
- Public endpoint fallback requires allowlisting Connector **public** IPs in OCI NSGs or `tcp.invited_nodes`
- Private endpoints: use VCN CIDR/subnet CIDR in access control list, not individual IPs
- OCI has no native console IP allowlist — use Twingate SSO/SaaS App Gating instead
- If no activity in Recent Activity: check Client is running, user has Resource access, no conflicting VPN

## Troubleshooting
| Symptom | Check |
|---------|-------|
| Connection refused | Connector IP in firewall / `tcp.invited_nodes` |
| DNS Failed | DNS zone tied to VPC, DNS server reachable from Connector |
| Connection Failed | Route exists Connector→DB, firewall allows port both ends |
| No Activity | Client running, Resource access granted, no VPN conflict |
| Port mismatch | Twingate Resource port matches `listener.ora` |

## Related Docs
- [AWS Database Access Guide](https://www.twingate.com/docs/database-access-aws)
- [Azure Database Access Guide](https://www.twingate.com/docs/database-access-azure)
- [GCP Database Access Guide](https://www.twingate.com/docs/database-access-gcp)
- [SaaS App Gating Guide](https://www.twingate.com/docs/saas-app-gating)
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)