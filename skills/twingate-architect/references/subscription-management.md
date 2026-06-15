# Subscription Management

## Summary
Twingate billing is usage-based on total Users and Service Accounts, billed monthly or annually. Monthly customers are billed at renewal based on end-of-cycle counts; annual customers receive prorated mid-cycle charges. Enterprise and invoice customers have separate billing arrangements.

## Key Information
- **License unit**: Each User (including Pending/Disabled) and each Service Account = 1 license
- **Users counted**: IdP-synced users, manually added users, Pending users, Disabled users
- **Service Accounts**: Count as 1 license regardless of number of Service Keys or key status
- **Monthly billing**: Charged at renewal based on user count on last day of previous cycle
- **Annual billing**: Mid-cycle additions → prorated charge on 1st of following month; removals apply at next annual renewal
- **Timezone note**: Billing transactions occur at midnight UTC; may appear as end-of-month charge depending on local timezone

## Plan Management Steps

### Downgrade Subscription
1. Admin Console → **Settings** → **Manage Plan**
2. Click your subscription → **Edit Subscription**
3. Select new plan → **Update Subscription**
4. Downgrade takes effect on next billing date

### Verify Scheduled Downgrade
1. Admin Console → **Settings** → **Manage Plan**
2. Click subscription → **View scheduled changes**
3. Option to cancel downgrade is available here

### Change Billing Email
Admin Console → **Settings** → **Manage Plan** → **Billing & Shipping Addresses**

### Access Past Invoices
Admin Console → **Settings** → **Manage Plan** → **Billing History** (PDF download)

## Configuration Notes
- Starter, Business, Teams plan changes: self-serve via Admin Console
- Enterprise plan changes: contact `sales@twingate.com`
- Invoice customers: contact account manager directly
- Billing questions: `billing@twingate.com`

## Gotchas
- **Pending and Disabled users consume licenses** — removing access does not reduce count until users are fully removed
- Annual plan reductions only take effect at next renewal, not immediately
- Downgrading from Annual to Monthly also follows the "next billing date" rule
- Mid-cycle annual additions generate a prorated charge on the 1st of the *following* calendar month, not immediately

## Related Docs
- [Users Management](https://www.twingate.com/docs/users)
- [How to Cancel Your Subscription](https://www.twingate.com/docs/cancel-subscription)
- [Upgrading to Twingate Home](https://www.twingate.com/docs/twingate-home)