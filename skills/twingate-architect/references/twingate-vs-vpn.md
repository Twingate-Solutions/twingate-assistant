# Twingate vs. VPNs

## Summary
Twingate implements Zero Trust Networking (ZTN) as an alternative to traditional VPNs, providing application-level access control instead of network-level access. Unlike VPNs, Twingate requires no public-facing gateways, eliminates traffic backhauling, and deploys without infrastructure changes.

## Key Information

**Security Differences**
- VPNs grant access to entire networks; Twingate grants access per-application (least privilege)
- VPN gateways are publicly visible and regularly exploited; Twingate Connectors make outbound-only connections, no public exposure
- Twingate supports contextual authorization: SSO/MFA, device posture, location, time-of-day, risk scores
- Breach blast radius is limited to specific apps, not entire network

**Performance Differences**
- Twingate uses split tunneling by default; VPNs use full tunnel (all traffic routed through VPN server)
- No backhauling: traffic routes directly to destination, not through central VPN server
- Decision processing pushed to client edge, reducing server bottlenecks

**Deployment Differences**
- VPNs require hardware procurement, network reconfiguration, segmentation planning
- Twingate deploys via lightweight container (Connector) on one device per network
- No IP address/hostname changes required
- Protocol agnostic; no per-application configuration needed

**Management Differences**
- Centralized admin console covers all networks (on-prem and cloud)
- Scales via UI clicks vs. hardware procurement
- SIEM integration available for centralized logging

## Prerequisites
- None for evaluation — no infrastructure changes required
- Existing VPNs can coexist during migration; no rip-and-replace needed

## Architecture Components
| Component | Role |
|-----------|------|
| Connector | Installed inside private network; makes outbound connections only |
| Client (ViPR) | Installed on user devices; handles split tunneling, auth processing, routing |
| Admin Console | Centralized policy and access management |

## Migration Path
1. Sign up (no infrastructure changes needed)
2. Deploy Connector container on one device per network
3. Pilot with single team on subset of resources
4. Expand gradually; existing VPN continues operating in parallel
5. Decommission VPN when ready

## Configuration Values
- No CLI flags or env vars documented on this page
- Connector delivered as container image
- Client available for self-service download by end users

## Gotchas
- VPN gateways must be publicly exposed; this is a persistent attack surface (e.g., Travelex $30M ransomware incident cited)
- VPN full-tunnel mode causes localization issues (content appears from VPN server's region, not user's)
- Split tunneling is Twingate's default behavior, not an opt-in feature
- Twingate handles load balancing, redundancy, and scaling — these are operator responsibilities with VPNs

## Related Docs
- Zero Trust Networking concepts
- Twingate Connector deployment
- Quick, simple, low-risk migration guide
- Free trial signup