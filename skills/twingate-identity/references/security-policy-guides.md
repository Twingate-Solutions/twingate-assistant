# Security Policy Guides

## Page Title
Security Policy Guides

## Summary
This is a top-level index page for Twingate's Security Policy documentation. It lists the available policy rule types with links to individual detailed guides. No implementation details are provided on this page itself.

## Key Information
- Twingate supports multiple distinct Security Policy rule types
- Four main policy areas are documented separately:
  - **Authentication** – controls re-authentication frequency and 2FA requirements
  - **Two-factor Authentication** – specific settings for 2FA within authentication requirements
  - **Device-only Resource Policies** – policies that evaluate device requirements exclusively
  - **Trusted Devices** – controls whether devices must be trusted (manually or automatically) to satisfy Security Policy requirements

## Prerequisites
- Access to Twingate admin console
- Refer to individual linked guides for specific prerequisites per policy type

## Step-by-Step
Not applicable — this is an index/navigation page only.

## Configuration Values
None defined on this page. See individual guides for specific parameters.

## Gotchas
- Device-only Resource Policies bypass user/auth checks — only device posture is evaluated
- Trusted Devices can be set to manual or automatic trust; behavior differs significantly between modes
- 2FA settings are a sub-component of Authentication settings, not independent top-level policies

## Related Docs
- Authentication settings guide
- Two-factor Authentication guide
- Device-only Resource Policies guide
- Trusted Devices guide (including automatic trust)