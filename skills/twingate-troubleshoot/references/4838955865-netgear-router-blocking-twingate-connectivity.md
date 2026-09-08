---
source: https://help.twingate.com/articles/4838955865-netgear-router-blocking-twingate-connectivity
type: help
fetched: 2026-09-06
source_version: 14157db09f589e53bbc791d91c99e03d3fd0ae2b7e6cacbb68452b46ed0c2333
---

# Netgear Router Blocking Twingate Connectivity

## Summary
NETGEAR Armor security feature blocks Twingate connections, causing the client to appear connected but fail to route traffic. Resolution requires either disabling NETGEAR Armor or configuring a URL exception.

## Key Information
- Affects both Twingate Client and Connector components
- NETGEAR Armor silently blocks Twingate infrastructure URLs
- Symptom appears as successful connection UI state with no actual traffic routing
- No error messages are typically shown to the user

## Symptoms
- Network URL entered after successful installation
- Client appears to connect but traffic does not flow
- No other VPN active that could cause conflict
- Other non-Twingate connections work normally

## Cause
NETGEAR Armor (router-level security feature) blocks outbound connections to Twingate infrastructure URLs.

## Resolution

**Option 1: Disable NETGEAR Armor**
- Disable NETGEAR Armor entirely on the router

**Option 2: Configure URL Exception (preferred)**
- Use NETGEAR's exception/allowlist feature to permit Twingate URLs
- Follow NETGEAR KB: *"NETGEAR Armor is blocking URLs that I want to access; what do I do?"*
- Add all Twingate infrastructure URLs to the NETGEAR Armor exception list

## Configuration Values
- Refer to Twingate's **Allowlist for outbound connections to Twingate infrastructure** for the complete list of URLs/domains to whitelist in NETGEAR Armor

## Gotchas
- The client UI may show a connected state even when NETGEAR Armor is blocking traffic — do not rely on client status indicator alone for diagnosis
- This issue occurs post-installation during initial network URL entry, which may be misdiagnosed as a configuration or credential problem
- Disabling Armor network-wide may not be acceptable in security-conscious environments; use the exception method instead

## Related Docs
- [Allowlist for outbound connections to Twingate infrastructure](https://help.twingate.com) — required URL list for NETGEAR Armor exceptions
- NETGEAR KB: "NETGEAR Armor is blocking URLs that I want to access; what do I do?"