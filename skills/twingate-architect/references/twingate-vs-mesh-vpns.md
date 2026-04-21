## Page Title
Twingate vs. Mesh VPNs

## Summary
Compares Twingate against mesh VPN products across deployment complexity, ongoing administration, enterprise security features, and end-user experience. Key practical difference: mesh VPNs require re-addressing all network resources and installing agents on every node; Twingate requires no infrastructure changes and only a Connector per remote network.

## Key Information
- **Infrastructure**: mesh VPNs require globally unique IPs — existing overlapping ranges must be re-addressed; Twingate supports overlapping IPs, no re-addressing, no infrastructure changes
- **Agent deployment**: mesh VPNs require an agent on every device including servers; Twingate requires only a client on user devices and a single Connector per remote network
- **Coexistence**: Twingate can run alongside existing VPN/mesh solutions for parallel evaluation — no rip-and-replace
- **Admin UX**: Twingate provides a GUI admin console; some mesh VPN products require JSON policy configuration
- **Enterprise security features** beyond basic access control:
  - Universal 2FA: applies 2FA to any protocol (SSH, RDP, databases) without application changes
  - Device posture restrictions: access policies based on device attributes
  - Identity-indexed network flow logs: all activity tied to user and device identity
- **Compatibility**: Twingate supports major IdPs (Okta, OneLogin, Google Workspace, Entra ID) and DNS filtering products

## Prerequisites
None — reference page.

## Step-by-Step
Not applicable.

## Configuration Values
None on this page.

## Gotchas
- Mesh VPN re-addressing is a blocking migration concern for organizations with complex overlapping IP topologies
- "Universal 2FA" applies at the Twingate access layer — the underlying application still handles its own auth after the Twingate connection is established
- Twingate's enterprise focus means simpler/self-hosted mesh VPNs (Tailscale, WireGuard) may still be appropriate for small teams without enterprise requirements

## Related Docs
- `/docs/twingate-vs-vpn` — comparison with traditional VPNs
- `/docs/ip-overlap` — overlapping IP address handling
- `/docs/architecture` — Twingate architecture overview
- `/docs/two-factor-authentication-security-policies` — 2FA policy configuration
