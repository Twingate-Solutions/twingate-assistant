---
source: https://www.twingate.com/docs/security-policy-guides
type: docs
fetched: 2026-11-13
source_version: 1f73fcf3752019d6ad6e22258a35d1e99a991e7b01deb962f60a6149daa670ec
trust: official
---

# Policy Guides (Twingate Security Policies)

**Source:** https://www.twingate.com/docs/security-policy-guides

## Summary
This is an index page for Twingate's Security Policy rules. It lists the individual guides covering authentication frequency, two-factor authentication, device-only resource policies, and device profiles. The page has no procedures or configuration details itself; those are in the linked guides.

## Key Information
- Twingate Security Policies support several rule types, each documented in its own guide.
- **Authentication** settings control how often users must re-authenticate and whether 2FA is required.
- **Two-factor authentication (2FA)** settings are applied as part of the authentication requirements.
- **Device-only Resource Policies** can be configured so that only device requirements are evaluated (no user authentication evaluation).
- **Device Profiles** determine whether a device must be trusted, either manually or automatically, to satisfy a Security Policy.
- Page was last updated "2 days ago" relative to scrape time.

## Prerequisites
None stated on this page. Individual guides likely require Admin Console access and an existing Twingate Network.

## Step-by-Step
Not applicable. This page is a navigation index only.

## Configuration Values
None listed. No env vars, CLI flags, or API parameters appear on this page. Consult the linked guides for specifics.

## Gotchas
- The page has no implementation details; do not rely on it for settings or values.
- Device trust requirements (via Device Profiles) interact with Security Policies. A device that doesn't meet trust criteria may fail policy evaluation, so review profiles alongside policy rules.
- Device-only policies skip user authentication evaluation, so use them deliberately.

## Related Docs
- Authentication policy guide (re-authentication frequency, 2FA requirements)
- Two-factor Authentication guide
- Device-only Resource Policies guide
- Device Profiles guide
- Parent: Twingate Security Policies overview