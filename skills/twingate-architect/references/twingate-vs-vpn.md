# Twingate vs. VPNs

## Summary
Twingate implements Zero Trust Networking (ZTN) as an alternative to corporate VPNs. Unlike VPNs which grant network-level access, Twingate provides per-application access control with no public-facing gateway. It deploys as software only (no hardware appliances) and can coexist with existing VPN infrastructure.

## Key Information

**Security Differences**
- VPNs grant access to entire network; Twingate grants access per-application (least privilege)
- VPN gateways are publicly visible and attackable; Twingate Connectors make outbound-only connections — no public exposure
- Twingate authorization supports SSO/MFA, device posture, location, time-of-day, and risk scores vs. VPN's username/password/IP
- Lateral movement is blocked; attackers cannot see or traverse the network

**Performance Differences**
- VPNs backhaul all traffic through a central server; Twingate routes traffic directly
- Twingate uses split tunneling by default — only private resource traffic routes internally
- Twingate clients handle edge processing (authorization, MFA checks) without round-tripping to cloud

**Deployment Differences**
- VPNs require hardware procurement and network reconfiguration; Twingate deploys via a single lightweight container (Connector) per network
- No IP/DNS changes required; existing resource names remain unchanged
- Protocol agnostic — no per-app configuration needed

**Operational Differences**
- Centralized admin console manages all networks vs. fragmented VPN management
- Scalability handled by Twingate service; no appliance procurement needed
- Integrates with SIEM systems for centralized logging

## Prerequisites
- None for evaluation — free trial available
- One device per private network to host the Connector container
- Existing VPN infrastructure does not need to be removed

## Deployment Notes
1. Sign up for Twingate (no hardware required)
2. Deploy Connector container on one device inside each private network
3. Define resources and access policies in admin console
4. Users install client app and self-enroll
5. Can run in parallel with existing VPN — no cutover required

## Configuration Values
- Connector: delivered as a container image
- Client: always-on, single-click activation, no server selection required
- Traffic routing: split tunnel by default

## Gotchas
- VPN gateways are public attack surfaces; all major vendors have had CVEs exploited in the wild
- Full-tunnel VPN degrades performance for all traffic, not just private resource access
- VPN with multi-network setups requires complex mesh of VPN-to-VPN connections
- Users behind VPNs appear to originate from VPN server location, causing content localization issues

## Related Docs
- [Zero Trust Networking concepts](https://www.twingate.com/docs/)
- [Quick, simple, low-risk migration guide](https://www.twingate.com/docs/)
- [Free trial signup](https://www.twingate.com/)