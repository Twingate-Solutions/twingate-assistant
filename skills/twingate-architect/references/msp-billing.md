# MSP Billing

## Summary
MSP billing is consolidated monthly, charged on the first of each calendar month, with separate line items per Customer Network. License count is calculated as total Users + Service Accounts minus Admins across all subtenants. Billing is managed exclusively through the MSP portal, not individual Customer Network consoles.

## Key Information
- Billing date: 1st of every calendar month
- Each Customer Network has a minimum charge of 1 license regardless of user count
- License formula: `(Total Users + Service Accounts) - Admins = Licenses charged`
- Invoices sent only to MSP email, not to end customers
- Billing pages are only visible in the MSP portal (not in Customer Network Admin Console)

## Billing Management Navigation
**Settings > Billing > "Manage Plan" button** opens the Manage Subscriptions modal, which provides access to:
- **Child subscriptions** – view all Customer Networks and monthly prices
- **Payment Methods** – update credit card information
- **Billing History** – view or download past invoices

## License Calculation Example
| Date | Users + Service Accounts | Admins | Licenses Charged |
|------|--------------------------|--------|-----------------|
| March 1 | 100 (as of Feb 28) | 5 | 95 |
| April 1 | 150 (as of Mar 31) | 5 | 145 |

Snapshot is taken on the last day of the month; charge applies on the 1st of the following month.

## Gotchas
- Billing page does **not** exist in Customer Network Admin Consoles — only in the MSP portal
- Each Customer Network incurs a **minimum of 1 license** even with zero non-admin users
- Admins are subtracted from license count; adding admins reduces billable licenses
- Plan changes for individual Customer Networks require contacting `partnersupport@twingate.com` — cannot be self-served

## Invoice/Notification Issues
- Invoices go to the email used at MSP portal signup
- To update billing email: MSP portal Billing page > **Manage** > edit Account Information

## Related Docs
- MSP Portal overview
- Customer Network management
- Service Accounts documentation