## Oracle Cloud Database Access with Twingate

Twingate routes traffic to Oracle Database (on-prem, OCI VMs, Exadata, other clouds) and OCI-managed services (Autonomous Database, MySQL HeatWave, NoSQL) through Connectors. The recommended path uses Private Endpoints so all traffic stays on Oracle's internal network; public endpoint access requires adding Connector IPs to firewall or sqlnet.ora rules.

**Key Information**
- Default Oracle listener port: 1521 (configurable in `listener.ora`)
- OCI-managed databases (Autonomous DB, MySQL HeatWave): use Private Endpoint inside VCN, or add Connector public IP to OCI Network Security Groups
- Self-managed Oracle: allowlist Connector IPs in firewall/Security List and optionally in `sqlnet.ora`
- OCI Console (`cloud.oracle.com`): no native IP allowlist; gate via SSO/SaaS App Gating
- Private Endpoints (OCI): Connector in same VCN; traffic never traverses public internet; no public IP allowlisting needed

**Prerequisites**
- Remote Network and Connector deployed (inside OCI VCN for private endpoint path)
- Oracle Database instance or OCI-managed database service
- Connector private IP (private endpoint path) or public IP (public endpoint / sqlnet.ora path)

**Step-by-Step (Autonomous Database)**
1. Create Twingate Resource: Autonomous DB host, port 1521; assign to groups
2. Set ACL to VCN and private subnet CIDR covering Connectors, or add Connector public IP to access control list
3. Download wallet; unzip; edit `sqlnet.ora` to set `DIRECTORY` to wallet absolute path
4. Set env var: `export TNS_ADMIN=/path/to/wallet`; get TNS name from `tnsnames.ora`
5. Connect: `sqlplus username/password@TNS_NAME`

**Step-by-Step (Self-managed Oracle)**
1. Create Twingate Resource: DB private IP or FQDN, port 1521; assign to groups
2. Configure firewall/Security List to allow Connector private IP on port 1521
3. Optionally add to `sqlnet.ora`: `tcp.validnode_checking = YES` and `tcp.invited_nodes = (ip1, ip2)`
4. Reload listener: `lsnrctl reload`
5. Connect: `sqlplus username/password@"//host.privatesubnet.oraclevcn.com:1521/orclpdb"`

**Configuration Values**
- `TNS_ADMIN=/path/to/wallet` -- tells sqlplus where to find wallet and tnsnames.ora
- `tcp.validnode_checking = YES` and `tcp.invited_nodes = (ip1, ip2)` in sqlnet.ora
- `lsnrctl reload` -- required after sqlnet.ora changes (full listener restart not needed)

**Gotchas**
- sqlnet.ora changes require `lsnrctl reload` to take effect -- forgetting this is a common misconfiguration
- Autonomous Database wallet path in `sqlnet.ora` must be the absolute path, not a relative path
- OCI has no console-level IP allowlist; Twingate + SSO is the only way to restrict Oracle Cloud Console access
- Port mismatches: default is 1521 but custom listener configs are common -- verify in `listener.ora`

**Related Docs**
- /docs/database-access-guide
- /docs/saas-app-gating
- /docs/connector-best-practices
