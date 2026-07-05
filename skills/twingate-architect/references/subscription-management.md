# Subscription Management

## Summary
Twingate billing is managed monthly or annually based on total Users and Service Accounts. Admins or users with the dedicated Billing role can manage billing via the Admin Console. Enterprise customers may have custom billing arrangements.

## Key Information

- **Billing roles**: Admin users or users with the dedicated **Billing** role (Billing role grants access to Billing page only)
- **License counts include**: IdP-synced users, manually added users, Admin users, Pending/Disabled users, Service Accounts (regardless of key count/status)
- **Monthly billing**: Charged at renewal based on user count on the last day of the previous cycle
- **Annual billing**: Charged at renewal based on last day of previous cycle; mid-cycle additions generate prorated charges billed on the 1st of each calendar month; reductions apply at next renewal
- **Invoice customers**: Contact account manager for billing changes
- **Timezone note**: Billing transactions occur at midnight UTC — may appear as end-of-month charges depending on local timezone

## Prerequisites

- Admin or Billing role access to the Twingate Admin Console

## Step-by-Step: Downgrade/Change Subscription Plan

1. Sign into Admin Console
2. **Settings** → **Manage Plan**
3. Click your subscription → **Edit Subscription**
4. Choose desired plan → **Update Subscription**

> Downgrades (including Annual → Monthly) take effect on the next billing date.

## Step-by-Step: Verify Scheduled Downgrade

1. Admin Console → **Settings** → **Manage Plan**
2. Click your subscription → **View scheduled changes**
3. Cancel downgrade from this view if needed

## Configuration Values

| Task | Location |
|------|----------|
| Change billing email | Settings → Manage Plan → Billing & Shipping Addresses |
| Download past invoices | Settings → Manage Plan → Billing History |
| Redeem Home promo code | Settings → Billing tab → current plan |

## Gotchas

- **Disabled/Pending users still count** toward license totals — remove them to reduce license count
- **Annual mid-cycle additions**: Prorated charges bill on the **1st of the month**, not immediately
- **Annual reductions**: Do NOT reduce your current bill — only apply at next renewal date
- Downgrade is not immediate; always verify via "View scheduled changes"
- Enterprise plan changes require contacting `sales@twingate.com`

## Related Docs

- [Users Management](https://www.twingate.com/docs/users)
- [Admin Roles](https://www.twingate.com/docs/admins)
- [Cancel Subscription](https://www.twingate.com/docs/cancel-subscription)
- [Twingate Home Upgrade Instructions](https://www.twingate.com/docs/twingate-home)
- Billing support: `billing@twingate.com`