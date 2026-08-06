---
source: https://help.twingate.com/articles/2783921459-checking-resource-definitions
type: help
fetched: 2026-08-06
source_version: ea076e5f5cd680a99c54ee04c390108ddf4f294a4f4d305bb1101d5d977bf99c
---

# Checking Resource Definitions

## Summary
Twingate Resources define which traffic the Client intercepts; all other traffic passes through normally. Resources are either DNS type (hostname/FQDN) or CIDR type (IP address). Correct Resource definitions are required for connectivity to work.

## Key Information
- **Two Resource types**: DNS (hostname/FQDN) and CIDR (IP ranges)
- Client only intercepts traffic matching defined Resources
- Exception: DoH enabled causes all DNS traffic to be handled by the Client
- Patterned DNS Resources support `*` and `?` wildcards in FQDNs

## Resource Type Selection
| Use Case | Resource Type |
|----------|--------------|
| Users connect via private IP | CIDR |
| Users connect via hostname/FQDN | DNS |

## CIDR Resource Options
- **Option 1**: Single IP — e.g., `10.1.2.3`
- **Option 2**: CIDR range — e.g., `10.1.2.0/24`

## DNS Resource Options

**FQDN only** (`server1.corp.int`):
- Option 1: Exact FQDN match
- Option 2: Patterned FQDN with wildcards (e.g., `*.corp.int`)

**Hostname + FQDN** (`server1`):
- Requires **two separate Resources**: one for the FQDN (`server1.corp.int`) and one for the bare hostname (`server1`)
- Single Resource covering only the FQDN will not intercept bare hostname traffic

## Troubleshooting Checklist
1. Confirm asset exists in the **Resources** list in Admin Console
2. For hostname access, verify both hostname and FQDN are covered (separate Resources or wildcard pattern)
3. For IP access, verify the IP falls within a defined CIDR Resource
4. Check if DoH is enabled — affects DNS traffic handling globally

## Gotchas
- Connecting via hostname (`server1`) when only an FQDN Resource (`server1.corp.int`) exists will fail — bare hostnames require their own Resource
- Wildcard patterns (`*`, `?`) can cover multiple FQDNs under one Resource, but must be configured explicitly
- Traffic not matching any Resource definition is ignored by the Client entirely

## Related Docs
- Patterned FQDN Resource definitions (wildcard details)
- Unqualified domain names explanation
- Twingate troubleshooting guide