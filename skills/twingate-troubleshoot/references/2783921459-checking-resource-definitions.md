---
source: https://help.twingate.com/articles/2783921459-checking-resource-definitions
type: help
fetched: 2026-09-06
source_version: 82941e42d4ec394b80aeb9454829dc61539575d05c58f47a8429559270c02430
---

# Checking Resource Definitions

## Page Title
Checking Resource Definitions

## Summary
Twingate uses two Resource types (DNS and CIDR) to determine which traffic the Client intercepts. Resources must be explicitly defined for each asset users need to reach. Incorrect or missing Resource definitions are a common connectivity troubleshooting issue.

## Key Information
- **CIDR Resources**: Used when connecting via private IP address
- **DNS Resources**: Used when connecting via hostname or FQDN
- Twingate Client only intercepts traffic matching defined Resources (all other traffic passes through normally)
- **Exception**: With DoH enabled, all DNS traffic is also handled by the Client

## Resource Type Requirements

### CIDR Resources
- Single IP (e.g., `10.1.2.3`) or CIDR range (e.g., `10.1.2.0/24`)
- Use when users connect via private IP address

### DNS/FQDN Resources
- Exact FQDN (e.g., `server1.corp.int`)
- Patterned FQDN using wildcards `*` or `?` (e.g., `*.corp.int`)

### Hostname (Unqualified) Resources
- Requires **two separate Resources**:
  1. One for the FQDN (`server1.corp.int`)
  2. One for the hostname alone (`server1`)

## Step-by-Step: Verifying Resource Definitions
1. Open the Admin Console → **Resources** list
2. Confirm the target asset exists as a Resource
3. For FQDN access: verify either the exact FQDN exists OR a wildcard pattern covers it
4. For hostname access: verify both the FQDN Resource and bare hostname Resource exist

## Configuration Values

| Connection Method | Resource Definition Options |
|---|---|
| Private IP | Single IP or CIDR range |
| FQDN | Exact FQDN or wildcard pattern (`*`/`?`) |
| Hostname only | Hostname Resource + separate FQDN Resource |

## Gotchas
- Connecting via hostname (`server1`) without a dedicated hostname Resource will fail even if the FQDN Resource (`server1.corp.int`) exists — both must be defined separately
- Wildcard patterns (`*`, `?`) can cover FQDNs but **do not** cover bare hostnames
- DoH mode changes Client behavior — all DNS traffic is intercepted, not just Resource-matched traffic
- Missing Resource = traffic is not intercepted = connection appears to fail or bypass Twingate

## Related Docs
- Patterned FQDN definitions (wildcard syntax details)
- Unqualified domain names explanation
- Twingate troubleshooting guide (parent document)