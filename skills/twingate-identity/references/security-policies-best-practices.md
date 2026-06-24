# Security Policies Best Practices

## Summary
Twingate provides three policy types to control access: Admin Console Security Policy, Minimum Authentication Requirements, and Resource Policies. This guide covers how to design, catalog, and configure these policies using risk-based frameworks with device verification and MFA. Includes a complete worked example mapping assets to policies with group-based exceptions.

## Key Information

- **Three policy types** with distinct scopes:
  - **Admin Console Security Policy**: Gates Admin Console access (Admin/DevOps/Support roles only); fixed 1-hour re-auth
  - **Minimum Authentication Requirements**: Applies to ALL users at Client connection; does not grant Resource access
  - **Resource Policy**: Applied per-Resource; controls auth frequency, MFA, and device trust

- **Minimum Auth Requirements best practice**: Set to 31 days, no MFA (use MFA at Resource Policy level instead)

- **Admin Console best practice**: Enforce MFA, assign Admin role to 2+ users to prevent lockout

- **Device verification methods**: EDR/MDM integrations (CrowdStrike, SentinelOne), manual serial number, or Twingate-native posture checks

- **Trusted Profiles** combine verification method + posture checks (HD encryption, screen lock, firewall, antivirus); multiple verification requirements in one profile = ALL must be met

## Policy Naming Convention
`<Re-auth>-<MFA>-<DeviceVerif>` (e.g., `2H-MFA-Verif`, `1D-NoMFA-None`)

## Risk-to-Policy Mapping

| Risk Level | Re-auth | MFA | Device Verification |
|------------|---------|-----|-------------------|
| High | 2 hours | Yes | Trusted device |
| Medium | 1 day | Yes | Trusted device |
| Low | 1 week | Yes | Trusted device |
| Very Low | 1 week | No | Trusted device |

## Step-by-Step: Policy Design

1. Catalog Resources and assign risk scores based on: data type, data volume, business impact of modifications, access method
2. Map risk scores to policy definitions (re-auth interval, MFA, device verification)
3. Configure EDR/MDM integrations under Device Settings
4. Create Trusted Profiles (separate profiles per OS/verification provider)
5. Create all required Security Policies in Twingate
6. Assign primary policies to Resources
7. Add group-based policy exceptions per Resource where needed

## "Everyone" Group Configuration

- Assign IdP resource (e.g., `*.okta.com`) and AD/Domain Controller resources
- Policy: **No authentication required**, device trust required
- Rationale: Allows Client to reach Domain Controllers before user logon

## Gotchas

- **Minimum Auth Requirements ≠ Resource access** — a user passing minimum auth still needs an applicable Resource Policy
- **Multiple verification requirements in one Trusted Profile** = AND logic (all must pass)
- **Contractors without EDR/MDM**: Use native OS posture checks (screen lock, biometrics) or no verification; block non-applicable OSes via Trusted Profile OS restrictions
- **IdP/AD traffic** should be assigned to "Everyone" with no auth — authentication belongs on the actual Resources, not infrastructure traffic
- **IT group exceptions**: Higher-privilege groups may need stricter policies than the primary policy on shared Resources (e.g., IT accessing POS needs `1D-MFA-Verif` vs. `1W-NoMFA-Verif` for Retail)
- Admin Console policy **cannot** change the 1-hour re-auth interval

## Related Docs
- Active Directory guide (referenced for Domain Controller setup)
- Trusted Profiles configuration
- Device Settings (EDR/MDM integration)