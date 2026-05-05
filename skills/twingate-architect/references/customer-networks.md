# Customer Networks (MSP Portal)

## Summary
Customer Networks are Twingate networks managed through an MSP Portal. MSPs create and manage these networks on behalf of customers, with each network having its own Admin Console and user-facing Client experience. Networks follow a trial → active → non-renewing lifecycle.

## Key Information
- Each Customer Network has its own unique subdomain URL, Admin Console, and user base
- Networks display name, URL, user count, service account count, plan, and status in MSP Portal
- License usage = total Users + Service Accounts − number of admins
- Deleted networks remain accessible until end of billing cycle; no refunds issued
- Deleted networks are hidden from the Customer Networks tab

## Prerequisites
- Active MSP Portal account
- Unique subdomain not used by any other Twingate network (MSP, Customer, or standalone)

## Required Attributes for New Customer Network

| Attribute | Description |
|-----------|-------------|
| Customer Network Name | Visible in Admin Console and user Clients |
| Customer Network URL | Unique subdomain |
| Admin Email | Initial admin user for the network |
| Business Legal Name | Customer organization name |
| Business Address | Customer address |
| Business URL | Customer website |
| Point of Contact | Contact person at customer company |

## Network Status Values
- **POC** – Within initial 14-day free trial
- **Active** – On active subscription (auto-transitions from trial)
- **Non-renewing** – Scheduled for deletion at end of billing cycle

## Gotchas
- MSP Portal URL and Customer Network URL **must be unique** — use distinct subdomains (e.g., `yourcompanymsp` vs. `yourcompany`)
- Customer Networks **cannot be converted** to standalone Twingate networks
- Canceling a trial via "Delete Network" is **immediate** — no end-of-cycle grace period
- Deleting an active network is **not immediate** — access continues until billing cycle ends
- End users receive **no notification** of deletion; only an Admin Console banner is shown
- **No refunds** for deleted Customer Networks

## Related Docs
- MSP Billing page (license and billing details)
- MSP Portal documentation