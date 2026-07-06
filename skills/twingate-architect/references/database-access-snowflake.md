# Snowflake Access with Twingate

## Summary
Secures Snowflake access (both Snowsight UI and database/warehouse queries) by routing traffic through Twingate Connectors and restricting Snowflake network policies to Connector public IPs. Works for JDBC, ODBC, SnowSQL, APIs, and the Snowsight web console.

## Key Information
- Snowflake uses **network policies** (containing network rules) to allowlist IP addresses or private endpoint identifiers
- Two separate access surfaces to secure: **Snowsight UI** (`*.snowflake.com`) and **database/warehouse** (`*.snowflakecomputing.com`)
- Both use the same network policy framework; port 443 (HTTPS) for both
- PrivateLink (AWS/Azure) or Private Service Connect (GCP) eliminates need to allowlist public IPs entirely

## Prerequisites
- Twingate Remote Network with at least one Connector deployed
- Connector's public IP noted (Admin Console → Remote Network → Connectors → Public IP)
- Snowflake account with `ACCOUNTADMIN` or `SECURITYADMIN` role

## Step-by-Step

### Database/Warehouse Access
1. Create Snowflake **Network Rule** scoped to Connector public IPs (Snowsight: Admin → Security → Network Rules)
2. Create Twingate Resource for `*.snowflakecomputing.com` or `myorg-myaccount.snowflakecomputing.com`, port `443`
3. Connect Twingate Client before running queries

### Snowsight UI Access
1. Create Snowflake **Network Policy** scoped to Connector IPs (Admin → Security → Network Policies) and activate it
2. Create Twingate Resource for `*.snowflake.com` or regional Snowsight URL, port `443`
3. Use same Remote Network as warehouse resources

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

## Gotchas
- **Multiple network policies**: Snowflake applies the most restrictive policy. User-level policies override account-level — ensure Connector IPs are in **both**
- **Account URL format**: Must use full identifier `myorg-myaccount` — missing segments cause connection failures
- **No Activity in Twingate logs**: Client not running, no resource access, or another VPN intercepting traffic
- **DNS Failed**: Connector can't resolve hostname — check DNS routing from Connector's network
- **Snowsight vs. warehouse**: Separate Twingate Resources needed for each domain

## Related Docs
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)
- [SaaS App Gating Guide](https://www.twingate.com/docs/saas-app-gating)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [Snowflake Configuring Private Connectivity](https://docs.snowflake.com/en/user-guide/private-link-overview)
- MongoDB/Redis Access Guides (parallel database patterns)