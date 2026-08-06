---
source: https://help.twingate.com/articles/4838955865-netgear-router-blocking-twingate-connectivity
type: help
fetched: 2026-08-06
source_version: 68f33a0992cecbba1d9ebf2538e7788e2cc2da51a5167b1ae2f76b00d8a13e72
---

# Netgear Router Blocking Twingate Connectivity

## Summary
NETGEAR routers with NETGEAR Armor security active will block Twingate connections, causing the client to appear connected but fail to route traffic. The fix requires either disabling NETGEAR Armor or configuring URL exceptions.

## Key Information
- Affects both Twingate Client and Connector components
- NETGEAR Armor silently blocks Twingate URLs without clear error messaging
- Client appears to connect successfully but traffic does not flow
- Issue is router-level, not a Twingate configuration problem

## Symptoms
- Network URL accepted and client appears to connect
- No actual connectivity through Twingate
- No other VPN active that could cause conflict
- Other non-Twingate connections work normally

## Resolution Options

### Option 1: Disable NETGEAR Armor
Turn off NETGEAR Armor entirely via the NETGEAR router admin interface.

### Option 2: Configure URL Exceptions (Preferred)
Add Twingate URLs to NETGEAR Armor's allowlist:
1. Access NETGEAR Armor settings in router admin panel
2. Follow NETGEAR's exception configuration process (refer to NETGEAR KB: *"NETGEAR Armor is blocking URLs that I want to access; what do I do?"*)
3. Add all Twingate infrastructure URLs from the Twingate allowlist reference

## Configuration Values
- URLs to allowlist: Refer to Twingate's **Allowlist for outbound connections to Twingate infrastructure** documentation for the complete list of required URLs/domains

## Gotchas
- No obvious error is presented — client appears to connect, making this difficult to diagnose
- Simply reinstalling Twingate will not resolve the issue
- Must allowlist all Twingate infrastructure URLs, not just the network URL

## Related Docs
- [Allowlist for outbound connections to Twingate infrastructure](https://help.twingate.com) — complete list of Twingate URLs requiring network access
- NETGEAR KB: *NETGEAR Armor is blocking URLs that I want to access*