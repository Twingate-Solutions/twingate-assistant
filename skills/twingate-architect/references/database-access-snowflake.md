## Snowflake Access with Twingate

Twingate routes Snowflake query traffic and Snowsight UI access through Connectors, with access enforced by Snowflake network policies that allowlist Connector public IP addresses. Network policies use network rules (IP CIDR lists or private endpoint identifiers); the same framework applies to both data warehouse connections and the Snowsight admin console. PrivateLink (AWS/Azure) and PSC (GCP) are supported for eliminating public IP management.

**Key Information**
- All connections use HTTPS, port 443
- Resource: `*.snowflakecomputing.com` (wildcard) or specific account URL `myorg-myaccount.snowflakecomputing.com`
- Snowsight (admin console): Resource `*.snowflake.com` or regional URL; same network policy framework
- Network policies contain network rules; rules define allowed IP CIDRs or private endpoint identifiers
- Creating/applying network policies requires ACCOUNTADMIN or SECURITYADMIN role
- Snowflake evaluates the most restrictive applicable policy (user-level vs account-level); Connector IPs must be in both if a user-level policy exists
- PrivateLink/PSC: no public IP allowlisting needed; use private endpoint identifier in network rules

**Prerequisites**
- Remote Network and Connector deployed
- Snowflake account with ACCOUNTADMIN or SECURITYADMIN role
- Connector public IP(s) noted from Twingate Admin Console

**Step-by-Step (Database/Warehouse Access)**
1. Create network rule in Snowflake: Admin -> Security -> Network Rules -> add Connector public IP in CIDR notation
2. Create/update network policy referencing the network rule
3. Create Twingate Resource: `*.snowflakecomputing.com`, port 443; assign to groups
4. Connect with Twingate Client running; verify `snow sql -q "select current_user();"` succeeds

**Step-by-Step (Snowsight)**
1. Create Twingate Resource: `*.snowflake.com`, port 443; use same Remote Network
2. Create/update Snowflake network policy to include Connector IPs
3. Apply policy at account level in Admin -> Security -> Network Policies

**Configuration Values**
- Snowflake CLI config: `[connections.myconn]` in `config.toml`; password via `SNOWFLAKE_CONNECTIONS_MYCONN_PASSWORD` env var
- SQL: `snow connection set-default myconn` to set default

**Gotchas**
- User-level network policies are more restrictive than account-level -- Connector IPs must be in both
- Incorrect account URL (missing org prefix `myorg-myaccount` vs just `myaccount`) is a common auth failure
- Snowflake network policies block ALL other IPs implicitly once activated -- test before enforcing

**Related Docs**
- /docs/database-access-guide
- /docs/saas-app-gating
- /docs/connector-best-practices
