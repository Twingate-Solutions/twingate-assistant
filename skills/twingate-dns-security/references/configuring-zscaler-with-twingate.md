# Configuring Zscaler to Work with Twingate

## Summary
Zscaler SSL inspection intercepts Twingate TLS sessions, causing certificate validation failures on the Twingate Client. Two resolution options exist: disable Zscaler entirely or configure SSL inspection bypass for Twingate domains.

## Key Information
- Zscaler intercepts Twingate TLS sessions, breaking secure channel establishment
- Issue manifests as "SSL Certificate is not pinned!" warnings and trust relationship errors
- Primarily affects Windows devices (error found in `twingate.log`)
- Both tools can run simultaneously with proper Zscaler bypass configuration

## Prerequisites
- Access to Zscaler admin console
- Twingate tenant name/network name
- Admin rights on affected Windows device

## Symptoms
Error in `twingate.log` on Windows:
```
[WARN] SSL check error from host: <twingate_network>.twingate.com. SSL Certificate is not pinned!
[ERROR] Failed to validate controller url
System.Net.Http.HttpRequestException: Could not establish trust relationship for SSL/TLS channel.
```

## Resolution Options

### Option 1: Disable Zscaler
- Uninstall Zscaler **or** stop/disable the Zscaler service
- **Note:** Simply exiting Zscaler is insufficient — the service must be fully stopped/disabled

### Option 2: Bypass SSL Inspection (Preferred — allows both tools simultaneously)

1. In Zscaler admin console, go to **Administration → IP & FQDN Groups → Destination IPv4 Groups**
2. Create a new group for SSL inspection bypass
3. Add `.twingate.com` to the group
4. Navigate to **Policy → Client Connector Portal → Windows**
5. Add `<tenant>.twingate.com` as an exception under **VPN Gateway Bypass**
6. Update policy on the Zscaler local agent

## Configuration Values
| Field | Value |
|---|---|
| FQDN bypass (group) | `.twingate.com` |
| VPN Gateway Bypass exception | `<tenant>.twingate.com` |

## Gotchas
- Exiting Zscaler UI does **not** stop the service — must disable/uninstall for Option 1 to work
- Both the FQDN group bypass and VPN Gateway Bypass exception are required for Option 2
- Policy must be pushed/updated on the local Zscaler agent after changes

## Related Docs
- [Zscaler documentation](https://help.zscaler.com) (for additional Zscaler configuration details)
- Twingate Windows Client logs: `twingate.log`