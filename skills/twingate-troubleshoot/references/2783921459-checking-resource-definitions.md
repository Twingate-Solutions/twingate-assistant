---
source: https://help.twingate.com/articles/2783921459-checking-resource-definitions
type: help
fetched: 2026-10-04
source_version: eafef6048ca0b15408a026665fc474cd22b96148f55dfefbc1fcb52ce74df4be
trust: official
---

# Checking Resource Definitions

## Page Title
Checking Resource Definitions

## Summary
Twingate Resources define what traffic the Client intercepts, supporting two types: DNS (hostname/FQDN-based) and CIDR (IP-based). Correct Resource definitions are essential for connectivity; misconfigured or missing definitions cause traffic to be ignored by the Client.

## Key Information
- **Two Resource types:**
  - `DNS` — used when connecting via hostname or FQDN
  - `CIDR` — used when connecting via private IP address
- All non-Resource traffic is ignored by the Twingate Client (exception: DoH enabled causes all DNS traffic to be handled by the Client)
- Resource definitions are checked in the Admin Console under the **Resources** list

## Resource Definition Options

### CIDR Resources
| Option | Example |
|--------|---------|
| Single IP | `10.1.2.3` |
| CIDR range | `10.1.2.0/24` |

### DNS Resources (FQDN)
| Option | Example |
|--------|---------|
| Exact FQDN | `server1.corp.int` |
| Patterned FQDN | `*.corp.int` or `server?.corp.int` |

### DNS Resources (Unqualified Hostname)
- Requires **two separate Resources**: one for the FQDN and one for the bare hostname (e.g., `server1.corp.int` **and** `server1`)

## Prerequisites
- Access to Twingate Admin Console
- Asset must exist as a Twingate Resource before Client can route traffic to it

## Gotchas
- Connecting via hostname (`server1`) without a dedicated hostname Resource will fail even if the FQDN Resource exists — both must be defined separately
- FQDN patterns using `*` or `?` can cover hostname variants but do **not** cover the unqualified hostname itself
- If DoH is enabled, all DNS traffic routes through the Client — not just Resource traffic; this changes expected behavior
- Missing a Resource entirely is a common cause of connection failure; always verify in the Admin Console first

## Related Docs
- Patterned FQDN definition details (linked in source)
- Unqualified domain names behavior (linked in source)
- Twingate troubleshooting guide