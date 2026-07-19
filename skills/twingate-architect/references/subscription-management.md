# Subscription Management

## Summary
Twingate subscriptions are billed monthly or annually based on total User and Service Account count. Billing management is accessible to Admin users and those with the dedicated Billing role. Enterprise and invoice customers have separate billing arrangements handled through account managers.

## Key Information
- **Billing roles**: Admin users OR users with dedicated Billing role (Billing role grants access to Billing page only)
- **License count includes**: IdP-synced users, manually added users, Admin users, Pending users, Disabled users, Service Accounts (regardless of key count/status)
- **Monthly billing**: Charged based on user/service account count on last day of previous billing cycle
- **Annual billing**: Mid-cycle additions incur prorated charges billed on the 1st of each calendar month; reductions apply at next renewal
- **Downgrades**: Take effect on next billing date, not immediately
- **Timezone note**: Billing transactions occur at midnight UTC — may appear as end-of-month charges depending on timezone

## Billing Cycle Examples
| Plan | Additions | Prorated? | Reductions |
|------|-----------|-----------|------------|
| Monthly | Counted at next renewal | No | Applied next cycle |
| Annual | Prorated from 1st of next month | Yes | Applied at next renewal |

## Step-by-Step: Downgrade/Change Plan
1. Admin Console → **Settings** → **Manage Plan**
2. Click your subscription → **Edit Subscription**
3. Select desired plan → **Update Subscription**

*(Enterprise plan changes: contact `sales@twingate.com`)*

## Step-by-Step: Verify Scheduled Downgrade
1. Admin Console → **Settings** → **Manage Plan**
2. Click subscription → **View scheduled changes**
3. Option to cancel the downgrade is available here

## Managing Billing Details
- **Invoice email**: Settings → Manage Plan → Billing & Shipping Addresses
- **Past invoices**: Settings → Manage Plan → Billing History (PDF download)
- **Twingate Home upgrade**: Redeem promo code in billing tab under current plan

## Gotchas
- Pending and Disabled users **still count** toward license totals
- Annual customers: removals mid-cycle do NOT reduce charges until next renewal date
- Annual customers: additions mid-cycle trigger prorated charges starting the 1st of next month
- Invoice customers must contact their account manager directly — self-service portal does not apply
- Downgrade is not immediate; always verify via "View scheduled changes"

## Contact
- General billing: `billing@twingate.com`
- Enterprise/sales: `sales@twingate.com`

## Related Docs
- [Users](https://www.twingate.com/docs/users) — adding/removing users
- [Admins & Roles](https://www.twingate.com/docs/admins) — Billing role details
- [How to Cancel Your Subscription](https://www.twingate.com/docs/how-to-cancel)
- [Twingate Home Upgrade Instructions](https://www.twingate.com/docs/twingate-home)