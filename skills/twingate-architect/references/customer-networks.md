# Customer Networks (MSP Portal)

## Summary
Customer Networks are Twingate network instances managed through an MSP Portal. Each network has its own Admin Console, URL, and user base. MSPs create and manage these on behalf of their customers.

## Key Information
- Each Customer Network gets its own unique subdomain URL and Admin Console
- Networks start with a 14-day free trial (POC status), then auto-convert to Active
- License count = Users + Service Accounts minus admins
- Deleted Customer Networks remain accessible until end of billing cycle
- Deleted networks are hidden from the Customer Networks tab

## Prerequisites
- Active MSP Portal account
- Unique subdomain not used by any other Twingate network (MSP Portal, Customer Network, or standalone)

## Required Attributes for New Customer Network
| Attribute | Description |
|-----------|-------------|
| Customer Network Name | Visible in Admin Console and user Clients |
| Customer Network URL | Unique subdomain |
| Admin Email | Initial admin user |
| Business Legal Name | Customer org name |
| Business Address | Customer address |
| Business URL | Customer website |
| Point of Contact | Customer contact person |

## Network Statuses
- **POC**: Within initial 14-day free trial
- **Active**: Active subscription (auto-assigned after trial)
- **Non-renewing**: Scheduled for deletion at end of billing cycle

## Gotchas
- MSP Portal URL and Customer Network URLs **must be unique** — recommended pattern: `yourcompanymsp` (portal) vs `yourcompany` (customer network)
- Customer Networks **cannot be converted** to standalone Twingate Networks
- Canceling a trial via "Delete Network" is **immediate** — no end-of-cycle grace period
- Deleting an active network (non-trial) retains access until billing cycle ends — no refunds issued
- End users receive **no notifications** when a network is deleted; only admins see a banner in the Admin Console

## Step-by-Step: Delete/Cancel a Customer Network
1. Navigate to Customer Networks tab in MSP Portal
2. Click the ellipses (`...`) at the end of the network's row
3. Click **"Delete Network"**
   - Trial networks: deleted immediately, no charge
   - Active networks: access continues until billing cycle ends, then deleted

## Related Docs
- MSP Billing page (for license usage details)
- MSP Portal documentation