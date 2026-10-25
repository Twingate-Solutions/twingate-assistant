---
source: https://www.twingate.com/docs/security-policies-best-practices
type: docs
fetched: 2026-10-25
source_version: 6da8ab3c701a9ff1b8dbd61c8fc483b7fe30450043f86ec967d589222c5c904c
trust: official
---

# Best Practices for Security Policies

## Summary
Twingate provides three types of security policies: Admin Console, Minimum Authentication Requirements, and Resource Policies. This guide walks through a methodology for cataloging resources by risk, mapping risk to policy definitions, and configuring device trust with group-based exceptions.

## Key Information

### Policy Types
| Type | Scope | Component |
|------|-------|-----------|
| Admin Console Security Policy | Admin-role users only | Admin Console |
| Minimum Authentication Requirements | All users at login | Client |
| Resource Policy | Per-resource access | Client |

### Recommended Policy Settings
- **Admin Console**: Re-auth every 1 hour (fixed), enforce MFA, assign ≥2 admin users
- **Minimum Auth Requirements**: Set long duration (e.g., 31 days), do NOT enforce MFA here — use Resource Policies for MFA instead
- **Resource Policies**: Enforce MFA and device trust at resource level

## Prerequisites
- Admin Console access
- EDR/MDM integrations configured (CrowdStrike, SentinelOne, etc.) under Device Settings if using automated verification
- Trusted Profiles created before assigning to Resource Policies

## Step-by-Step: Designing Resource Policies

1. **Catalog resources** by risk dimensions: data type (PII vs. non-PII), data volume, business impact, access method
2. **Score risk** numerically and map to policy tiers:
   - High: re-auth 2h, MFA required, trusted device
   - Medium: re-auth 1 day, MFA required, trusted device
   - Low: re-auth 7 days, MFA required, trusted device
   - Very Low: re-auth 7 days, no MFA, trusted device
3. **Map groups to device verification** capabilities (employees → EDR, BYOD contractors → manual/none)
4. **Create Trusted Profiles** per OS/provider combination (e.g., macOS+CrowdStrike, Windows+SentinelOne, Windows+manual)
5. **Name policies** using convention: `<Re-auth>-<MFA>-<DeviceVerif>` (e.g., `2H-MFA-Verif`, `1D-NoMFA-None`)
6. **Apply group-level policy overrides** per resource for exceptions
7. **Configure Everyone Group** with IdP and AD/DC resources requiring no authentication

## Configuration Values

### Example Policy Definitions
| Policy Name | Re-auth | MFA | Device Security |
|-------------|---------|-----|-----------------|
| `2H-MFA-Verif` | 2 hours | Required | Trusted devices only |
| `1D-MFA-Verif` | 1 day | Required | Trusted devices only |
| `7D-MFA-Verif` | 7 days | Required | Trusted devices only |
| `7D-NoMFA-Verif` | 7 days | Not required | Trusted devices only |
| `1D-NoMFA-None` | 1 day | Not required | Any device |
| `1D-MFA-None` | 1 day | Required | Any device |

## Gotchas

- **Minimum Auth Requirements do not grant resource access** — they only gate environment login
- **Everyone Group resources** (IdP, AD/DC) must have **no authentication required** so the Twingate Client can reach Domain Controllers before user logon
- **Multiple verification requirements in a single Trusted Profile** = both are required simultaneously (not OR logic)
- Contractors without EDR/MDM still need a policy path — use native posture checks (screen lock, biometrics) as a fallback
- Assign `1D-NoMFA-None` (Any Device) only to IdP/AD traffic intercepted by Twingate, not to sensitive resources

## Related Docs
- [Active Directory Guide](https://www.twingate.com/docs/) — required for Windows domain controller resource setup
- Trusted Profiles configuration — Admin Console → Device Settings
- Everyone Group configuration — Admin Console → Groups