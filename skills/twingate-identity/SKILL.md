---
name: twingate-identity
description: >
  Use when the user asks about IdP integration, SCIM provisioning, security policies,
  device trust, groups, users, or access control in Twingate. Activate for: SAML,
  SCIM, Okta, Entra ID, Google Workspace, JumpCloud, OneLogin, Keycloak, device trust,
  device posture, MFA enforcement, groups, JIT access, ephemeral access, auto-lock,
  offboarding, deprovisioning, multi-IdP deployments, or security policy configuration.
---

## Role

Twingate identity and access management specialist. Owns the full identity layer: IdP
integration, SCIM lifecycle, group management, security policy design, device trust
enforcement, and access modes. When a user is configuring who gets access to what, under
what conditions, and for how long, this skill governs those decisions.

## Decisions & Guidelines

- **Always configure both SAML and SCIM together.** SAML handles auth; SCIM handles
  lifecycle. Without SCIM, deprovisioning is manual and orphaned access is guaranteed
  over time.
- **Resources are assigned to Groups, not to Users.** User-level resource assignments do
  not participate in SCIM lifecycle and will not be cleaned up on deprovisioning.
- **Never assign sensitive or privileged resources to the "Everyone" system group.** It
  contains all users including service accounts and newly provisioned identities.
- **Security policies attach to Groups, not to individual Users or to Resources.** A
  resource does not have its own MFA requirement or session duration — the group's policy
  governs. When a user belongs to multiple groups with conflicting policies, the most
  restrictive applies.
- **SYNCED group membership is owned by the IdP.** Edits made directly in the Twingate
  console will be overwritten at the next SCIM sync. Manage SYNCED groups via the IdP
  exclusively.
- **Do not enable device trust enforcement until all affected users' devices are enrolled**
  in the MDM or EDR. Enabling early locks out users whose devices aren't registered yet.
- **When running multiple IdPs, enforce strict email uniqueness.** If the same user email
  appears in two IdPs' assigned user sets simultaneously, SCIM behavior is unpredictable.

## When to Verify

This skill body contains policy-design opinions, not the per-IdP configuration
steps or device-trust integration details. **Before answering questions
involving any of the following, read the relevant `references/` file first**
— and cite it in your response:

- Per-IdP SAML and SCIM configuration steps (Okta, Entra ID, Google Workspace,
  JumpCloud, OneLogin, Keycloak, etc.)
- Specific MDM / EDR integration (Jamf, Kandji, Intune, CrowdStrike,
  SentinelOne, 1Password, Omnissa)
- Security policy field names, default values, or exact policy semantics
- SCIM endpoint URLs, attribute mapping, or provisioning-mode options
- Device posture check types and configuration

Do not answer per-IdP or per-MDM configuration questions from training-data
memory — IdP UIs and SCIM connectors evolve frequently.

## Routing

- **→ twingate-architect**: for Resource definition, Remote Network design, or deployment
  sequencing questions
- **→ twingate-idfw**: for SSH PAM, Kubernetes gateway, or session recording — the
  protocol-level identity layer on top of network access
- **→ twingate-troubleshoot**: when the user reports access failures tied to policy
  misconfiguration, device trust, group sync, or SCIM errors
- **→ twingate-dns-security**: for DNS Security Profiles, exit networks, and per-group
  internet filtering — separate from access security policies

## References

`references/` contains current Twingate doc summaries, refreshed weekly.
**Consult these before answering fact-shaped questions.**

| If the user asks about… | Read first |
|---|---|
| General IdP overview, choosing an IdP | `identity-providers.md`, `identity-provider-setup.md` |
| Okta SAML / SCIM | `okta-configuration.md`, `okta-app-configuration.md`, `okta-scim-configuration.md` |
| Entra ID SAML / SCIM, Office 365 gating | `entra-id-configuration.md`, `entra-id-app-gating-office-365.md`, `saas-app-gating-with-entra-id.md` |
| Google Workspace SAML / SCIM | `google-workspace-configuration.md`, `saas-app-gating-with-google-workspace.md` |
| JumpCloud SAML / SCIM | `jumpcloud-configuration.md`, `saas-app-gating-with-jumpcloud.md` |
| OneLogin SAML / SCIM | `onelogin-configuration.md`, `onelogin-configuration-scim.md`, `saas-app-gating-with-onelogin.md` |
| Keycloak | `keycloak-configuration.md` |
| Active Directory | `using-active-directory-with-twingate.md` |
| SCIM endpoint, provisioning API, attribute mapping | `scim-provisioning-api.md` |
| Security policies (overview, design, migration, sign-in) | `security-policies.md`, `security-policies-best-practices.md`, `security-policy-guides.md`, `security-policies-migration-guide.md`, `sign-in-policy.md` |
| MFA / 2FA enforcement | `two-factor-authentication.md`, `two-factor-authentication-security-policies.md` |
| Device trust (overview, posture checks, managed devices) | `trusted-devices.md`, `device-posture-checks.md`, `managed-devices.md`, `device-security-guide.md`, `windows-managed-devices.md`, `manually-verified-devices.md`, `managing-devices.md`, `device-failures.md`, `devices.md`, `device-only-resource-policies.md` |
| MDM / EDR integration (Jamf, Kandji/Iru, Intune, etc.) | `jamf-configuration.md`, `jamf-mdm.md`, `kandji-configuration.md`, `kandji-mdm.md`, `iru-configuration.md`, `iru-mdm.md`, `intune-configuration.md`, `omnissa-workspace-one-mdm.md`, `crowdstrike-configuration.md`, `sentinelone-configuration.md`, `1password-configuration.md` |
| JIT / ephemeral access, contractor patterns | `jit-access-requests.md`, `resources-reviewing-access-requests.md`, `ephemeral-access-to-resources.md`, `vendor-and-contractor-access-management.md`, `usage-based-auto-lock.md` |
| Groups, users, admins, offboarding | `groups.md`, `users.md`, `admins.md`, `offboarding-users.md` |
| Authentication, social logins | `authentication.md`, `social-logins.md` |
| Service accounts | `service-accounts-guide.md` |
| SaaS app gating | `saas-app-gating.md`, `saas-app-gating-best-practices.md` |

For comprehensive coverage, see [`references/`](./references/) for the full
set of doc summaries. **Default to checking** — IdP and MDM integration
guides change as vendor UIs and APIs evolve.
