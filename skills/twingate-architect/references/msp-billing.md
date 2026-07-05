# MSP Billing

## Page Title
MSP Billing

## Summary
MSP partners receive consolidated monthly billing on the first of each calendar month, with separate line items per Customer Network. License count is calculated as total Users and Service Accounts minus Admins across all subtenants. Billing management is handled exclusively through the MSP portal, not individual Customer Network consoles.

## Key Information
- Billing date: 1st of every calendar month
- Each Customer Network has a minimum charge of **1 license** regardless of user count
- Invoices are sent only to the MSP, not to end customers
- Billing page exists **only** in the MSP portal (not in Customer Network Admin Consoles)

## License Calculation
```
Licenses charged = (Total Users + Service Accounts across all subtenants) - Total Admins
```
- Count is taken from the **last day of the prior month**
- Admins are excluded from license counts
- Example: 150 Users/SAs - 5 Admins = 145 licenses billed

## Step-by-Step: Access Billing Settings
1. Navigate to MSP portal → **Settings > Billing**
2. Click **"Manage Plan"** to open the Manage Subscriptions modal
3. From the modal, access:
   - **Child subscriptions** — view all Customer Networks and monthly prices
   - **Payment Methods** — update credit card information
   - **Billing History** — view or download past invoices

## Configuration Values
| Setting | Location |
|---|---|
| Invoice email address | MSP portal Billing page → "Manage" → Account Information |
| Customer Network plan changes | Contact `partnersupport@twingate.com` |

## Gotchas
- **Billing page not visible in Customer Network Admin Console** — must use MSP portal
- Minimum 1 license charged per Customer Network even with zero non-admin users
- Invoices go to the **signup email** for the MSP portal — update via Account Information if needed
- Plan changes for individual Customer Networks require contacting partner support directly; cannot be self-served

## Related Docs
- MSP Portal documentation
- Twingate licensing/plans documentation