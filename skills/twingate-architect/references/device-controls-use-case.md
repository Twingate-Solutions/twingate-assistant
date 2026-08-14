---
source: https://www.twingate.com/docs/device-controls-use-case
type: docs
fetched: 2026-08-14
source_version: ebb8a92519f13626ca9f48248458a065217a070c31f6ba5af6c3f1c4333f7dae
---

# Device Security Controls Use Case

## Page Title
Device Security Controls Use Case

## Summary
Twingate provides granular device-based access controls that screen users and devices against permitted characteristics (OS type, screen lock, MDM/EDR status). Policies are enforced at the edge on client devices rather than centrally. Integrates with major IdP, MDM, and EDR providers.

## Key Information
- Access policies evaluate device attributes: OS type, screen lock status, MDM enrollment, EDR presence
- Split tunneling enabled by default (unlike traditional VPNs)
- Policy enforcement happens on client devices (edge), not in the cloud
- Web-based admin console available; Public API available for programmatic configuration
- Supports principle of least privilege with per-resource device requirements

## Prerequisites
- Twingate account with admin access
- Identity Provider configured (Okta, JumpCloud, Entra ID, OneLogin, or Google)
- Optional: MDM provider (Intune, Jamf, Iru) or EDR solution (CrowdStrike, SentinelOne) for delegated trust

## Integrations Supported

**Identity Providers:**
- Okta, JumpCloud, Entra ID, OneLogin, Google

**MDM Providers:**
- Intune, Jamf, Iru

**EDR Solutions:**
- CrowdStrike, SentinelOne

**Password Managers:**
- 1Password XAM

## Configuration Guides (Step-by-Step References)
1. Device Security Guide (primary setup reference)
2. List of Device Security Posture Checks
3. Automate Trusting Devices – Python CLI
4. Automate Trusting Devices – JavaScript CLI
5. Delegate Device Trust to CrowdStrike
6. Delegate Device Trust to SentinelOne
7. Delegate Device Trust to Intune
8. Delegate Device Trust to Jamf
9. Delegate Device Trust to Iru
10. Delegate Device Trust to 1Password XAM

## Gotchas
- Device posture checks apply at the resource level, so different resources can have different device requirements — plan policy structure carefully
- Delegated trust (MDM/EDR) requires additional integration setup beyond basic Twingate configuration
- Split tunneling is on by default; non-Twingate traffic routes normally outside the tunnel

## Related Docs
- Device Security Guide
- List of Device Security Posture Checks
- Identity Provider integration docs
- Resources, Networks, and Policies administration
- Twingate Public API