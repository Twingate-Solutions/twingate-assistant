# Twingate vs. VPNs

## Summary
Twingate implements Zero Trust Networking (ZTN) as an alternative to traditional VPNs, providing application-level access control rather than network-level access. Unlike VPNs, Twingate requires no public-facing gateway, eliminates backhauling, and deploys without infrastructure changes.

## Key Information

### Security Advantages over VPNs
- **Granular access control**: Per-application permissions vs. full network access
- **Hidden network**: Connectors make outbound connections only; no public gateway exposed to internet
- **Rich authorization context**: SSO/MFA, location, time-of-day, device posture, risk scores
- **Limited lateral movement**: Breach scope limited to specific apps, not entire network
- **Centralized logging**: Single view across all networks; SIEM integration supported

### Performance Advantages
- **No backhauling**: Traffic routes directly without passing through central VPN server
- **Split tunneling by default**: Only private resource traffic routes through internal network
- **Edge processing**: Client-side authorization processing reduces server roundtrips (ViPR technology)

### Deployment Advantages
- **No appliances**: Software-only, deploys in minutes
- **No infrastructure changes**: Single lightweight connector (container) per network
- **No IP/DNS changes**: Existing resource names remain unchanged
- **Protocol agnostic**: Supports all private applications without additional config
- **Coexists with existing VPNs**: Can run alongside VPN infrastructure during migration

### Cost Advantages
- OpEx model vs. VPN CapEx
- Lower IT admin burden
- Reduced help desk load

## Prerequisites
- None for testing alongside existing infrastructure
- Connector requires one device per private network to install container on

## Deployment Approach
1. Sign up (free trial available)
2. Install lightweight connector (container) on one device inside target network
3. Configure per-application access policies in admin console
4. Users download client and self-enroll
5. Roll out gradually (pilot with one team/resource subset)

## Configuration Values
- **Tunneling mode**: Split tunnel (default) — only private resource traffic routed internally
- **Client behavior**: Always-on, no manual toggle required
- **Authorization**: Processed at client edge before connection initiated to resource

## Gotchas
- VPN grants full network access upon auth; a compromised VPN credential exposes the entire network
- VPN gateways are publicly visible and regularly targeted (e.g., Travelex $30M ransomware incident)
- Full-tunnel VPN routes all traffic through potentially distant server, degrading performance for all internet activity
- VPNs may cause incorrect content localization (traffic appears to originate from VPN server location)

## Architecture Distinction
- **VPN**: Public gateway → user authenticates → full network access granted
- **Twingate**: Hidden connectors make outbound connections → per-resource access verified with contextual data → no network visibility to unauthorized users

## Related Docs
- Zero Trust Networking concepts
- Twingate Connector deployment
- Quick, simple, low-risk migration guide
- Free trial signup