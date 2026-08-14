---
source: https://www.twingate.com/docs/customer-networks
type: docs
fetched: 2026-08-14
source_version: ae18f250c55a5a4eb36fa818434efd4c85b8f791f80b575792ef882a77843b61
---

# Customer Networks (MSP Portal)

## Summary
Customer Networks are Twingate network instances managed through an MSP Portal. MSPs create and manage these networks on behalf of their customers, with each network having its own Admin Console and user-facing Client experience.

## Key Information
- Each Customer Network gets its own unique URL (subdomain), Admin Console, and user base
- Network status lifecycle: **POC** (14-day trial) → **Active** (auto-promotion after trial) → **Non-renewing** (scheduled deletion at billing cycle end)
- License count = Users + Service Accounts − Admins
- Deleted networks remain accessible until end of billing cycle; no refunds issued
- Deleted networks are hidden from the Customer Networks tab in the MSP Portal

## Prerequisites
- Active MSP Portal account
- Unique subdomain not used by any other Twingate network (MSP Portal, Customer Network, or standalone)

## Required Fields for New Customer Network

| Attribute | Description |
|---|---|
| Customer Network Name | Display name in Admin Console and Client |
| Customer Network URL | Unique subdomain |
| Admin Email | Initial admin user |
| Business Legal Name | Customer org name |
| Business Address | Customer address |
| Business URL | Customer website |
| Point of Contact | POC at customer company |

## Gotchas
- **URLs must be globally unique** across all Twingate network types — recommended pattern: `yourcompanymsp` (MSP Portal) + `yourcompany` (Customer Network)
- **No conversion path**: MSP Customer Networks cannot be converted to standalone Twingate Networks
- **Trial cancellation** via "Delete Network" is immediate and permanent — no billing charges incurred
- **Non-trial deletion** schedules removal at billing cycle end — access continues until then
- **No user notifications** on deletion — only a banner in the Admin Console; end users receive nothing
- **No refunds** for deleted Customer Networks

## Actions
- **Delete trial network**: Ellipses menu → "Delete Network" (immediate)
- **Delete active network**: Ellipses menu → "Delete Network" (takes effect at billing cycle end)

## Related Docs
- [MSP Billing](https://www.twingate.com/docs/msp-billing) — license counting details