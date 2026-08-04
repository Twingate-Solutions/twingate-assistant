# Team Management

## Summary
The Team section in Twingate manages Users, Groups, and Identity Provider (IdP) integrations. Users gain access to Resources through Group membership, and Groups can be populated manually or synced from an external IdP.

## Key Information
- **Users** are the entities that access Resources; can be added manually or auto-synced via IdP
- **Groups** are the access control mechanism — Group membership determines which Resources a User can access
- **Identity Providers** serve dual purpose: user authentication AND automatic group membership synchronization
- All Users within a Group inherit access to all Resources assigned to that Group

## Core Concepts

| Concept | Role |
|---|---|
| Users | Principals that access Resources |
| Groups | Access control boundary linking Users to Resources |
| Identity Providers | Auth source + directory sync |

## Access Control Model
```
User → Group Membership → Resource Access
```
- Users must be in a Group
- Groups must be assigned to Resources
- No direct User-to-Resource assignment (Group is the intermediary)

## Identity Provider Integration
- Supports multiple IdP integrations
- IdP handles: (1) user authentication, (2) group sync
- Existing IdP group membership carries over to Twingate automatically when synced

## Gotchas
- Users not in any Group have no Resource access
- Manual user management and IdP sync can coexist, but IdP-synced users/groups may have limitations on manual edits
- Group membership changes in IdP propagate to Twingate (sync-dependent latency)

## Related Docs
- [Users](https://www.twingate.com/docs/users)
- [Groups](https://www.twingate.com/docs/groups)
- [Identity Provider Configuration Guides](https://www.twingate.com/docs/identity-providers)