# Subscription Management

## Summary
Twingate billing is based on total number of Users and Service Accounts, billed monthly or annually. Monthly customers pay based on counts at end of billing cycle; annual customers pay prorated charges for mid-cycle additions. Enterprise and invoice customers have separate billing arrangements.

## Key Information

- **License unit**: Each User (including Pending/Disabled) + each Service Account = 1 license
- **Users counted**: All IdP-synced users, manually added users, Pending users, Disabled users
- **Service Accounts**: Each counts as 1 license regardless of number of Service Keys or key status
- **Billing timezone**: Midnight UTC — charges may appear end-of-month depending on local timezone

## Billing Models

| Type | Behavior |
|------|----------|
| Monthly | Billed on renewal date based on count at end of previous cycle |
| Annual | Billed annually; mid-cycle additions trigger prorated charge on 1st of next month; reductions apply at next renewal |
| Invoice | Contact account manager directly |

## Common Operations

### Downgrade Subscription
1. Admin Console → **Settings** → **Manage Plan**
2. Click your subscription → **Edit Subscription**
3. Select new plan → **Update Subscription**
4. *(Takes effect on next billing date)*

### Verify Scheduled Downgrade / Cancel Downgrade
1. Admin Console → **Settings** → **Manage Plan**
2. Click subscription → **View scheduled changes**

### Change Billing Email
Admin Console → **Settings** → **Manage Plan** → **Billing & Shipping Addresses** → update email

### Access Past Invoices
Admin Console → **Settings** → **Manage Plan** → **Billing History** → download PDF

### Change Plan (Starter/Business/Teams)
Admin Console → **Settings** → **Manage Plan** → subscription → **Edit Subscription**

## Gotchas

- **Pending and Disabled users still consume licenses** — removing from active use is not enough to reduce license count
- Annual mid-cycle user additions: prorated charge hits on **April 1** (first of next month), not immediately
- Annual reductions only take effect at **next renewal**, not immediately
- Downgrades (including Annual → Monthly) never take effect immediately — always next billing date
- Enterprise plan changes require contacting `sales@twingate.com`

## Contact

- Billing questions: `billing@twingate.com`
- Enterprise/invoice changes: account manager or `sales@twingate.com`

## Related Docs

- [Users Management](https://www.twingate.com/docs/users)
- [How to Cancel Your Subscription](https://www.twingate.com/docs/cancel-subscription)
- [Upgrading to Twingate Home](https://www.twingate.com/docs/twingate-home)