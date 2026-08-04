# Twingate GraphQL API Reference

## Page Title
Twingate GraphQL API Reference

## Summary
Complete GraphQL schema reference for the Twingate API, covering queries and mutations for managing all Twingate resources. The API uses per-tenant endpoints with API key authentication. Supports CRUD operations for connectors, remote networks, resources, groups, users, devices, service accounts, and more.

## Key Information
- **API Type**: GraphQL (queries + mutations)
- **Endpoint pattern**: `https://<network-name>.twingate.com/api/graphql/`
- **Auth**: Header-based API key (`X-API-KEY`)
- **Pagination**: Cursor-based (`before`, `after`, `first`, `last`) on all list queries
- **List responses**: Return `pageInfo`, `edges`, and `totalCount`
- **Mutation responses**: Always return `ok` (Boolean) and `error` (String)

## Prerequisites
- Twingate account with admin access
- API token generated from the admin console
- Network name (subdomain) for your tenant

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Header | `X-API-KEY: <YOUR_TOKEN_HERE>` |
| Endpoint | `https://<network name>.twingate.com/api/graphql/` |

## Available Queries
- `accessRequest(id)` / `accessRequests(filter)`
- `certificateAuthority(id)` / `certificateAuthorities()`
- `connector(id)` / `connectors(filter)`
- `device(id)` / `devices(filter)` / `devicePosture(id)`
- `dnsFilteringProfile(id)` / `dnsFilteringProfiles()`
- `gateway(id)` / `gateways()`
- `group(id)` / `groups(filter)`
- `remoteNetwork(id|name)` / `remoteNetworks(filter)`
- `resource(id)` / `resources(filter)`
- `securityPolicy(id|name)` / `securityPolicies(filter)`
- `serialNumbers(filter)`
- `serviceAccount(id)` / `serviceAccounts(filter)` / `serviceAccountKey(id|name)`
- `user(id)` / `users(filter)`

## Available Mutations
- **Access Requests**: `accessRequestApprove`, `accessRequestReject`
- **Connectors**: `connectorCreate`, `connectorUpdate`, `connectorDelete`, `connectorGenerateTokens`
- **Devices**: `deviceArchive`, `deviceUnarchive`, `deviceBlock`, `deviceUnblock`, `deviceUpdate`
- **DNS Filtering**: `dnsFilteringProfileCreate`, `dnsFilteringProfileUpdate`, `dnsFilteringProfileDelete`
- **Gateways**: `gatewayCreate`, `gatewayUpdate`, `gatewayDelete`
- **Groups**: `groupCreate`, `groupUpdate`, `groupDelete`
- **Kubernetes Resources**: `kubernetesResourceCreate`, `kubernetesResourceUpdate`
- **Remote Networks**: `remoteNetworkCreate`, `remoteNetworkUpdate`, `remoteNetworkDelete`
- **Resources**: `resourceCreate`, `resourceUpdate`, `resourceDelete`, `resourceAccessAdd`, `resourceAccessRemove`, `resourceAccessSet`
- **Security Policies**: `securityPolicyUpdate`
- **Serial Numbers**: `serialNumbersCreate`, `serialNumbersDelete`
- **Service Accounts**: `serviceAccountCreate`, `serviceAccountDelete`, `serviceAccountKeyCreate`

## Gotchas
- `remoteNetwork` query accepts **either** `id` or `name` (both optional, use one)
- `groupUpdate` has both full-replace (`resourceIds`, `userIds`) and incremental (`addedResourceIds`, `removedResourceIds`) patterns — using both simultaneously may conflict
- `resourceUpdate`: passing `securityPolicyId: null` resets to Default Policy; omitting it leaves it unchanged
- `resourceUpdate`: passing `alias: null` clears the alias; omitting it leaves it unchanged
- `serviceAccountKeyCreate`: `expirationTime` is in days, range 0–365 inclusive
- `gatewayUpdate`: setting `sshCAId: null` **unassigns** the SSH CA
- DNS filtering