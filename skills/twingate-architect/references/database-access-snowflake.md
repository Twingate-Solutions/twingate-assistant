# Snowflake Access with Twingate

## Summary
Route Snowflake traffic (Snowsight UI and database queries) through Twingate Connectors and restrict access via Snowflake network policies scoped to Connector public IPs. Covers both warehouse/API access and Snowsight admin console lockdown.

## Key Information
- Snowflake uses network policies (containing network rules) to allowlist/blocklist IP addresses or private endpoint identifiers
- Both Snowsight UI and database connections (JDBC, ODBC, SnowSQL, APIs) use the same policy framework
- Connector public IPs are found in: Admin Console → Remote Network → Connectors → Public IP
- PrivateLink (AWS/Azure) or Private Service Connect (GCP) eliminates need for public IP allowlisting

## Prerequisites
- Twingate Remote Network configured with at least one Connector deployed
- Snowflake account with `ACCOUNTADMIN` or `SECURITYADMIN` role
- Connector public IP addresses noted for network rule configuration

## Step-by-Step

### Database/Warehouse Access
1. Create Snowflake Network Rule scoped to Connector IPs: Admin → Security → Network Rules → `+ Network Rule`
2. Create Twingate Resource for `myorg-myaccount.snowflakecomputing.com` (or `*.snowflakecomputing.com`), port `443`
3. Connect Twingate Client; configure Snowflake CLI connection

### Snowsight (Admin Console)
1. Create Snowflake Network Policy scoped to Connector IPs: Admin → Security → Network Policies → `+ Network Policy`; activate the policy
2. Create Twingate Resource for `*.snowflake.com` or regional URL (e.g., `apps-api.c1.us-west-2.aws.app.snowflake.com`), port `443`
3. Use same Remote Network as warehouse resources; connect Twingate Client before accessing `https://app.snowflake.com`

## Configuration Values
```toml
# ~/.snowflake/config.toml
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
- **Resource port**: `443` (HTTPS)
- **Account URL format**: `myorg-myaccount.snowflakecomputing.com`

## Gotchas
- **Multiple network policies**: Snowflake applies the most restrictive policy; if user-level policy exists, Connector IPs must be in both account-level and user-level policies
- **Account URL format**: Must use full identifier `myorg-myaccount` — missing segments cause connection failures
- **IP CIDR typos**: Double-check CIDR notation in network rules; common cause of access denied errors
- Twingate Client must be connected — queries fail with IP-blocked error when disconnected

## Troubleshooting (via Admin Console → Recent Activity)
| Symptom | Cause |
|---|---|
| DNS Failed | Connector can't resolve hostname; check DNS/VPC linkage |
| Connection Failed | Connector can't reach destination; check firewall/security groups |
| No Activity | Client not running or another VPN intercepting traffic |

## Related Docs
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)
- [SaaS App Gating Guide](https://www.twingate.com/docs/saas-app-gating)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [Snowflake: Configuring Private Connectivity](https://docs.snowflake.com/en/user-guide/private-snowflake-service)