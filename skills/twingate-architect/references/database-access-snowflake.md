# Snowflake Access with Twingate

## Summary
Route Snowflake traffic (Snowsight UI and database queries) through Twingate Connectors and enforce Snowflake network policies scoped to Connector public IPs. Covers both warehouse/API access and the Snowsight admin console. Optionally use PrivateLink/Private Service Connect to avoid public IP allowlisting entirely.

## Key Information
- Snowflake uses **network policies** (containing **network rules**) to allowlist IP addresses or private endpoint identifiers
- Twingate Connector public IPs are added to Snowflake network rules/policies
- Two separate resource types need protection: **Snowsight UI** (`*.snowflake.com`) and **database/warehouse access** (`*.snowflakecomputing.com`)
- Both use port **443 (HTTPS)**
- PrivateLink (AWS/Azure) or Private Service Connect (GCP) eliminates need for public IP allowlisting

## Prerequisites
- Twingate Remote Network deployed with at least one Connector
- Connector public IPs noted (Admin Console → Remote Network → Connectors → Public IP)
- Snowflake account with `ACCOUNTADMIN` or `SECURITYADMIN` role

## Step-by-Step

### Database/Warehouse Access
1. Create Snowflake **Network Rule** scoped to Connector public IPs (Snowsight UI: Admin → Security → Network Rules, or via SQL)
2. Create Twingate Resource for `myorg-myaccount.snowflakecomputing.com` (port 443)
3. Connect Twingate Client; configure Snowflake CLI connection

### Snowsight Console Access
1. Create Snowflake **Network Policy** scoped to Connector public IPs (Admin → Security → Network Policies) and activate it
2. Create Twingate Resource for `*.snowflake.com` or regional URL (port 443, same Remote Network)
3. Connect Twingate Client before accessing `https://app.snowflake.com`

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
| Resource port | `443` |
| Snowsight URL pattern | `*.snowflake.com` |
| Warehouse URL pattern | `*.snowflakecomputing.com` |

## Gotchas
- **Multiple network policies**: Snowflake applies the most restrictive policy — ensure Connector IPs appear in both user-level and account-level policies if both are set
- **Full account identifier required**: Use `myorg-myaccount` format; missing segments cause connection failures
- Disconnected Twingate Client = immediate access denial (error 250001, IP not allowed)
- Snowsight and warehouse access require **separate** Twingate Resources and Snowflake policy entries

## Troubleshooting
| Symptom | Check |
|---------|-------|
| Access denied | Connector IP in network rule; policy applied to account |
| DNS Failed (Recent Activity) | Connector can resolve hostname; DNS server accessible |
| Connection Failed | Route exists Connector→DB; firewall allows port 443 |
| No Activity | Twingate Client running; no conflicting VPN |

## Related Docs
- [SaaS App Gating Guide](https://www.twingate.com/docs/saas-app-gating)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [Snowflake Configuring Private Connectivity](https://docs.snowflake.com/en/user-guide/private-snowflake-service)
- Twingate Troubleshooting Guide