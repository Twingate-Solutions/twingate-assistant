---
source: https://www.twingate.com/docs/subscription-management
type: docs
fetched: 2026-08-14
source_version: de7c40d3d6cd2b4df5a8ddc217498e62d831ce939256e4f115cbdb014b2ee7de
---

# Subscription Management

## Summary
Twingate subscriptions are billed monthly or annually based on total user and service account count. Billing is managed through the Admin Console by Admin users or users with the dedicated Billing role. Enterprise customers may have custom billing arrangements.

## Key Information
- **License counts include**: IdP-synced users, manually added users, admin users, pending/disabled users, and service accounts (regardless of key status)
- **Monthly billing**: Charged based on user count on last day of previous billing cycle
- **Annual billing**: Mid-cycle additions incur prorated charges billed on the 1st of each calendar month; reductions apply at next renewal
- **Billing role**: Grants access to Billing page only—use to delegate without full Admin access
- **Invoice customers**: Must contact account manager for changes
- **Charges appear at midnight UTC**, which may display as end-of-month depending on timezone

## Prerequisites
- Admin role or Billing role in Twingate Admin Console
- Active Twingate subscription

## Step-by-Step: Downgrade/Change Subscription Plan
1. Sign into Admin Console
2. **Settings** → **Manage Plan**
3. Click your subscription → **Edit Subscription**
4. Select desired plan → **Update Subscription**

*Note: Downgrades take effect on next billing date*

## Step-by-Step: Verify Scheduled Changes
1. **Settings** → **Manage Plan**
2. Click your subscription → **View scheduled changes**
3. Cancel downgrade here if needed

## Step-by-Step: Update Billing Email
1. **Settings** → **Manage Plan** → **Billing & Shipping Addresses**
2. Update email address (applies to next invoice)

## Step-by-Step: Access Past Invoices
1. **Settings** → **Manage Plan** → **Billing History**
2. Download invoices in PDF format

## Configuration Values
- Billing contact: `billing@twingate.com`
- Enterprise/sales contact: `sales@twingate.com`

## Gotchas
- **Disabled and pending users still count** toward license total
- Annual plan reductions only apply at renewal—no mid-cycle credit
- Annual plan additions trigger prorated billing on the **1st of next month**, not immediately
- Subscription changes for Enterprise require contacting sales—self-serve not available
- Twingate Home upgrades require a promo code

## Related Docs
- [Users Management](https://www.twingate.com/docs/users)
- [Admins & Roles](https://www.twingate.com/docs/admins)
- [How to Cancel Your Subscription](https://www.twingate.com/docs/cancel-subscription)
- [Twingate Home Upgrade Instructions](https://www.twingate.com/docs/twingate-home)