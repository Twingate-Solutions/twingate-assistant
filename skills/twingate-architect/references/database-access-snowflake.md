# Snowflake Access with Twingate

## Summary
Configure Twingate to route Snowflake traffic (Snowsight UI and database queries) through Connectors, then restrict Snowflake access via network policies scoped to Connector public IPs. Covers both warehouse/API access and Snowsight admin console lockdown.

## Key Information
- Snowflake uses **network policies** (containing network rules) to allowlist IP addresses or private endpoint identifiers
- Two separate resources needed: one for database access (`*.snowflakecomputing.com`) and one for Snowsight (`*.snowflake.com`)
- Both use port **443 (HTTPS)**
- PrivateLink/Private Service Connect eliminates need to allowlist public IPs — traffic stays on cloud provider's internal network

## Prerequisites
- Twingate Remote Network deployed with at least one Connector
- Connector public IP addresses (Admin Console → Remote Network → Connectors → Public IP)
- Snowflake account with `ACCOUNTADMIN` or `SECURITYADMIN` role

## Step-by-Step

### Database/Warehouse Access
1. Create Snowflake Network Rule scoped to Connector IPs (Admin → Security → Network Rules)
2. Create Twingate Resource for `myorg-myaccount.snowflakecomputing.com`, port 443
3. Connect Twingate Client before running queries

### Snowsight Access
1. Create Snowflake Network Policy scoped to Connector IPs (Admin → Security → Network Policies) and **activate it**
2. Create Twingate Resource for `*.snowflake.com` or regional URL, port 443
3. Use same Remote Network as warehouse resources

## Configuration Values

```toml
# ~/.snowflake/config.toml
[connections.myconn]
account = "myaccount"
user = "jondoe"
role = "accountadmin"
```

```bash
# CLI setup
export SNOWFLAKE_CONNECTIONS_MYCONN_PASSWORD='abc123'
snow connection set-default myconn
snow sql -q "select current_user();"
```

## Gotchas
- **Network policy activation**: Creating a policy does not enforce it — must explicitly activate
- **Multiple policies**: Snowflake applies the most restrictive policy; Connector IPs must appear in both user-level and account-level policies if both exist
- **Account URL format**: Must use full identifier `myorg-myaccount` — partial identifiers cause connection failures
- **Snowsight vs DB**: These are separate endpoints requiring separate Twingate Resources and separate Snowflake policy configurations
- **PrivateLink**: When using PrivateLink, allowlist the private endpoint ID instead of public IPs

## Troubleshooting
| Symptom | Check |
|---|---|
| Access denied | Connector IP in network rule, policy applied, correct CIDR notation |
| DNS Failed | Connector can resolve hostname, DNS server accessible |
| Connection Failed | Route exists Connector→Snowflake, firewall allows port 443 |
| No Activity | Client running, user has Resource access, no VPN conflict |

## Related Docs
- [Snowflake Network Policies SQL Reference](https://docs.snowflake.com)
- [Snowflake Private Connectivity Configuration](https://docs.snowflake.com)
- Twingate: SaaS App Gating Guide
- Twingate: Connector Best Practices
- Twingate: Troubleshooting Guide