# Customer Networks (Twingate MSP)

## Summary
Customer Networks are Twingate network instances managed through an MSP Portal. Each network has its own Admin Console, URL, and user base. MSP partners create and manage these on behalf of their customers.

## Key Information
- Each Customer Network gets its own Admin Console and Client-visible name
- License usage = total Users + Service Accounts − number of admins
- Networks start with a 14-day free trial (POC status), then auto-convert to Active
- Deleted Customer Networks remain accessible until end of billing cycle
- Deleted networks do not appear in the Customer Networks tab

## Prerequisites
- Active MSP Portal account
- Unique subdomain for each network (MSP Portal and Customer Networks cannot share URLs)

## Required Attributes for New Network

| Attribute | Description |
|-----------|-------------|
| Customer Network Name | Visible in Admin Console and Client |
| Customer Network URL | Unique subdomain |
| Admin Email | Initial admin user |
| Business Legal Name | Customer org name |
| Business Address | Customer address |
| Business URL | Customer website |
| Point of Contact | Customer contact person |

## Network Status Values
- **POC** – Within initial 14-day free trial
- **Active** – On active subscription (auto-assigned after trial)
- **Non-renewing** – Scheduled for deletion at end of billing cycle

## Configuration Values
- URL uniqueness required across all Twingate network types (MSP Portal, Customer Networks, standalone networks)
- Recommended naming: `yourcompanymsp` (MSP Portal) / `yourcompany` (Customer Network)

## Step-by-Step: Delete a Network
1. Navigate to Customer Networks tab in MSP Portal
2. Click ellipses (`...`) at end of target network's row
3. Click **Delete Network**
   - **Trial networks**: Deleted immediately, no charge
   - **Active networks**: Accessible until end of billing cycle, then deleted

## Gotchas
- MSP Customer Networks **cannot** be converted to standalone Twingate Networks
- **No refunds** issued for deleted Customer Networks
- End users receive **no notifications** when a network is deleted — only a banner in the Admin Console indicates pending deletion
- Admins are excluded from license count; regular users and Service Accounts are billed

## Related Docs
- MSP Billing page (for license management details)
- MSP Portal documentation