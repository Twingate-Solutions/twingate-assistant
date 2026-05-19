# Security Policies Best Practices

## Summary
Twingate provides three policy types to control access: Admin Console Security Policy, Minimum Authentication Requirements, and Resource Policies. Resource Policies are the primary mechanism for granular access control, applied per-resource with optional group-level overrides. Best practice involves cataloging resources by risk score and mapping risk levels to policy definitions.

## Key Information

- **Three policy types** with different scopes:
  - Admin Console Policy → admins only, enforced at console login
  - Minimum Authentication Requirements → all users, enforced at Client connection (does NOT grant resource access)
  - Resource Policy → per-resource, enforced when accessing resources

- **Policy naming convention**: `<Re-auth>-<MFA>-<DeviceVerif>` (e.g., `2H-MFA-Verif`, `1D-NoMFA-None`)

- **Device verification**: Requires EDR/MDM integration (CrowdStrike, SentinelOne, Kandji, Jamf) or manual Admin Console verification

- **Trusted Profiles** combine verification method + posture checks (HD encryption, screen lock, firewall, antivirus); multiple verification requirements in one profile are AND conditions

- **Everyone Group**: Cannot be deleted; assign IdP and Active Directory resources here with no-auth policies to allow pre-logon traffic

## Prerequisites

- EDR/MDM integrations configured in Admin Console under Device Settings before creating Trusted Profiles
- At least 2 Admin-role users assigned (lockout prevention)
- Risk assessment completed for all resources

## Configuration Values

**Admin Console Security Policy:**
- Re-auth: every 1 hour (fixed, cannot change)
- MFA: enforced

**Minimum Authentication Requirements (recommended):**
- Re-auth duration: 31 days
- MFA: disabled (delegate to Resource Policies)

**Resource Policy Risk Mapping:**
| Risk Level | Re-auth | MFA | Device |
|---|---|---|---|
| High | 2 hours | Required | Trusted only |
| Medium | 1 day | Required | Trusted only |
| Low | 1 week | Required | Trusted only |
| Very Low | 1 week | Not required | Trusted only |

**Minimum policies needed for typical org (7 total):**
`1D-MFA-Verif`, `2H-MFA-Verif`, `7D-NoMFA-Verif`, `7D-MFA-Verif`, `1D-NoMFA-Verif`, `1D-NoMFA-None`, `1D-MFA-None`

## Gotchas

- Minimum Authentication Requirements do **not** grant resource access; resources still need explicit policies
- IdP and Active Directory traffic resources must use **no-auth policies** on the Everyone Group — they support authentication for other resources, not standalone access
- Multiple verification requirements in a single Trusted Profile require **all** to be satisfied (AND logic)
- Contractors without EDR/MDM must use native OS posture checks or manual serial number verification
- Group-level policy **overrides** are required when different groups accessing the same resource need different policies (e.g., IT accessing POS needs stricter policy than Retail)
- Windows environments need Domain Controller resources in Everyone Group with no-auth to enable pre-logon Client access

## Related Docs

- Active Directory guide (referenced for DC resource configuration)
- Trusted Profiles configuration
- Device Settings (EDR/MDM integration setup)
- Everyone Group documentation