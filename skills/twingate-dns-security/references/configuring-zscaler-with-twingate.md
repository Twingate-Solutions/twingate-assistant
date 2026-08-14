---
source: https://www.twingate.com/docs/configuring-zscaler-with-twingate
type: docs
fetched: 2026-08-14
source_version: 1f7b2cbebac74272a86f54ffdb09323a4755a1494bb793a4ea6f8423a91e879e
---

# Configuring Zscaler to Work with Twingate

## Summary
Zscaler intercepts Twingate TLS sessions, causing certificate validation failures that prevent the Twingate Client from establishing secure channels. This guide provides two resolution options: disabling Zscaler or configuring SSL inspection bypass.

## Key Information
- Zscaler performs SSL inspection that breaks Twingate's certificate pinning
- Issue manifests as "SSL Certificate is not pinned!" warnings and trust relationship errors
- Both tools can run simultaneously if Zscaler is properly configured

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
- **Note:** Simply exiting the application is insufficient — the service must be stopped

### Option 2: Bypass SSL Inspection (Recommended for coexistence)

**Step 1: Create IP/FQDN bypass group**
1. Zscaler admin console → **Administration** → **IP & FQDN Groups** → **Destination IPv4 Groups**
2. Create a new group for SSL inspection bypass
3. Add `.twingate.com` to the group

**Step 2: Add VPN Gateway exception**
1. Go to **Policy** → **Client Connector Portal** → **Windows**
2. Add `<tenant>.twingate.com` as an exception under **VPN Gateway Bypass**

**Step 3: Apply changes**
- Update policy on Zscaler local agent

## Configuration Values

| Location | Value |
|---|---|
| SSL bypass FQDN | `.twingate.com` |
| VPN Gateway Bypass exception | `<tenant>.twingate.com` |

## Gotchas
- Exiting Zscaler UI does not stop the service; the service must be explicitly stopped or disabled
- Both the wildcard domain (`.twingate.com`) for SSL inspection and the specific tenant domain for VPN bypass are required — they serve different purposes
- Issue is Windows-specific based on documented log path (`twingate.log`)

## Related Docs
- [Zscaler documentation](https://help.zscaler.com) (external)