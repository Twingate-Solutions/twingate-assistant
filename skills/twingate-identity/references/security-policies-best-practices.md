# Security Policies Best Practices

## Summary
Twingate provides three types of security policies: Admin Console, Minimum Authentication Requirements, and Resource Policies. This guide covers how to design, map, and configure these policies based on risk-scored assets, device verification, and group-based access. Includes a naming convention system and complete worked example.

## Key Information

- **Three policy types** with distinct scopes:
  - **Admin Console Policy**: Admin/DevOps/Support roles only; fixed 1-hour re-auth; enforce MFA
  - **Minimum Auth Requirements**: All users at Client connection; does NOT grant Resource access
  - **Resource Policy**: Per-resource; controls auth frequency, MFA, and device trust

- **Recommended Minimum Auth Requirements**: 31-day duration, no MFA (use Resource Policies for MFA instead)

- **Device verified** = passed EDR/MDM integration (CrowdStrike, SentinelOne, Jamf, etc.) OR manually marked in Admin Console

- **Device trusted** = verified + passes additional posture checks (HD Encryption, Screen Lock, Firewall, Antivirus)

- **Naming convention**: `<ReAuth>-<MFA>-<DeviceVerif>` (e.g., `2H-MFA-Verif`, `1D-NoMFA-None`)

## Prerequisites

- Admin Console access with Admin role
- EDR/MDM integrations configured under Device Settings (if using automated verification)
- Groups defined for users and devices
- Resources cataloged with risk assessments

## Step-by-Step: Designing Resource Policies

1. **Catalog Resources** — assess risk dimensions: data type, data volume, business impact, access method
2. **Score risk** — assign High/Medium/Low/Very Low per asset
3. **Map risk to policy** — define re-auth frequency, MFA requirement, device verification per tier
4. **Identify exceptions** — group-level overrides (e.g., contractors without EDR, IT with elevated access)
5. **Create Trusted Profiles** — one per OS/EDR combination (e.g., macOS+CrowdStrike, Windows+SentinelOne)
6. **Define minimal policy set** — deduplicate, add exception-only policies
7. **Assign policies to Resources** with group-level overrides where needed

## Configuration Values

| Policy Name | Re-auth | MFA | Device |
|---|---|---|---|
| `2H-MFA-Verif` | 2 hours | Required | Trusted only |
| `1D-MFA-Verif` | 1 day | Required | Trusted only |
| `1D-NoMFA-Verif` | 1 day | Not required | Trusted only |
| `1D-NoMFA-None` | 1 day | Not required | Any device |
| `1D-MFA-None` | 1 day | Required | Any device |
| `7D-MFA-Verif` | 7 days | Required | Trusted only |
| `7D-NoMFA-Verif` | 7 days | Not required | Trusted only |

## Gotchas

- **Everyone Group resources** (IdP, AD/Domain Controllers) must have **no authentication required** — these support authentication for other resources and must be accessible before user logon on Windows
- Multiple verification requirements in a single Trusted Profile require **both** to pass (AND logic, not OR)
- Admin Console policy re-auth interval is **fixed at 1 hour** (cannot be changed)
- Assign **at least 2 Admin users** to prevent Admin Console lockout
- Contractors without EDR/MDM need a separate policy path (e.g., native posture checks only, or `Any Device`)
- Minimum Auth Requirements alone do not grant Resource access unless the Resource Policy has authentication disabled

## Related Docs

- Trusted Profiles configuration
- Active Directory guide (Windows environments)
- Device Settings (EDR/MDM integrations)
- Everyone Group documentation