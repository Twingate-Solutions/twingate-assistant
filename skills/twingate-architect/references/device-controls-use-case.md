# Device Security Controls Use Case

## Page Title
Device Security Controls Use Case

## Summary
Twingate provides granular device-based access controls that screen devices against permitted characteristics (OS type, screen lock, MDM/EDR status) before granting access to private resources. Policies are enforced at the edge on client devices, supporting integrations with major MDM and EDR providers.

## Key Information
- Access policies evaluate device posture characteristics: OS type, screen lock status, MDM enrollment, EDR presence
- Split tunneling enabled by default (unlike traditional VPNs)
- Policy enforcement happens on client devices (edge), not in the cloud
- Supports programmatic configuration via Public API

## Integrations Supported
**Identity Providers:** Okta, JumpCloud, Entra ID, OneLogin, Google

**MDM Providers:** Intune, Jamf, Kandji

**EDR Solutions:** CrowdStrike, SentinelOne

**Other:** 1Password XAM

## Configuration Guides (Linked)
- Device Security Guide (main reference)
- List of Device Security Posture Checks
- Automate Trusting Devices (Python CLI)
- Automate Trusting Devices (JavaScript CLI)
- Delegate Device Trust to CrowdStrike
- Delegate Device Trust to SentinelOne
- Delegate Device Trust to Intune
- Delegate Device Trust to Jamf
- Delegate Device Trust to Kandji
- Delegate Device Trust to 1Password XAM

## Gotchas
- This page is an overview only — actual configuration requires following provider-specific delegation guides
- Device trust delegation to third-party MDM/EDR replaces manual device approval workflows

## Related Docs
- Device Security Guide
- Device Security Posture Checks list
- Resources, Networks, and Policies (admin console)
- Public API documentation
- Identity Provider integration docs