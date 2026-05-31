# Security Policies Best Practices

## Summary
Twingate provides three distinct policy types controlling access at different levels: Admin Console, environment connection, and individual Resources. This guide covers designing a risk-based policy framework using resource cataloging, device verification, and group-based policy exceptions.

## Key Information

### Policy Types
| Type | Scope | Component |
|------|-------|-----------|
| Admin Console Security Policy | Admin/DevOps/Support roles only | Admin Console |
| Minimum Authentication Requirements | All users connecting to environment | Client |
| Resource Policy | Users accessing specific Resources | Client |

### Recommended Defaults
- **Admin Console Policy**: Re-auth every 1 hour (fixed), enforce MFA, assign Admin role to 2+ users
- **Minimum Auth Requirements**: Set to 31 days, no MFA (use Resource Policies for MFA instead)
- **Everyone Group Resources**: No auth required, device trust required; add IdP resource + AD/Domain Controllers (Windows)

## Policy Design Workflow

1. **Catalog Resources** by risk dimensions: data type (PII/non-PII), data volume, business impact of modifications, access method
2. **Map risk scores to policies** using re-auth frequency + MFA + device verification
3. **Apply group-based exceptions** (e.g., contractors without EDR, elevated IT access)

## Risk-to-Policy Mapping
| Risk Level | Re-auth | MFA | Device Verification |
|------------|---------|-----|---------------------|
| High | 2 hours | Yes | Required |
| Medium | 1 day | Yes | Required |
| Low | 1 week | Yes | Required |
| Very Low | 1 week | No | Required |

## Configuration Values

### Policy Naming Convention
`<Re-auth>-<MFA>-<DeviceVerif>` — e.g., `2H-MFA-Verif`, `1D-NoMFA-None`

### Trusted Profile Requirements (create separately per provider)
- macOS + CrowdStrike
- Windows + CrowdStrike  
- Windows + SentinelOne
- Windows + manual verification

### Windows Device Posture Checks (optional additions to Trusted Profiles)
- HD Encryption, Screen Lock, Firewall, Antivirus

## Gotchas

- **Minimum Auth Requirements do NOT grant Resource access** — only Resource Policies grant access
- **Everyone Group**: IdP and AD/Domain Controller resources must have auth disabled so Twingate Client can reach Domain Controllers before user logon
- **Multiple verification requirements in one Trusted Profile** = ALL must be satisfied (AND logic, not OR)
- **Contractors without EDR**: Use native posture checks (Screen Lock, Biometric) as alternative; block non-applicable OSes via Minimum OS Requirements
- **Policy exceptions per group**: A Resource can have a primary policy with group-level overrides (e.g., IT staff get stricter policy on POS than Retail group)
- Admin Console re-auth frequency of 1 hour cannot be modified

## Prerequisites
- EDR/MDM integrations configured under Device Settings (CrowdStrike, SentinelOne, etc.) before creating Trusted Profiles
- Groups defined and users assigned before configuring Resource access

## Related Docs
- [Trusted Profiles](https://www.twingate.com/docs)
- [Active Directory Guide](https://www.twingate.com/docs)
- [Device Settings](https://www.twingate.com/docs)