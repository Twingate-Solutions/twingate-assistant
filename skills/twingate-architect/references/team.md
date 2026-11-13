---
source: https://www.twingate.com/docs/team
type: docs
fetched: 2026-11-13
source_version: 940f64d95a0819114ef16f0968037aa2402a5b698aa7eb15276da6874b0d86e1
trust: official
---

# Team

## Summary
The Team section of the Twingate docs covers managing the people and access structure of a Twingate network: Users, Groups, and Identity Provider (IdP) integrations. Access to Resources is granted to Users, typically via Group membership, and users and groups can be added manually or synced from an IdP. This page is an overview and links to detailed pages.

## Key Information
- **Users**: The entities that ultimately receive access to Resources. They can be added manually or synchronized automatically from an Identity Provider.
- **Groups**: Group membership determines which Resources a User can access. All Users in a Group get access to every Resource assigned to that Group.
- **Identity Providers**: Twingate integrates with several IdPs to handle user authentication and to automatically sync existing group membership from the source IdP.
- Page last updated roughly 5 months before it was scraped.

## Prerequisites
None stated on this page. Detailed pages may require a Twingate account with admin permissions and, for IdP sync, an account with a supported IdP.

## Step-by-Step
Not applicable. This page is a landing and overview page. Specific procedures are in the linked pages for Users, Groups, and IdP configuration guides.

## Configuration Values
None listed on this page (no env vars, CLI flags, or API parameters).

## Gotchas
- Access is assigned via Resources-to-Group mapping, so changes to Group membership change Resource access for all members.
- When using IdP sync, group membership originates in the source IdP. Manual changes to synced groups may conflict with or be overwritten by sync, so verify behavior in the Groups and IdP guides.
- The overview doesn't say which IdPs are supported. Check the IdP configuration guides for the current list.

## Related Docs
- Users (Learn more about Users)
- Groups (Learn more about Groups)
- Identity Provider configuration guides
- Resources (referenced for access assignment)