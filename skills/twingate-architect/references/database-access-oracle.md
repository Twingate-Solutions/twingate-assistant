# Oracle Cloud Database Access with Twingate

## Summary
Twingate secures access to Oracle Database (on-prem, OCI, or other clouds) and OCI managed services (Autonomous Database, MySQL HeatWave, NoSQL) by routing traffic through Connectors. Private endpoints are strongly preferred to avoid public internet exposure. Firewall and listener rules restrict access to Connector IPs only.

## Key Information
- Default Oracle DB port: **1521**
- Supported: Oracle DB (self-managed), Autonomous Database, MySQL HeatWave, NoSQL Database
- Private endpoint deployment eliminates need to allowlist public IPs
- OCI Console access can be gated via Twingate SSO/SaaS App Gating

## Prerequisites
- Twingate Remote Network created with one or more Connectors deployed
- Connectors placed **inside the same VCN/LAN** as the database (private endpoint setup)
- Oracle Database instance accessible on port 1521 (or custom port from `listener.ora`)

## Step-by-Step

### OCI Managed Databases (Autonomous DB, HeatWave, NoSQL)
1. Deploy database with **private endpoint** inside VCN
2. Add Resource in Twingate Admin Console using private IP or FQDN; assign user groups
3. Set OCI Network Security Group/firewall ACL to allow Connector private IPs or VCN CIDR
4. Download wallet, configure `sqlnet.ora` with wallet directory, set `TNS_ADMIN`
5. Connect via `sqlplus username/password@TNS_NAME`

### Self-Managed Oracle Database
1. Add Resource in Twingate Admin Console (private IP/FQDN, port 1521)
2. Restrict firewall to Connector private IPs / VCN CIDR
3. Optionally configure `sqlnet.ora` valid node checking and reload listener
4. Connect: `sqlplus username/password@"//host:1521/orclpdb"`

## Configuration Values

```bash
# sqlnet.ora - Valid Node Checking
tcp.validnode_checking = YES
tcp.invited_nodes = (1.2.3.4, 1.2.3.5)  # Connector IPs

# Wallet setup for Autonomous DB
export TNS_ADMIN=/path/to/wallet
export TNS_NAME=nw0xyz123_high

# Listener reload after sqlnet.ora changes
lsnrctl reload

# Connection string
sqlplus username/password@"//host.oraclevcn.com:1521/orclpdb"
```

## Gotchas
- `sqlnet.ora` changes require `lsnrctl reload` to take effect
- `tcp.invited_nodes` missing/incorrect causes Oracle to reject connections silently
- Public IP allowlisting only needed when Connector traverses the internet
- OCI Console has no native IP allowlist; use Twingate SSO/SaaS App Gating instead
- If no activity shows in Twingate logs, check that Client is running and no other VPN is intercepting traffic
- DNS failures indicate Connector cannot resolve hostname — verify DNS zone is tied to VPC and reachable

## Troubleshooting
| Symptom | Check |
|---|---|
| Connection refused | Connector IP in firewall + `tcp.invited_nodes` |
| DNS Failed | DNS zone tied to VPC, DNS server accessible from Connector |
| Connection Failed | Route between Connector and DB, firewall port rules |
| No Activity | Twingate Client running, Resource access granted, no conflicting VPN |

## Related Docs
- [SaaS App Gating Guide](https://www.twingate.com/docs)
- [Connector Best Practices](https://www.twingate.com/docs)
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs)
- [Oracle Private Endpoints in OCI](https://docs.oracle.com/en-us/iaas/Content/Database/Tasks/adbprivateaccess.htm)