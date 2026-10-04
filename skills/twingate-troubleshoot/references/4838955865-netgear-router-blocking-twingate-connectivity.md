---
source: https://help.twingate.com/articles/4838955865-netgear-router-blocking-twingate-connectivity
type: help
fetched: 2026-10-04
source_version: 5524f7622471188e4724ba3e452a2e827bd6561692ff50820bad36fb160a502f
trust: official
---

# Netgear Router Blocking Twingate Connectivity

## Summary
NETGEAR Armor (router-level security) blocks Twingate connections, causing the client to appear connected but fail to route traffic. The fix is either disabling NETGEAR Armor or configuring a URL exception for Twingate domains.

## Key Information
- Affects both Twingate Client and Connector components
- Applies to any platform behind a NETGEAR router with NETGEAR Armor active
- Twingate installs and appears to connect successfully, but traffic does not flow
- No other VPN conflicts involved; other internet traffic works normally

## Symptoms
- Network URL entered after successful installation
- Client shows connected state but resources are unreachable
- No other active VPNs
- General internet connectivity is unaffected

## Cause
NETGEAR Armor performs URL-level filtering that intercepts and blocks Twingate infrastructure URLs.

## Resolution Options

### Option 1: Disable NETGEAR Armor
Turn off NETGEAR Armor entirely via the NETGEAR router admin interface or the NETGEAR app.

### Option 2: Add Twingate URL Exception in NETGEAR Armor
Configure an allowlist exception within NETGEAR Armor using NETGEAR's own process for unblocking specific URLs. Refer to NETGEAR's KB article: *"NETGEAR Armor is blocking URLs that I want to access; what do I do?"* (available on the NETGEAR support site).

## Configuration Values
- No Twingate-side configuration changes required
- Twingate URLs to allowlist: refer to the **Twingate Allowlist for outbound connections** documentation for the full list of required domains/IPs

## Gotchas
- The client does **not** show an obvious error — it appears to connect, making this a non-obvious failure mode
- NETGEAR Armor must be configured at the router level, not on the endpoint; endpoint-side changes will not resolve this
- If managing multiple devices, the exception must be set once at the router level to cover all devices on the network

## Related Docs
- [Allowlist for outbound connections to Twingate infrastructure](https://help.twingate.com) — full list of Twingate URLs/IPs to whitelist
- NETGEAR Armor URL exception KB (NETGEAR support site)