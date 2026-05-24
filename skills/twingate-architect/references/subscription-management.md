# Subscription Management

## Summary
Twingate billing is based on total Users (including pending/disabled) and Service Accounts. Monthly customers are billed at renewal based on end-of-cycle counts; annual customers are billed annually with mid-cycle additions prorated monthly. Enterprise and invoice customers have separate arrangements.

## Key Information

- **License counting**: All Users (synced from IdP, manual, pending, disabled) + Service Accounts count toward license total
- **Service Accounts**: Each counts as one license regardless of number of Service Keys or key status
- **Monthly billing**: Charged at renewal based on user count on last day of previous billing cycle
- **Annual billing**: Mid-cycle additions incur prorated charge on the 1st of each calendar month; reductions apply at next renewal
- **Billing timezone**: Transactions run at midnight UTC — may appear as end-of-month charges depending on local timezone
- **Downgrades**: Always take effect on next billing date, not immediately

## Plan Management Steps

### Change/Downgrade Plan
1. Admin Console → **Settings** → **Manage Plan**
2. Click your subscription → **Edit Subscription**
3. Select desired plan → **Update Subscription**

### Verify Scheduled Downgrade
1. Admin Console → **Settings** → **Manage Plan**
2. Click your subscription → **View scheduled changes**
3. Option to cancel the downgrade is available here

### Update Billing Email
Admin Console → **Settings** → **Manage Plan** → **Billing & Shipping Addresses**

### Access Past Invoices
Admin Console → **Settings** → **Manage Plan** → **Billing History** (PDF download available)

## Configuration Notes

- Enterprise plan changes: contact `sales@twingate.com`
- Billing questions: contact `billing@twingate.com`
- Invoice customers: contact account manager directly

## Gotchas

- **Pending and Disabled users still count** toward license totals — removing them from the license count requires deletion, not just disabling
- Annual plan reductions don't save money mid-cycle; credits only apply at next renewal
- Annual-to-monthly downgrades also wait until next billing date
- Prorated charges for annual plans appear on the **1st of the month**, not immediately when users are added

## Related Docs

- [Users Management](https://www.twingate.com/docs/users)
- [How to Cancel Your Subscription](https://www.twingate.com/docs/how-to-cancel)
- [Twingate Home Upgrade Instructions](https://www.twingate.com/docs/twingate-home)