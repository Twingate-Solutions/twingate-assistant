## Page Title
Twingate vs. VPNs

## Summary
VPNs grant network-level access — authenticated users reach the entire network segment, which expands blast radius and requires exposing a public gateway. Twingate implements Zero Trust Networking with per-application access control, no public gateway, and rich contextual authorization (identity, device posture, location, time, risk score). The key architectural shift: Twingate Connectors make outbound connections only — the private network is never publicly visible.

## Key Information
- **VPN model**: castle-and-moat perimeter; remote users join the network via a public VPN gateway
- **ZTN model**: every access attempt verified regardless of network location; no implicit trust
- **No public gateway**: Twingate Connectors initiate outbound connections — nothing is exposed on the internet for attackers to probe
- **Per-application access**: users access only specific authorized resources, not the whole network — limits lateral movement
- **Rich auth context**: identity (SSO/MFA), device posture (OS, MDM, EDR, screen lock), physical location, time of day, risk score
- **Centralized logging**: single pane across all networks; integrates with SIEM
- **Least privilege**: access granted at resource level, not network level — key ZTN principle
- **VPN vulnerabilities**: public gateways are constantly probed; major vendor CVEs (e.g. Travelex $30M ransomware) are a pattern

## Prerequisites
None — this is a comparison/concept page.

## Step-by-Step
Not applicable.

## Configuration Values
None on this page.

## Gotchas
- "Zero trust" here refers to the network access model (ZTN), not a product category — Twingate is a ZTN implementation
- VPN replacement is a common starting use case but Twingate's policy engine (device posture, contextual auth) goes beyond what VPNs support
- Twingate does not require replacing existing identity providers — it integrates with SSO/MFA

## Related Docs
- `/docs/architecture` — how Twingate's four components implement ZTN
- `/docs/use-cases` — VPN replacement and other scenarios
- `/docs/quick-start` — getting started
