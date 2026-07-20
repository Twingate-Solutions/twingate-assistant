# MSP Billing

## Page Title
MSP Billing

## Summary
MSP billing is consolidated and charged on the first of each calendar month, with separate line items per Customer Network. License count is calculated as total Users and Service Accounts minus Admins across all subtenants at end of billing period.

## Key Information
- Billing cycle: Monthly, charged on the 1st of each calendar month
- Each Customer Network has a minimum charge of **1 license** regardless of user count
- License formula: `(Total Users + Service Accounts) - Admins = Licenses charged`
- Admins are excluded from license count
- Billing is snapshot-based at end of month (e.g., March 31 count → April 1 charge)
- Invoices sent only to MSP portal signup email, not to Customer Networks

## Prerequisites
- Must be operating through the Twingate MSP portal
- Billing page is only accessible from the MSP portal, not Customer Network Admin Consoles

## Navigation
**Settings → Billing → "Manage Plan" button → Manage Subscriptions modal**

Modal options:
| Button | Function |
|--------|----------|
| Child subscriptions | View all Customer Networks and monthly prices |
| Payment Methods | Update credit card information |
| Billing History | View or download past invoices |

## Configuration Values / Parameters
None (UI-only management)

## Licensing Example
| Event | Value |
|-------|-------|
| Users + Service Accounts on Feb 28 | 100 |
| Admins on Feb 28 | 5 |
| **Charged March 1** | **95** |
| Add 50 users March 25 → total March 31 | 150 |
| Admins March 31 | 5 |
| **Charged April 1** | **145** |

## Gotchas
- Billing page does **not** appear in Customer Network Admin Consoles — only in the MSP portal
- Plan changes for individual Customer Networks require emailing `partnersupport@twingate.com` (cannot self-serve)
- Invoice email is tied to MSP portal signup email; update via Billing → Manage → Account Information
- Each Customer Network is billed a minimum of 1 license even with zero non-admin users

## Related Docs
- MSP Portal documentation
- Contact: `partnersupport@twingate.com` for Customer Network plan changes