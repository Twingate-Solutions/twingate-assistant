# Customer Networks (Twingate MSP)

## Summary
Customer Networks are Twingate network instances managed through an MSP Portal. Each network has its own Admin Console, URL, and user base. MSP partners create and manage these on behalf of their customers.

## Key Information
- Each Customer Network gets its own unique subdomain URL and Admin Console
- Networks are visible to end users in their Twingate Client
- MSP Portal dashboard shows: name, URL, user count, service account count, plan, and status
- License usage = (Users + Service Accounts) − number of admins

## Network Status Values
| Status | Meaning |
|--------|---------|
| **POC** | Within initial 14-day free trial |
| **Active** | On active subscription (auto-transitions from POC) |
| **Non-renewing** | Scheduled for deletion at end of billing cycle |

## Required Fields for New Network
- **Customer Network Name** – displayed in Admin Console and Client
- **Customer Network URL** – unique subdomain
- **Admin** – initial admin email address
- **Business Legal Name**
- **Business Address**
- **Business URL**
- **Point of Contact**

## Configuration Values
- All Twingate URLs (MSP Portal, Customer Networks, standalone networks) must be **globally unique**
- Recommended naming convention: `yourcompanymsp` (MSP Portal) / `yourcompany` (Customer Network)

## Deletion Behavior
- **Trial cancellation**: Ellipsis menu → "Delete Network" → **immediate** deletion; no charge
- **Active network deletion**: Ellipsis menu → "Delete Network" → access retained until end of billing cycle, then deleted
- Deleted networks are **not shown** in the Customer Networks tab
- **No refunds** issued for deleted networks

## Gotchas
- MSP Customer Networks **cannot be converted** to standalone Twingate Networks
- End users receive **no notifications** when a network is deleted; only a banner in the Admin Console indicates scheduled deletion
- Admins are **excluded** from license count calculations
- Billing cycle access continues after deletion request for active (non-trial) networks

## Related Docs
- [MSP Billing](https://www.twingate.com/docs/msp-billing) – license management details
- MSP Portal documentation