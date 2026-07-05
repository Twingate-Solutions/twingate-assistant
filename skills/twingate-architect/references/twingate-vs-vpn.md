# Twingate vs. VPNs

## Summary
Twingate implements Zero Trust Networking (ZTN) as an alternative to traditional VPNs, providing application-level access control instead of network-level access. Unlike VPNs, Twingate requires no public-facing gateway, eliminates traffic backhauling, and deploys without infrastructure changes.

## Key Information

### Security Advantages
- **Application-level access control** — grants access per-app, not per-network (least-privilege enforcement)
- **No public gateway** — Connectors make outbound connections only; network stays hidden from internet
- **Rich authorization context** — supports SSO, MFA, device posture, location, time-of-day, risk scores
- **Limits lateral movement** — breach scope limited to specific apps, not entire network
- **Centralized logging** — single audit view across all networks; integrates with SIEM

### Performance Advantages
- **No backhauling** — traffic routes directly, not through a central VPN server
- **Split tunneling by default** — only private resource traffic routes through internal network
- **Edge processing** — client (ViPR technology) handles authorization locally, reducing round-trips

### Deployment Advantages
- No hardware/appliances required
- Connector is a lightweight container installed on one internal device
- No IP address or DNS name changes required
- Protocol agnostic
- Can coexist with existing VPN infrastructure (no rip-and-replace)

### Operational Advantages
- Centralized admin console for org-wide access management
- Scaling via admin UI (no appliance procurement)
- Twingate manages availability, load balancing, redundancy, patching

## Prerequisites
- None for evaluation — software-only, no infrastructure changes required
- Existing VPN can remain in place during migration

## Step-by-Step (Migration Approach)
1. Sign up and deploy a Connector (container) inside target network
2. Define Resources (specific apps/services) in admin console
3. Assign user/group access policies to Resources
4. Pilot with a single team and subset of resources
5. Gradually expand rollout; decommission VPN segments over time

## Configuration Values
- **Connector delivery**: Container (Docker-compatible)
- **Tunneling mode**: Split tunnel (default)
- **Auth factors**: SSO/IdP, MFA, device posture, IP/location, time-of-day, risk score
- **SIEM integration**: Supported

## Gotchas
- VPN grants network-wide access on authentication; Twingate grants per-resource access — requires upfront resource definition in admin console
- Connector makes **outbound** connections only — no inbound firewall rules needed, but network must allow outbound HTTPS/QUIC
- Split tunneling is default — traffic to public internet does **not** route through corporate network (may conflict with policies requiring full-tunnel)

## Related Docs
- [Zero Trust Networking overview](https://www.twingate.com/docs/)
- [Quick, simple, low-risk migration guide](https://www.twingate.com/docs/)
- [Free trial signup](https://www.twingate.com/)