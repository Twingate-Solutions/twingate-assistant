# Configuring Zscaler to Work with Twingate

## Page Title
How to Configure Zscaler to Work with Twingate

## Summary
Zscaler intercepts Twingate TLS sessions, causing certificate validation failures that prevent the Twingate Client from establishing secure channels. The fix requires either disabling Zscaler entirely or configuring SSL inspection bypass rules for Twingate domains.

## Key Information
- Affects Windows devices running both Zscaler and Twingate simultaneously
- Root cause: Zscaler performs SSL/TLS inspection, breaking Twingate's certificate pinning
- Two resolution paths: disable Zscaler or configure bypass rules

## Symptoms
Error in `twingate.log` on Windows:
```
[WARN] SSL check error from host: <twingate_network>.twingate.com. SSL Certificate is not pinned!
[ERROR] Failed to validate controller url
System.Net.Http.HttpRequestException: Could not establish trust relationship for SSL/TLS channel.
```

## Step-by-Step

### Option 1: Disable Zscaler
- Uninstall Zscaler **or** stop/disable the Zscaler service
- Note: Simply exiting Zscaler is **not sufficient**

### Option 2: Bypass SSL Inspection (Preferred for coexistence)
1. In Zscaler admin console → **Administration** → **IP & FQDN Groups** → **Destination IPv4 Groups**
2. Create a new group for SSL inspection bypass
3. Add `.twingate.com` to the group
4. Navigate to **Policy** → **Client Connector Portal** → **Windows**
5. Add `<tenant>.twingate.com` as an exception under **VPN Gateway Bypass**
6. Push/update policy on the Zscaler local agent

## Configuration Values
| Field | Value |
|-------|-------|
| FQDN to bypass | `.twingate.com` |
| VPN Gateway Bypass exception | `<tenant>.twingate.com` |

## Gotchas
- Exiting the Zscaler app does **not** stop SSL inspection — the service must be fully stopped or uninstalled for Option 1 to work
- Both the FQDN group bypass **and** the VPN Gateway Bypass exception are required; configuring only one may be insufficient
- Policy must be explicitly updated/pushed to the local Zscaler agent after changes

## Related Docs
- [Zscaler documentation](https://help.zscaler.com) (for detailed Zscaler configuration)
- Twingate Client logs: `twingate.log` on Windows