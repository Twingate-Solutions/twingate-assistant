# MSP Billing

## Summary
MSP accounts receive consolidated monthly billing on the first of each calendar month, with separate line items per Customer Network. License counts are calculated based on total Users and Service Accounts minus Admins across all subtenants at end of billing period.

## Key Information
- Billing cycle: 1st of every calendar month
- Each Customer Network has a minimum charge of 1 license regardless of user count
- Invoices sent only to MSP portal owner email, not to Customer Networks
- Billing page exists only in MSP portal, not in Customer Network Admin Consoles

## License Calculation
**Formula:** Total Users + Service Accounts (across all subtenants) − Total Admins = Licenses charged

**Example:**
| Date | Users/Service Accounts | Admins | Licenses Billed |
|------|----------------------|--------|-----------------|
| March 1 | 100 | 5 | 95 |
| April 1 | 150 | 5 | 145 |

Snapshot taken on last day of month; billed on 1st of following month.

## Navigation Path
`Settings > Billing > Manage Plan` → opens **Manage Subscriptions modal**

### Modal Options
- **Child subscriptions** — view all Customer Networks and monthly prices
- **Payment Methods** — update credit card
- **Billing History** — view/download past invoices

## Configuration & Management

| Task | Method |
|------|--------|
| Change Customer Network plan | Email `partnersupport@twingate.com` |
| Update invoice email address | MSP Portal Billing page → Manage → Account Information |
| View per-network charges | Manage Subscriptions → Child subscriptions |

## Gotchas
- Admins are **excluded** from license count; only Users and Service Accounts count
- Minimum 1 license per Customer Network even if it has zero non-admin users
- Invoice email is the MSP portal signup email — must update manually in Account Information if it changes
- Customer Network admins cannot see billing — only MSP portal owner has access

## Related Docs
- MSP Portal overview
- User roles and Admin definitions
- Twingate Service Accounts documentation