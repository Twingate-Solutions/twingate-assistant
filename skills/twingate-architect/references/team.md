# Twingate Team Management

## Page Title
Team — Users, Groups, and Identity Provider Management

## Summary
The Team section covers managing Users, Groups, and Identity Provider (IdP) integrations in Twingate. Resource access is controlled through Group membership, with Users either added manually or synced via IdP.

## Key Information
- **Users** are the primary entities granted access to Resources
- **Groups** are the mechanism linking Users to Resources — all Users in a Group inherit access to that Group's Resources
- **Identity Providers** serve dual purpose: user authentication AND automatic group membership synchronization
- Users can be provisioned manually or automatically via IdP sync

## Core Concepts

| Concept | Role |
|---|---|
| Users | Entities that access Resources |
| Groups | Access control boundary — maps Users to Resources |
| Identity Provider | Auth source + automated user/group sync |

## Access Control Model
```
User → Group membership → Resource access
```
- A User must belong to a Group
- That Group must be assigned to a Resource
- User gains access only when both conditions are met

## Identity Provider Integration
- Supports multiple IdP integrations
- Syncs existing group membership from source IdP (no manual re-mapping required)
- Manages authentication in addition to provisioning

## Prerequisites
- Twingate account with admin access
- For IdP integration: existing IdP with configured groups

## Configuration Options
- **Manual**: Add users individually through the Team UI
- **Automated**: Connect an IdP to sync users and groups automatically

## Gotchas
- Group membership is the sole determinant of Resource entitlement — Users without Group membership cannot access Resources
- IdP sync reflects source IdP group structure; changes in IdP propagate to Twingate access

## Related Docs
- [Users](https://www.twingate.com/docs/users)
- [Groups](https://www.twingate.com/docs/groups)
- [Identity Provider Configuration Guides](https://www.twingate.com/docs/identity-providers)