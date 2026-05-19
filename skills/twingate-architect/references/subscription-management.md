# Twingate Subscription Management

## Summary
Twingate billing is monthly or annual based on total Users and Service Accounts. Monthly customers are billed at renewal based on prior cycle end count; annual customers receive prorated mid-cycle charges. Enterprise customers may have custom billing arrangements.

## Key Information

- **License units**: Users (including Pending and Disabled) + Service Accounts
- **User sources counted**: IdP-synced users, manually added users, all states (pending/disabled)
- **Service Accounts**: Each counts as 1 license regardless of number of Service Keys or key status
- **Monthly billing**: Charged at renewal based on user count on last day of previous cycle
- **Annual billing**: Mid-cycle additions trigger prorated charge on the 1st of next calendar month; reductions apply at next renewal
- **Billing transactions**: Processed at midnight UTC (may appear as end-of-month charge depending on timezone)
- **Invoices sent to**: Email address entered during billing address setup at purchase

## Prerequisites
- Admin Console access
- Appropriate account permissions to manage billing

## Step-by-Step

### Downgrade Subscription
1. Admin Console → **Settings** → **Manage Plan**
2. Click your subscription → **Edit Subscription**
3. Choose new plan → **Update Subscription**
> Downgrades (including Annual→Monthly) take effect on next billing date

### Verify Scheduled Downgrade
1. Admin Console → **Settings** → **Manage Plan**
2. Click your subscription → **View scheduled changes**
> Also allows canceling a pending downgrade

### Change Billing Email
Admin Console → **Settings** → **Manage Plan** → **Billing & Shipping Addresses** → update email

### Access Past Invoices
Admin Console → **Settings** → **Manage Plan** → **Billing History** → download PDF

### Change Plan (Starter/Business/Teams)
Admin Console → **Settings** → **Manage Plan** → subscription → **Edit Subscription** → select plan → **Update Subscription**

## Configuration Values
| Setting | Location |
|---|---|
| Plan changes | Settings → Manage Plan → Edit Subscription |
| Billing email | Settings → Manage Plan → Billing & Shipping Addresses |
| Invoice history | Settings → Manage Plan → Billing History |
| Scheduled changes | Settings → Manage Plan → View scheduled changes |

## Gotchas
- **Pending and Disabled users count** toward license total — removing access doesn't reduce billing unless users are fully removed
- Annual customers: reductions don't credit mid-cycle; savings apply only at next renewal
- Annual customers: additions are prorated from the **1st of next month**, not the day added
- Enterprise plan changes require contacting `sales@twingate.com`
- Invoice customers must contact their account manager for billing changes

## Related Docs
- [Users Management](https://www.twingate.com/docs/users)
- [How to Cancel Your Subscription](https://www.twingate.com/docs/cancel-subscription)
- [Upgrading to Twingate Home](https://www.twingate.com/docs/twingate-home)
- Billing questions: `billing@twingate.com`