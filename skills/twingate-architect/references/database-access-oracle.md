# Oracle Cloud Database Access with Twingate

## Summary
Twingate secures access to Oracle Database (on-prem, OCI VMs, Autonomous Database, MySQL HeatWave, NoSQL) by routing traffic through Connectors deployed inside the same network as the database. Private endpoints are strongly preferred over public endpoints to avoid internet exposure.

## Key Information
- Default Oracle DB port: **1521**
- Connector placement: inside the same VCN/subnet as the database (private IP preferred)
- Supports: Oracle DB, Autonomous Database, MySQL HeatWave, OCI NoSQL
- OCI Console gating requires SSO integration (no native IP allowlist in OCI)

## Prerequisites
- Twingate Remote Network created with Connector deployed in same VCN/LAN as database
- Oracle Database instance accessible (private or public endpoint)
- Connector private or public IP addresses noted for firewall rules

## Step-by-Step

### OCI Managed Databases (Autonomous DB, HeatWave, NoSQL)
1. **Create Twingate Resource** — use private IP/FQDN, assign to user groups
2. **Configure network restrictions** — allowlist Connector IPs in OCI Network Security Groups or VCN CIDR in access control list
3. **Connect** — download wallet, set `sqlnet.ora` DIRECTORY, export `TNS_ADMIN` and `TNS_NAME`, run `sqlplus`

### Self-Managed Oracle Database
1. **Create Twingate Resource** — use private IP/FQDN, port 1521 (or per `listener.ora`)
2. **Configure firewall** — allow DB port from Connector private IPs only
3. **Configure `sqlnet.ora`** (optional) — enable Valid Node Checking
4. **Connect** via SQL*Plus using private FQDN

## Configuration Values

### sqlnet.ora (Valid Node Checking)
```
tcp.validnode_checking = YES
tcp.invited_nodes = (CONNECTOR_IP_1, CONNECTOR_IP_2)
```

### Wallet-based Connection (Autonomous DB)
```bash
export TNS_ADMIN=/path/to/wallet
export TNS_NAME=<name_from_tnsnames.ora>
sqlplus username/password@TNS_NAME
```

### Direct Connection (Self-managed)
```bash
sqlplus username/password@"//hostname.oraclevcn.com:1521/orclpdb"
```

### Listener Reload After sqlnet.ora Changes
```bash
lsnrctl reload
```

## Gotchas
- Changes to `sqlnet.ora` require `lsnrctl reload` — connections won't update automatically
- `tcp.invited_nodes` missing or incorrect → Oracle rejects connection entirely
- Port mismatch between Twingate Resource and `listener.ora` causes silent failures
- OCI has no native console IP allowlist; use SSO + SaaS App Gating to restrict `cloud.oracle.com`
- If no activity shows in Twingate console, check that no other VPN is intercepting the connection

## Troubleshooting Quick Reference
| Symptom | Likely Cause |
|---|---|
| DNS Failed | Connector can't resolve hostname; check DNS Resource or VPC DNS zone |
| Connection Failed | Route missing or firewall blocking port on Connector→DB path |
| No Activity | Client not running, no Resource access, or VPN hijacking traffic |
| Slow connections | Connector health issue or upstream firewall throttling |

## Related Docs
- [SaaS App Gating Guide](https://www.twingate.com/docs)
- [Connector Best Practices](https://www.twingate.com/docs)
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs)
- [Oracle Private Endpoints in OCI](https://docs.oracle.com/en-us/iaas/Content/Database/Tasks/adbprivateaccess.htm)