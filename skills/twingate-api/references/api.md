# Twingate GraphQL API Reference

## Page Title
Twingate GraphQL API Reference

## Summary
Twingate exposes a GraphQL API for programmatic management of network resources, connectors, users, devices, groups, and security policies. All requests require an API token passed via HTTP header to a tenant-specific endpoint. The API supports full CRUD operations on core Twingate objects.

## Key Information
- **API Type**: GraphQL (queries + mutations)
- **Endpoint**: `https://<network-name>.twingate.com/api/graphql/`
- **Auth Header**: `X-API-KEY: <YOUR_TOKEN_HERE>`
- **Pagination**: Cursor-based (`before`, `after`, `first`, `last`) on all list queries
- **Mutation responses**: Always include `ok` (Boolean) and `error` (String) fields

## Prerequisites
- Twingate account with admin access
- API token generated from the admin console
- Network name (subdomain) for your Twingate tenant

## Configuration Values

| Parameter | Description |
|-----------|-------------|
| `X-API-KEY` | HTTP header; API token from admin console |
| `<network name>` | Your Twingate subdomain in the endpoint URL |

## Available Queries
- `accessRequest(id)` / `accessRequests(filter, pagination)`
- `connector(id)` / `connectors(filter, pagination)`
- `device(id)` / `devices(filter, pagination)` / `devicePosture(id)`
- `group(id)` / `groups(filter, pagination)`
- `remoteNetwork(id|name)` / `remoteNetworks(filter, pagination)`
- `resource(id)` / `resources(filter, pagination)`
- `securityPolicy(id|name)` / `securityPolicies(filter, pagination)`
- `serviceAccount(id)` / `serviceAccounts` / `serviceAccountKey(id|name)`
- `user(id)` / `users(filter, pagination)`
- `gateway(id)` / `gateways` / `certificateAuthority(id)` / `certificateAuthorities`
- `dnsFilteringProfile(id)` / `dnsFilteringProfiles`
- `serialNumbers(filter, pagination)`

## Available Mutations
- **Access**: `accessRequestApprove`, `accessRequestReject`
- **Connectors**: `connectorCreate`, `connectorUpdate`, `connectorDelete`, `connectorGenerateTokens`
- **Devices**: `deviceArchive`, `deviceUnarchive`, `deviceBlock`, `deviceUnblock`, `deviceUpdate`
- **Groups**: `groupCreate`, `groupUpdate`, `groupDelete`
- **Remote Networks**: `remoteNetworkCreate`, `remoteNetworkUpdate`, `remoteNetworkDelete`
- **Resources**: `resourceCreate`, `resourceUpdate`, `resourceDelete`, `resourceAccessAdd`, `resourceAccessRemove`, `resourceAccessSet`
- **Kubernetes Resources**: `kubernetesResourceCreate`, `kubernetesResourceUpdate`
- **Service Accounts**: `serviceAccountCreate`, `serviceAccountDelete`, `serviceAccountKeyCreate`, `serviceAccountKeyRevoke`, `serviceAccountKeyUpdate`, `serviceAccountKeyDelete`
- **Security Policies**: `securityPolicyUpdate`
- **DNS Filtering**: `dnsFilteringProfileCreate`, `dnsFilteringProfileUpdate`, `dnsFilteringProfileDelete`
- **Serial Numbers**: `serialNumbersCreate`, `serialNumbersDelete`
- **Gateways**: `gatewayCreate`, `gatewayUpdate`, `gatewayDelete`

## Gotchas
- **`groupUpdate`**: Use `addedUserIds`/`removedUserIds` for incremental changes OR `userIds` for full replacement — not both simultaneously
- **`resourceUpdate` tags**: Passing `null` removes all tags; omitting the field leaves tags unchanged
- **`resourceUpdate` alias**: Passing `null` clears the alias; omitting leaves it unchanged
- **`serviceAccountKeyCreate`**: Token value is only returned at creation time — store it immediately
- **`serviceAccountKeyCreate` expiration**: `expirationTime` is days (0–365 inclusive)
- **`securityPolicyId` on update**: Passing `null` resets to default policy; omitting