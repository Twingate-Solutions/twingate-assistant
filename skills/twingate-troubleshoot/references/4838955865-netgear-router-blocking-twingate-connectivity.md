---
source: https://help.twingate.com/articles/4838955865-netgear-router-blocking-twingate-connectivity
type: help
fetched: 2026-11-01
source_version: 9e6c03140679082ee09dee2fed354f23a7c62e432e017b734380ed843d6aeba6
trust: official
---

# Netgear Router Blocking Twingate Connectivity

## Summary
NETGEAR routers with NETGEAR Armor enabled can block Twingate connections, causing the client to appear connected but fail to route traffic. The fix is either disabling NETGEAR Armor or adding a URL exception for Twingate.

## Key Information
- Affects both Twingate Client and Connector components
- NETGEAR Armor silently blocks Twingate URLs without clear error messaging
- Client appears to connect successfully but traffic does not flow
- Issue is router-level, not Twingate configuration

## Symptoms
- Network URL entered after successful installation
- Client shows connected state but no traffic passes
- No other VPN active that could interfere
- Other non-Twingate connections work normally

## Prerequisites
- NETGEAR router with NETGEAR Armor feature active
- Twingate Client or Connector already installed

## Resolution Options

### Option 1: Disable NETGEAR Armor
Disable NETGEAR Armor entirely via the router admin interface.

### Option 2: Add Twingate URL Exception (Preferred)
Use NETGEAR's built-in exception/allowlist mechanism:
1. Access NETGEAR Armor settings via router admin panel or NETGEAR app
2. Locate the blocked URL list or exception configuration
3. Add Twingate URLs as exceptions
4. Refer to NETGEAR's KB article: *"NETGEAR Armor is blocking URLs that I want to access; what do I do?"* (available on NETGEAR support site)

## Configuration Values
- Twingate URLs to allowlist: See [Twingate Allowlist for outbound connections](https://help.twingate.com) (covers all applicable Twingate infrastructure URLs)

## Gotchas
- The client showing a "connected" state is misleading — NETGEAR Armor blocks at the network level after the connection handshake appears complete
- Simply disabling/re-enabling the client will not resolve the issue; the block must be addressed at the router level
- Exception configuration is managed through NETGEAR's app or router UI, not through Twingate settings

## Related Docs
- [Allowlist for outbound connections to Twingate infrastructure](https://help.twingate.com) — list of all Twingate URLs requiring outbound access
- NETGEAR KB: *NETGEAR Armor is blocking URLs that I want to access; what do I do?*