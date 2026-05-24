# Twingate MSP Portal

## Summary
Twingate's MSP portal provides multi-tenant management for Managed Service Providers to create and manage Customer Networks with consolidated billing. Each Customer Network represents a full customer account with independent Resources, Connectors, and team members.

## Key Information
- Credit card required to create Customer Networks; each gets a **14-day free POC period**
- Consolidated monthly billing across all Customer Networks
- MSP Portal users ≠ Customer Network users — must be added separately to each
- Users can be added manually or via Identity Provider sync
- All Twingate URLs are **permanent and unique** — cannot be changed after creation

## Prerequisites
- Credit card on file
- MSP portal account (sign up at twingate.com/docs/msp)

## Configuration Values

| Setting | Notes |
|---|---|
| MSP Portal URL | Permanent; set at creation |
| Customer Network URL | Separate unique URL per customer |
| Billing cycle | Monthly, consolidated |
| Free trial | 14 days per Customer Network |

## URL Naming Convention
- Recommended: use `yourcompanymsp` or `yourcompanyportal` for MSP portal URL
- Reserve `yourcompany` URL for your own internal Twingate network

## Step-by-Step: Remove a Customer

1. Locate Customer Network row in portal
2. Click ellipses (`...`) at end of row
3. Choose removal method:
   - **Offboard Network** — access retained until end of billing cycle → downgrades to Starter tier, removed from MSP Network, billing stops
   - **Delete Network** — access retained until end of billing cycle → network permanently deleted, billing stops

## Gotchas
- **URLs cannot be changed** after creation — plan naming carefully upfront
- MSP Portal users have **no access** to Customer Networks by default; must be explicitly added to each network
- "Offboard" vs "Delete" are distinct: offboard preserves network at Starter tier; delete permanently removes it
- Billing continues until end of cycle regardless of offboard/delete action

## Related Docs
- [MSP Billing](https://www.twingate.com/docs/msp-billing)
- [Customer Networks](https://www.twingate.com/docs/customer-networks)
- Identity Provider sync (referenced but linked separately in Twingate docs)