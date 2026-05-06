# Twingate MSP Portal

## Summary
Twingate's MSP portal provides multi-tenant management for Customer Networks and consolidated billing. MSPs can create, manage, and offboard customer accounts through a single portal interface. Each Customer Network gets a 14-day free POC period before billing begins.

## Key Information
- Multi-tenant portal manages multiple Customer Networks from one interface
- Consolidated monthly billing across all Customer Networks
- Users added to MSP Portal only access the portal itself — must be separately added to each Customer Network
- Portal URL cannot be changed after creation

## Prerequisites
- Credit card required to create Customer Networks
- Sign up at Twingate's MSP portal signup page

## URL Naming Convention
- MSP Portal URL and all Customer Network URLs must be globally unique
- **Recommended pattern**: Use `yourcompanymsp` or `yourcompanyportal` for the MSP portal URL
- This reserves `yourcompany` for your own company's Twingate Network (as standalone or Customer Network)

## Step-by-Step: Key Operations

### Adding Users
1. Add manually via portal UI, or
2. Sync automatically via Identity Provider integration
3. Add users to specific Customer Networks separately if access needed

### Removing Customers
- **Offboard Network**: Customer retains access until end of billing cycle → downgraded to Starter tier → removed from MSP Network (no deletion)
- **Delete Network**: Customer retains access until end of billing cycle → account permanently deleted

Both options: accessed via ellipses (`...`) menu on Customer Network row → select option

## Configuration Values
None (UI-driven, no CLI/API params documented on this page)

## Gotchas
- **URL is permanent** — cannot be changed after creation; plan naming carefully before setup
- MSP Portal users ≠ Customer Network users; access must be granted at each level independently
- "Offboard" preserves data on Starter tier; "Delete" permanently removes the network
- Credit card required upfront, but 14-day free POC per Customer Network before charges apply
- Billing cycle end determines actual termination, not the date you initiate offboard/delete

## Related Docs
- MSP Billing page (consolidated billing details)
- Customer Networks page (creating, deleting, assigning admins)
- Identity Provider sync documentation