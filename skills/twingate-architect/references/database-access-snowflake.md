---
source: https://www.twingate.com/docs/database-access-snowflake
type: docs
fetched: 2026-08-14
source_version: d4cbc04ea55a8391502871a2a5da39b351b6db602d2fc932ae105a13875cc626
---

# Snowflake Access with Twingate

## Summary
Route Snowflake traffic (Snowsight UI and database queries) through Twingate Connectors and restrict access via Snowflake network policies scoped to Connector public IPs. Covers both HTTPS/UI access and JDBC/ODBC/API query access on port 443.

## Key Information
- Snowflake uses network policies + network rules to allowlist IP addresses or private endpoint identifiers
- Twingate Connector public IPs are added to Snowflake network rules/policies to gate access
- Same framework applies to both Snowsight (web UI) and warehouse/database connections
- PrivateLink (AWS/Azure) or Private Service Connect (GCP) eliminates need for public IP allowlisting

## Prerequisites
- Twingate Remote Network configured with at least one Connector deployed
- Connector public IP addresses noted (Admin Console → Remote Network → Connectors → Public IP)
- Snowflake account with `ACCOUNTADMIN` or `SECURITYADMIN` role

## Step-by-Step

### Database/Query Access
1. Create Network Rule in Snowflake scoped to Connector IPs: Snowsight → Admin → Security → Network Rules → `+ Network Rule`
2. Create Twingate Resource for `myorg-myaccount.snowflakecomputing.com` (or `*.snowflakecomputing.com`), port `443`
3. Connect Twingate Client; configure Snowflake CLI connection

### Snowsight (Web UI) Access
1. Create Network Policy in Snowflake: Admin → Security → Network Policies → `+ Network Policy` → activate policy
2. Create Twingate Resource for `*.snowflake.com` or regional URL (e.g., `apps-api.c1.us-west-2.aws.app.snowflake.com`), port `443`
3. Use same Remote Network as warehouse resources

## Configuration Values

```toml
# config.toml (Snowflake CLI)
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
| Port | `443` (HTTPS) |
| Resource URL (DB) | `myorg-myaccount.snowflakecomputing.com` |
| Resource URL (UI) | `*.snowflake.com` or regional URL |

## Gotchas
- **Multiple network policies**: Snowflake applies the most restrictive policy; Connector IPs must be in both user-level and account-level policies if both exist
- **Account URL format**: Must use full identifier `myorg-myaccount` — partial identifiers cause connection failures
- **Policy not active**: Network policy must be explicitly activated after creation
- **Twingate disconnected**: Queries fail with `Incoming request with IP... is not allowed to access Snowflake`
- **DNS Failed in Recent Activity**: Ensure DNS zone is tied to VPC and resolvable from Connector

## Troubleshooting
- **No Activity**: Client not running, no Resource access, or another VPN intercepting traffic
- **Connection Failed**: Route missing between Connector and Snowflake, or firewall blocking port 443
- **Access Denied**: Connector IP missing from network rule or typo in CIDR notation

## Related Docs
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)
- [Snowflake Configuring Private Connectivity](https://docs.snowflake.com/en/user-guide/privatelink-azure)
- [SaaS App Gating](https://www.twingate.com/docs/saas-app-gating)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)