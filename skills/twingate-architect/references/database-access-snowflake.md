# Snowflake Access with Twingate

## Summary
Route Snowflake traffic (Snowsight UI and database queries) through Twingate Connectors and restrict access via Snowflake network policies scoped to Connector public IPs. Covers both warehouse/API access and Snowsight admin console access. PrivateLink/Private Service Connect is the preferred approach for cloud deployments.

## Key Information
- Snowflake uses **network policies** (containing network rules) to allowlist IP addresses or private endpoint identifiers
- Same network policy framework applies to both Snowsight UI and database/warehouse connections
- Connector public IPs found at: Admin Console → Remote Network → Connectors → Public IP
- Two resource types needed: one for `*.snowflakecomputing.com` (queries) and one for `*.snowflake.com` (Snowsight)
- PrivateLink/PSC eliminates need to manage public IP allowlists entirely

## Prerequisites
- Twingate Remote Network with at least one Connector deployed in a secure egress location
- Snowflake account with `ACCOUNTADMIN` or `SECURITYADMIN` role
- Connector public IP addresses noted before configuring network policies

## Step-by-Step

### Database/Warehouse Access
1. Create Network Rule in Snowflake: Admin → Security → Network Rules → add Connector IPs
2. Create Twingate Resource: URL `myorg-myaccount.snowflakecomputing.com`, port `443`
3. Connect Twingate Client before issuing queries

### Snowsight UI Access
1. Create Network Policy in Snowflake: Admin → Security → Network Policies → add Connector IPs → activate policy
2. Create Twingate Resource: URL `*.snowflake.com` or regional URL (e.g., `apps-api.c1.us-west-2.aws.app.snowflake.com`), port `443`, same Remote Network
3. Connect Twingate Client before accessing `app.snowflake.com`

## Configuration Values

```toml
# Snowflake CLI config.toml
[connections.myconn]
account = "myaccount"
user = "jondoe"
role = "accountadmin"
```

```bash
export SNOWFLAKE_CONNECTIONS_MYCONN_PASSWORD='abc123'
snow connection set-default myconn
snow sql -q "select current_user();"
```

| Parameter | Value |
|-----------|-------|
| Resource port | `443` |
| Resource URL (queries) | `myorg-myaccount.snowflakecomputing.com` |
| Resource URL (Snowsight) | `*.snowflake.com` |

## Gotchas
- **Multiple network policies**: Snowflake applies the most restrictive policy; if user-level policy exists, Connector IPs must be in **both** account-level and user-level policies
- **Account URL format**: Must use full identifier `myorg-myaccount` — missing segments cause connection failures
- **PrivateLink**: When using AWS/Azure/GCP private connectivity, allowlisting public IPs is unnecessary — use private endpoint identifiers instead
- Disconnected Twingate Client produces HTTP 250001 error: "Incoming request with IP/Token is not allowed"

## Troubleshooting
| Symptom | Check |
|---------|-------|
| Access denied | Connector IP in network rule, policy applied to account, CIDR notation correct |
| DNS Failed (Recent Activity) | DNS zone tied to VPC, DNS server reachable from Connector |
| Connection Failed | Route exists Connector→Snowflake, firewall allows port 443 |
| No Activity | Client running, Resource access granted, no conflicting VPN |

## Related Docs
- [Snowflake Configuring Private Connectivity](https://docs.snowflake.com)
- [Twingate SaaS App Gating](https://www.twingate.com/docs/saas-app-gating)
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)