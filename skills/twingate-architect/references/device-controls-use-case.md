# Device Security Controls Use Case

## Page Title
Device Security Controls Use Case

## Summary
Twingate provides granular device-based access controls that screen users and devices against permitted characteristics (OS type, screen lock, MDM/EDR status, etc.). Policies are enforced at the edge on client devices rather than centrally, enabling least-privilege access without VPN performance overhead.

## Key Information
- Access policies evaluate device attributes: OS type, screen lock enabled, MDM enrollment, EDR status
- Split tunneling enabled by default (unlike traditional VPNs)
- Policy enforcement happens on client devices (edge), not cloud
- Admin console available for manual management; Public API for programmatic configuration

## Supported Integrations

**Identity Providers:**
- Okta, JumpCloud, Entra ID, OneLogin, Google

**MDM Providers:**
- Intune, Jamf, Kandji

**EDR Solutions:**
- CrowdStrike, SentinelOne

**Other:**
- 1Password XAM

## Configuration Resources (Step-by-Step Guides)
1. Device Security Guide (general setup)
2. List of Device Security Posture Checks
3. Automate Trusting Devices – Python CLI
4. Automate Trusting Devices – JavaScript CLI
5. Delegate Device Trust to CrowdStrike
6. Delegate Device Trust to SentinelOne
7. Delegate Device Trust to Intune
8. Delegate Device Trust to Jamf
9. Delegate Device Trust to Kandji
10. Delegate Device Trust to 1Password XAM

## Gotchas
- This page is an overview only — implementation details are in linked sub-guides
- Device trust delegation to third-party MDM/EDR requires separate integration configuration per provider
- Bring-your-own-device and contractor scenarios require explicit policy design; defaults may not restrict unmanaged devices

## Related Docs
- Identity Provider integration docs (Okta, JumpCloud, Entra ID, OneLogin, Google)
- Resources, Networks, and Policies administration docs
- Twingate Public API docs
- VPN comparison documentation