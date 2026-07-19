# Device Security Controls Use Case

## Page Title
Device Security Controls Use Case

## Summary
Twingate provides granular device-based access controls that screen users and devices against permitted characteristics (OS type, screen lock, MDM/EDR status, etc.). Policies are enforced at the edge on client devices rather than in the cloud. Supports integration with major IdPs, MDM providers, and EDR solutions.

## Key Information
- Access policies can require specific device characteristics per resource
- Split tunneling enabled by default (unlike traditional VPNs)
- Policy enforcement happens on client devices (edge), not cloud
- Web-based admin console available; programmatic config via Public API
- Supports delegating device trust to third-party security tools

## Prerequisites
- Twingate account with admin access
- Identity Provider configured (Okta, JumpCloud, Entra ID, OneLogin, or Google)
- Optional: MDM or EDR solution for delegated trust

## Supported Integrations
**Identity Providers:** Okta, JumpCloud, Entra ID, OneLogin, Google

**MDM Providers:** Intune, Jamf, Iru

**EDR Solutions:** CrowdStrike, SentinelOne

**Password Managers:** 1Password XAM

## Configuration Areas
- Device posture checks (OS type, screen lock, MDM enrollment, EDR status)
- Per-resource device requirements (least privilege per resource)
- Delegated device trust to MDM/EDR providers
- Automated device trust via Python or JavaScript CLIs

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
- Public API docs (for programmatic config)

## Gotchas
- This is an overview/use-case page — implementation details are in linked sub-guides
- Device trust delegation requires separate configuration per MDM/EDR provider
- No VPN-style full-tunnel routing; split tunneling is the default behavior