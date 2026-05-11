# Twingate MSP Portal

## Summary
Twingate's MSP Portal provides a multi-tenant management interface for Managed Service Providers to manage Customer Networks and consolidated billing. Each Customer Network represents a full customer account with its own Resources, Connectors, and team members. MSP Portal users require separate explicit access grants to each Customer Network.

## Key Information
- Sign-up requires credit card; each new Customer Network gets a **14-day free POC period**
- MSP Portal URLs are **permanent and cannot be changed after creation**
- Users added to the MSP Portal do **not** automatically get access to Customer Networks — must be added separately to each
- Consolidated monthly billing across all Customer Networks
- Users can be added manually or via Identity Provider sync

## Prerequisites
- Credit card required to create Customer Networks
- Unique URL selection at signup (plan carefully — cannot be changed)

## URL Naming Convention
| Use Case | Recommended Pattern |
|----------|-------------------|
| MSP Portal | `yourcompanymsp` or `yourcompanyportal` |
| Your own company network | `yourcompany` (kept free) |

## Customer Network Management

**Create/Delete:** Managed through the MSP Portal dashboard.

**Offboard vs. Delete distinction:**
- **Offboard Network**: Customer retains access until end of billing cycle → then downgraded to Starter tier and removed from MSP Network; billing stops
- **Delete Network**: Customer retains access until end of billing cycle → then permanently deleted; billing stops

## Configuration Notes
- Identity Provider sync available for MSP Portal user management
- Billing details (history, address, payment methods) managed within the portal

## Gotchas
- URL uniqueness is global across all Twingate networks — reserve your company's primary URL before creating the MSP portal URL
- MSP Portal access ≠ Customer Network access; must grant users access to each network independently
- Free POC period is 14 days per Customer Network; credit card charged after expiration
- "Offboard" leaves the network as Starter tier (not deleted); use "Delete" if full removal is intended

## Related Docs
- MSP Billing page
- Customer Networks page
- Identity Provider integration docs
- MSP Portal signup