# Oracle Cloud Database Access with Twingate

## Summary
Twingate enables secure private access to Oracle Database (on-prem, OCI, or other clouds) and OCI-managed services (Autonomous Database, MySQL HeatWave, NoSQL) by routing traffic through Connectors. The recommended approach uses private endpoints to keep traffic off the public internet entirely. Firewall rules and Oracle's `sqlnet.ora` Valid Node Checking restrict access to Connector IPs only.

## Key Information
- Supports: Oracle DB (self-managed), Autonomous Database, MySQL HeatWave, NoSQL Database
- Default Oracle DB port: **1521**
- Private endpoint deployment eliminates need to allowlist Connector public IPs
- OCI Console access can be gated via Twingate SSO/SaaS App Gating

## Prerequisites
- Twingate Remote Network and Connector deployed inside the same VCN/LAN as the database (for private endpoints)
- Connector public IP captured if using public endpoints
- Oracle Database instance accessible on port 1521 (or custom port from `listener.ora`)

## Step-by-Step

### OCI Managed Databases (Autonomous DB, HeatWave, NoSQL)
1. Create Twingate Resource using database private IP or FQDN
2. Set OCI Network Security Group / ACL to allow traffic from Connector private IPs or VCN/subnet CIDR
3. Download wallet, configure `sqlnet.ora` `DIRECTORY`, set `TNS_ADMIN`, connect via `sqlplus`

### Self-Managed Oracle Database
1. Create Twingate Resource with private IP/FQDN and correct port
2. Allow DB port traffic from Connector private IPs in firewall/Security List
3. (Optional) Configure `sqlnet.ora` Valid Node Checking, reload listener
4. Connect via `sqlplus username/password@"//host:1521/service"`

## Configuration Values

```bash
# sqlnet.ora - Valid Node Checking
tcp.validnode_checking = YES
tcp.invited_nodes = (CONNECTOR_IP1, CONNECTOR_IP2)

# Wallet setup for Autonomous DB
# In sqlnet.ora:
METHOD_DATA = (DIRECTORY="/path/to/wallet")

export TNS_ADMIN=/path/to/wallet
export TNS_NAME=nw0xyz123_high

sqlplus username/password@TNS_NAME
```

```bash
# Reload Oracle listener after sqlnet.ora changes
lsnrctl reload
```

## Gotchas
- Changes to `sqlnet.ora` require `lsnrctl reload` to take effect
- Missing/incorrect `tcp.invited_nodes` entries cause Oracle to refuse connections
- Public endpoint fallback requires allowlisting Connector **public** IPs in OCI NSGs
- No native OCI Console IP allowlist — use Twingate SSO/SaaS App Gating instead
- If using custom Oracle port, match it exactly in the Twingate Resource definition

## Troubleshooting
| Symptom | Check |
|---|---|
| DNS Failed | Connector can't resolve hostname; verify DNS zone tied to VPC |
| Connection Failed | Route exists between Connector and DB; IP allowlists and firewall ports correct |
| No Activity | Client running, has Resource access, no conflicting VPN |
| Timeouts | Connector online and reachable |

## Related Docs
- [AWS Database Access Guide](https://www.twingate.com/docs/database-access-aws)
- [Azure Database Access Guide](https://www.twingate.com/docs/database-access-azure)
- [GCP Database Access Guide](https://www.twingate.com/docs/database-access-gcp)
- [SaaS App Gating Guide](https://www.twingate.com/docs/saas-app-gating)
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)