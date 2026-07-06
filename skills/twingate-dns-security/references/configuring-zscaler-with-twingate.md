# Configuring Zscaler to Work with Twingate

## Summary
Zscaler intercepts Twingate TLS sessions, causing certificate validation failures that prevent the Twingate Client from establishing secure channels. The fix requires either disabling Zscaler or configuring SSL inspection bypass for Twingate domains.

## Key Information
- Zscaler performs SSL inspection that breaks Twingate's certificate pinning
- Issue manifests as "SSL Certificate is not pinned!" warnings in `twingate.log`
- Affects Windows devices (log-based symptoms documented for Windows)
- Two resolution paths: full Zscaler disable or targeted SSL bypass

## Prerequisites
- Access to Zscaler admin console
- Admin rights on affected Windows devices
- Knowledge of your Twingate tenant name (`<tenant>.twingate.com`)

## Symptoms
Error in `twingate.log` on Windows:
```
[WARN] SSL check error from host: <twingate_network>.twingate.com. SSL Certificate is not pinned!
[ERROR] Failed to validate controller url
System.Net.Http.HttpRequestException: Could not establish trust relationship for SSL/TLS channel.
```

## Step-by-Step: SSL Bypass Configuration (Option 2)

1. In Zscaler admin console, navigate to **Administration → IP & FQDN Groups → Destination IPv4 Groups**
2. Create a new group for SSL inspection bypass
3. Add `.twingate.com` (wildcard) to the group
4. Navigate to **Policy → Client Connector Portal → Windows**
5. Add `<tenant>.twingate.com` as an exception under **VPN Gateway Bypass**
6. Push/update policy on the Zscaler local agent

## Configuration Values
| Field | Value |
|-------|-------|
| FQDN bypass (wildcard) | `.twingate.com` |
| VPN Gateway Bypass exception | `<tenant>.twingate.com` |

## Gotchas
- Simply exiting Zscaler is insufficient for Option 1 — the service must be fully stopped or uninstalled
- Two separate Zscaler configurations are needed for Option 2: the IP/FQDN group AND the VPN Gateway Bypass exception
- Policy must be explicitly updated on the local Zscaler agent after changes

## Related Docs
- [Zscaler documentation](https://help.zscaler.com) (for detailed Zscaler-side configuration)
- Twingate log location: `twingate.log` on Windows devices