# Snowflake Access with Twingate

## Summary
Route Snowflake traffic (Snowsight UI and database queries) through Twingate Connectors and restrict access using Snowflake network policies scoped to Connector public IP addresses. Covers both HTTPS-based admin console access and SQL/API query access. PrivateLink is recommended for cloud deployments to avoid public IP allowlisting.

## Key Information
- Snowflake uses network policies (containing network rules) to allowlist IP addresses or private endpoint identifiers
- Twingate Connector public IPs are added to Snowflake network rules/policies
- Both Snowsight (`*.snowflake.com`) and warehouse access (`*.snowflakecomputing.com`) require separate Resources
- All connections use port 443 (HTTPS)
- PrivateLink/Private Service Connect eliminates need for public IP allowlisting on AWS/Azure/GCP

## Prerequisites
- Twingate Remote Network deployed with at least one Connector
- Connector public IP addresses (Admin Console → Remote Network → Connectors → Public IP)
- Snowflake account with `ACCOUNTADMIN` or `SECURITYADMIN` role

## Step-by-Step

### Database/Warehouse Access
1. In Snowflake: Admin → Security → Network Rules → create rule with Connector public IPs
2. In Twingate: Create Resource for `myorg-myaccount.snowflakecomputing.com`, port 443
3. Connect Twingate Client before running queries

### Snowsight UI Access
1. In Snowflake: Admin → Security → Network Policies → create and activate policy with Connector IPs
2. In Twingate: Create Resource for `*.snowflake.com` or regional URL (e.g., `apps-api.c1.us-west-2.aws.app.snowflake.com`), port 443
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

### Twingate Resource Settings
| Field | Warehouse | Snowsight |
|-------|-----------|-----------|
| Address | `*.snowflakecomputing.com` | `*.snowflake.com` |
| Port | 443 | 443 |

## Gotchas
- **Multiple network policies**: Snowflake applies the most restrictive policy; if user-level policy exists, Connector IPs must be in both account-level and user-level policies
- **Account URL format**: Must use full identifier `myorg-myaccount` — missing segments cause connection failures
- **Policy activation**: Network policy must be explicitly activated after creation
- **PrivateLink**: Use private connectivity to avoid managing public IP allowlists entirely
- Disconnected Twingate Client produces error: `Incoming request with IP/Token X.X.X.X is not allowed to access Snowflake`

## Troubleshooting
| Symptom | Check |
|---------|-------|
| Access denied | Connector IP in network rule, policy applied, no CIDR typos |
| DNS Failed | Connector can resolve hostname, DNS server accessible |
| Connection Failed | Route exists Connector→DB, firewall allows port 443 |
| No Activity | Client running, Resource access granted, no conflicting VPN |

## Related Docs
- [Snowflake Private Connectivity](https://docs.snowflake.com/en/user-guide/admin-security-privatelink)
- Twingate SaaS App Gating Guide
- Twingate Connector Best Practices
- Twingate Troubleshooting Guide