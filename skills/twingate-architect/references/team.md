# Twingate Team Management

## Summary
The Team section covers management of Users, Groups, and Identity Provider (IdP) integrations in Twingate. Access to Resources is controlled through Group membership, with Users either manually added or synced via IdP.

## Key Information
- **Users** are the entities that receive access to Resources
- **Groups** are the mechanism that links Users to Resources — all Users in a Group inherit access to that Group's assigned Resources
- **Identity Providers** serve dual purpose: user authentication AND automatic group membership synchronization
- Users can be added manually or automatically via IdP sync

## Core Concepts

### Users
- Fundamental access unit in Twingate
- Manual addition or automatic IdP synchronization supported

### Groups
- Bridge between Users and Resources
- Resource access is granted at the Group level, not individual User level
- All Users within a Group get access to all Resources assigned to that Group

### Identity Providers
- Manages user authentication
- Syncs existing group membership from source IdP
- Multiple IdP integrations supported

## Prerequisites
- Twingate account with admin access
- For IdP integration: existing Identity Provider with supported configuration

## Related Docs
- [Users documentation](https://www.twingate.com/docs/users)
- [Groups documentation](https://www.twingate.com/docs/groups)
- [Identity Provider configuration guides](https://www.twingate.com/docs/identity-providers)

## Gotchas
- Access control is Group-centric: assign Resources to Groups, not directly to Users
- IdP sync affects both authentication and group membership — changes in IdP propagate to Twingate access automatically
- No direct User-to-Resource assignment; must go through Groups