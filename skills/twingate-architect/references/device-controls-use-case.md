# Device Security Controls Use Case

## Page Title
Device Security Controls Use Case

## Summary
Twingate provides granular device-based access controls for corporate resources, screening devices against characteristics like OS type, screen lock status, and MDM/EDR enrollment. Policies are enforced at the edge (on client devices) rather than centrally, reducing latency. Integrations with major IdPs, MDM, and EDR providers enable automated device trust delegation.

## Key Information
- Access policies can require specific device attributes: OS type, screen lock, MDM enrollment, EDR presence
- Split tunneling enabled by default (unlike traditional VPNs)
- Policy enforcement happens on client devices (edge), not in the cloud
- Web-based admin console available; programmatic config via Public API
- Supports principle of least privilege with per-resource device requirements

## Prerequisites
- Twingate account with admin access
- Identity Provider configured (Okta, JumpCloud, Entra ID, OneLogin, or Google)
- Optional: MDM provider (Intune, Jamf, Iru) or EDR solution (CrowdStrike, SentinelOne) for delegated trust

## Configuration Values
No direct env vars or CLI flags on this page. Configuration is done via:
- Admin Console (web UI) for resources, networks, and policies
- Public API for programmatic configuration

## Integration Support
| Category | Supported Providers |
|----------|-------------------|
| Identity Providers | Okta, JumpCloud, Entra ID, OneLogin, Google |
| MDM | Intune, Jamf, Iru |
| EDR | CrowdStrike, SentinelOne |
| Password/XAM | 1Password XAM |

## Related Docs
- Device Security Guide
- List of Device Security Posture Checks
- Automate Trusting Devices (Python CLI)
- Automate Trusting Devices (JavaScript CLI)
- Delegate Device Trust to CrowdStrike
- Delegate Device Trust to SentinelOne
- Delegate Device Trust to Intune
- Delegate Device Trust to Jamf
- Delegate Device Trust to Iru
- Delegate Device Trust to 1Password XAM

## Gotchas
- This page is an overview only; actual posture check configuration requires following linked sub-guides
- Device trust delegation to third-party MDM/EDR requires separate integration setup per provider
- No step-by-step configuration on this page — all implementation details are in linked documents