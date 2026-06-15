# Security Policies Best Practices

## Page Title
Best Practices for Security Policies

## Summary
Twingate provides three policy types—Admin Console Security Policy, Minimum Authentication Requirements, and Resource Policies—each covering different scopes and components. Resource Policies are the primary tool for granular access control, requiring admins to catalog resources by risk and map policies accordingly. The guide walks through a complete example of designing, naming, and configuring policies with group-based overrides.

## Key Information

### Policy Types
| Policy | Scope | Enforced At |
|--------|-------|-------------|
| Admin Console Security Policy | Admin/DevOps/Support role users | Admin Console access |
| Minimum Authentication Requirements | All users | Client connection |
| Resource Policy | Users accessing specific Resources | Resource access attempt |

### Recommended Settings
- **Admin Console Policy**: 1-hour auth (fixed), enforce MFA, assign ≥2 Admin users
- **Minimum Auth Requirements**: 31-day duration, no MFA (use Resource Policies for MFA instead)
- **Resource Policies**: Risk-based; always require device verification

### Risk-to-Policy Mapping Example
| Risk | Re-auth | MFA | Device |
|------|---------|-----|--------|
| High | 2 hours | Yes | Verified |
| Medium | 1 day | Yes | Verified |
| Low | 1 week | Yes | Verified |
| Very Low | 1 week | No | Verified |

### Naming Convention
`<Re-auth>-<MFA>-<DeviceVerif>` (e.g., `2H-MFA-Verif`, `1D-NoMFA-None`)

## Prerequisites
- EDR/MDM integrations configured (CrowdStrike, SentinelOne, Jamf, etc.) under Device Settings
- Trusted Profiles created per OS/verification provider combination
- Resources cataloged with risk scores

## Step-by-Step

1. **Catalog Resources** — Score each by data type, volume, business impact, access method
2. **Map risk scores to policy definitions** — Define re-auth frequency, MFA, and device requirements per tier
3. **Configure Device Settings** — Add EDR/MDM integrations in Admin Console
4. **Create Trusted Profiles** — One per OS/provider combination (e.g., macOS+CrowdStrike, Windows+SentinelOne)
5. **Add posture checks to Trusted Profiles** — HD Encryption, Screen Lock, Firewall, Antivirus (Windows)
6. **Define Resource Policies** — Create only unique policy combinations needed
7. **Assign Resources to Groups** with primary policy + group-level overrides

## Configuration Values

- **Admin Console re-auth**: Fixed at 1 hour (cannot change)
- **Minimum Auth recommended duration**: 31 days
- **High risk re-auth**: 2 hours
- **Medium risk re-auth**: 1 day
- **Low/Very Low re-auth**: 7 days

## Gotchas

- **Everyone Group** cannot be deleted; assign IdP and AD/Domain Controller resources here with **no authentication required** so Twingate Client can reach Domain Controllers before user logon
- **Minimum Auth Requirements do not grant Resource access**—only a Resource Policy with auth disabled would allow that
- Selecting multiple verification requirements in one Trusted Profile requires **both** to pass
- Contractor groups without EDR access need a separate policy with `NoVerif` and device blocked to allowed OS only
- IdP and AD/Domain Controller non-admin resources should use the Everyone group with no auth—authentication is handled by the Resources they support

## Related Docs
- Trusted Profiles configuration
- Active Directory guide
- Device Settings (EDR/MDM integrations)
- Everyone Group documentation