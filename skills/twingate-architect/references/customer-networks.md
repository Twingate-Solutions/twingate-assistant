# Customer Networks (MSP Portal)

## Summary
Customer Networks are tenant environments managed through the Twingate MSP Portal. Each network has its own Admin Console, URL, and user base. MSP partners create and manage these networks on behalf of their customers.

## Key Information
- Each Customer Network gets its own Admin Console and Client-visible name
- Network status types: **POC** (14-day trial), **Active** (post-trial/subscribed), **Non-renewing** (pending deletion at billing cycle end)
- License count = Users + Service Accounts − Admins
- Deleted networks remain accessible until end of billing cycle; no refunds issued
- Deleted networks do not appear on the Customer Networks tab
- MSP Customer Networks **cannot** be converted to standalone Twingate Networks

## Prerequisites
- Active MSP Portal account
- Unique subdomain URL (distinct from MSP Portal URL and all other Twingate networks)

## Required Information for New Customer Network

| Attribute | Description |
|-----------|-------------|
| Customer Network Name | Visible in Admin Console and user Clients |
| Customer Network URL | Unique subdomain for network access |
| Admin Email | Initial administrative user |
| Business Legal Name | Customer organization name |
| Business Address | Customer address |
| Business URL | Customer website |
| Point of Contact | Customer company contact |

## Step-by-Step: Delete a Network
1. Locate the network row in the MSP Portal Customer Networks tab
2. Click the ellipses (`...`) at the end of the row
3. Click **"Delete Network"**
   - **Trial networks**: Deleted immediately, no charge
   - **Active networks**: Accessible until billing cycle end, then deleted

## Gotchas
- All Twingate URLs must be globally unique — MSP Portal and its Customer Networks cannot share a subdomain
- Recommended naming convention: `yourcompanymsp` (portal) vs `yourcompany` (customer network)
- End users receive **no notification** of scheduled deletion — only a banner appears in the Admin Console
- No refunds for deleted Customer Networks regardless of remaining billing period
- Direct conversion from MSP Customer Network → standalone network is **not supported**

## Related Docs
- MSP Billing page (license usage details)
- MSP Portal documentation