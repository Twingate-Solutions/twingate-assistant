# Device Security Controls Use Case

## Page Title
Device Security Controls Use Case

## Summary
Twingate provides granular device-based access controls that screen users and devices against permitted characteristics (OS type, screen lock, MDM/EDR status). Policies are enforced at the edge on client devices rather than centrally, and integrate with major IdP, MDM, and EDR providers.

## Key Information
- Access policies evaluate device attributes: OS type, screen lock, MDM enrollment, EDR status
- Split tunneling enabled by default (unlike traditional VPNs)
- Policy enforcement happens on client devices (edge), not in the cloud
- Web-based admin console available; programmatic config via Public API
- Supports principle of least privilege with per-resource device requirements

## Prerequisites
- Twingate account with admin access
- Identity Provider configured (Okta, JumpCloud, Entra ID, OneLogin, or Google)
- Optional: MDM provider (Intune, Jamf, Iru) or EDR solution (CrowdStrike, SentinelOne) for delegation

## Configuration Options

### Supported Integrations
| Category | Providers |
|----------|-----------|
| Identity Providers | Okta, JumpCloud, Entra ID, OneLogin, Google |
| MDM | Intune, Jamf, Iru |
| EDR | CrowdStrike, SentinelOne |
| Password/Access Mgmt | 1Password XAM |

## Implementation Paths
1. **Manual device trust** – Configure via web admin console
2. **Automated device trust** – Use Python or JavaScript CLI tools
3. **Delegated device trust** – Integrate with CrowdStrike, SentinelOne, Intune, Jamf, Iru, or 1Password XAM
4. **Programmatic config** – Use Public API for large-scale administration

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
- This page is an overview only; actual posture check configuration and delegation setup require referencing the linked sub-guides
- Device posture checks apply at the resource level, enabling different requirements for different resources (not a single global policy)