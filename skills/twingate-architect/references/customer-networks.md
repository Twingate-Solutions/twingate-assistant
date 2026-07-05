# Customer Networks (MSP Portal)

## Summary
Customer Networks are tenant instances managed through the Twingate MSP Portal. Each network has its own Admin Console, URL, and user base. MSP partners create and manage these on behalf of their customers.

## Key Information
- Each Customer Network gets its own Admin Console and Client-visible name
- Network status types: **POC** (14-day trial), **Active** (post-trial subscription), **Non-renewing** (pending deletion at billing cycle end)
- License count = Users + Service Accounts − Admins
- Deleted networks remain accessible until end of billing cycle; no refunds issued
- Deleted networks are hidden from the Customer Networks tab
- MSP Customer Networks cannot be converted to standalone Twingate Networks

## Prerequisites
- Active MSP Portal account
- Unique subdomain for each network (MSP Portal and Customer Networks cannot share URLs)

## Required Information for New Customer Network

| Attribute | Description |
|-----------|-------------|
| Customer Network Name | Visible in Admin Console and user Clients |
| Customer Network URL | Unique subdomain |
| Admin Email | Initial admin user |
| Business Legal Name | Customer org name |
| Business Address | Customer address |
| Business URL | Customer website |
| Point of Contact | Contact at customer company |

## Step-by-Step: Delete a Customer Network
1. Locate the network row in the MSP Portal Customer Networks tab
2. Click the ellipses (`...`) at the end of the row
3. Click **"Delete Network"**
   - **Trial networks**: Deleted immediately; no charge
   - **Active networks**: Access retained until billing cycle end, then deleted

## Gotchas
- **No refunds** for deleted Customer Networks
- End users receive **no deletion notifications** — only a banner appears in the Admin Console
- MSP Portal URL and Customer Network URL must be **unique**; recommended convention: `yourcompanymsp` (portal) vs. `yourcompany` (network)
- Cannot convert a Customer Network to a standalone Twingate Network
- Trial cancellation is immediate and irreversible

## Related Docs
- MSP Billing page (license usage details)
- MSP Portal documentation