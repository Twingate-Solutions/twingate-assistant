# Snowflake Access with Twingate

## Summary
Route Snowflake traffic (Snowsight UI and database queries) through Twingate Connectors and restrict access via Snowflake network policies scoped to Connector public IPs. Covers both warehouse/API access and Snowsight admin console lockdown. PrivateLink eliminates the need for IP allowlisting entirely.

## Key Information
- Snowflake uses **network policies** (containing network rules) to restrict access by IP or private endpoint ID
- Same policy framework applies to both Snowsight UI and database/warehouse connections
- Connector public IPs are the allowlisted identifiers in non-PrivateLink deployments
- PrivateLink (AWS/Azure) or Private Service Connect (GCP) keeps traffic off public internet—no IP allowlisting needed

## Prerequisites
- Twingate Remote Network deployed with at least one Connector
- Connector public IP(s) noted from: Admin Console → Remote Network → Connectors → Public IP
- Snowflake account with `ACCOUNTADMIN` or `SECURITYADMIN` role

## Step-by-Step

### Database/Warehouse Access
1. Create **Network Rule** in Snowflake (Admin → Security → Network Rules) scoped to Connector public IPs
2. Create Twingate Resource for `myorg-myaccount.snowflakecomputing.com` (or `*.snowflakecomputing.com`), port `443`
3. Connect Twingate Client before running queries

### Snowsight UI Access
1. Create **Network Policy** in Snowflake (Admin → Security → Network Policies) scoped to Connector public IPs; activate it
2. Create Twingate Resource for `*.snowflake.com` or regional URL (e.g., `apps-api.c1.us-west-2.aws.app.snowflake.com`), port `443`
3. Use same Remote Network as warehouse resources

## Configuration Values

### Snowflake CLI (`config.toml`)
```toml
[connections.myconn]
account = "myaccount"
user = "jondoe"
role = "accountadmin"
```

### Environment Variable
```bash
export SNOWFLAKE_CONNECTIONS_MYCONN_PASSWORD='abc123'
```

### CLI Commands
```bash
snow connection add
snow connection list
snow connection set-default myconn
snow sql -q "select current_user();"
```

### Twingate Resource Settings
| Field | Value |
|-------|-------|
| Address | `myorg-myaccount.snowflakecomputing.com` or `*.snowflake.com` |
| Port | `443` |

## Gotchas
- **Multiple network policies**: Snowflake applies the most restrictive policy. If user-level policy exists, Connector IPs must be in **both** user-level and account-level policies
- **Account URL format**: Must use full identifier `myorg-myaccount`—missing segments cause connection failures
- **No Activity in logs**: Client not sending traffic to Connector; check Client is running and no other VPN is intercepting
- **DNS Failed**: Connector can't resolve hostname—verify DNS zone is accessible from Connector's network
- **IP CIDR typos**: Verify exact notation in network rules; mismatches silently block access

## Related Docs
- [Snowflake Configuring Private Connectivity](https://docs.snowflake.com)
- [Twingate SaaS App Gating Guide](https://www.twingate.com/docs/saas-app-gating)
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)