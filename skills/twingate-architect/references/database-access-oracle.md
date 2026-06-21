# Oracle Cloud Database Access with Twingate

## Summary
Twingate secures access to Oracle Database (on-premises, OCI VMs, or managed services like Autonomous Database/MySQL HeatWave) by routing traffic through Connectors, eliminating public endpoints. Private endpoints are strongly recommended to keep traffic on Oracle's internal network fabric.

## Key Information
- Default Oracle DB port: **1521**
- Covers: Oracle Database (self-managed), Autonomous Database, MySQL HeatWave, NoSQL Database
- Private endpoint deployment eliminates need to allowlist Connector public IPs
- OCI Console access can be gated via SSO/SaaS App Gating (no native OCI IP allowlist)

## Prerequisites
- Twingate Remote Network created with Connector(s) deployed inside the same VCN/LAN as the database
- Connector placed in same VCN for private endpoint access; public IP captured if public endpoint required
- Oracle DB instance accessible on port 1521 (or custom port from `listener.ora`)

## Step-by-Step

### OCI Managed Databases (Autonomous DB / MySQL HeatWave)
1. Deploy database with private endpoint inside VCN (recommended)
2. Create Twingate Resource using private IP or FQDN; assign user groups
3. Configure OCI Network Security Groups to allow traffic from Connector private IPs or VCN CIDR
4. Download wallet, configure `sqlnet.ora` `DIRECTORY` to wallet absolute path
5. Set `TNS_ADMIN` env var; connect via `sqlplus username/password@TNS_NAME`

### Self-Managed Oracle Database
1. Create Twingate Resource with private IP/FQDN and port 1521
2. Configure firewall/Security List to allow DB port from Connector private IPs only
3. (Optional) Configure `sqlnet.ora` Valid Node Checking, then reload listener
4. Connect: `sqlplus username/password@"//hostname:1521/orclpdb"`

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

### Listener Reload
```bash
lsnrctl reload
```

## Gotchas
- Changes to `sqlnet.ora` require `lsnrctl reload` to take effect
- Missing/incorrect `tcp.invited_nodes` causes Oracle to refuse connections entirely
- Public endpoint fallback requires allowlisting Connector **public** IPs in OCI Network Security Groups
- If another VPN is active, it may hijack connections before Twingate Client captures traffic
- DNS failures: ensure hosted zone is tied to VPC and DNS server is reachable from Connector

## Troubleshooting Reference
| Symptom | Check |
|---|---|
| Connection refused | Connector IP in firewall + `tcp.invited_nodes` |
| Port mismatch | Resource port matches `listener.ora` |
| DNS Failed | Hosted zone tied to VPC; DNS reachable from Connector |
| Connection Failed | Route exists Connector→DB; firewall allows port both ends |
| No Activity | Client running; Resource access granted; no VPN conflict |

## Related Docs
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)
- [OCI Private Endpoints](https://docs.oracle.com/en-us/iaas/Content/Database/Tasks/adbprivateendpoint.htm)
- AWS/Azure/GCP Database Access Guides
- SaaS App Gating Guide
- Connector Best Practices