# Customer Networks (MSP Portal)

## Summary
Customer Networks are tenant networks managed through a Twingate MSP Portal. Each network has its own Admin Console, URL, and user base. MSP partners create and manage these on behalf of customers.

## Key Information
- Each Customer Network gets a unique subdomain URL and Admin Console
- Network status cycles: **POC** (14-day trial) → **Active** (auto-promotion after trial) → **Non-renewing** (pending deletion at billing cycle end)
- Deleted networks remain accessible until end of billing cycle; not shown in Customer Networks tab afterward
- License count = Users + Service Accounts − Admins

## Prerequisites
- Active MSP Portal account
- Unique subdomain not used by any other Twingate network (MSP Portal, Customer Network, or standalone)

## Required Attributes for New Customer Network

| Attribute | Description |
|---|---|
| Customer Network Name | Visible in Admin Console and user Clients |
| Customer Network URL | Unique subdomain |
| Admin Email | Initial admin user |
| Business Legal Name | Customer org name |
| Business Address | Customer address |
| Business URL | Customer website |
| Point of Contact | Customer contact person |

## Step-by-Step: Cancel Trial Network
1. Locate network row in MSP Portal
2. Click ellipses (`...`) at end of row
3. Click **Delete Network**
4. Network is immediately deleted; no charge incurred

## Step-by-Step: Delete Active Customer Network
1. Locate network row in MSP Portal
2. Click ellipses (`...`) at end of row
3. Click **Delete Network**
4. Network enters **Non-renewing** status; deleted at end of billing cycle

## Gotchas
- **MSP Portal URL ≠ Customer Network URL** — all Twingate URLs must be unique; recommended pattern: `yourcompanymsp` (portal) and `yourcompany` (customer network)
- **No conversion path** — MSP Customer Networks cannot be converted to standalone Twingate Networks
- **No refunds** — deleting a network mid-cycle does not trigger a refund
- **End users not notified** — only a banner in the Admin Console indicates scheduled deletion; no user-facing notifications sent
- **Trial cancellation is immediate** — unlike active network deletion, trial deletion takes effect instantly

## Related Docs
- MSP Billing page (license usage details)
- MSP Portal documentation