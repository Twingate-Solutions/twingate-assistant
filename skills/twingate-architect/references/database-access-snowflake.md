# Snowflake Access with Twingate

## Summary
Route Snowflake traffic (Snowsight UI and database queries) through Twingate Connectors and restrict access via Snowflake network policies scoped to Connector public IPs. Covers both JDBC/ODBC/API query access and Snowsight web UI access. PrivateLink/Private Service Connect eliminates need for IP allowlisting entirely.

## Key Information
- Snowflake uses network policies (containing network rules) to allowlist IP addresses or private endpoint identifiers
- Two separate access surfaces: Snowsight UI (`*.snowflake.com`) and database queries (`*.snowflakecomputing.com`)
- Both use port 443 (HTTPS)
- PrivateLink (AWS/Azure) or Private Service Connect (GCP) keeps traffic off public internet; no IP allowlisting needed

## Prerequisites
- Twingate Remote Network with at least one deployed Connector
- Connector public IP addresses (Admin Console → Remote Network → Connectors → Public IP)
- Snowflake account with `ACCOUNTADMIN` or `SECURITYADMIN` role

## Step-by-Step

### Database/Query Access
1. Create Snowflake Network Rule scoped to Connector IPs (Admin → Security → Network Rules or SQL)
2. Create Twingate Resource for `myorg-myaccount.snowflakecomputing.com`, port 443
3. Connect Twingate Client before running queries

### Snowsight UI Access
1. Create Snowflake Network Policy scoped to Connector IPs (Admin → Security → Network Policies) and activate it
2. Create Twingate Resource for `*.snowflake.com` or regional URL (e.g., `apps-api.c1.us-west-2.aws.app.snowflake.com`), port 443
3. Connect Twingate Client before accessing `https://app.snowflake.com`

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

**Twingate Resource settings:**
- Address: `*.snowflakecomputing.com` (queries) or `*.snowflake.com` (Snowsight)
- Port: `443`

## Gotchas
- Snowflake evaluates the **most restrictive** applicable policy — if user-level policy exists alongside account-level, Connector IPs must appear in **both**
- Use full account identifier (`myorg-myaccount`), not partial — missing segments cause connection failures
- "No Activity" in Twingate logs means Client didn't route traffic to Connector (check Client is running, no conflicting VPN)
- "DNS Failed" means Connector can't resolve hostname — verify DNS is reachable from Connector subnet
- Multiple network policies can conflict; audit all applied policies

## Related Docs
- [Snowflake Private Connectivity](https://docs.snowflake.com/en/user-guide/private-connectivity)
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)
- [SaaS App Gating](https://www.twingate.com/docs/saas-app-gating)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)