---
source: https://help.twingate.com/articles/8616217757-troubleshooting-access-issues-to-twingate-ip-resources-on-macos
type: help
fetched: 2026-11-01
source_version: da9a2943f948f3aa74514c8998ab0ff658748b57537f4c6f3636ca00824d9319
trust: official
---

# Troubleshooting Access Issues to Twingate IP Resources on macOS

## Page Title
Troubleshooting Access Issues to Twingate IP Resources on macOS

## Summary
On macOS, IP-only Twingate resources may fail to load when the local network subnet overlaps with the Twingate resource subnet. macOS incorrectly prioritizes the local route over the Twingate tunnel, causing traffic to bypass the secure tunnel entirely. This is a macOS-specific routing limitation.

## Key Information
- **Affected component:** Twingate Client on macOS
- **Root cause:** macOS route priority conflict when local network subnet overlaps with a Twingate IP resource subnet
- **Symptom:** Traffic goes over local network instead of through Twingate tunnel
- **Scope:** IP-only resources only; other OS platforms handle route priorities correctly

## Prerequisites
- Twingate Client installed on macOS
- Access to define/edit Twingate resources (admin)
- Terminal access (for advanced route removal option)

## Resolution Options

### Option 1: Use More Specific IP Resources (Recommended)
- Define resources as specific IP addresses rather than broad subnets
- Narrower route definitions allow macOS to correctly prioritize the Twingate tunnel route over the local network route
- No terminal access required; handled via Twingate admin console

### Option 2: Remove Conflicting Local Routes (Advanced)
- Manually remove the conflicting local route via macOS Terminal
- Use `route delete` commands targeting the overlapping local subnet
- **Warning:** Removing local routes may break communication with other devices on the local network
- Changes may not persist across network changes or reboots

## Gotchas
- This is a **macOS platform limitation**, not a Twingate bug — other OS clients handle overlapping subnets without issue
- Route removal (Option 2) is a temporary workaround; the route may be re-added automatically when the network interface changes
- Broad subnet resources (e.g., `/16`, `/24`) are more likely to trigger conflicts than single-host (`/32`) resources
- Always test local network connectivity after making routing table changes

## Configuration Values
- No specific env vars or CLI flags documented for this issue
- Resource definition granularity is set in the Twingate Admin Console under Resources

## Related Docs
- Twingate Resource Configuration (Admin Console)
- Twingate Client troubleshooting guides
- macOS `route` and `netstat -rn` commands for inspecting routing tables