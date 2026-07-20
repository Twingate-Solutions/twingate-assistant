# Twingate Team Management

## Page Title
Team — Users, Groups, and Identity Providers

## Summary
The Team section covers how to manage Users, Groups, and Identity Provider (IdP) integrations in Twingate. Access to Resources is controlled through Group membership, with Users either added manually or synced automatically via an IdP.

## Key Information
- **Users**: The fundamental entity for Resource access; can be manually added or auto-synced from an IdP
- **Groups**: Determine Resource access entitlements; all Users in a Group inherit access to that Group's assigned Resources
- **Identity Providers**: Used for both authentication and automatic Group/User synchronization from the source IdP

## Core Concepts

### Access Model
```
User → Group membership → Resource access
```
- Users must belong to a Group to access Resources
- Group assignment drives all Resource entitlement
- No direct User-to-Resource assignment (must go through Groups)

### User Management Options
| Method | Use Case |
|--------|----------|
| Manual | Small teams, no IdP |
| IdP Sync | Automated provisioning from existing directory |

### Identity Provider Capabilities
- Handles **user authentication**
- Syncs **group membership** from source IdP to Twingate
- Eliminates manual User/Group management when configured

## Prerequisites
- Admin access to Twingate Admin Console
- For IdP integration: existing IdP with SCIM/SSO support (refer to specific IdP guides)

## Gotchas
- Users without Group membership cannot access any Resources — Group assignment is required
- IdP sync mirrors source IdP groups; changes must be made in the IdP, not Twingate, when sync is active
- Both authentication and provisioning are handled by IdP integration (not independently configurable per this page)

## Related Docs
- [Users documentation](https://www.twingate.com/docs/users)
- [Groups documentation](https://www.twingate.com/docs/groups)
- [Identity Provider configuration guides](https://www.twingate.com/docs/identity-provider-guides)