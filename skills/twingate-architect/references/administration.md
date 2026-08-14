---
source: https://www.twingate.com/docs/administration
type: docs
fetched: 2026-08-14
source_version: 5c01b17cbbff6e580e4bfa6d1428074329755b653faf356a93c70d34e664cd64
---

# Twingate Administration

## Summary
The Administration section covers Admin Console security configuration, subscription management, and reporting options. It provides access to authentication policies for admin users and billing/licensing management.

## Key Information
- Admin Console access is governed by a **special authentication policy** separate from standard user policies
- 2FA enforcement for Admin Console access is configurable
- Reporting covers both network-level and user activity
- Subscription/billing management is available within the Admin Console

## Core Administration Areas

### Admin Console Security
- Controls authentication requirements for admins accessing the Admin Console
- 2FA can be set as required or optional for Admin Console access
- Separate from standard user authentication policies

### Reporting
- Network-level activity reporting available
- User activity reporting available
- Multiple reporting options/formats supported

### Subscription Management
- Billing and licensing FAQ available
- Plan changes managed through Admin Console

## Prerequisites
- Must have Admin role to access Admin Console settings
- Account must be active on Twingate

## Gotchas
- Admin Console security policy is **distinct** from user-facing resource access policies — changes here only affect admin login, not end-user access
- 2FA configuration for admins is managed separately from 2FA settings for regular users

## Related Docs
- [Reporting](https://www.twingate.com/docs/reporting)
- [Admin Console Security](https://www.twingate.com/docs/admin-console-security)
- [Subscription Management](https://www.twingate.com/docs/subscription)