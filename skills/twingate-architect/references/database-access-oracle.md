# Oracle Cloud Database Access with Twingate

## Summary
Twingate secures access to Oracle Database (on-prem, OCI VMs, or managed services like Autonomous Database/MySQL HeatWave) by routing traffic through Connectors, eliminating public endpoint exposure. Private endpoints are strongly recommended to keep all traffic on Oracle's internal network fabric.

## Key Information
- Default Oracle DB port: **1521**
- Supports: Oracle DB (self-managed), Autonomous Database, MySQL HeatWave, NoSQL Database
- Private endpoint deployment removes need to allowlist Connector public IPs
- OCI Console access can be gated via SSO/SaaS App Gating (no native OCI IP allowlist)

## Prerequisites
- Twingate Remote Network and Connector deployed inside same VCN/LAN as database
- Oracle Database instance accessible via private IP or FQDN
- For public endpoints: Connector public IPs for allowlisting

## Step-by-Step

### OCI Managed Databases (Autonomous DB, HeatWave, NoSQL)
1. Create Twingate Resource using private IP/FQDN; assign to user groups
2. Configure OCI Network Security Groups to allow traffic from Connector private IPs or VCN CIDR
3. Download wallet, configure `sqlnet.ora` `DIRECTORY`, set `TNS_ADMIN`, connect via `sqlplus`

### Self-Managed Oracle Database
1. Create Twingate Resource with private IP/FQDN and port 1521
2. Set firewall/Security List to allow DB port from Connector private IPs only
3. *(Optional)* Configure `sqlnet.ora` Valid Node Checking, reload listener
4. Connect via `sqlplus username/password@"//hostname:1521/orclpdb"`

## Configuration Values

```bash
# sqlnet.ora - Valid Node Checking
tcp.validnode_checking = YES
tcp.invited_nodes = (CONNECTOR_IP_1, CONNECTOR_IP_2)

# Wallet setup (Autonomous DB)
export TNS_ADMIN=/path/to/wallet
export TNS_NAME=<tns_name_from_tnsnames.ora>

# Connect
sqlplus username/password@TNS_NAME
lsnrctl reload  # after sqlnet.ora changes
```

## Gotchas
- `sqlnet.ora` changes require `lsnrctl reload` to take effect
- `tcp.invited_nodes` misconfiguration causes Oracle to reject connections outright
- Public endpoint fallback requires allowlisting Connector **public** IPs in OCI NSGs
- Other VPNs may hijack connections if Client shows no activity in Recent Activity logs
- OCI has no native console IP allowlist — use SSO/SaaS App Gating instead

## Troubleshooting (Recent Activity States)
| State | Cause |
|-------|-------|
| DNS Failed | Connector can't resolve hostname; check DNS Resource/routing |
| Connection Failed | Connector reached but can't reach DB; check firewall/IP allowlist |
| No Activity | Client not sending traffic; check Client running, Resource access, VPN conflicts |

## Related Docs
- [AWS Database Access](https://www.twingate.com/docs/database-access-aws)
- [Azure Database Access](https://www.twingate.com/docs/database-access-azure)
- [GCP Database Access](https://www.twingate.com/docs/database-access-gcp)
- [SaaS App Gating](https://www.twingate.com/docs/saas-app-gating)
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)