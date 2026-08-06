---
source: https://www.twingate.com/docs/subscription-management
type: docs
fetched: 2026-08-05
source_version: e34426ab118bc211d5cdf44cfcbb14924eaf7ab9c3cb9f87d9e1eeb6f8f76236
---

# Subscription Management

## Summary
Twingate subscriptions are billed monthly or annually based on total Users and Service Accounts. Billing is managed through the Admin Console by Admin users or users with the dedicated Billing role. Enterprise customers may have custom billing arrangements.

## Key Information

- **Billing roles**: Admin users or dedicated Billing role (Billing role grants Billing page access only)
- **License counting includes**: IdP-synced users, manually added users, Admin users, Pending/Disabled users, Service Accounts (regardless of key count/status)
- **Monthly billing**: Billed at renewal based on user count on last day of previous cycle
- **Annual billing**: Billed at renewal based on last day of previous cycle; mid-cycle additions incur prorated charges at start of each calendar month; reductions apply at next billing cycle start
- **Invoice customers**: Must contact account manager for changes
- **Billing transactions** occur at midnight UTC (may appear as end-of-month charges depending on timezone)

## Billing Actions (Admin Console → Settings → Manage Plan)

| Action | Path |
|--------|------|
| Downgrade/Change plan | Subscription → Edit Subscription → Update Subscription |
| View scheduled changes | Subscription → View scheduled changes |
| Update billing email | Billing & Shipping Addresses |
| Download past invoices | Billing History (PDF format) |
| Cancel downgrade | Subscription → View scheduled changes |

## Step-by-Step: Change Subscription Plan

1. Sign into Admin Console
2. Click **Settings**
3. Click **Manage Plan**
4. Click your subscription
5. Click **Edit Subscription**
6. Choose desired plan
7. Click **Update Subscription**

> Note: All downgrades (including Annual → Monthly) take effect on the **next billing date**

## Gotchas

- **Disabled and Pending users still count** toward license totals — remove them explicitly to reduce billing
- Annual mid-cycle additions are prorated and charged **on the 1st of the following month**, not immediately
- Annual reductions are **not credited mid-cycle** — savings apply only at next renewal
- Billing email is tied to billing address, not account login; update separately in Billing & Shipping Addresses
- Enterprise plan changes require contacting `sales@twingate.com`

## Contact

- General billing: `billing@twingate.com`
- Enterprise/invoice: account manager or `sales@twingate.com`

## Related Docs

- [Users management](https://www.twingate.com/docs/users)
- [Admin roles](https://www.twingate.com/docs/admins)
- [Cancel subscription](https://www.twingate.com/docs/how-to-cancel)
- [Twingate Home upgrade instructions](https://www.twingate.com/docs/twingate-home)