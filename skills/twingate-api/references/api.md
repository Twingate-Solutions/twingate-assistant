# Twingate GraphQL API Reference

## Summary
Twingate exposes a GraphQL API for managing all platform resources including networks, connectors, resources, groups, users, devices, and service accounts. All requests require an API token passed via header. The API supports full CRUD operations via queries and mutations with cursor-based pagination.

## Key Information
- **API Type**: GraphQL (queries + mutations)
- **Pagination**: Cursor-based using `before`, `after`, `first`, `last` arguments; responses include `pageInfo`, `edges`, `totalCount`
- **Mutation responses**: Always return `ok` (Boolean) and `error` (String) fields
- **IDs**: Base64-encoded (e.g., `"YWJjMTIzeHl6Nzg5"`)
- **Resource types**: AccessRequests, CertificateAuthorities, Connectors, Devices, DNS Filtering Profiles, Gateways, Groups, Remote Networks, Resources, Security Policies, Serial Numbers, Service Accounts, Users

## Prerequisites
- API token generated from the Twingate admin console
- Network name (subdomain) for your Twingate tenant

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Endpoint | `https://<network_name>.twingate.com/api/graphql/` |
| Auth Header | `X-API-KEY: <YOUR_TOKEN_HERE>` |

## Core Operations Reference

**Queries** (all support pagination filters):
- `resource(id)` / `resources(filter)` — fetch resources
- `remoteNetwork(id|name)` / `remoteNetworks(filter)`
- `connector(id)` / `connectors(filter)`
- `group(id)` / `groups(filter)`
- `user(id)` / `users(filter)`
- `device(id)` / `devices(filter)` + `devicePosture(id)`
- `serviceAccount(id)` / `serviceAccounts(filter)`
- `securityPolicy(id|name)` / `securityPolicies(filter)`
- `dnsFilteringProfile(id)` / `dnsFilteringProfiles`

**Mutations**:
- Resource: `resourceCreate`, `resourceUpdate`, `resourceDelete`, `resourceAccessAdd`, `resourceAccessRemove`, `resourceAccessSet`
- Group: `groupCreate`, `groupUpdate`, `groupDelete`
- Connector: `connectorCreate`, `connectorUpdate`, `connectorDelete`, `connectorGenerateTokens`
- Remote Network: `remoteNetworkCreate`, `remoteNetworkUpdate`, `remoteNetworkDelete`
- Device: `deviceUpdate`, `deviceBlock`, `deviceUnblock`, `deviceArchive`, `deviceUnarchive`
- Service Account: `serviceAccountCreate`, `serviceAccountDelete`, `serviceAccountKeyCreate`, `serviceAccountKeyRevoke`, `serviceAccountKeyDelete`
- Access Requests: `accessRequestApprove`, `accessRequestReject`

## Gotchas
- `groupUpdate` supports both full replacement (`resourceIds`, `userIds`) and incremental (`addedResourceIds`, `removedResourceIds`) — do not mix
- `resourceUpdate`: passing `null` for `securityPolicyId` resets to default policy; omitting it leaves unchanged
- `resourceUpdate`: passing `null` for `tags` removes all tags; omitting leaves unchanged; same pattern for `alias`
- `serviceAccountKeyCreate`: `expirationTime` is in days (0–365 inclusive); token is only returned at creation time
- `dnsFilteringProfile` queries return `null` when DNS filtering is not enabled
- `remoteNetwork` can be queried by either `id` OR `name` (both optional)
- `resourceAccessSet` **replaces all existing access** — use `resourceAccessAdd`/`Remove` for incremental changes

## Related Docs
- [Getting Started with the API](https://www.twingate.com/docs) (referenced in page intro)
- [Twingate Support](https://www.twingate.com/support)