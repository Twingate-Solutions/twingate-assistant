# Cancel Your Subscription

## Summary
Instructions for canceling automatic renewal of a Twingate subscription via the Admin Console. Cancellation stops auto-renewal; access continues until the current subscription term ends. Downgrading to Starter plan is the cancellation mechanism.

## Key Information
- Cancellation = disabling automatic renewal, not immediate termination
- Access remains active until end of current billing period
- Cancellation is performed by downgrading to the **Twingate Starter** plan
- Must be completed through the Admin Console UI (no API/CLI method documented)

## Prerequisites
- Active automatically renewing Twingate subscription (paid plan)
- Admin Console access with billing permissions

## Step-by-Step

1. Sign into the Admin Console
2. Click **Settings**
3. Click **Billing**
4. Click **Manage Plan**
5. Click on your current subscription
6. Click **Edit Subscription**
7. Select the **Twingate Starter** plan
8. Click **Update Subscription**

## Configuration Values
- None (UI-only workflow, no env vars, CLI flags, or API parameters)

## Gotchas
- Subscription is not immediately terminated — it runs to the end of the current term
- "Cancellation" is effectively a plan downgrade to Starter, not a true account deletion
- No confirmation of cancellation method other than UI (no email trigger or API endpoint documented)

## Related Docs
- Billing settings documentation
- Twingate Starter plan feature comparison
- Account deletion (separate from subscription cancellation)