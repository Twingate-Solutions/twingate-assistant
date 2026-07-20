# Oracle Cloud Database Access with Twingate

## Summary
Twingate secures access to Oracle Database (on-prem, OCI VMs, or managed services like Autonomous Database) by routing traffic through Connectors, enabling private endpoints without public internet exposure. Supports Oracle DB, Autonomous Database, MySQL HeatWave, and NoSQL Database on OCI.

## Key Information
- Default Oracle Database port: **1521**
- Connector placement: inside same VCN/LAN as database for private endpoint access
- Private endpoints eliminate need to manage Connector public IP allowlists
- OCI Console access can be gated via SSO/SaaS App Gating (no native IP allowlist in OCI)

## Prerequisites
- Twingate Remote Network created with Connector(s) deployed in target VCN/LAN
- Oracle Database instance (self-managed or OCI-managed)
- For private endpoints: Connector on same private network as database
- For public endpoints: Connector public IPs collected for allowlisting

## Step-by-Step

### OCI-Managed Databases (Autonomous DB / MySQL HeatWave / NoSQL)
1. **Create Twingate Resource** — use database private IP or FQDN; assign to user groups
2. **Configure network restrictions** — allow Connector private IPs via OCI Network Security Groups or Security Lists; set ACL to VCN/private subnet CIDR
3. **Connect** — download wallet, configure `sqlnet.ora` with wallet path, set `TNS_ADMIN`, connect via `sqlplus`

### Self-Managed Oracle Database
1. **Create Twingate Resource** — use private IP/FQDN, port 1521 (or custom per `listener.ora`)
2. **Configure firewall** — allow DB port only from Connector private IPs
3. **Configure listener restrictions** (optional) — edit `sqlnet.ora`, reload listener
4. **Connect** — `sqlplus username/password@"//host:1521/orclpdb"`

## Configuration Values

### sqlnet.ora (Valid Node Checking)
```
tcp.validnode_checking = YES
tcp.invited_nodes = (1.2.3.4, 1.2.3.5)  # Connector IPs
```

### Wallet Setup (Autonomous DB)
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
- `sqlnet.ora` changes require `lsnrctl reload` to take effect
- Changes to `tcp.invited_nodes` without reload will silently fail to update
- Public endpoints require Connector public IPs in both firewall rules AND `sqlnet.ora`
- OCI has no native console IP allowlist — use SSO/SaaS App Gating instead
- Twingate Client must be running; other VPNs may hijack connections (check Recent Activity if "No Activity" shown)
- DNS failures: ensure DNS hosted zone is tied to VPC and reachable from Connector

## Troubleshooting Reference
| Symptom | Cause | Fix |
|---|---|---|
| Connection refused | IP not in `tcp.invited_nodes` or firewall | Update allowlist, reload listener |
| DNS Failed | Connector can't resolve hostname | Check DNS zone, routes |
| Connection Failed | Connector can't reach DB | Check routes, firewall, security groups |
| No Activity | Client not sending traffic | Check Client running, Resource access, VPN conflicts |

## Related Docs
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)
- AWS/Azure/GCP Database Access Guides
- SaaS App Gating Guide
- Connector Best Practices