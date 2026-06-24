# Device Security Controls Use Case

## Page Title
Device Security Controls Use Case

## Summary
Twingate provides granular device-based access controls that screen users and devices against permitted characteristics (OS type, screen lock, MDM/EDR status, etc.). Policies are enforced at the edge on client devices rather than centrally. Integrations with major IdPs, MDM, and EDR providers are supported.

## Key Information
- Access policies enforce device posture checks including: OS type, screen lock status, MDM enrollment, EDR presence
- Split tunneling enabled by default (unlike traditional VPNs)
- Policy enforcement happens on client devices (edge), not in the cloud
- Admin console available for manual management; Public API available for programmatic configuration

## Prerequisites
- Twingate account with admin access
- Identity Provider configured (Okta, JumpCloud, Entra ID, OneLogin, or Google)
- Optional: MDM provider (Intune, Jamf, Iru) or EDR solution (CrowdStrike, SentinelOne) for delegated trust

## Configuration Options

### Delegated Device Trust Integrations
| Provider | Type |
|----------|------|
| CrowdStrike | EDR |
| SentinelOne | EDR |
| Intune | MDM |
| Jamf | MDM |
| Iru | MDM |
| 1Password XAM | Device Trust |

## Step-by-Step (Implementation Path)
1. Configure device security posture checks via Device Security Guide
2. Set up delegated device trust with MDM/EDR provider (if applicable)
3. Automate device trust via Python or JavaScript CLI (optional)
4. Apply policies to Resources and Networks via admin console or Public API

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
- Twingate Public API docs

## Gotchas
- This page is a use-case overview only; actual configuration requires following the linked sub-guides
- Device posture checks require Twingate client installed on end-user devices
- Delegated trust to MDM/EDR means those systems become a dependency for access decisions