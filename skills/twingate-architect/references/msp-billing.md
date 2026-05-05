# MSP Billing

## Summary
MSP accounts receive consolidated monthly billing on the first of each calendar month, with separate line items per Customer Network. License counts are calculated based on total Users and Service Accounts minus Admins across all subtenants.

## Key Information
- Billing occurs on the **1st of every calendar month**
- Each Customer Network has a **minimum charge of 1 license** regardless of user count
- License formula: `Total Users + Service Accounts - Admins = Licenses charged`
- Invoices sent only to MSP portal email; **not visible in Customer Network Admin Consoles**
- Billing page location: **Settings > Billing > Manage Plan**

## Licensing Calculation

| Variable | Counts Toward Licenses |
|----------|----------------------|
| Users | Yes |
| Service Accounts | Yes |
| Admins | No (subtracted) |

**Example:**
- Feb 28: 100 Users/Service Accounts, 5 Admins → March 1 charge: **95 licenses**
- Mar 31: 150 Users/Service Accounts, 5 Admins → April 1 charge: **145 licenses**

## Managing Billing (Manage Subscriptions Modal)

| Action | Button |
|--------|--------|
| View Customer Networks & pricing | Child Subscriptions |
| Update credit card | Payment Methods |
| View/download invoices | Billing History |

## Gotchas
- Billing page **only exists in the MSP portal**; Customer Network admins cannot access it
- License count is a **snapshot at end of month** (not prorated mid-month additions)
- To change a Customer Network's plan, you must email `partnersupport@twingate.com` — no self-serve option
- Invoice emails go to the **MSP portal signup email**; update via Billing > Manage > Account Information

## Prerequisites
- Access to MSP portal (not Customer Network Admin Console)
- Billing admin permissions within MSP portal

## Related Docs
- MSP Portal Overview
- Customer Networks Management
- User and Service Account Administration