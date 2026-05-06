# Twingate vs. VPN

## Page Title
Twingate vs. VPNs

## Summary
Twingate implements Zero Trust Networking (ZTN) as an alternative to corporate VPNs, providing application-level access control instead of network-level access. It eliminates public-facing gateways, reduces latency through split tunneling, and deploys without infrastructure changes. Designed to coexist with existing VPNs for gradual migration.

## Key Information

**Security Advantages over VPN:**
- Per-application access control (vs. full network access with VPNs)
- No public-facing gateway — connectors make outbound connections only; network stays hidden
- Rich authorization context: SSO/MFA, location, time-of-day, device posture, risk scores
- Limits lateral movement — breach scope contained to specific apps
- Centralized logging across all networks; SIEM integration supported

**Performance Advantages:**
- Split tunneling by default — only private resource traffic routes through internal network
- No backhauling — traffic routes directly, not through distant VPN servers
- Edge-based decision making via intelligent clients (ViPR technology) reduces tromboning latency
- MFA checks performed before connection initiation

**Deployment Advantages:**
- No hardware/appliances required
- Connector is a lightweight container installed on one device per network
- No IP address or DNS name changes required
- Protocol agnostic
- Deployable in minutes

**Operational Advantages:**
- Managed scalability — no appliance procurement or network reconfiguration to scale
- Centralized admin console for org-wide access management
- Can coexist with existing VPNs — no rip-and-replace required

## Prerequisites
- None for initial deployment; connector requires a single host within each private network

## Step-by-Step (Migration Approach)
1. Deploy Twingate alongside existing VPN infrastructure (no infrastructure changes needed)
2. Pilot with a single team and subset of resources
3. Gradually roll out to additional teams/resources
4. Decommission VPN infrastructure when ready

## Configuration Values
- No specific env vars or CLI flags documented on this page
- Connector delivered as a container image

## Gotchas
- VPN mode is "full tunnel" (all traffic); Twingate is split tunnel by default — behavior differs for users expecting all traffic routed through corporate network
- VPN gateways are publicly visible and regularly exploited (zero-days, unpatched CVEs); Twingate has no equivalent public endpoint — architectural difference matters for threat modeling
- User traffic appears to originate from actual location (not VPN server location) — affects geo-localized content behavior

## Related Docs
- [Zero Trust Networking explanation](https://www.twingate.com/docs/twingate-vs-vpn) (inline in this page)
- [Quick, simple, low-risk migration guide](https://www.twingate.com/docs/)
- Twingate free trial signup