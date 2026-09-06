---
source: https://help.twingate.com/articles/8616217757-troubleshooting-access-issues-to-twingate-ip-resources-on-macos
type: help
fetched: 2026-09-06
source_version: 993362ef31a33853341f4179fa448c7d229c6f17f3ac8f7ea51c62c7db988dd4
---

# Troubleshooting Access Issues to Twingate IP Resources on macOS

## Summary
On macOS, overlapping subnets between local network and Twingate IP resources can cause routing conflicts where traffic bypasses the Twingate tunnel. macOS incorrectly prioritizes local network routes over Twingate routes, unlike other operating systems. This affects IP-only resources exclusively.

## Key Information
- **Root cause**: macOS routing table conflicts when local subnet overlaps with Twingate IP resource subnet
- **Symptom**: Traffic routes over local network instead of through Twingate tunnel
- **Scope**: IP-only resources on macOS only; not a Twingate bug but a macOS limitation
- **Impact**: Resources fail to load or function as expected

## Prerequisites
- Twingate Client installed on macOS
- Access to Terminal (for advanced routing fix)
- Understanding of your local network subnet ranges

## Resolution Options

### Option 1: Use More Specific IP Resources (Recommended)
1. Identify the specific IP addresses needed rather than entire subnets
2. In Twingate Admin Console, redefine the resource using a more specific IP (e.g., single host `/32`) instead of a broad subnet
3. macOS will correctly prioritize the more specific route through Twingate

### Option 2: Remove Conflicting Local Routes (Advanced)
1. Open Terminal
2. Identify conflicting route: `netstat -rn`
3. Remove the conflicting local route manually using `route delete <subnet>`
4. Test connectivity to the Twingate resource

> ⚠️ Removing local routes may break communication with other devices on your local network. Use with caution.

## Configuration Values
| Parameter | Notes |
|-----------|-------|
| Resource IP specificity | Prefer `/32` single-host or narrower CIDR over broad subnets |

## Gotchas
- This is a **macOS-specific limitation**; Windows and Linux handle route priorities correctly
- Manually deleted routes may be restored after network reconnection or reboot
- Removing local routes can disrupt LAN device communication (printers, NAS, etc.)
- Broad subnet resources (e.g., `10.0.0.0/8`) are most prone to conflicts

## Related Docs
- Twingate resource configuration (Admin Console)
- macOS routing table management (`man route`)