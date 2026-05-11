# Twingate Administration

## Summary
Top-level administration hub covering Admin Console security configuration, reporting options, and subscription management. Provides links to sub-sections for each administrative domain.

## Key Information
- Admin Console access is governed by a **special authentication policy** separate from standard user policies
- 2FA enforcement for Admin Console access is configurable
- Reporting covers both network-level and user activity
- Subscription/billing management is available within the Admin Console

## Sub-Sections

| Section | Description |
|---|---|
| Reporting | Network-level and user activity reports |
| Admin Console Security | 2FA and authentication policy for admins |
| Subscription Management | Billing, licensing FAQ, plan changes |

## Admin Console Security
- Admins accessing the Admin Console are subject to a dedicated authentication policy
- 2FA can be set as **required or optional** for Admin Console access
- Configuration is separate from end-user authentication policies

## Reporting
- Available reporting covers:
  - Network-level activity
  - User activity
- See dedicated reporting documentation for full option details

## Subscription Management
- Billing and licensing model details available via FAQ
- Plan changes managed through Admin Console

## Gotchas
- Admin Console authentication policy is **distinct** from policies applied to regular users — changes to user policies do not affect admin access requirements
- 2FA requirement for admins must be explicitly configured; not inherited from other policies

## Related Docs
- [Reporting](https://www.twingate.com/docs/reporting)
- [Admin Console Security](https://www.twingate.com/docs/admin-console-security)
- [Subscription Management](https://www.twingate.com/docs/subscription-management)