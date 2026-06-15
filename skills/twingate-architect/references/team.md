# Twingate Team Management

## Summary
The Team section covers management of Users, Groups, and Identity Provider (IdP) integrations in Twingate. Access to Resources is controlled through Group membership, with Users either added manually or synced via an IdP.

## Key Information
- **Users** are the entities that receive access to Resources
- **Groups** are the mechanism that links Users to Resources — all Users in a Group can access that Group's assigned Resources
- **Identity Providers** handle both user authentication and automatic group membership synchronization
- Users can be added manually or automatically via IdP sync

## Core Concepts

### Users
- Access to Resources is granted through Users
- Can be manually created or auto-synchronized from an Identity Provider

### Groups
- Group membership = Resource access entitlement
- All Users in a Group inherit access to all Resources assigned to that Group
- Primary access control mechanism in Twingate

### Identity Providers
- Dual function: manage authentication AND sync group membership
- Supported IdPs have dedicated configuration guides
- IdP sync automates User provisioning/deprovisioning

## Access Control Model
```
User → Group → Resource
```
A User must be a member of a Group that has the Resource assigned to gain access.

## Related Docs
- Users documentation
- Groups documentation
- Identity Provider configuration guides