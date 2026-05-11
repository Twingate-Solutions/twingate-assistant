# Security Policies Best Practices

## Summary
Twingate provides three policy types to control access: Admin Console Security Policy, Minimum Authentication Requirements, and Resource Policies. Best practice involves cataloging resources by risk level, mapping risk to policy definitions, and applying group-based exceptions. Resource Policies are the primary mechanism for granular access control.

## Key Information

- **Three policy types**: Admin Console (console access only), Minimum Auth Requirements (environment access, not resource access), Resource Policies (resource-level control)
- **Minimum Auth Requirements** apply to ALL users regardless of group; do NOT grant resource access unless resource policy has auth disabled
- **Resource Policy** controls: authentication requirement, device trust, MFA, re-auth frequency
- **Device verification**: via EDR/MDM integration (CrowdStrike, SentinelOne, Kandji, Jamf) or manual marking in Admin Console
- **Everyone Group**: cannot be deleted; should contain IdP and Active Directory resources with no-auth policies
- **Trusted Profiles**: combining multiple verification methods requires ALL to pass (AND logic, not OR)

## Prerequisites

- Admin Console access with Admin role
- EDR/MDM integrations configured under Device Settings (if using automated verification)
- Risk assessment of resources completed
- Groups defined for users and contractors

## Configuration Values

**Admin Console Security Policy:**
- Re-auth: every 1 hour (hardcoded, cannot change)
- MFA: enforced
- Minimum 2 Admin-role users assigned

**Minimum Authentication Requirements:**
- Re-auth: 31 days (recommended)
- MFA: disabled (use Resource Policies for MFA instead)

**Risk-to-Policy Mapping:**
| Risk | Re-auth | MFA | Device |
|------|---------|-----|--------|
| High | 2 hours | Yes | Trusted |
| Medium | 1 day | Yes | Trusted |
| Low | 1 week | Yes | Trusted |
| Very Low | 1 week | No | Trusted |

**Recommended Policy Set (naming: `<reauth>-<MFA>-<device>`):**
- `2H-MFA-Verif` — prod infra, source code, IdP/AD admin
- `1D-MFA-Verif` — fileshare, non-prod, support systems
- `7D-NoMFA-Verif` — POS (primary)
- `7D-MFA-Verif` — synthetic data repo (primary)
- `1D-NoMFA-Verif` — AD non-admin (Everyone group)
- `1D-NoMFA-None` — IdP non-admin (Everyone group)
- `1D-MFA-None` — contractor exception (no device verification available)

## Gotchas

- **IdP and AD/DC traffic** must be intercepted by Twingate; assign to Everyone group with **no auth required** — AD must be accessible before user logon
- **Multiple verification in one Trusted Profile** = AND logic; both required simultaneously
- **Contractors without EDR** require separate policies without device verification (`*-None` suffix); can still enforce OS-level posture checks (screen lock, biometrics)
- **IT staff** may need stricter policies than primary group when accessing shared resources (e.g., IT accessing POS needs override: `1D-MFA-Verif` instead of `7D-NoMFA-Verif`)
- Minimum Auth Requirements alone do NOT grant resource access

## Step-by-Step (Policy Design Process)

1. Catalog resources and assign risk scores
2. Map risk scores to re-auth/MFA/device policy definitions
3. Define device groups and verification methods per group
4. Configure EDR/MDM integrations in Device Settings
5. Create Trusted Profiles (per OS + verification provider combination)
6. Identify exceptions (contractor device limits, role-based access differences)
7. Create all required policies + exception policies in Twingate
8. Assign primary policies to resources; apply group-level overrides
9. Assign IdP and AD resources to Everyone group with no-auth policy

## Related Docs

- Trusted Profiles configuration
- Active Directory guide (Windows environments)
- Device Settings / EDR integration setup
- Everyone Group documentation