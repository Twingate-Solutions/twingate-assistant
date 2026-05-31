# Configuring Zscaler to Work with Twingate

## Summary
Zscaler SSL inspection intercepts Twingate TLS sessions, causing certificate validation failures that prevent the Twingate Client from establishing secure channels. Two resolution paths exist: disable Zscaler entirely or configure SSL inspection bypass for Twingate domains.

## Key Information
- Affects Windows devices running both Zscaler and Twingate Client simultaneously
- Root cause: Zscaler intercepts TLS sessions, invalidating Twingate's certificate pinning
- Simply exiting Zscaler is insufficient — the service must be fully stopped/uninstalled for Option 1

## Symptoms
Error in `twingate.log` on Windows:
```
[WARN] SSL check error from host: <twingate_network>.twingate.com. SSL Certificate is not pinned!
[ERROR] Failed to validate controller url
System.Net.Http.HttpRequestException: Could not establish trust relationship for SSL/TLS channel.
```

## Resolution Options

### Option 1: Disable Zscaler
- Uninstall Zscaler **or** stop/disable the Zscaler service entirely
- Exiting the application is not sufficient

### Option 2: Bypass SSL Inspection (Recommended for coexistence)

| Step | Location in Zscaler Console | Action |
|------|----------------------------|--------|
| 1 | Administration → IP & FQDN Groups → Destination IPv4 Groups | Create SSL inspection bypass group; add `.twingate.com` |
| 2 | Policy → Client Connector Portal → Windows | Add `<tenant>.twingate.com` as VPN Gateway Bypass exception |
| 3 | Zscaler local agent | Update policy |

## Configuration Values
- **Domain to bypass:** `.twingate.com` (wildcard)
- **Tenant-specific exception:** `<tenant>.twingate.com`
- **Log file location:** `twingate.log` (Windows)

## Gotchas
- Exiting Zscaler UI does not stop the service — must disable/uninstall for full removal
- Both the IP/FQDN group entry and the VPN Gateway Bypass exception are required for Option 2
- Policy must be explicitly updated on the local Zscaler agent after changes

## Related Docs
- [Zscaler documentation](https://help.zscaler.com) — for detailed Zscaler configuration steps
- Twingate Windows Client logs (`twingate.log`) for diagnostic verification