---
source: https://www.twingate.com/docs/msp-billing
type: docs
fetched: 2026-08-14
source_version: 3a3a86ff7434ab20a64748a0a84b01720b87bea4f2dc83b386166594aa6d56ab
---

# MSP Billing

## Summary
Twingate MSP accounts receive consolidated monthly billing on the first of each calendar month, with separate line items per Customer Network. License counts are calculated based on total Users and Service Accounts minus Admins across all subtenants at end of billing period.

## Key Information
- Billing date: 1st of every calendar month
- Each Customer Network has a minimum charge of **1 license** regardless of user count
- Invoice recipients: MSP portal email only — Customer Networks do **not** receive invoices
- Billing page is only visible in the MSP portal, not in Customer Network Admin Consoles

## License Calculation
```
Licenses Charged = (Total Users + Service Accounts across all subtenants) - (Total Admins across all subtenants)
```
Snapshot taken on **last day of the month**; charged on the **1st of the following month**.

**Example:**
| Date | Users + Service Accounts | Admins | Licenses Charged (next month 1st) |
|------|--------------------------|--------|-----------------------------------|
| Feb 28 | 100 | 5 | 95 |
| Mar 31 | 150 | 5 | 145 |

## Configuration & Management (UI)
Navigate: **Settings > Billing > Manage Plan**

| Action | Location in Modal |
|--------|-------------------|
| View Customer Networks & pricing | "Child subscriptions" button |
| Update credit card | "Payment Methods" button |
| View/download invoices | "Billing History" button |
| Change Customer Network plan | Email partnersupport@twingate.com |
| Update billing email | Billing page > Manage > Account Information |

## Gotchas
- Admins are **excluded** from license count; adding admins reduces billable licenses
- Mid-month user additions are counted in the **end-of-month** snapshot (not prorated mid-month)
- Customer Network plan changes require contacting partner support — not self-serve
- Invoices go to the MSP signup email; if not receiving them, update Account Information in billing settings
- Minimum 1 license per Customer Network even with zero non-admin users

## Prerequisites
- Must have MSP portal access (not a standard Customer Network account)
- Billing management requires MSP-level credentials

## Related Docs
- MSP Portal overview
- Customer Network management
- User/Service Account administration