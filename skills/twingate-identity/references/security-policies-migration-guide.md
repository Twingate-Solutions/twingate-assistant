## Security Policies Migration Guide

Historical migration document: when Twingate moved from IdP-based **Access Policies** to native **Security Policies** (April 21, 2021). Read this if you're trying to understand legacy terminology, or if you encounter very old Twingate documentation that references the old model.

**TL;DR:**
- Migration was **automatic** and **preserved existing security rules**
- Post-migration user experience is identical
- New terminology + new capabilities (per-Resource 2FA, custom session lifetimes, etc.)

### Terminology Mapping

| Old (Access Policies in IdP) | New (Security Policies) | Notes |
|---|---|---|
| Default Access Policy | **Network Sign In policy** + **Default Policy** | Split into two: one for Client sign-in, one for default Group access |
| Admin Access Policy (Okta/OneLogin only) | **Admin Console Sign In policy** | Renamed; same behavior |
| Custom Access Policies (Okta/OneLogin only) | **Custom Resource Policies** | Expanded capabilities |

For Google Workspace and Entra ID, the old "Admin Access Policy" was identical to the Default; nothing splits there.

### What Changed

**New capabilities introduced with Security Policies:**
- **2FA without IdP** -- Twingate-native TOTP/WebAuthn (see /docs/two-factor-authentication)
- **Per-Resource 2FA** -- enforce 2FA only on sensitive Resources, not blanket
- **Custom session lifetimes per Resource** -- shorter re-auth for high-risk Resources
- Foundation for later capabilities: **device posture**, **geolocation restrictions**, **trusted device profiles**

**Configured under**: Policies tab in the Admin Console (vs. previously in IdP).

### Migration Behavior (Historical, April 2021)

**Google / Entra ID / no IdP:**
- Network Sign In Policy -- got the existing Default Access Policy session lifetime
- 2FA -- preserved if previously enabled
- Default Policy -- same session lifetime; no extra controls; assigned to all Groups
- Admin Console Sign In -- created with 2FA preserved if previously enabled

**Okta / OneLogin (with custom Access Policies):**
- All of the above, plus:
- Each additional custom Access Policy -> a corresponding Security Policy with same name + session lifetime
- Original Group assignments preserved

### Why This Doc Still Matters

- If you're working in an old Twingate tenant or reading legacy docs, you may see the old terminology -- this map clarifies it
- For new deployments: skip this doc; go straight to /docs/security-policies and /docs/security-policies-best-practices
- For tenants migrated long ago: behavior is unchanged; this is purely historical context

**Gotchas:**
- Old "Default Access Policy" is now **two separate policies** (Sign In + Default) -- editing the old name doesn't exist anymore; you edit the appropriate policy in Policies tab
- IdP-side configuration changes (like 2FA settings in Okta) no longer affect Twingate's behavior -- Security Policies live entirely in Twingate now
- If you're hitting old docs that reference IdP-managed policies for Twingate, those instructions are outdated

**Related Docs:**
- /docs/security-policies -- Current model reference
- /docs/security-policies-best-practices -- Risk-tier design
- /docs/security-policy-guides -- Per-rule deeper guides
- /docs/two-factor-authentication -- Native 2FA (introduced with Security Policies)
