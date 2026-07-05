# Twingate Team Management

## Summary
The Team section covers management of Users, Groups, and Identity Provider (IdP) integrations in Twingate. Access to Resources is controlled through Group membership, with Users either added manually or synced via IdP.

## Key Information
- **Users**: The fundamental unit for Resource access in Twingate
- **Groups**: Determine Resource entitlements — all Users in a Group inherit access to that Group's assigned Resources
- **Identity Providers**: Enable both authentication management and automatic Group/User synchronization from external IdPs

## Core Concepts

### Users
- Can be added **manually** or **automatically synchronized** via Identity Provider
- Resource access is ultimately granted at the User level

### Groups
- Membership-based access control model
- Resources are assigned to Groups, not individual Users
- All Users in a Group get access to all Resources assigned to that Group

### Identity Providers
- Dual function: manage **user authentication** + **sync group membership**
- Syncs existing group structure from the source IdP into Twingate

## Access Control Model
```
User → Group membership → Resource access
```
Users gain access to Resources by being members of Groups that have those Resources assigned.

## Related Docs
- [Users documentation](https://www.twingate.com/docs/users)
- [Groups documentation](https://www.twingate.com/docs/groups)
- [Identity Provider configuration guides](https://www.twingate.com/docs/identity-providers)

## Gotchas
- Access is Group-centric, not User-centric — Resources must be assigned to Groups, not directly to Users
- IdP sync affects both authentication and group membership; changes in the IdP propagate to Twingate