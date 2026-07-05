# Device Security Controls Use Case

## Page Title
Device Security Controls Use Case

## Summary
Twingate provides granular device-level access controls that screen users and devices against permitted characteristics (OS type, screen lock, MDM/EDR status, etc.). Policies are enforced at the edge on client devices rather than centrally, reducing latency and user friction. Integrations with major IdP, MDM, and EDR providers allow automated device trust delegation.

## Key Information
- Access policies enforce device posture checks including: OS type, screen lock status, MDM enrollment, EDR presence
- Split tunneling enabled by default (unlike traditional VPNs)
- Policy enforcement occurs on client devices (edge), not in the cloud
- Admin console available for manual management; Public API available for programmatic configuration
- Device trust can be delegated to third-party security tools

## Prerequisites
- Twingate account with admin access
- Identity Provider configured (Okta, JumpCloud, Entra ID, OneLogin, or Google)
- Optional: MDM or EDR solution for delegated trust

## Supported Integrations
**Identity Providers:** Okta, JumpCloud, Entra ID, OneLogin, Google

**MDM Providers:** Intune, Jamf, Iru

**EDR Solutions:** CrowdStrike, SentinelOne

**Password Managers:** 1Password XAM

## Configuration Paths
- Manual: Web-based Admin Console → manage resources, networks, policies
- Programmatic: Twingate Public API
- Automated device trust: Python CLI or JavaScript CLI tools

## Related Docs
- Device Security Guide
- List of Device Security Posture Checks
- How to Automate Trusting Devices (Python CLI)
- How to Automate Trusting Devices (JavaScript CLI)
- How to Delegate Device Trust to CrowdStrike
- How to Delegate Device Trust to SentinelOne
- How to Delegate Device Trust to Intune
- How to Delegate Device Trust to Jamf
- How to Delegate Device Trust to Iru
- How to Delegate Device Trust to 1Password XAM

## Gotchas
- This is an overview/use-case page; actual posture check configuration details are in the linked Device Security Guide and posture checks reference
- Device trust delegation requires separate integration setup per MDM/EDR provider
- Least privilege enforcement requires defining specific device requirements per resource/group combination