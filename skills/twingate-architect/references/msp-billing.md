# MSP Billing

## Summary
MSP billing is consolidated monthly, charged on the first of each calendar month, with separate line items per Customer Network. License counts are calculated based on total Users and Service Accounts minus Admins across all subtenants. Billing is managed exclusively through the MSP portal, not individual Customer Network consoles.

## Key Information
- **Billing cycle**: Charged on the 1st of every calendar month
- **Snapshot date**: License count taken on the last day of the prior month
- **Minimum charge**: Each Customer Network is billed for at least 1 license regardless of actual user count
- **License formula**: `Total Users + Service Accounts - Admins = Licenses charged`
- **Invoices sent to**: MSP portal signup email address only (not forwarded to end customers)

## Prerequisites
- Access to the MSP portal (billing pages are not visible in Customer Network Admin Consoles)
- Billing management requires navigating to **Settings > Billing > Manage Plan**

## Configuration Values / Billing Calculation

| Variable | Description |
|---|---|
| Users | All users across all subtenants |
| Service Accounts | All service accounts across all subtenants |
| Admins | Subtracted from total (across all subtenants) |
| **Licenses** | **(Users + Service Accounts) - Admins** |

**Example:**
- Feb 28: 100 Users/Service Accounts, 5 Admins → **95 licenses billed March 1**
- Mar 31: 150 Users/Service Accounts, 5 Admins → **145 licenses billed April 1**

## Step-by-Step: Managing Billing

1. Log into **MSP portal** (not a Customer Network console)
2. Navigate to **Settings > Billing**
3. Click **Manage Plan** to open the Manage Subscriptions modal
4. From the modal:
   - **Child subscriptions** → view per-Customer Network pricing
   - **Payment Methods** → update credit card
   - **Billing History** → view/download past invoices

## Gotchas
- Billing page **does not exist** in Customer Network Admin Consoles — only visible in the MSP portal
- Each Customer Network incurs a **minimum 1 license charge** even with zero non-admin users
- Invoice email is tied to the MSP portal signup email; update via **Billing > Manage > Account Information**
- Plan changes for individual Customer Networks require contacting **partnersupport@twingate.com** — cannot be self-served

## Related Docs
- MSP Portal documentation
- Customer Network administration
- Contact: partnersupport@twingate.com for plan changes