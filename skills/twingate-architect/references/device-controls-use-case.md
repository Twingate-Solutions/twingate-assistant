# Device Security Controls Use Case

## Page Title
Device Security Controls Use Case

## Summary
Twingate provides granular device-based access controls that screen users and devices against permitted characteristics (OS type, screen lock, MDM/EDR status, etc.). Policies are enforced at the edge on client devices rather than centrally, reducing latency and user friction. Integrations with major IdP, MDM, and EDR providers allow automated device trust delegation.

## Key Information
- Access policies evaluate device attributes: OS type, screen lock status, MDM enrollment, EDR presence
- Split tunneling enabled by default (unlike traditional VPNs)
- Policy enforcement happens on client devices (edge), not in the cloud
- Admin console available for manual management; Public API available for programmatic configuration
- Device trust can be delegated to third-party MDM/EDR solutions

## Supported Integrations
**Identity Providers:** Okta, JumpCloud, Entra ID, OneLogin, Google

**MDM Providers:** Intune, Jamf, Kandji

**EDR Solutions:** CrowdStrike, SentinelOne

**Other:** 1Password XAM

## Configuration Guides (Linked)
- Device Security Guide (primary reference)
- List of Device Security Posture Checks
- Automate Trusting Devices (Python CLI)
- Automate Trusting Devices (JavaScript CLI)
- Delegate Device Trust to: CrowdStrike, SentinelOne, Intune, Jamf, Kandji, 1Password XAM

## Gotchas
- This page is an overview/use-case page only — no direct configuration steps here; implementation details are in linked sub-guides
- Device posture checks vary by platform; consult the posture checks list for supported attributes per OS

## Related Docs
- Device Security Guide
- List of Device Security Posture Checks
- Identity Provider integration docs (Okta, JumpCloud, Entra ID, OneLogin, Google)
- MDM/EDR delegation guides (Intune, Jamf, Kandji, CrowdStrike, SentinelOne)
- Twingate Public API
- Resources, Networks, and Policies admin docs