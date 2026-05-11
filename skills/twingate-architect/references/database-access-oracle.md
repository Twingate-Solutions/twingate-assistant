# Oracle Cloud Database Access with Twingate

## Summary
Twingate secures access to Oracle Database (on-prem, OCI VMs, Autonomous Database, MySQL HeatWave, NoSQL) by routing traffic through Connectors, eliminating public endpoint exposure. Best practice is private endpoints with Connectors deployed inside the same VCN/subnet.

## Key Information
- Default Oracle DB port: **1521**
- Supported: Oracle DB (self-managed), Autonomous Database, MySQL HeatWave, NoSQL Database
- Private endpoints are strongly preferred—no IP allowlisting needed, traffic stays on internal network fabric
- OCI Console access can be gated via Twingate SSO/SaaS App Gating

## Prerequisites
- Twingate Remote Network created with one or more Connectors deployed
- Connectors placed **inside the same VCN** for private endpoint access
- Oracle Database instance accessible on port 1521 (or custom listener port)

## Step-by-Step

### OCI Managed Databases (Autonomous DB, HeatWave, NoSQL)
1. Deploy database with **private endpoint** inside VCN
2. Create Twingate Resource using private IP or FQDN; assign user groups
3. Set OCI Network Security Group/ACL to allow traffic from Connector private IPs or VCN CIDR
4. Download wallet, configure `sqlnet.ora` `DIRECTORY` to wallet path
5. Set `TNS_ADMIN` env var; connect via `sqlplus username/password@TNS_NAME`

### Self-Managed Oracle Database
1. Create Twingate Resource with private IP/FQDN and port 1521
2. Configure firewall/Security List to allow DB port from Connector private IPs
3. (Optional) Configure `sqlnet.ora` Valid Node Checking, then `lsnrctl reload`
4. Connect: `sqlplus username/password@"//host:1521/orclpdb"`

## Configuration Values

```bash
# sqlnet.ora - Valid Node Checking
tcp.validnode_checking = YES
tcp.invited_nodes = (CONNECTOR_IP1, CONNECTOR_IP2)

# Wallet configuration
METHOD_DATA = (DIRECTORY="/path/to/Wallet")

# Environment variables
export TNS_ADMIN=/path/to/Wallet
export TNS_NAME=<tns_alias_from_tnsnames.ora>

# Connection
sqlplus username/password@TNS_NAME
```

## Gotchas
- `sqlnet.ora` changes require `lsnrctl reload` to take effect
- Public endpoint fallback requires allowlisting Connector **public** IPs in OCI NSG or `tcp.invited_nodes`
- OCI has no native console IP allowlist—use SSO/SaaS App Gating instead
- If using Connector public IPs, capture them before configuring firewall rules

## Troubleshooting
| Symptom | Check |
|---|---|
| Connection refused | Connector IP in firewall / `tcp.invited_nodes` |
| Port mismatch | Resource port matches `listener.ora` |
| DNS Failed | DNS zone tied to VPC; DNS server is a Twingate Resource |
| Connection Failed | Route exists Connector→DB; firewall allows port both ends |
| No Activity | Client running; Resource access assigned; no conflicting VPN |

## Related Docs
- [SaaS App Gating Guide](https://www.twingate.com/docs/saas-app-gating)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)
- [Oracle Private Endpoints in OCI](https://docs.oracle.com/en-us/iaas/Content/Database/Tasks/adbprivateendpoint.htm)