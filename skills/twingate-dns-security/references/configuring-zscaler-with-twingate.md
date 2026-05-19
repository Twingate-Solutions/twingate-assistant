# Configuring Zscaler to Work with Twingate

## Summary
Zscaler intercepts Twingate TLS sessions, causing certificate validation failures that prevent the Twingate Client from establishing secure channels. Resolution requires either disabling Zscaler or configuring SSL inspection bypass rules for Twingate domains.

## Key Information
- Conflict occurs because Zscaler performs SSL/TLS inspection on Twingate connections
- Twingate uses certificate pinning, which breaks when Zscaler substitutes its own certificate
- Issue manifests on Windows clients (logged in `twingate.log`)

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
- Note: Simply exiting the Zscaler app is **not sufficient** — the service must be fully stopped

### Option 2: Bypass SSL Inspection (Preferred for coexistence)

**Step 1 — Create destination group:**
1. Zscaler Admin Console → **Administration** → **IP & FQDN Groups** → **Destination IPv4 Groups**
2. Create a new group for SSL inspection bypass
3. Add `.twingate.com` to the group

**Step 2 — Add VPN Gateway Bypass exception:**
1. Go to **Policy** → **Client Connector Portal** → **Windows**
2. Add `<tenant>.twingate.com` as an exception under **VPN Gateway Bypass**

**Step 3 — Apply policy:**
- Update policy on the Zscaler local agent

## Configuration Values
| Field | Value |
|-------|-------|
| Domain for bypass group | `.twingate.com` |
| VPN Gateway Bypass exception | `<tenant>.twingate.com` |

## Gotchas
- Exiting Zscaler UI does not stop the service — must fully disable/uninstall for Option 1
- Both the wildcard domain (`.twingate.com`) and the tenant-specific domain need to be configured in separate locations
- Windows-specific log path: `twingate.log`

## Related Docs
- [Zscaler Documentation](https://help.zscaler.com) (external)