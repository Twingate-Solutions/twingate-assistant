---
source: https://www.twingate.com/docs/msp
type: docs
fetched: 2026-08-14
source_version: 07abe0dde2902191127f42b75c975614f75434770f385724b9096f41a9813a85
---

# Twingate MSP Portal

## Summary
Twingate's MSP portal provides a multi-tenant management interface for managed service providers to create and manage Customer Networks and consolidated billing. Each Customer Network represents a full customer account with isolated resources, connectors, and team members.

## Key Information
- MSP Portal is separate from Customer Networks; users added to the portal don't automatically get Customer Network access
- Each new Customer Network gets a 14-day free POC period before billing starts
- Consolidated monthly billing across all Customer Networks
- Users can be added manually or synced via Identity Provider
- All Twingate URLs are globally unique and **cannot be changed after creation**

## Prerequisites
- Credit card required to create Customer Networks (not charged until after 14-day trial)
- Sign up at Twingate MSP portal signup page

## URL Naming Convention
- MSP Portal URL recommendation: `yourcompanymsp` or `yourcompanyportal`
- Reserves `yourcompany` for your own internal Twingate Network
- Plan URL names carefully — permanent after creation

## Step-by-Step: Removing a Customer

**Offboard Network:**
1. Click ellipses at end of Customer Network row
2. Select "Offboard Network"
3. Customer retains access until end of billing cycle
4. Network downgrades to Starter tier and is removed from MSP portal
5. No further charges after billing cycle ends

**Delete Network:**
1. Click ellipses at end of Customer Network row
2. Select "Delete Network"
3. Customer retains access until end of billing cycle
4. Network is permanently deleted after billing cycle ends
5. No further charges after billing cycle ends

## Configuration Notes
| Feature | Behavior |
|---|---|
| User access scope | MSP Portal users ≠ Customer Network users (must add separately) |
| Billing | Consolidated monthly; per Customer Network |
| Trial period | 14 days per new Customer Network |
| URL changes | Not supported after creation |

## Gotchas
- MSP Portal admins must be explicitly added to each Customer Network they need to access — portal access does not cascade
- "Offboard" vs "Delete" both retain access until billing cycle end, but Offboard downgrades to Starter tier rather than full deletion
- URL uniqueness is global across all Twingate networks, not just your MSP portal

## Related Docs
- MSP Billing page (billing history, payment methods, billing address)
- Customer Networks page (create/delete networks, assign admins)
- Identity Provider setup (for automatic user sync to MSP Portal)