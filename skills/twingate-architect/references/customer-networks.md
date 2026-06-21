# Customer Networks (MSP Portal)

## Summary
Customer Networks are Twingate network instances managed through an MSP Portal. MSPs create and manage these networks on behalf of their clients, with each network having its own Admin Console, users, and billing plan.

## Key Information
- Each Customer Network has its own unique URL (subdomain), Admin Console, and user base
- Networks start with a 14-day free trial (POC status), then auto-convert to Active
- License count = Users + Service Accounts minus admins
- Deleted networks remain accessible until end of billing cycle; no refunds issued
- Deleted networks do not appear in the Customer Networks tab
- MSP Customer Networks **cannot** be converted to standalone Twingate Networks

## Prerequisites
- Active MSP Portal account
- Unique subdomain not used by any other Twingate network (MSP Portal, Customer Network, or standalone)

## Required Attributes for New Customer Network

| Attribute | Description |
|---|---|
| Customer Network Name | Displayed in Admin Console and client apps |
| Customer Network URL | Unique subdomain |
| Admin Email | Initial admin user |
| Business Legal Name | Customer org name |
| Business Address | Customer address |
| Business URL | Customer website |
| Point of Contact | Customer contact person |

## Network Status Values
- **POC** — 14-day free trial period
- **Active** — Paid subscription (auto-assigned after trial)
- **Non-renewing** — Scheduled for deletion at end of billing cycle

## Operations

**Cancel trial:**
- Click ellipsis (⋯) on network row → "Delete Network"
- Immediate deletion; no charge incurred

**Delete active network:**
- Click ellipsis (⋯) on network row → "Delete Network"
- Access retained until end of billing cycle, then deleted

## Gotchas
- MSP Portal URL and Customer Network URLs must all be unique across the entire Twingate platform
- Recommended naming: `yourcompanymsp` for MSP Portal, `yourcompany` for the Customer Network
- End users receive **no notification** when a network is deleted — only a banner in the Admin Console signals pending deletion
- No refunds for deleted Customer Networks regardless of timing
- MSP-linked Customer Networks cannot be migrated to standalone networks

## Related Docs
- MSP Billing page (for license management details)
- MSP Portal documentation