# Configuring Zscaler to Work with Twingate

## Summary
Zscaler intercepts Twingate TLS sessions, causing certificate validation failures that prevent the Twingate Client from establishing secure channels. The fix requires either disabling Zscaler or configuring SSL inspection bypass for Twingate domains.

## Key Information
- Conflict occurs because Zscaler performs SSL/TLS inspection on Twingate connections
- Twingate uses certificate pinning, which fails when Zscaler substitutes its own certificate
- Issue manifests on Windows clients (logged in `twingate.log`)
- Both tools can coexist with proper Zscaler configuration

## Symptoms
Error in `twingate.log` on Windows:
```
[WARN] SSL check error from host: <twingate_network>.twingate.com. SSL Certificate is not pinned!
[ERROR] Failed to validate controller url
System.Net.Http.HttpRequestException: Could not establish trust relationship for SSL/TLS channel.
```

## Resolution Options

### Option 1: Disable Zscaler
- Uninstall Zscaler or stop/disable the Zscaler service
- **Note:** Simply exiting the Zscaler application is insufficient — the service must be fully stopped/disabled

### Option 2: Bypass SSL Inspection (Preferred — Allows Coexistence)

**Step 1: Create SSL Bypass Group**
1. Zscaler Admin Console → `Administration` → `IP & FQDN Groups` → `Destination IPv4 Groups`
2. Create a new group for SSL inspection bypass
3. Add `.twingate.com` to the group

**Step 2: Add VPN Gateway Exception**
1. Go to `Policy` → `Client Connector Portal` → `Windows`
2. Add `<tenant>.twingate.com` as an exception under **VPN Gateway Bypass**

**Step 3: Apply Policy**
- Update policy on the Zscaler local agent

## Configuration Values
| Parameter | Value |
|-----------|-------|
| FQDN to bypass | `.twingate.com` |
| Tenant-specific exception | `<tenant>.twingate.com` |

## Gotchas
- Exiting Zscaler UI does **not** stop the service — must disable/uninstall to fully remove interference
- Both the FQDN group bypass and the VPN Gateway exception are required; doing only one may not resolve the issue
- Configuration is Windows-specific per the documented symptoms, though the underlying TLS conflict could affect other platforms

## Related Docs
- [Zscaler Documentation](https://help.zscaler.com/) — for Zscaler-specific configuration details