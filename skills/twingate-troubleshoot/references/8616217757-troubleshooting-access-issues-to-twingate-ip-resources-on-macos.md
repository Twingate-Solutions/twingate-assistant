---
source: https://help.twingate.com/articles/8616217757-troubleshooting-access-issues-to-twingate-ip-resources-on-macos
type: help
fetched: 2026-08-06
source_version: b12218db748ee0f31c37f1d92dfe8c2f5957dcbce1c209d65b7006c51a49cde2
---

# Troubleshooting Access Issues to Twingate IP Resources on macOS

## Summary
On macOS, overlapping subnets between local networks and Twingate IP resources can cause routing conflicts where traffic bypasses the Twingate tunnel. This is a macOS-specific limitation in route priority handling. Defining more specific IP resources or manually removing conflicting routes resolves the issue.

## Key Information
- **Affected component**: Twingate Client on macOS
- **Root cause**: macOS incorrectly prioritizes local network routes over Twingate tunnel routes when subnets overlap
- **Scope**: Affects IP-only resources (not FQDN-based resources)
- **OS behavior**: Other operating systems handle route priorities correctly; this is a macOS-specific limitation
- **Symptom**: IP resources fail to load or function; traffic routes over local network instead of through Twingate

## Prerequisites
- Twingate Client installed on macOS
- Access to Twingate Admin Console (to modify resource definitions)
- Terminal access (for advanced route removal option)

## Resolution Options

### Option 1: Use More Specific IP Resources (Recommended)
1. Identify the specific IP addresses causing conflicts
2. In Twingate Admin Console, replace broad subnet resources with more specific IP address definitions
3. More specific routes take priority over broader local subnet routes on macOS

### Option 2: Remove Conflicting Local Routes (Advanced)
1. Open Terminal
2. Identify conflicting local routes via `netstat -rn` or `route -n get <IP>`
3. Remove the conflicting route manually using terminal commands
4. **Caution**: Removing local routes may break communication with other devices on the local network

## Gotchas
- This fix requires modifying resource definitions in Twingate — not a client-side setting alone
- Manually removed routes may be restored after network changes or reboots
- Removing local routes can disrupt LAN device communication — test carefully in non-production environments
- No workaround exists at the OS level without either approach; this is a macOS routing limitation

## Related Docs
- Twingate IP Resource configuration (Admin Console)
- Twingate Client troubleshooting guides
- macOS routing table management (`man route`)