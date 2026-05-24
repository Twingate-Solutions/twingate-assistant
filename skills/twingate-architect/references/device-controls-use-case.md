# Device Security Controls Use Case

## Page Title
Device Security Controls Use Case

## Summary
Twingate provides granular device-level access controls that screen users and devices against permitted characteristics (OS type, screen lock, MDM/EDR status, etc.). Policies are enforced at the edge on client devices rather than centrally, reducing latency and user friction compared to VPN-based approaches.

## Key Information
- Access policies support device attributes: OS type, screen lock status, MDM enrollment, EDR status
- Split tunneling enabled by default (unlike traditional VPNs)
- Policy enforcement happens on client devices (edge), not cloud
- Web-based admin console available; programmatic configuration via Public API
- Principle of least privilege supported with per-resource device requirements

## Supported Integrations
**Identity Providers:** Okta, JumpCloud, Entra ID, OneLogin, Google

**MDM Providers:** Intune, Jamf, Iru

**EDR Solutions:** CrowdStrike, SentinelOne

**Other:** 1Password XAM

## Configuration Resources (Linked Guides)
- Device Security Guide (primary setup reference)
- List of Device Security Posture Checks
- Automate Trusting Devices (Python CLI)
- Automate Trusting Devices (JavaScript CLI)
- Delegate Device Trust to: CrowdStrike, SentinelOne, Intune, Jamf, Iru, 1Password XAM

## Gotchas
- Device trust delegation to third-party MDM/EDR requires separate per-integration configuration
- No inline configuration values on this page — refer to linked guides for specific parameters
- This is an overview/use-case page; implementation details are in linked documentation

## Related Docs
- Identity Provider integrations (Okta, JumpCloud, Entra ID, OneLogin, Google)
- Resources, Networks, and Policies administration
- Twingate Public API
- VPN comparison context (split tunneling behavior)