# Security Policies Best Practices

## Summary
Twingate provides three policy types controlling Admin Console access, environment authentication, and Resource access. Admins should catalog resources by risk level, map risk to policy definitions, and apply group-based exceptions. A systematic naming convention and policy matrix simplifies managing access across diverse user groups.

## Key Information
- **Three policy types**: Admin Console Security Policy, Minimum Authentication Requirements, Resource Policies
- **Minimum Auth Requirements** apply to ALL users but do NOT grant Resource access
- **Resource Policies** gate actual resource access with auth frequency, MFA, and device trust controls
- Device is "verified" via EDR/MDM integration (CrowdStrike, SentinelOne, etc.) or manual Admin Console verification
- **Everyone Group** cannot be deleted; assign IdP and AD/DC resources here with no-auth policy
- Policy naming convention: `<Re-auth>-<MFA>-<DeviceVerif>` (e.g., `2H-MFA-Verif`)

## Prerequisites
- EDR/MDM integrations configured in Admin Console under Device Settings (if using automated verification)
- Trusted Profiles created per OS/verification provider combination
- Risk assessment completed for all resources before policy design

## Configuration Values

### Admin Console Security Policy
| Setting | Recommended Value |
|---|---|
| Re-auth frequency | Every 1 hour (fixed) |
| MFA | Enforced |
| Min admin accounts | 2 users |

### Minimum Authentication Requirements
| Setting | Recommended Value |
|---|---|
| Duration | 31 days |
| MFA | Disabled (use Resource Policies instead) |

### Resource Policy Risk Matrix
| Risk | Re-auth | MFA | Device |
|---|---|---|---|
| High | 2 hours | Required | Verified |
| Medium | 1 day | Required | Verified |
| Low | 1 week | Required | Verified |
| Very Low | 1 week | Not required | Verified |

### Minimum Policy Set (7 policies covers most scenarios)
`1D-MFA-Verif`, `2H-MFA-Verif`, `7D-NoMFA-Verif`, `7D-MFA-Verif`, `1D-NoMFA-Verif`, `1D-NoMFA-None`, `1D-MFA-None`

## Step-by-Step

1. Catalog all resources; score risk across: data type, data volume, business impact, access method
2. Map risk scores to policy definitions (re-auth interval, MFA, device verification)
3. Identify group-based exceptions (e.g., contractors without EDR/MDM)
4. Configure EDR/MDM integrations in Admin Console → Device Settings
5. Create Trusted Profiles per OS/verification provider (separate profiles for CrowdStrike macOS, CrowdStrike Windows, SentinelOne Windows, manual Windows)
6. Add posture checks to Trusted Profiles (HD encryption, screen lock, firewall, antivirus)
7. Create Resource Policies using naming convention
8. Assign Resources to Groups with primary policies; add group-level override policies for exceptions
9. Configure Everyone Group: add IdP resource + AD/DC resources (Windows); set no-auth, device-trust policy

## Gotchas
- **Trusted Profile multi-verification**: Selecting multiple verification requirements means ALL must be satisfied
- **IdP/AD traffic**: Must be in Everyone Group with no-auth policy—these support other resource access and need pre-logon availability
- **Contractors without EDR**: Use native OS posture checks (screen lock, biometrics) as compensating controls; block non-applicable OSes
- **IT vs. regular users on same resource**: Requires group-level policy override, not just primary policy
- **Identity Provider (non-admin)**: Should have `No Auth` policy—authentication happens at the resource level, not here

## Related Docs
- Trusted Profiles configuration
- Active Directory guide
- Device Settings / EDR integration docs
- Everyone Group documentation