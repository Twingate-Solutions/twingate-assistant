# Twingate vs. VPNs

## Summary
Twingate implements Zero Trust Networking (ZTN) as an alternative to corporate VPNs, providing application-level access control rather than network-level access. Unlike VPNs, Twingate requires no public-facing gateway, eliminates traffic backhauling, and deploys as a software-only service with no hardware or infrastructure changes required.

## Key Information

### Security Advantages Over VPNs
- **Granular access control**: Per-application permissions vs. full network access with VPNs
- **Hidden network**: No public gateway exposed; Connectors make outbound-only connections from inside private networks
- **Rich authorization context**: SSO/MFA, location, time-of-day, device posture, risk scores
- **Lateral movement prevention**: Breach scope limited to specific apps; network remains invisible to attackers
- **Centralized logging**: Single SIEM-integrated view across all networks

### Performance Advantages
- **No backhauling**: Traffic routes directly; not forced through a distant VPN server
- **Split tunneling by default**: Only internal traffic routes through private network
- **Edge processing (ViPR technology)**: Client handles authorization locally, reducing round-trip latency
- **Reduced corporate network congestion**

### Deployment Differences
| VPN | Twingate |
|-----|----------|
| Hardware appliances required | Software-only, no hardware |
| Network reconfiguration needed | No infrastructure changes |
| Complex setup | Deploy in minutes |
| Manual scaling | Scale with clicks |
| Per-server client configuration | Always-on, automatic routing |

## Prerequisites
- None for testing — can run alongside existing VPN infrastructure without changes
- Single lightweight Connector (container) installed inside target network

## Deployment Notes
1. Sign up for Twingate (free trial available)
2. Install Connector container on one device inside the private network
3. Configure resource access policies in admin console
4. Users download client and self-enroll with single click
5. Optionally pilot with one team/resource subset before full rollout

## Configuration Values
- **Connector delivery**: Container (Docker/equivalent)
- **Tunnel mode**: Split tunnel (default)
- **Auth factors supported**: SSO, MFA, IP, location, time, device posture, risk score
- **Protocol support**: Protocol-agnostic (all private applications)

## Gotchas
- VPN gateways are publicly visible and regularly targeted by exploits (CVEs exist for all major vendors); Twingate Connectors are not publicly exposed
- VPN full-tunnel mode routes all traffic through corporate network regardless of destination — degrades performance for non-corporate traffic
- With VPNs, a single breach exposes the entire network; Twingate limits blast radius to specific authorized resources
- No IP/hostname changes required when migrating — existing resource names work as-is

## Cost Model
- VPN: Upfront capex (appliances) + ongoing expert staffing for patching/maintenance
- Twingate: Opex subscription, no hardware, lower admin overhead

## Related Docs
- Zero Trust Networking concepts
- Twingate Connector installation
- Quick, simple, low-risk migration guide
- Free trial signup