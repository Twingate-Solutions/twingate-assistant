---
source: https://www.twingate.com/docs/security-policies-best-practices
type: docs
fetched: 2026-08-14
source_version: 9c52473541346c9b85687a1a87c3ae961e8b072217b4f918f009a647c8fb8cc4
---

# Security Policies Best Practices

## Summary
Twingate provides three policy types controlling access at different scopes: Admin Console Security Policy, Minimum Authentication Requirements, and Resource Policies. The guide walks through a risk-based framework for designing Resource Policies by cataloging assets, mapping risk scores to policy definitions, and handling group-based exceptions.

## Key Information

- **Three policy types** with distinct scopes:
  - Admin Console Policy → admin role users only, enforced at console login
  - Minimum Auth Requirements → all users, enforced at Client connection (does NOT grant resource access)
  - Resource Policy → per-resource, enforced when accessing that resource

- **Minimum Auth Requirements** should be kept long (e.g., 31 days) with MFA disabled—use Resource Policies for MFA enforcement instead

- **Resource Policy naming convention**: `<ReAuth>-<MFA>-<DeviceVerif>` (e.g., `2H-MFA-Verif`, `1D-NoMFA-None`)

- **Device verification** = passed EDR/MDM integration (CrowdStrike, SentinelOne, Jamf, etc.) OR manually marked verified in Admin Console

- **Device trust** = device verification + additional posture checks (HD encryption, screen lock, firewall, antivirus)

- **Everyone Group**: Cannot be deleted; assign IdP and Active Directory resources here with **no authentication required** (needed for domain controller access before user logon)

## Prerequisites
- EDR/MDM integrations configured under Device Settings in Admin Console before creating Trusted Profiles
- At least 2 users assigned admin roles (prevents lockout)
- Risk assessment completed for all resources before policy design

## Step-by-Step: Policy Design Framework

1. **Catalog resources** by risk dimensions: data type (PII/non-PII), data volume, business impact of modification, access method (UI/CLI/RDP/SSH)
2. **Score risk** numerically → map to risk tiers (High/Medium/Low/Very Low)
3. **Map risk tiers to policy parameters** (re-auth frequency, MFA required, device verification)
4. **Define device groups** by OS and verification method available
5. **Identify exceptions** (e.g., contractors without EDR, elevated access for IT group)
6. **Create Trusted Profiles** per verification provider per OS combination
7. **Create only distinct policies needed** (deduplicate primary + exception policies)
8. **Assign primary policy + per-group overrides** to each resource

## Configuration Values

| Policy | Re-auth | MFA | Device |
|--------|---------|-----|--------|
| `2H-MFA-Verif` | 2 hours | Required | Trusted only |
| `1D-MFA-Verif` | 1 day | Required | Trusted only |
| `7D-MFA-Verif` | 7 days | Required | Trusted only |
| `7D-NoMFA-Verif` | 7 days | Not required | Trusted only |
| `1D-NoMFA-None` | 1 day | Not required | Any device |
| `1D-MFA-None` | 1 day | Required | Any device |

**Admin Console Policy**: Re-auth every 1 hour (fixed), MFA enforced

## Gotchas

- Multiple verification requirements in a single Trusted Profile require **all** to be satisfied (AND logic, not OR)
- IdP and Active Directory resources must be in the **Everyone Group with no auth**—these support other resources and must be accessible pre-login
- Minimum Authentication Requirements alone do NOT grant resource access unless resource policy has auth disabled
- BYOD contractors often cannot support EDR/MDM—handle via native posture checks (screen lock, biometric) and fall back to `*-None` device policies

## Related Docs
- Active Directory guide (linked in page for Domain Controller setup)
- Trusted Profiles configuration
- Device Settings (EDR/MDM integration setup)
- Everyone Group configuration