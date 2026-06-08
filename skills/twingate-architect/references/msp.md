# Twingate MSP Portal

## Summary
Twingate's MSP portal provides multi-tenant management for Managed Service Providers to handle multiple customer networks and consolidated billing. Each customer network is an isolated account containing all resources, connectors, and team members. A 14-day free POC period applies to each new customer network before billing begins.

## Key Information
- Multi-tenant portal separates MSP administration from individual customer networks
- Credit card required at signup, but no charges during 14-day POC per customer network
- Consolidated monthly billing across all customer networks
- MSP portal users ≠ customer network users — access must be granted separately to each
- Users can be added manually or via Identity Provider sync
- URLs are **permanent** — cannot be changed after creation

## Prerequisites
- Credit card for MSP portal signup
- Unique URL chosen for MSP portal (distinct from any customer network URLs)

## Step-by-Step

### Initial Setup
1. Sign up at Twingate MSP portal signup page
2. Choose MSP portal URL (recommended pattern: `yourcompanymsp` or `yourcompanyportal`)
3. Add payment method

### Adding Users
1. Add users manually via portal UI **or** configure Identity Provider sync
2. For customer network access, add users separately within each customer network

### Offboarding a Customer
1. Click ellipses (`...`) at end of customer network row
2. Choose removal option:
   - **Offboard Network** — access continues until billing cycle ends, then downgraded to Starter tier and removed from MSP
   - **Delete Network** — access continues until billing cycle ends, then permanently deleted

## Configuration Values
| Item | Notes |
|------|-------|
| MSP Portal URL | Set at creation; immutable |
| Customer Network URL | Must be globally unique across all Twingate |
| POC Period | 14 days per customer network |
| Post-offboard tier | Starter (Offboard path only) |

## Gotchas
- **URLs cannot be changed** after creation — plan naming convention carefully before signup
- MSP portal URL and customer network URLs must all be globally unique — reserve `yourcompany` separately if needed for your own network
- Users added to MSP portal do **not** automatically get access to any customer network
- Both offboard and delete options still allow access until end of billing cycle — neither is immediate termination
- "Offboard" leaves the network intact at Starter tier; "Delete" destroys it permanently

## Related Docs
- MSP Billing page (linked in portal docs)
- Customer Networks page (linked in portal docs)
- Identity Provider configuration (for automated user sync)