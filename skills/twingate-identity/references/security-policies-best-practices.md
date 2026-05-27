# Security Policies Best Practices

## Summary
Twingate provides three types of security policies: Admin Console, Minimum Authentication Requirements, and Resource Policies. This guide covers how to design and implement granular Resource Policies based on risk assessment, device verification, and group-based access control. Includes a naming convention system and complete policy mapping workflow.

## Key Information

- **Three policy types**: Admin Console (admin users only), Minimum Auth Requirements (all users, no resource access granted), Resource Policies (per-resource access control)
- **Resource Policy controls**: authentication frequency, device trust requirements, MFA requirement, re-authentication interval
- **Device verification methods**: EDR/MDM integration (CrowdStrike, SentinelOne, Jamf, etc.) or manual marking in Admin Console
- **Recommended naming convention**: `<ReAuth>-<MFA>-<DeviceVerif>` (e.g., `2H-MFA-Verif`, `1D-NoMFA-None`)
- **Everyone Group**: Cannot be deleted; should contain IdP and Active Directory resources with no-auth policies to support infrastructure traffic

## Prerequisites

- EDR/MDM integrations configured under Device Settings before creating Trusted Profiles
- At least 2 Admin-role users assigned (lockout prevention)
- Risk assessment completed for all resources before policy design

## Step-by-Step: Policy Design Workflow

1. **Catalog resources** — assess risk dimensions: data type (PII vs non-PII), data volume, business impact of modifications, access method
2. **Score risk** — assign High/Medium/Low/Very Low to each resource
3. **Map risk to policy definitions**:
   - High: re-auth every 2h, MFA required, verified device
   - Medium: re-auth every 1 day, MFA required, verified device
   - Low: re-auth every 1 week, MFA required, verified device
   - Very Low: re-auth every 1 week, no MFA, verified device
4. **Define device groups** — map OS restrictions and verification methods per group (EDR, MDM, manual serial)
5. **Create Trusted Profiles** — separate profiles per OS/verification provider combination
6. **Identify exceptions** — contractor groups without EDR, elevated IT permissions, etc.
7. **Create policies** — only unique policy combinations needed; reuse across resources

## Configuration Values

| Policy Name | Re-auth | MFA | Device Security |
|---|---|---|---|
| `2H-MFA-Verif` | 2 hours | Required | Trusted only |
| `1D-MFA-Verif` | 1 day | Required | Trusted only |
| `1D-NoMFA-Verif` | 1 day | Not required | Trusted only |
| `1D-NoMFA-None` | 1 day | Not required | Any device |
| `1D-MFA-None` | 1 day | Required | Any device |
| `7D-MFA-Verif` | 7 days | Required | Trusted only |
| `7D-NoMFA-Verif` | 7 days | Not required | Trusted only |

**Admin Console Policy**: Re-auth every 1 hour (fixed), MFA enforced  
**Minimum Auth Requirements**: 31-day session, no MFA (delegate MFA to Resource Policies)

## Gotchas

- Minimum Auth Requirements do **not** grant resource access — they only gate client connection
- Admin Console re-auth interval (1 hour) **cannot be changed**
- IdP and Active Directory traffic resources (Everyone group) must have **no authentication** to allow pre-logon domain controller access on Windows
- Multiple verification requirements in one Trusted Profile = **both required** (AND logic, not OR)
- Selecting a Trusted Profile for a group with no available EDR (e.g., BYOD contractors) requires a separate no-verification policy path

## Related Docs

- Active Directory guide (referenced for Domain Controller setup)
- Trusted Profiles configuration
- Device Settings (EDR/MDM integration setup)
- Everyone Group documentation