---
source: https://www.twingate.com/docs/admins
type: docs
fetched: 2026-08-05
source_version: 83b3e31c2133e89bb92a979318fbd9bcea52b609b26fd6caad4a0e870117a9c9
---

# Twingate Admins

## Summary
Twingate supports five admin roles with varying access levels to the Admin Console. The network creator is the default admin; additional admins must be manually designated. All admin users consume a license seat.

## Key Information
- Five distinct admin roles with granular read/write permissions
- Admin Console URL: `https://your-subdomain.twingate.com`
- Non-Admin roles display a badge next to the Twingate logo indicating their role
- Blocked actions show an error message to restricted admins

## Admin Roles Reference

| Role | Write Access | Read Access |
|------|-------------|-------------|
| **Admin** | Entire Admin Console | Entire Admin Console |
| **DevOps** | Network tab (Resources, Connectors, Remote Networks, Groups on Resources, Access Requests) | All tabs except Secure DNS and Client Configuration in Internet Security |
| **Support** | None | Entire Admin Console |
| **Access Reviewer** | Access Requests page only | Access Requests page only |
| **Billing** | Billing Settings (plan changes, payment) | Billing page only |

## Prerequisites
- Must be an Admin role to assign roles to other users
- Billing role requires self-serve Billing page (not available for invoice-billed tenants, MSP portal tenants, or MSP subtenants)

## Step-by-Step: Assign Admin Role
1. Navigate to Admin Console → **Users** tab
2. Click the target user's name
3. Select **Manage Role**
4. Choose the desired role

## Gotchas
- **License consumption**: Admin users count against your license like regular users — factor this into seat planning
- **Billing role availability**: Not available on invoice-billed accounts or MSP-related tenants
- **Default state**: Only the network creator has admin access by default; no other users are admins until explicitly assigned
- **DevOps read restriction**: DevOps role cannot read Secure DNS or Client Configuration sections under Internet Security
- **Access Reviewer scope**: Extremely limited — read and write restricted to Access Requests page only; not suitable for general monitoring

## Configuration Values
- Admin Console login URL: `https://<your-subdomain>.twingate.com`
- Authentication: Uses configured identity provider or supported social identities

## Related Docs
- Access Requests management
- Remote Networks and Connectors configuration
- Internet Security / Secure DNS settings
- Billing and plan management