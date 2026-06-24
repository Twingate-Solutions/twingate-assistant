# MSP Billing

## Summary
MSP accounts receive consolidated monthly billing on the first of each calendar month, with separate line items per Customer Network. Licensing is calculated based on total Users and Service Accounts minus Admins across all subtenants.

## Key Information
- Billing date: 1st of every calendar month
- Each Customer Network has a minimum charge of 1 license regardless of user count
- License count = Total Users + Service Accounts - Admins (across all subtenants)
- Invoices sent only to MSP portal email address, not to Customer Networks
- Billing pages are only visible in the MSP portal, not in Customer Network Admin Consoles

## Billing Management Navigation
- **Settings > Billing > Manage Plan** opens the Manage Subscriptions modal
- Modal sub-sections:
  - **Child subscriptions** — view all Customer Networks and monthly prices
  - **Payment Methods** — update credit card information
  - **Billing History** — view or download past invoices

## Licensing Calculation

| Variable | Description |
|----------|-------------|
| Billable licenses | (Total Users + Service Accounts) - Admins |
| Snapshot timing | End of prior month |
| Charge date | 1st of following month |

**Example:**
- Feb 28: 100 Users/Service Accounts, 5 Admins → **95 licenses charged March 1**
- Mar 31: 150 Users/Service Accounts, 5 Admins → **145 licenses charged April 1**

## Gotchas
- Billing page does not appear in Customer Network Admin Consoles — MSP portal only
- Plan changes for individual Customer Networks require contacting `partnersupport@twingate.com` (cannot self-serve)
- Invoice email goes to the signup email on the MSP portal; update via **Billing > Manage > Account Information**
- Minimum 1 license per Customer Network even with zero non-admin users

## Contact
- Plan changes: `partnersupport@twingate.com`

## Related Docs
- MSP Portal overview
- Customer Network management
- User and Service Account administration