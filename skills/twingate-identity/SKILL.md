---
name: twingate-identity
description: |
  Twingate identity management — IdP integration, SCIM provisioning, security
  policies, device trust, groups, users, and access control. Use this skill when
  the user mentions identity providers, SAML, SCIM, Okta, Entra ID, Google
  Workspace, JumpCloud, OneLogin, Keycloak, security policies, device trust,
  device posture, MFA, groups, users, access control, JIT access, ephemeral
  access, or offboarding.
---

# Twingate Identity Management

## When to Use This Skill

Trigger this skill when the user asks about any of the following:

- Connecting an identity provider (Okta, Entra ID, Azure AD, Google Workspace, JumpCloud, OneLogin, Keycloak)
- SAML SSO configuration or troubleshooting
- SCIM provisioning, deprovisioning, or attribute sync
- User lifecycle management: onboarding, offboarding, role changes
- Group management: creating groups, syncing groups from IdP, group-based access
- Security policies: MFA enforcement, session duration, re-authentication frequency
- Device trust: CrowdStrike, SentinelOne, Intune, Jamf, Kandji, 1Password XAM
- Device posture requirements before network access
- Just-in-time (JIT) access requests and approvals
- Ephemeral or time-limited resource access
- Usage-based auto-lock (dormant account access suspension)
- Multi-IdP deployments or IdP migrations
- Access modes: MANUAL, AUTO_LOCK, ACCESS_REQUEST
- Contractor access, temporary access, auditor access patterns
- Social login configuration for smaller deployments

## Quick Reference

| Concept | Key Fact |
|---|---|
| Auth protocol | SAML 2.0 for SSO |
| Provisioning protocol | SCIM 2.0 for lifecycle |
| Supported IdPs | Entra ID, Google Workspace, Okta, OneLogin, JumpCloud, Keycloak |
| Multi-IdP | Yes — 2+ IdPs supported simultaneously |
| Group types | MANUAL, SYNCED, SYSTEM |
| Security policy target | Groups (not users, not resources) |
| Effective policy rule | Most restrictive policy across all a user's groups |
| Access modes | MANUAL, AUTO_LOCK, ACCESS_REQUEST |
| Device trust vendors | CrowdStrike, SentinelOne, Intune, Jamf, Kandji, 1Password XAM |
| JIT model | User requests → approver grants time-bounded access |
| Offboarding (with SCIM) | Remove from IdP → auto-deprovisioned in Twingate |
| Offboarding (without SCIM) | Must manually disable/remove in Twingate admin console |

## Evergreen Knowledge

### IdP Integration: SAML + SCIM Together

Always recommend configuring both SAML and SCIM. They serve distinct purposes:

- **SAML 2.0** handles authentication — SSO sign-in, session tokens, MFA delegation to the IdP.
- **SCIM 2.0** handles provisioning lifecycle — user creation, user deactivation, group membership sync.

Without SCIM, Twingate users and groups must be managed manually. This creates orphaned access after offboarding and makes group management error-prone at scale. With both configured, the IdP becomes the single authoritative source of truth for who has access and what groups they belong to.

### Supported Identity Providers

Twingate supports native SAML + SCIM integrations with:

- **Entra ID (Azure AD)** — enterprise gallery app, app provisioning for SCIM
- **Google Workspace** — custom SAML app, Google Directory API for SCIM
- **Okta** — Okta Integration Network (OIN) app, Okta provisioning for SCIM
- **OneLogin** — SAML + SCIM connector
- **JumpCloud** — SAML + SCIM connector
- **Keycloak** — SAML with custom SCIM plugin or manual provisioning

For smaller or consumer deployments, Twingate also supports social logins (Google, GitHub) without full enterprise IdP setup.

### Multi-IdP Support

Twingate supports running two or more IdPs simultaneously. Common use cases:

- **IdP migrations** — add the new IdP before removing the old one, migrate user cohorts incrementally, validate, then remove the legacy IdP
- **Multi-domain organizations** — different business units or acquired companies each have their own IdP domain
- **Hybrid environments** — corporate IdP for employees, a separate IdP for contractors or partners

When running multiple IdPs, be deliberate about group naming conventions across providers. SCIM conflicts can arise if two providers attempt to provision the same user (identified by email). Plan the migration order carefully.

### Group Types

Twingate has three group types with distinct management behaviors:

**MANUAL groups** are created and managed entirely within the Twingate admin console. Membership is set manually by administrators. Use for one-off groupings that don't map cleanly to IdP group structure.

**SYNCED groups** are created by SCIM from IdP groups. Membership is controlled by the IdP and synced automatically. This is the correct type for production access control — any change to IdP group membership is reflected in Twingate within the SCIM sync window. Do not manually edit SYNCED group membership in Twingate; those changes will be overwritten on the next sync.

**SYSTEM groups** are built-in groups that Twingate manages. The most important is the "Everyone" group, which automatically includes all users in the account. Never assign privileged or sensitive resources to the Everyone group — it grants access to every user, including service accounts and newly provisioned users.

### Security Policies

Security policies define authentication and access behavior constraints. A policy specifies:

- **Authentication frequency** — how often users must re-authenticate (e.g., every 1 hour, 8 hours, 24 hours)
- **MFA enforcement** — whether MFA is required at sign-in
- **Device trust requirements** — whether the connecting device must pass a posture check
- **Geoblocking** — whether connections from certain countries are blocked

**Policies attach to Groups, not to individual users or to resources.** A resource does not have its own authentication frequency or MFA requirement — those are defined by the group(s) the resource belongs to. When a user belongs to multiple groups with different security policies, Twingate applies the most restrictive policy.

Configure security policies in the Twingate admin console under Settings → Security Policies.

### Device Trust

Device trust enforces that the endpoint meets a security posture baseline before the Twingate Client is permitted to establish connections. Supported integrations:

- **CrowdStrike Falcon** — ZTA score threshold
- **SentinelOne** — device health check
- **Microsoft Intune** — compliance policy check
- **Jamf Pro / Jamf Now** — MDM-enrolled device check
- **Kandji** — compliance blueprint check
- **1Password Extended Access Management (XAM)** — unified device health + credential security

Configure device trust in the Twingate admin console under Settings → Device Trust. Assign device trust requirements to Security Policies. A group's security policy can require device trust, which means any user in that group must be on a compliant device to connect.

**Do not enforce device trust before ensuring all affected users' devices are enrolled in the MDM or EDR platform.** Enabling enforcement before rollout is complete will lock out users whose devices haven't been registered yet.

### Access Modes

Every resource assignment to a group has an access mode that controls how long access persists:

**MANUAL** — always-on access. The user has access for as long as they are a member of the group. This is the default mode and appropriate for standard employee access to everyday resources.

**AUTO_LOCK (usage-based auto-lock)** — access is automatically suspended after a configurable period of inactivity. If the user hasn't used Twingate for N days, their access is locked. The user can be unlocked by an admin or by signing in again. Use this for contractor access, part-time employees, or any identity that may go dormant.

**ACCESS_REQUEST (JIT access)** — the user must explicitly request access and have it approved before they can connect. Approved access is time-bounded and expires automatically. Use this for privileged resources, production systems, and any access that requires an audit trail.

### Just-in-Time (JIT) Access

JIT access uses the ACCESS_REQUEST mode. The workflow:

1. User attempts to access a resource and sees that access requires a request
2. User submits an access request (optionally with a reason/justification)
3. Designated approvers (admins or named approvers) receive a notification
4. Approver grants time-limited access (e.g., 4 hours, 24 hours, 7 days)
5. User connects during the approved window
6. Access expires automatically when the window closes

JIT is well-suited for: production database access, infrastructure management, privileged admin tools, auditor access, and incident response.

### Ephemeral Access

Ephemeral access is resource membership with a defined expiry date/time. When the expiry is reached, the user automatically loses access to that resource without any manual admin action. This differs from JIT in that the access window is set at provisioning time rather than at request time.

Use ephemeral access for: contractor project access, time-limited vendor support windows, and compliance-driven access reviews where access must expire on a fixed date.

### Usage-Based Auto-Lock

The AUTO_LOCK access mode monitors usage. When a user with AUTO_LOCK access mode hasn't used Twingate for the configured idle period, their access to resources in that group is automatically suspended. This protects against dormant accounts that retain network access after an employee changes roles, goes on extended leave, or is informally offboarded without proper IdP cleanup.

Configure the idle period in days when setting up the group resource assignment.

### Offboarding

With SCIM configured: remove the user from the IdP (or deactivate their IdP account) → SCIM automatically deprovisions the Twingate account, revokes all group memberships, and terminates active sessions. This is the recommended path — no manual Twingate action required.

Without SCIM: you must manually disable or delete the user in the Twingate admin console. This step is easy to miss, creating orphaned access where a former employee retains network-level access to resources even after their IdP account is deactivated. Always configure SCIM to eliminate this risk.

## Current Documentation

For current IdP setup steps, SCIM configuration, security policy options, and device trust configuration, read the reference files in this skill's `references/` directory.

If a reference file seems outdated or missing, fetch the doc directly:

```
curl -s https://www.twingate.com/docs/identity-providers
curl -s https://www.twingate.com/docs/azure-ad
curl -s https://www.twingate.com/docs/google
curl -s https://www.twingate.com/docs/okta
curl -s https://www.twingate.com/docs/scim
curl -s https://www.twingate.com/docs/security-policies
curl -s https://www.twingate.com/docs/device-trust
curl -s https://www.twingate.com/docs/groups
curl -s https://www.twingate.com/docs/just-in-time-access
curl -s https://www.twingate.com/docs/offboarding
```

Key doc slugs by topic:

| Topic | Slug |
|---|---|
| IdP overview | `identity-providers` |
| Entra ID / Azure AD | `azure-ad` |
| Google Workspace | `google` |
| Okta | `okta` |
| OneLogin | `onelogin` |
| JumpCloud | `jumpcloud` |
| Keycloak | `keycloak` |
| SCIM provisioning | `scim` |
| Security policies | `security-policies` |
| Device trust | `device-trust` |
| Groups | `groups` |
| JIT access | `just-in-time-access` |
| Offboarding | `offboarding` |
| Social logins | `social-logins` |
| MFA | `mfa` |
| Ephemeral access | `ephemeral-access` |
| Auto-lock | `auto-lock` |

## Common Patterns

### Standard Okta or Entra ID Setup

1. Create the Twingate SAML app in the IdP (use the gallery app for Okta; follow the enterprise app setup for Entra ID)
2. Configure SAML: paste Twingate's ACS URL and Entity ID into the IdP app settings
3. Enable SCIM provisioning: generate a SCIM token in Twingate, paste into the IdP provisioning configuration
4. In the IdP, assign the application to the user groups that should have Twingate access
5. SCIM syncs: groups and their members are provisioned in Twingate as SYNCED groups
6. In Twingate, assign resources to those synced groups
7. Test: add a user to an IdP group → confirm they appear in Twingate and can connect → remove them → confirm deprovisioning

### Tiered Security Policies

Design security policies around risk tiers rather than individual users:

- **Standard Users** — MFA required, 8-hour session, no device trust required
- **Admins** — MFA required, 1-hour session, device trust required (Intune/CrowdStrike)
- **Contractors** — MFA required, 4-hour session, AUTO_LOCK after 7 days idle
- **Privileged Production Access** — ACCESS_REQUEST mode, MFA required, 1-hour session, device trust required

Assign each group to the appropriate security policy. Users who are in both "Standard Users" and "Admins" groups will be subject to the more restrictive admin policy.

### JIT for Production Access

1. Create a "Production DBs" group (or similar) in Twingate
2. Assign the production database resources to this group
3. Set the access mode to ACCESS_REQUEST
4. Assign a security policy requiring MFA and device trust
5. Designate approvers for the group
6. When a developer needs production access: they request access, an approver grants a time-bounded window (e.g., 4 hours), the developer connects, access expires automatically

This pattern creates an audit trail and enforces least-privilege without requiring admin intervention to revoke access after each use.

### Contractor Lifecycle with SCIM

1. Contractor is added to the IdP with an appropriate group (e.g., "Contractors - ProjectX")
2. SCIM provisions the Twingate account and adds them to the corresponding SYNCED group
3. The group's resource assignment uses AUTO_LOCK mode with a 14-day idle threshold
4. The contractor's security policy requires MFA and has a 4-hour session duration
5. Project ends: remove the contractor from the IdP group → SCIM deprovisions Twingate access automatically
6. No manual Twingate cleanup required

### Multi-IdP During Migration

1. Configure the new IdP alongside the existing IdP — both active simultaneously
2. Create a pilot group in the new IdP; map it to a Twingate SYNCED group
3. Migrate a cohort of test users to the new IdP; validate SSO and SCIM sync
4. Roll out by cohort, validating group sync and resource access at each stage
5. Once all users are migrated, deactivate SCIM for the old IdP and remove the old IdP configuration
6. Monitor for any users who may have been missed (check for MANUAL group memberships that were not migrated)

## Anti-Patterns and Gotchas

**Deploying without SCIM.** Manual group management scales poorly and creates orphaned access. After offboarding, if an admin forgets to remove the user from Twingate, that user retains network-level access indefinitely. Always configure SCIM to close this gap.

**Assigning resources directly to users.** Twingate's access model is group-centric. Resources are assigned to groups; users are members of groups. User-level resource assignments exist but do not participate in SCIM lifecycle — they won't be removed when the user is deprovisioned via SCIM. Always use groups as the intermediary.

**Using the Everyone system group for sensitive resources.** The Everyone group includes all users in the account, including newly provisioned service accounts and IdP sync accounts. Never assign sensitive, privileged, or internal-only resources to Everyone. Reserve it only for truly universal resources (e.g., a public status page proxy) if used at all.

**Assuming security policies apply to resources.** A common misconception is that a resource has its own MFA or re-auth requirement. It does not. Security policies attach to Groups. If you want MFA enforced for access to a specific resource, put that resource in a group, and apply a policy requiring MFA to that group.

**Multi-IdP group name collisions.** If two SCIM providers both attempt to create a group with the same name in Twingate, or both attempt to manage the same user (matched by email), the behavior can be unpredictable. When running multiple IdPs, use naming conventions that make the IdP source explicit (e.g., `okta-engineering`, `entra-contractors`) and ensure no user email appears in both IdPs' assigned user sets at the same time.

**Enabling device trust before MDM/EDR rollout is complete.** If you flip on device trust enforcement in a security policy before all users in the affected groups have their devices enrolled in the MDM or EDR, those users will be blocked from connecting. Stage the rollout: enroll devices first, verify enrollment coverage, then enable device trust enforcement.

**Editing SYNCED group membership in Twingate.** Changes made to SYNCED group membership directly in the Twingate admin console will be overwritten at the next SCIM sync. Manage SYNCED group membership exclusively through the IdP.

## Related Skills

- **twingate-architect** — overall Twingate architecture, remote networks, resources, and how groups connect to resources
- **twingate-connectors** — connector deployment for the infrastructure that serves the resources groups access
- **twingate-idfw** — Identity Firewall for SSH PAM and Kubernetes gateway: protocol-level identity enforcement layered on top of Twingate network access
- **twingate-troubleshoot** — debugging access failures caused by policy misconfiguration, device trust posture failures, group sync issues, or SCIM errors
