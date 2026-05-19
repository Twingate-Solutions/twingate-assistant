# Twingate vs. VPNs

## Page Title
Twingate vs. VPNs

## Summary
Twingate implements Zero Trust Networking (ZTN) as an alternative to traditional VPNs. Unlike VPNs that grant broad network-level access, Twingate provides per-application access control with no public-facing gateway. It can coexist with existing VPN infrastructure, enabling gradual migration without infrastructure changes.

## Key Information

- **Access model**: Per-application (least privilege) vs. VPN's full network access
- **Gateway exposure**: No public-facing gateway required; Connectors make outbound connections only
- **Traffic routing**: Split tunnel by default (only private resource traffic routed internally)
- **No backhauling**: Traffic routes directly without passing through a central VPN server
- **Auth factors**: SSO/IdP with MFA, location, time-of-day, device posture, risk scores
- **Coexistence**: Runs alongside existing VPNs without infrastructure changes
- **Deployment**: Container-based Connector; no appliances, no network reconfiguration
- **SIEM integration**: Centralized logging compatible with SIEM systems

## Prerequisites
- None for evaluation; Twingate installs a lightweight Connector (container) on one device per network
- No network reconfiguration, IP/DNS changes, or appliance procurement required

## Architecture Differences

| Dimension | VPN | Twingate |
|---|---|---|
| Access scope | Network-level | Per-application |
| Gateway | Public-facing | No public gateway |
| Tunneling | Full tunnel | Split tunnel |
| Lateral movement | Possible | Blocked |
| Scaling | Manual (appliances) | Cloud service |

## Configuration Values
- No documented env vars or CLI flags on this page
- Connector delivered as a **container**
- Client: always-on, no user interaction required
- Technology: **ViPR** (handles split tunneling, auth processing, eliminates backhauling)

## Gotchas

- VPN gateways are publicly visible and regularly exploited (CVEs from all major vendors)
- VPN full-tunnel routes all traffic through potentially distant servers, increasing latency
- VPN breach = full network exposure; Twingate breach = limited to specific app(s)
- "Tromboning" in VPNs (client → server → resource) adds latency that Twingate avoids by edge-processing auth
- Users behind VPNs see incorrectly localized content (traffic appears from VPN server location)

## Deployment Notes
- Pilot testing possible on a subset of users/resources without touching existing VPN
- No "rip and replace" required
- Rollout can be phased incrementally

## Related Docs
- [Quick, Simple and Low Risk Migration](https://www.twingate.com/docs/) (referenced inline)
- Zero Trust Networking concepts (covered inline on this page)
- Free trial signup available at twingate.com