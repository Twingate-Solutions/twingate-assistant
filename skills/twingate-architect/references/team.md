# Team Management – Twingate

## Summary
The Team section covers management of Users, Groups, and Identity Provider (IdP) integrations in Twingate. Access to Resources is controlled through Group membership, and Users can be managed manually or synced via an IdP.

## Key Information
- **Users**: The fundamental entity for Resource access; can be added manually or auto-synced from an IdP
- **Groups**: Define access entitlements — all Users in a Group inherit access to that Group's assigned Resources
- **Identity Providers**: Used for both user authentication and automatic group membership synchronization

## Core Concepts

| Concept | Role |
|---|---|
| Users | Granted access to Resources |
| Groups | Link Users to Resources |
| Identity Providers | Authenticate users + sync group membership |

## Access Control Model
- Resources are assigned to **Groups**, not directly to Users
- Users gain Resource access by being members of a Group that has that Resource assigned
- Group membership can be managed manually or synced automatically from an external IdP

## Identity Provider Integration
- Supports multiple IdP integrations
- Handles two functions: **authentication** and **group sync**
- Group membership from the source IdP is automatically replicated into Twingate

## Related Docs
- [Users](https://www.twingate.com/docs/users)
- [Groups](https://www.twingate.com/docs/groups)
- [Identity Provider Configuration Guides](https://www.twingate.com/docs/identity-providers)