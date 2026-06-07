# Twingate Team Management

## Summary
The Team section manages Users, Groups, and Identity Provider integrations in Twingate. Access to Resources is controlled through Group membership, with Users assigned to Groups that have specific Resource permissions. Users can be managed manually or synced automatically via an IdP.

## Key Information
- **Users**: The fundamental access entity; can be added manually or auto-synced via Identity Provider
- **Groups**: Determine Resource access — all Users in a Group inherit access to that Group's assigned Resources
- **Identity Providers (IdP)**: Dual purpose — handle user authentication AND sync existing group membership from the source IdP

## Core Concepts

### Access Model
```
User → Group → Resource
```
- Users belong to Groups
- Groups are assigned Resources
- Users access Resources through Group membership

### User Management Options
- **Manual**: Add users directly in Twingate
- **Automated**: Sync users from a connected Identity Provider

### Identity Provider Capabilities
- User authentication
- Automatic group membership synchronization from source IdP

## Supported Identity Providers
*(See linked IdP configuration guides for full list)*

## Related Docs
- [Users documentation](#)
- [Groups documentation](#)
- [Identity Provider configuration guides](#)

## Gotchas
- Group membership is the sole mechanism for Resource entitlement — Users without Group membership cannot access Resources
- IdP sync affects both authentication and group membership; changes in source IdP propagate to Twingate
- Manual user management and IdP sync can conflict; establish one source of truth for user/group management