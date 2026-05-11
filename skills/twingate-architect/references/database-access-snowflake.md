# Snowflake Access with Twingate

## Page Title
Snowflake Access with Twingate

## Summary
Route Snowflake traffic (Snowsight UI and database queries) through Twingate Connectors and enforce Snowflake network policies scoped to Connector public IPs. Covers both Snowsight (web UI) and database/warehouse access (JDBC, ODBC, SnowSQL, APIs) via port 443/HTTPS.

## Key Information
- Snowflake uses **network policies** (containing network rules) to allowlist IP addresses or private endpoint identifiers
- Twingate Connector public IPs are added to Snowflake network rules/policies to restrict access
- Two separate resource types needed: one for Snowsight (`*.snowflake.com`) and one for database access (`*.snowflakecomputing.com`)
- PrivateLink (AWS/Azure) or Private Service Connect (GCP) eliminates need for IP allowlisting entirely—traffic stays on cloud provider's internal network

## Prerequisites
- Twingate Remote Network configured with at least one Connector deployed
- Connector **public IP addresses** noted (Admin Console → Remote Network → Connectors → Public IP)
- Snowflake account with **ACCOUNTADMIN** or **SECURITYADMIN** role

## Step-by-Step

### Database/Warehouse Access
1. Create Snowflake Network Rule with Connector public IPs (Admin → Security → Network Rules)
2. Create Twingate Resource for `*.snowflakecomputing.com` or `myorg-myaccount.snowflakecomputing.com`, port `443`
3. Connect Twingate Client; configure Snowflake CLI connection

### Snowsight (Web UI)
1. Create Snowflake Network Policy with Connector IPs (Admin → Security → Network Policies) and activate it
2. Create Twingate Resource for `*.snowflake.com` or regional URL (e.g., `apps-api.c1.us-west-2.aws.app.snowflake.com`), port `443`
3. Connect Twingate Client; access `https://app.snowflake.com`

## Configuration Values

**Snowflake CLI (`config.toml`):**
```toml
[connections.myconn]
account = "myaccount"
user = "jondoe"
role = "accountadmin"
```

**Environment variable:**
```bash
export SNOWFLAKE_CONNECTIONS_MYCONN_PASSWORD='abc123'
```

**CLI commands:**
```bash
snow connection list
snow connection set-default myconn
snow sql -q "select current_user();"
```

**Twingate Resource port:** `443` (HTTPS)

## Gotchas
- Snowflake evaluates the **most restrictive** applicable policy—user-level policies override account-level; Connector IPs must be in **both** if both are set
- Use the full account identifier (`myorg-myaccount`) in URLs; partial identifiers cause connection failures
- No activity in Twingate logs = Client not routing traffic (check Client is running, no competing VPN)
- DNS Failed in logs = Connector cannot resolve hostname (check DNS zone tied to VPC)
- Connection Failed in logs = Connector reached but can't connect to destination (check security groups/firewall on both ends)

## Related Docs
- [SaaS App Gating Guide](https://www.twingate.com/docs)
- [Connector Best Practices](https://www.twingate.com/docs)
- [Snowflake Configuring Private Connectivity](https://docs.snowflake.com)
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs)