---
source: https://help.twingate.com/articles/6581096205-signing-into-the-twingate-help-center
type: help
fetched: 2026-08-09
source_version: 8ab11466845d4c7398180f3c54b32620857b0c89490d43032f6ffa5f70a7c533
---

# Accessing the Twingate Customer Portal

## Summary
Twingate Admins with Technical Support Entitlement can access the Customer Portal through SSO from the admin console. First-time access requires a one-time email verification. Accounts without Technical Support Entitlement are redirected to Reddit community support instead.

## Key Information
- Authentication is SSO-based, initiated from the Twingate admin console
- One-time email verification required on first login or after email address change
- **Community** option in Help menu = no Technical Support Entitlement (redirects to Reddit)
- **Support** option in Help menu = Technical Support Entitlement present
- After verification, subsequent logins via **Support** are direct (no re-verification)

## Prerequisites
- Twingate Admin role
- Technical Support Entitlement on account
- Access to the email address associated with your Twingate admin account

## Step-by-Step

1. In Twingate admin console, click **Help** → **Support**
   - If you see **Community** instead, you lack Technical Support Entitlement
2. Click **Send Email** if prompted for email verification
3. Check inbox for verification email from Twingate
4. Click **Verify email** in the email
5. Browser confirms successful verification; click **Go to Twingate Help Center**
6. Future logins: click **Help** → **Support** for direct portal access

## Gotchas
- Email verification must be repeated if your admin email address changes
- Creating a Customer Portal account does not guarantee email technical support — Technical Support Entitlement is required for responses
- No CLI, API, or configuration values involved — process is entirely UI-driven

## Related Docs
- [Technical Support Entitlement](https://help.twingate.com) (referenced but not linked in source)
- Twingate admin console Help menu