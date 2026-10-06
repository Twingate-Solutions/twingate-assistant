---
source: https://help.twingate.com/articles/8616217757-troubleshooting-access-issues-to-twingate-ip-resources-on-macos
type: help
fetched: 2026-10-04
source_version: 64178c612f473c09300f02faac3107facbd3c62403ad5f4d4b76e24efe7231a2
trust: official
---

# Troubleshooting Access Issues to Twingate IP Resources on macOS

## Summary
On macOS, overlapping subnets between local networks and Twingate IP resources can cause routing conflicts where traffic bypasses the Twingate tunnel and routes locally instead. This is a macOS-specific limitation in route priority handling. The issue only affects IP-only resources (not FQDN resources).

## Key Information
- macOS may incorrectly prioritize local network routes over Twingate tunnel routes when subnets overlap
- Other operating systems handle route priorities correctly; this is macOS-specific
- Affects IP-based Twingate resources only, not FQDN-based resources
- Symptom: IP resources fail to load or connect despite Twingate being active

## Prerequisites
- Twingate Client installed on macOS
- Access to Twingate Admin Console (to modify resource definitions)
- Terminal access (for advanced route removal option)

## Resolution Options

### Option 1: Use More Specific IP Resources (Recommended)
1. Identify the conflicting IP resource (broad subnet) in the Twingate Admin Console
2. Replace the broad subnet resource with more specific IP addresses or narrower CIDR ranges
3. This ensures macOS correctly prioritizes the Twingate tunnel route over the local network route

### Option 2: Remove Conflicting Local Route (Advanced)
1. Open Terminal on macOS
2. Identify the conflicting route using `netstat -rn` or `route -n get <IP>`
3. Manually delete the conflicting local route using `sudo route delete <subnet>`
4. **Caution:** Removing local routes may break communication with other devices on the local network; this is a temporary fix (routes may restore on reconnect)

## Configuration Values
- No specific env vars or CLI flags; resolution is handled via Admin Console resource configuration or macOS `route` commands

## Gotchas
- Removing local routes can disrupt LAN connectivity — use with caution and understand the impact before proceeding
- Manually removed routes may be re-added automatically by macOS when network changes occur (e.g., reconnecting Wi-Fi)
- This is a **macOS OS-level limitation**, not a Twingate bug; no client update will fully resolve it
- Broad subnet resources (e.g., `/16`, `/8`) are most likely to trigger conflicts with common local network ranges (e.g., `192.168.x.x`, `10.x.x.x`)

## Related Docs
- Twingate resource configuration (Admin Console)
- macOS networking: `man route`, `man netstat`