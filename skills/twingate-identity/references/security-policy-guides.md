---
source: https://www.twingate.com/docs/security-policy-guides
type: docs
fetched: 2026-08-14
source_version: 3096e46d7a0787993bb4a64e18b4fb83e4a4d77a2ca74f5a407dd0b1a201001d
---

# Policy Guides

## Page Title
Security Policy Guides

## Summary
Twingate Security Policies support multiple rule types that control access to resources. This page serves as an index linking to individual guides for each policy rule category.

## Key Information
- Four main Security Policy rule types are documented:
  - **Authentication** – controls re-authentication frequency and 2FA requirements
  - **Two-factor Authentication (2FA)** – specific settings for 2FA enforcement
  - **Device-only Resource Policies** – policies that evaluate only device-based requirements (bypasses user auth checks)
  - **Trusted Devices** – controls whether devices must be trusted (manually or automatically) to satisfy policy requirements

## Prerequisites
- Twingate admin access to configure Security Policies
- Policies are applied at the resource or group level

## Step-by-Step
*This page is an index only; refer to individual linked guides for implementation steps.*

## Configuration Values
*No direct env vars, CLI flags, or API params on this page; see individual guides.*

## Gotchas
- Device-only Resource Policies skip user authentication evaluation — ensure this is intentional when configuring
- Trusted Device requirements have two modes (manual vs. automatic trust); verify which mode aligns with your security posture before applying broadly

## Related Docs
- Authentication Policy Guide
- Two-factor Authentication Policy Guide
- Device-only Resource Policies Guide
- Trusted Devices Policy Guide