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

See [`references/`](./references/) for current doc summaries.

Key references:

- `identity-provider-setup.md` — SAML and SCIM configuration for all supported IdPs
