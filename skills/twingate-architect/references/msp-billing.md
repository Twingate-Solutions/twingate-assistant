# MSP Billing

## Summary
MSP billing is consolidated monthly, charged on the 1st of each calendar month. Licenses are calculated based on total Users and Service Accounts minus Admins across all subtenants. Billing is managed exclusively through the MSP portal, not individual Customer Network consoles.

## Key Information
- Billing cycle: 1st of every calendar month
- Each Customer Network has a separate invoice line item
- Each Customer Network is charged a **minimum of one license** regardless of user count
- License count = Total Users + Service Accounts − Admins (across all subtenants)
- Invoices sent only to MSP, not end customers
- Billing pages are **not visible** in Customer Network Admin Consoles

## License Calculation Example
| Date | Users + Service Accounts | Admins | Licenses Charged |
|------|--------------------------|--------|-----------------|
| March 1 | 100 (as of Feb 28) | 5 | 95 |
| April 1 | 150 (as of Mar 31) | 5 | 145 |

## Navigation Path
**Settings → Billing → Manage Plan → Manage Subscriptions modal**

Modal options:
- **Child subscriptions** — view all Customer Networks and monthly prices
- **Payment Methods** — update credit card
- **Billing History** — view/download invoices

## Configuration / Management Actions
| Task | How |
|------|-----|
| View Customer Networks & pricing | Manage Subscriptions → Child subscriptions |
| Update credit card | Manage Subscriptions → Payment Methods |
| View/download invoices | Manage Subscriptions → Billing History |
| Change Customer Network plan | Email `partnersupport@twingate.com` |
| Update invoice email address | MSP portal Billing page → Manage → Account Information |

## Gotchas
- Billing page only exists in the **MSP portal**; Customer Network admins cannot see billing
- Minimum charge per Customer Network is **one license**, even with zero non-admin users
- License count snapshot appears to be taken at **end of month** (last day counts toward next month's bill)
- Invoices go to the **signup email** — must update Account Information to change invoice recipient
- Plan changes for individual Customer Networks require contacting support; cannot be self-served

## Related Docs
- MSP Portal overview
- Customer Networks management
- User/Service Account administration