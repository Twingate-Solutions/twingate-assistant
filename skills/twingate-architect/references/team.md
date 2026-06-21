# Twingate Team Management

## Page Title
Team — Users, Groups, and Identity Provider Management

## Summary
The Team section covers managing Users, Groups, and Identity Provider (IdP) integrations in Twingate. Users gain Resource access through Group membership, and provisioning can be manual or automated via IdP sync.

## Key Information
- **Users**: The fundamental unit of Resource access; created manually or auto-synced via IdP
- **Groups**: Determine Resource entitlements — all Users in a Group inherit access to that Group's assigned Resources
- **Identity Providers**: Enable both authentication and automated Group/User synchronization from an external IdP

## Core Concepts

### Users
- Can be added manually through the Twingate Admin Console
- Can be automatically provisioned/deprovisioned via IdP integration
- Resource access is ultimately user-level

### Groups
- Intermediary between Users and Resources
- Many-to-many: Users can belong to multiple Groups; Groups can have multiple Resources
- Access model: `User → Group → Resource`

### Identity Providers
- Serve dual purpose: authentication + user/group sync
- Existing IdP group membership can be mirrored into Twingate automatically
- Supported IdPs have dedicated configuration guides (linked from this page)

## Prerequisites
- Twingate Admin access to configure Team settings
- For IdP integration: valid IdP account with admin permissions to configure SAML/SCIM or equivalent

## Gotchas
- Users without Group membership cannot access any Resources — Group assignment is required for access
- IdP sync overrides manual group management; mixing manual and IdP-managed groups can cause unexpected behavior
- Removing a User from an IdP group will remove their Twingate Resource access if groups are synced

## Related Docs
- [Users](https://www.twingate.com/docs/users)
- [Groups](https://www.twingate.com/docs/groups)
- [Identity Provider Configuration Guides](https://www.twingate.com/docs/identity-providers)