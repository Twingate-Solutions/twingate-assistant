# Subscription Management

## Summary
Twingate billing is based on total Users and Service Accounts, with monthly or annual billing cycles. Monthly customers are billed at renewal based on prior cycle's end count; annual customers receive prorated mid-cycle charges for additions. Enterprise/invoice customers have separate arrangements.

## Key Information
- **License count includes**: All Users (IdP-synced + manual), Pending Users, Disabled Users, and Service Accounts
- **Service Accounts**: Each counts as one license regardless of number of Service Keys or key status
- **Monthly billing**: Charged at renewal based on headcount on last day of previous cycle
- **Annual billing**: Mid-cycle additions generate prorated charges billed on the 1st of each calendar month; reductions apply at next renewal
- **Downgrades**: Always take effect on next billing date, not immediately
- **Timezone note**: Billing transactions occur at midnight UTC — may appear as end-of-month charges depending on your timezone

## Prerequisites
- Admin Console access required for all self-service billing changes
- Enterprise/invoice customers must contact account manager or sales for plan changes

## Step-by-Step: Downgrade Subscription
1. Admin Console → **Settings** → **Manage Plan**
2. Click your subscription → **Edit Subscription**
3. Choose new plan → **Update Subscription**

## Step-by-Step: Verify Scheduled Downgrade
1. Admin Console → **Settings** → **Manage Plan**
2. Click your subscription → **View scheduled changes**
3. Cancel downgrade here if needed

## Step-by-Step: Change Billing Email
1. Admin Console → **Settings** → **Manage Plan** → **Billing & Shipping Addresses**
2. Update email — takes effect on next invoice

## Step-by-Step: Access Past Invoices
1. Admin Console → **Settings** → **Manage Plan** → **Billing History**
2. Download invoices as PDF

## Configuration Values
| Item | Value |
|------|-------|
| Billing support email | billing@twingate.com |
| Enterprise sales email | sales@twingate.com |
| Proration billing date | 1st of each calendar month |
| Billing transaction time | Midnight UTC |

## Gotchas
- **Pending and Disabled Users still count** toward license total — removing access doesn't automatically reduce license count
- Downgrade from Annual to Monthly also only takes effect at next billing date
- Annual reductions don't generate credits mid-cycle; savings only apply at renewal
- Mid-cycle additions on annual plans are prorated from the 1st of the following month, not the day of addition

## Related Docs
- [Users Management](https://www.twingate.com/docs/users)
- [How to Cancel Your Subscription](https://www.twingate.com/docs/cancel-subscription)
- [Twingate Home Upgrade Instructions](https://www.twingate.com/docs/twingate-home)