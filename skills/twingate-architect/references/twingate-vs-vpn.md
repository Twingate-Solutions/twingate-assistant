# Twingate vs. VPNs

## Page Title
Twingate vs. VPNs — Conceptual Overview

## Summary
Explains architectural and operational differences between traditional VPN-based perimeter security and Twingate's Zero Trust Networking (ZTN) model. Covers security, performance, deployment, UX, and cost dimensions. Intended as an evaluation/decision guide rather than implementation reference.

## Key Information

**Security Advantages over VPN:**
- Per-application access control (not network-level)
- No public-facing gateway; connectors make outbound-only connections
- Authorization uses contextual factors: SSO/MFA, location, time, device posture, risk score
- Lateral movement blocked — attackers cannot traverse network even if one resource is compromised
- Centralized logging; SIEM integration supported

**Performance Advantages:**
- Split tunneling by default — only private traffic routes internally
- No backhauling — traffic routes directly, not through central VPN server
- Edge-based authorization processing (Twingate ViPR technology in client)
- Reduced corporate network congestion

**Deployment Differences:**
- No hardware/appliances required
- Single lightweight connector (container) per network
- No IP/DNS changes required
- Protocol agnostic
- Can coexist with existing VPNs — no rip-and-replace needed

**Management:**
- Centralized admin console for all networks
- Scaling via UI clicks vs. hardware procurement

## Prerequisites
- None for evaluation
- Connector deployment requires a host within the target private network (container-based)

## Configuration Values
None specified in this document (conceptual overview only).

## Gotchas
- VPN = full tunnel (all traffic); Twingate = split tunnel by default — behavior change users should expect
- VPN gateways are publicly visible and probed by attackers; Twingate connectors are internal and initiate outbound connections only
- Twingate can run alongside existing VPNs during phased migration — no forced cutover

## Related Docs
- [Quick, simple and low risk migration guide](#) (linked inline)
- Zero Trust Networking explanation (covered inline in this doc)
- Free trial signup (linked inline)