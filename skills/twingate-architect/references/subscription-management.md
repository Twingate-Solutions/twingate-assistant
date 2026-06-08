# Subscription Management

## Summary
Twingate billing is based on total number of Users and Service Accounts, billed monthly or annually. Monthly customers pay based on count at end of billing cycle; annual customers pay prorated charges for mid-cycle additions. Enterprise and invoice customers have separate arrangements.

## Key Information
- **License counting**: All Users (including Pending and Disabled) + Service Accounts count toward license total
- **IdP-synced users**: Counted regardless of sync source or manual addition method
- **Service Accounts**: Each counts as one license regardless of number of Service Keys or key status
- **Billing timezone**: Transactions process at midnight UTC — may appear as end-of-month charges depending on locale

## Billing Models

### Monthly
- Billed at renewal based on User/Service Account count on **last day of previous cycle**

### Annual
- Renewal billed based on count on **last day of previous cycle**
- Mid-cycle additions: prorated charge billed on **1st of the following calendar month**
- Mid-cycle reductions: applied at **start of next billing cycle** (no mid-cycle credit)

### Invoice Customers
- Contact account manager directly for changes

## Step-by-Step: Downgrade Subscription
1. Admin Console → **Settings** → **Manage Plan**
2. Click your subscription → **Edit Subscription**
3. Choose new plan → **Update Subscription**
4. Downgrade takes effect on **next billing date**

To verify downgrade is scheduled: Settings → Manage Plan → subscription → **View scheduled changes** (also allows canceling the downgrade)

## Step-by-Step: Change Plan (Starter/Business/Teams)
Same path as downgrade: Settings → Manage Plan → Edit Subscription → select plan → Update Subscription

**Enterprise plan changes**: Contact `sales@twingate.com`

## Billing Administration
| Task | Path |
|------|------|
| Change invoice email | Settings → Manage Plan → Billing & Shipping Addresses |
| Download past invoices | Settings → Manage Plan → Billing History (PDF) |
| Redeem Home promo code | Settings → Billing tab under current plan |

## Gotchas
- **Pending and Disabled users still consume licenses** — remove explicitly to reduce count
- Annual customers get **no credit for mid-cycle user removals**; reduction only applies at next renewal
- Annual additions are prorated from **April 1** (start of next calendar month), not from the date added
- Billing contact email is set at purchase; must be manually updated post-activation
- All downgrades (including Annual → Monthly frequency changes) are deferred to next billing date

## Contact
- Billing questions: `billing@twingate.com`
- Enterprise/invoice: account manager or `sales@twingate.com`

## Related Docs
- [Users management](https://www.twingate.com/docs/users)
- [How to Cancel Your Subscription](https://www.twingate.com/docs/cancel-subscription)
- [Upgrading to Twingate Home](https://www.twingate.com/docs/twingate-home)