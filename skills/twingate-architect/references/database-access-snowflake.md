# Snowflake Access with Twingate

## Summary
Routes Snowflake traffic (Snowsight UI and database queries) through Twingate Connectors, then restricts Snowflake access via network policies to only allow Connector public IPs. Covers both warehouse/API access and Snowsight admin console access.

## Key Information
- Snowflake uses **network policies** (containing network rules) to allowlist IP addresses or private endpoint identifiers
- Two separate resources may be needed: one for `*.snowflake.com` (Snowsight UI) and one for `*.snowflakecomputing.com` (queries/API)
- PrivateLink (AWS/Azure) or Private Service Connect (GCP) eliminates need to manage public IP allowlists
- Same network policy framework applies to both Snowsight and warehouse connections
- Port: **443 (HTTPS)** for all Snowflake traffic

## Prerequisites
- Twingate Remote Network deployed with at least one Connector
- Connector public IP addresses (Admin Console → Remote Network → Connectors → Public IP)
- Snowflake account with `ACCOUNTADMIN` or `SECURITYADMIN` role

## Step-by-Step

### Database/Warehouse Access
1. Create Snowflake Network Rule scoped to Connector IP addresses (Admin → Security → Network Rules → + Network Rule)
2. Create Twingate Resource for `myorg-myaccount.snowflakecomputing.com`, port 443
3. Connect Twingate Client before running queries

### Snowsight Access
1. Create Snowflake Network Policy scoped to Connector IPs (Admin → Security → Network Policies → + Network Policy) and activate it
2. Create Twingate Resource for `*.snowflake.com` or regional URL (e.g., `apps-api.c1.us-west-2.aws.app.snowflake.com`), port 443
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
snow connection set-default myconn
snow sql -q "select current_user();"
```

## Gotchas
- **Multiple network policies**: Snowflake applies the most restrictive policy — if a user-level policy exists, Connector IPs must be in **both** user-level and account-level policies
- **Account URL format**: Must use full identifier `myorg-myaccount` — missing segments cause connection failures
- **Two resource types needed**: Snowsight (`*.snowflake.com`) and query access (`*.snowflakecomputing.com`) are separate hostnames requiring separate Twingate Resources
- Without Twingate connected, connections fail with `Incoming request with IP/Token X.X.X.X is not allowed`

## Troubleshooting
| Symptom | Check |
|---|---|
| Access denied | Connector IP in network rule; policy applied to account; CIDR typos |
| DNS Failed | Connector can resolve hostname; DNS server reachable |
| Connection Failed | Route from Connector to Snowflake; firewall/security groups on port 443 |
| No Activity | Client running; Resource access granted; no conflicting VPN |

## Related Docs
- [Snowflake Configuring Private Connectivity](https://docs.snowflake.com)
- [Twingate SaaS App Gating Guide](https://www.twingate.com/docs/saas-app-gating)
- [Twingate Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/troubleshooting)