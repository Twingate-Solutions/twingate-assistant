# Twingate vs. VPNs

## Page Title
Twingate vs. VPNs

## Summary
Twingate implements Zero Trust Networking (ZTN) as an alternative to traditional VPNs, providing application-level access control rather than network-level access. Unlike VPNs, Twingate requires no public-facing gateway, eliminates traffic backhauling via split tunneling, and deploys without infrastructure changes.

## Key Information

**Security Advantages over VPNs:**
- Granular per-application access control (not network-wide)
- No public gateway exposed on internet — connectors make outbound-only connections
- Authorization uses rich context: SSO/MFA, location, time, device posture, risk scores
- Limits lateral movement if credentials are compromised
- Centralized logging with SIEM integration support

**Performance Advantages:**
- Split tunneling by default — only private resource traffic routes through internal network
- No backhauling — traffic takes direct path, not through distant VPN server
- Edge processing via intelligent clients (Twingate ViPR technology) reduces latency
- Decentralized authorization decisions reduce bottlenecking

**Deployment Advantages:**
- No hardware appliances required
- Connector is a lightweight container installed on one device per network
- No IP/DNS changes required
- Protocol agnostic
- Works alongside existing VPNs — no rip-and-replace needed

## Prerequisites
- None for evaluation; free trial available
- Existing VPN infrastructure can remain in place during migration

## Step-by-Step (Migration Approach)
1. Deploy Twingate connector (container) inside existing network — no infra changes needed
2. Pilot with single team and subset of resources
3. Gradually expand rollout
4. Decommission VPN infrastructure when ready

## Configuration Values
- Connector deployed as a **container** (Docker-compatible)
- Supports all private application protocols (protocol agnostic)
- Split tunneling: **enabled by default**

## Gotchas
- VPN gateways are publicly visible and frequently exploited (CVEs from all major vendors); Twingate has no equivalent exposure
- VPN full-tunnel mode routes ALL traffic through corporate network — causes congestion and latency even for non-corporate traffic
- VPN access grants network-wide access; a single compromised credential exposes entire network segment
- Multi-VPN environments (multiple networks) require complex interconnection; Twingate centralizes via single admin console

## Architecture Difference
| VPN | Twingate |
|-----|----------|
| Network-level access | Application-level access |
| Public gateway (inbound) | Private connector (outbound only) |
| Full tunnel | Split tunnel |
| Perimeter trust model | Zero trust model |
| Hardware appliances | Software/container only |

## Related Docs
- [Zero Trust Networking explanation](https://www.twingate.com/docs/twingate-vs-vpn)
- Quick, simple migration guide (referenced internally)
- Free trial signup available at twingate.com