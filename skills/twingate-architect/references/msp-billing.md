# MSP Billing

## Summary
MSP billing is consolidated monthly, charged on the 1st of each calendar month. Invoices are generated per Customer Network with license counts based on total Users and Service Accounts minus Admins across all subtenants.

## Key Information
- Billing date: 1st of every calendar month
- Each Customer Network = minimum 1 license (regardless of user count)
- License count = (Total Users + Service Accounts) − Admins across all subtenants
- Invoices sent only to MSP portal email; Customer Networks have no billing page
- Snapshot for billing taken on last day of previous month

## Billing Navigation
All billing managed via: **Settings > Billing > Manage Plan**

| Modal Button | Function |
|---|---|
| Child subscriptions | View all Customer Networks and monthly prices |
| Payment Methods | Update credit card |
| Billing History | View/download past invoices |

## Licensing Calculation Example

| Date | Users + Service Accounts | Admins | Licenses Charged |
|---|---|---|---|
| March 1 | 100 (as of Feb 28) | 5 | 95 |
| April 1 | 150 (as of Mar 31) | 5 | 145 |

## Gotchas
- Billing page is **only visible in the MSP portal**, not in individual Customer Network Admin Consoles
- Invoices go to the email used to register the MSP portal account — update via Billing > Manage > Account Information
- Plan changes for individual Customer Networks require contacting `partnersupport@twingate.com` (cannot self-serve)
- Each Customer Network incurs at least 1 license charge even with zero non-admin users

## Prerequisites
- MSP portal access (not standard tenant admin access)

## Related Docs
- MSP Portal overview
- Customer Network management
- Contact: `partnersupport@twingate.com` for plan changes