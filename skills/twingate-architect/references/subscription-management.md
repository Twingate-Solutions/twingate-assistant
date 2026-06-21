# Subscription Management

## Summary
Twingate billing is based on total number of Users and Service Accounts, with monthly or annual billing cycles. Monthly customers are billed at renewal based on end-of-cycle counts; annual customers get prorated mid-cycle charges. Enterprise/invoice customers have separate arrangements.

## Key Information
- **License units**: Users (IdP-synced, manually added, admin, pending, disabled) + Service Accounts all count
- **Monthly billing**: Total count on last day of billing cycle determines next bill
- **Annual billing**: Mid-cycle additions trigger prorated charges on the 1st of the following calendar month; reductions apply at next renewal
- **Billing timezone**: Transactions process at midnight UTC (may appear as end-of-month charges in non-UTC timezones)
- **Downgrades**: Take effect on next billing date, not immediately

## Prerequisites
- Access to Twingate Admin Console with admin privileges
- Active subscription on Starter, Teams, Business, or Enterprise plan

## Step-by-Step: Downgrade/Change Plan
1. Admin Console → **Settings** → **Manage Plan**
2. Click your subscription → **Edit Subscription**
3. Select desired plan → **Update Subscription**

*For Enterprise plan changes: contact sales@twingate.com*

## Step-by-Step: Verify Scheduled Downgrade
1. Admin Console → **Settings** → **Manage Plan**
2. Click your subscription → **View scheduled changes**
3. Optionally cancel the downgrade from this screen

## Step-by-Step: Update Billing Email
1. Admin Console → **Settings** → **Manage Plan** → **Billing & Shipping Addresses**
2. Update email address; applies to next invoice

## Step-by-Step: Access Past Invoices
1. Admin Console → **Settings** → **Manage Plan** → **Billing History**
2. Download invoices as PDF

## Gotchas
- Disabled and pending users **still consume licenses**
- Service Accounts count regardless of whether keys are active or how many keys exist
- Annual mid-cycle additions are billed prorated starting **April 1** (first of following month), not immediately
- Annual reductions only apply at the **next renewal date**, not mid-cycle
- Downgrade from Annual → Monthly also waits until next billing date

## Contact
- General billing: billing@twingate.com
- Enterprise/invoice: account manager or sales@twingate.com

## Related Docs
- [Users Management](https://www.twingate.com/docs/users)
- [How to Cancel Your Subscription](https://www.twingate.com/docs/cancel-subscription)
- [Upgrading to Twingate Home](https://www.twingate.com/docs/twingate-home)