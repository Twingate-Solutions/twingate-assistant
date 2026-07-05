# Security Policies Best Practices

## Summary
Twingate provides three policy types—Admin Console, Minimum Authentication Requirements, and Resource Policies—each controlling different access scopes. Resource Policies are the primary mechanism for granular access control and should be designed around asset risk scoring. The guide provides a complete framework for mapping risks to policy definitions with group-based overrides.

## Key Information

- **Three policy types**: Admin Console (console access only), Minimum Auth Requirements (client connection, all users), Resource Policies (per-resource access)
- **Minimum Auth Requirements** do NOT grant resource access—they only gate client connection
- **Policy naming convention recommended**: `<ReAuth>-<MFA>-<DeviceVerif>` (e.g., `2H-MFA-Verif`)
- **Device verified** = passed EDR/MDM integration (CrowdStrike, SentinelOne, etc.) OR manually marked in Admin Console
- **Everyone Group**: Cannot be deleted; assign IdP and Active Directory resources here with **no auth required** (needed pre-logon for domain controllers)

## Prerequisites

- EDR/MDM integrations configured under Device Settings (CrowdStrike, SentinelOne, etc.)
- Groups defined per user category (employees, contractors, etc.)
- Resources cataloged with risk scores assigned

## Risk-to-Policy Mapping

| Risk Level | Re-auth | MFA | Device Verification |
|------------|---------|-----|-------------------|
| High | 2 hours | Required | Trusted device |
| Medium | 1 day | Required | Trusted device |
| Low | 1 week | Required | Trusted device |
| Very Low | 1 week | Not required | Trusted device |

## Configuration Values

**Admin Console Policy (fixed):**
- Re-authenticate every: `1 hour` (cannot be changed)
- MFA: enforced
- Min admins: 2 users assigned Admin role

**Minimum Authentication Requirements:**
- Duration: `31 days` (recommended)
- MFA: disabled (use Resource Policies for MFA instead)

**Trusted Profile requirements (Windows):** HD Encryption, Screen Lock, Firewall, Antivirus

## Step-by-Step: Policy Design

1. Catalog resources and assign risk scores (data type, volume, business impact, access method)
2. Map risk scores → policy definitions
3. Define group device capabilities (EDR available? BYOD? OS restrictions?)
4. Create Trusted Profiles per verification provider/OS combination
5. Identify policy exceptions per group (e.g., contractors without EDR)
6. Create minimal set of unique policies
7. Assign primary policy + group-level override policies per resource

## Gotchas

- **Trusted Profiles with multiple verification requirements**: ALL must be satisfied (AND logic, not OR)
- **IdP and AD resources** must be in Everyone group with **no auth policy**—required for Windows pre-logon domain controller access
- **Contractors without EDR**: Use native posture checks (screen lock, biometrics) as fallback; block non-applicable OSes
- **Group override policies**: Apply when a specific group needs stricter/different policy than the resource's primary policy (e.g., IT accessing POS needs MFA even if primary policy doesn't require it)
- Minimum Auth Requirements only grants environment access—resource access still requires a Resource Policy (unless Resource Policy has auth disabled)

## Related Docs

- Trusted Profiles configuration
- Active Directory guide (for Domain Controller setup)
- Device Settings (EDR/MDM integration)
- Everyone Group documentation