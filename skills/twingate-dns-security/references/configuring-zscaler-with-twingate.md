# Configuring Zscaler to Work with Twingate

## Page Title
How to Configure Zscaler to Work with Twingate

## Summary
Zscaler intercepts Twingate TLS sessions, causing certificate validation failures that prevent the Twingate Client from establishing secure channels. The fix requires either disabling Zscaler or configuring SSL inspection bypass rules for Twingate domains.

## Key Information
- Zscaler performs SSL/TLS inspection that breaks Twingate's certificate pinning
- Issue manifests on Windows devices via `twingate.log` errors
- Two resolution paths: disable Zscaler entirely or configure bypass rules

## Symptoms
Error in `twingate.log` on Windows:
```
[WARN] SSL check error from host: <twingate_network>.twingate.com. SSL Certificate is not pinned!
[ERROR] Failed to validate controller url
System.Net.Http.HttpRequestException: Could not establish trust relationship for SSL/TLS channel.
```

## Prerequisites
- Access to Zscaler admin console
- Admin rights to configure IP & FQDN Groups and Policy settings

## Step-by-Step (Option 2: Bypass SSL Inspection — Recommended)

1. In Zscaler admin console, navigate to **Administration → IP & FQDN Groups → Destination IPv4 Groups**
2. Create a new group for SSL inspection bypass
3. Add `.twingate.com` (wildcard) to the group
4. Navigate to **Policy → Client Connector Portal → Windows**
5. Add `<tenant>.twingate.com` as an exception under **VPN Gateway Bypass**
6. Push/update policy on the Zscaler local agent

## Option 1: Disable Zscaler (Alternative)
- Uninstall Zscaler **or** stop/disable the Zscaler service
- Simply exiting the Zscaler app is **not sufficient** — the service must be fully stopped

## Configuration Values
| Field | Value |
|-------|-------|
| FQDN bypass (wildcard) | `.twingate.com` |
| VPN Gateway Bypass exception | `<tenant>.twingate.com` |

## Gotchas
- Exiting Zscaler UI does not stop SSL inspection — the service must be disabled/uninstalled for Option 1 to work
- Both the wildcard domain group (`.twingate.com`) and the tenant-specific VPN Gateway Bypass exception are required for Option 2
- Issue is Windows-specific per documented symptoms, though Zscaler interference may affect other platforms

## Related Docs
- [Zscaler Documentation](https://help.zscaler.com) (external)
- Twingate Client logs: `twingate.log` on Windows