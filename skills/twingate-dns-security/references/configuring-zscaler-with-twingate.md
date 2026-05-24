# Configuring Zscaler to Work with Twingate

## Summary
Zscaler intercepts Twingate TLS sessions, causing certificate validation failures that prevent the Twingate Client from establishing secure channels. The fix requires either disabling Zscaler or configuring SSL inspection bypass rules for Twingate domains.

## Key Information
- Affects Windows devices (confirmed via `twingate.log`)
- Root cause: Zscaler performs SSL inspection, invalidating Twingate's certificate pinning
- Two resolution paths: disable Zscaler entirely or configure bypass rules

## Symptoms
Error in `twingate.log`:
```
[WARN] SSL check error from host: <twingate_network>.twingate.com. SSL Certificate is not pinned!
[ERROR] Failed to validate controller url
System.Net.Http.HttpRequestException: Could not establish trust relationship for SSL/TLS channel.
```

## Resolution Options

### Option 1: Disable Zscaler
- Uninstall Zscaler or stop/disable the Zscaler service
- **Note:** Simply exiting Zscaler is insufficient — the service must be fully stopped/disabled

### Option 2: Bypass SSL Inspection (Preferred for coexistence)

**Step 1 — Create SSL bypass group:**
1. Zscaler Admin Console → `Administration` → `IP & FQDN Groups` → `Destination IPv4 Groups`
2. Create a new group for SSL inspection bypass
3. Add `.twingate.com` to the group

**Step 2 — Add VPN Gateway exception:**
1. Navigate to `Policy` → `Client Connector Portal` → `Windows`
2. Add `<tenant>.twingate.com` as an exception under **VPN Gateway Bypass**

**Step 3 — Apply policy:**
- Update policy on the Zscaler local agent

## Configuration Values
| Field | Value |
|-------|-------|
| FQDN bypass domain | `.twingate.com` |
| VPN Gateway Bypass exception | `<tenant>.twingate.com` |

## Gotchas
- Exiting the Zscaler client UI does **not** stop SSL interception — the underlying service must be disabled
- Both the wildcard domain (`.twingate.com`) and the tenant-specific URL (`<tenant>.twingate.com`) need to be configured in separate policy locations
- Policy must be explicitly pushed/updated to the local Zscaler agent after changes

## Related Docs
- [Zscaler documentation](https://help.zscaler.com) (for detailed Zscaler-side configuration)
- Twingate Client logs location: `twingate.log` on Windows