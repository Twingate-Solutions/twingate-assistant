# Customer Networks (MSP Portal)

## Summary
Customer Networks are tenant instances managed through a Twingate MSP Portal. Each network has its own Admin Console, URL, and user base. MSP partners create and manage these networks on behalf of their customers.

## Key Information
- Each Customer Network gets its own unique subdomain URL and Admin Console
- Networks start with a 14-day free trial (POC status), then auto-move to Active
- License count = Users + Service Accounts minus admins
- Deleted networks remain accessible until end of billing cycle; no refunds issued
- Deleted networks are not shown in the Customer Networks tab
- MSP Customer Networks **cannot** be converted to standalone Twingate Networks

## Prerequisites
- Active MSP Portal account
- Unique subdomain (cannot reuse MSP Portal URL)

## Required Attributes for New Customer Network

| Attribute | Description |
|-----------|-------------|
| Customer Network Name | Displayed in Admin Console and user Clients |
| Customer Network URL | Unique subdomain for network access |
| Admin Email | Initial admin user email address |
| Business Legal Name | Customer organization name |
| Business Address | Customer physical address |
| Business URL | Customer website URL |
| Point of Contact | POC at customer company |

## Network Status Values
- **POC** — Within initial 14-day free trial
- **Active** — On active subscription (auto-assigned after trial)
- **Non-renewing** — Scheduled for deletion at end of billing cycle

## Operational Procedures

**Cancel a trial network:**
1. Locate network row in Customer Networks tab
2. Click ellipses (`...`) at end of row
3. Click "Delete Network"
4. Immediate deletion; no charge incurred

**Delete an active network:**
1. Locate network row in Customer Networks tab
2. Click ellipses (`...`) at end of row
3. Click "Delete Network"
4. Network remains accessible until billing cycle ends, then deleted

## Gotchas
- MSP Portal URL and Customer Network URL must be **different** (all Twingate URLs globally unique); convention: `yourcompanymsp` for portal, `yourcompany` for customer network
- End users receive **no notification** when a network is deleted; only a banner appears in the Admin Console
- No refunds for deleted Customer Networks regardless of timing
- Trial cancellation is immediate and irreversible
- Customer Network is permanently tied to MSP Portal — no standalone conversion path

## Related Docs
- MSP Billing page (license calculation details)
- MSP Portal documentation
- Standalone Twingate Network setup