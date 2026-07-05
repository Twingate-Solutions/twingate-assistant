# Twingate MSP Portal

## Summary
Twingate's MSP portal provides multi-tenant management for Managed Service Providers to handle multiple customer networks and consolidated billing. Each customer network is an isolated account containing all resources, connectors, and team members. MSPs manage billing centrally while customer access is controlled per-network.

## Key Information
- MSP portal requires credit card on signup; each Customer Network gets 14-day free POC period
- URLs are permanent and globally unique — cannot be changed after creation
- MSP portal users ≠ Customer Network users; access must be granted separately per network
- Users can be added manually or via Identity Provider sync
- Consolidated monthly billing across all Customer Networks

## Prerequisites
- Credit card required to create Customer Networks
- MSP portal account (sign up at twingate.com/docs/msp)

## URL Naming Strategy
- MSP Portal URL: use `yourcompanymsp` or `yourcompanyportal`
- Reserves `yourcompany` for your own internal Twingate network
- **URLs cannot be changed after creation** — plan carefully

## Customer Network Management
- Create/delete Customer Networks from the portal
- Assign admins to Customer Networks through the portal
- Each network is fully isolated (resources, connectors, team members)

## Offboarding Customers (Two Options)

| Action | Effect | Billing |
|---|---|---|
| **Offboard Network** | Access until end of billing cycle → downgraded to Starter tier, removed from MSP | No longer charged after cycle ends |
| **Delete Network** | Access until end of billing cycle → network deleted | No longer charged after cycle ends |

*Access via ellipsis menu (⋯) at end of customer network row.*

## Gotchas
- Users added to the MSP portal do **not** automatically get access to any Customer Network — must be added individually to each network
- 14-day free POC applies per Customer Network, but credit card is required upfront
- URL uniqueness is global across all Twingate networks (MSP portals, customer networks, standalone networks)
- Offboarded networks revert to Starter tier (not deleted); deleted networks are permanently removed — choose intentionally

## Related Docs
- [MSP Billing](https://www.twingate.com/docs/msp-billing)
- [Customer Networks](https://www.twingate.com/docs/customer-networks)
- Identity Provider sync (for user management)