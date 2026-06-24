# Resource Policies

## Summary
Resource Policies define security requirements (authentication, device, location) that users must satisfy to access specific Twingate Resources. Policies are assigned at the Resource level and can be overridden per Group. Every network includes a non-deletable Default Policy applied to all new Resources.

## Key Information
- Managed under **Policies → Resource Policies** tab in Admin Console
- Three requirement types: Authentication, Device Security, Location (all optional)
- Default Policy auto-assigned to new Resources; editable but not deletable
- Least permissive policy applies when user belongs to multiple Groups with conflicting policies
- Group-level overrides persist even if the Resource-level policy changes

## Prerequisites
- Enterprise plan required for Location Requirements (geoblocking)
- Trusted Profiles and Approved OS configurations must exist before referencing in Device Security
- MFA requires Twingate's native MFA to be configured

## Configuration Values

### Authentication Requirements
| Setting | Range/Options |
|---|---|
| Authentication frequency | 1 hour to 31 days |
| MFA | Enabled/Disabled |
| Rolling window | Resets timer on ANY successful auth across all Resources |

### Device Security Modes
- `Any Device` – meets Approved OS requirements or Trusted Profile (default)
- `Only Trusted Devices` – must match a Trusted Profile specifically
- `Custom` – select specific Trusted Profiles and Approved OS configs

### Location Requirements
- Allowlist or denylist by country
- **Permanently blocked (non-overridable):** Cuba, Iran, North Korea, Syria

## Step-by-Step: Create and Assign a Policy
1. Navigate to Admin Console → **Policies → Resource Policies**
2. Click **Create**; provide a name
3. Configure Authentication, Device, and/or Location requirements as needed
4. Save the policy
5. Open target Resource's detail page
6. Select the new policy from available options
7. Optionally override policy per Group on the same Resource detail page

## Session Behavior
- Prompt displayed ~10 minutes before timer expiry if user is actively accessing Resource
- Re-auth checks stored IdP session first; redirects to IdP only if expired
- All session timers reset on successful re-authentication
- Dismissing the prompt cuts off access; next access attempt triggers fresh auth

## Gotchas
- Group-level policy overrides **do not inherit future Resource-level policy changes** — must be manually reset
- Authentication timer resets are session-wide (rolling), not per-Resource
- Disabling authentication requirements creates a device-only policy (valid use case)
- Multi-group users get the **least permissive** overlapping policy applied

## Related Docs
- Device Profiles
- Location Requirements
- Multi-Factor Authentication
- Device-only Resource Policies
- How Sessions Work