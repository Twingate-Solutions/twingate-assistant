# Subscription Management

## Summary
Twingate billing is based on total Users and Service Accounts, with monthly or annual billing cycles. Monthly customers are billed at renewal based on the last day of the previous cycle; annual customers receive prorated charges for mid-cycle additions. Enterprise and invoice customers have separate billing arrangements.

## Key Information
- **License counting**: All Users (including Pending and Disabled) + Service Accounts = total licenses
- **IdP-synced users count**: All users synced from Identity Provider count toward licensing
- **Service Accounts**: Each counts as 1 license regardless of number of Service Keys or key status
- **Downgrades**: Always take effect on the next billing date, not immediately
- **Billing timezone**: Transactions occur at midnight UTC — may appear as end-of-month charges depending on timezone

## Billing Models

### Monthly
- Billed at renewal based on user count on **last day of previous billing cycle**

### Annual
- Mid-cycle additions: prorated charge billed on **1st of following calendar month**
- Mid-cycle removals: reflected at **next annual renewal date**

### Invoice Customers
- Contact account manager directly for changes

## Step-by-Step Procedures

**Downgrade Subscription:**
1. Admin Console → Settings → Manage Plan
2. Click subscription → Edit Subscription
3. Select new plan → Update Subscription

**Check Scheduled Downgrade:**
1. Admin Console → Settings → Manage Plan
2. Click subscription → View Scheduled Changes
3. Can cancel downgrade from this view

**Change Billing Email:**
- Settings → Manage Plan → Billing & Shipping Addresses

**Access Past Invoices:**
- Settings → Manage Plan → Billing History (PDF download available)

**Change Plan (Starter/Business/Teams):**
- Settings → Manage Plan → subscription → Edit Subscription

**Enterprise Plan Changes:**
- Contact sales@twingate.com

## Gotchas
- **Pending and Disabled users still count** toward license total — remove them to reduce billing
- **Downgrade is not immediate** — takes effect next billing date; verify via "View Scheduled Changes"
- Annual customers: user reductions only apply at next **annual** renewal, not monthly
- Mid-cycle annual additions are prorated from April 1 through the end of the current annual term

## Related Docs
- [Users Management](https://www.twingate.com/docs/users)
- [How to Cancel Your Subscription](https://www.twingate.com/docs/cancel-subscription)
- [Upgrading to Twingate Home](https://www.twingate.com/docs/twingate-home)
- Billing support: billing@twingate.com
- Enterprise sales: sales@twingate.com