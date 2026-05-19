# Twingate Team Management

## Page Title
Team — Users, Groups, and Identity Provider Management

## Summary
The Team section covers how to manage Users, Groups, and Identity Provider (IdP) integrations in Twingate. Users gain Resource access through Group membership, and both can be managed manually or synced automatically via an IdP.

## Key Information
- **Users**: The fundamental entity for Resource access; can be added manually or synced via IdP
- **Groups**: Determine Resource entitlements — all Users in a Group inherit access to that Group's assigned Resources
- **Identity Providers**: Used for both authentication and automatic group/user synchronization from external directories

## Core Concepts

### Users
- Access to Resources is granted at the User level
- Two provisioning methods: manual addition or automatic IdP synchronization

### Groups
- Group membership is the mechanism that links Users to Resources
- All members of a Group get access to all Resources assigned to that Group
- Many-to-many relationship: Users can belong to multiple Groups; Groups can have multiple Resources

### Identity Providers
- Serve dual purpose: user authentication + group membership synchronization
- Eliminates manual user management by pulling existing directory structure into Twingate

## Configuration Values
- No direct CLI flags or API params documented on this page — see linked sub-pages for specifics

## Gotchas
- Resource access is **Group-scoped**, not User-scoped directly — assigning a Resource means assigning it to a Group, not an individual User
- If using IdP sync, group membership changes in the source IdP propagate to Twingate automatically; manual overrides may be overwritten on sync

## Related Docs
- [Users](https://www.twingate.com/docs/users)
- [Groups](https://www.twingate.com/docs/groups)
- [Identity Provider Configuration Guides](https://www.twingate.com/docs/identity-providers)