---
source: https://www.twingate.com/docs/api
type: docs
fetched: 2026-08-16
source_version: faea69a3047182e89ceaeec8027b9d99c2b22a6f8e4f207be0876aa4b2685a75
---

# Twingate GraphQL API Reference

## Page Title
Twingate GraphQL API Reference

## Summary
Complete GraphQL schema reference for Twingate's API, covering queries and mutations for managing resources, groups, connectors, users, devices, and network infrastructure. All requests require an API token in the header. The API uses cursor-based pagination for list operations.

## Key Information
- **API Type**: GraphQL
- **Endpoint**: `https://<network-name>.twingate.com/api/graphql/`
- **Auth Header**: `X-API-KEY: <YOUR_TOKEN_HERE>`
- **Pagination**: Cursor-based (`before`, `after`, `first`, `last` args on all list queries)
- **List responses**: Return `pageInfo`, `edges`, and `totalCount`
- **Mutation responses**: Return `ok` (Boolean), `error` (String), and optionally `entity`

## Prerequisites
- Twingate network with admin access
- API token generated from admin console
- Network name (subdomain) for endpoint construction

## Available Queries
| Query | Description |
|-------|-------------|
| `accessRequest(id)` | Single access request |
| `accessRequests(filter)` | List access requests |
| `connector(id)` / `connectors(filter)` | Connector(s) |
| `device(id)` / `devices(filter)` | Device(s) |
| `devicePosture(id)` | Device posture status |
| `dnsFilteringProfile(id)` / `dnsFilteringProfiles` | DNS filtering |
| `gateway(id)` / `gateways` | Gateway(s) |
| `group(id)` / `groups(filter)` | Group(s) |
| `remoteNetwork(id\|name)` / `remoteNetworks(filter)` | Remote network(s) |
| `resource(id)` / `resources(filter)` | Resource(s) |
| `securityPolicy(id\|name)` / `securityPolicies(filter)` | Security policies |
| `serviceAccount(id)` / `serviceAccounts(filter)` | Service accounts |
| `user(id)` / `users(filter)` | User(s) |
| `serialNumbers(filter)` | Serial numbers |
| `certificateAuthority(id)` / `certificateAuthorities` | CAs |

## Available Mutations
**Access**: `accessRequestApprove`, `accessRequestReject`  
**Connectors**: `connectorCreate`, `connectorUpdate`, `connectorDelete`, `connectorGenerateTokens`  
**Devices**: `deviceArchive`, `deviceUnarchive`, `deviceBlock`, `deviceUnblock`, `deviceUpdate`  
**DNS**: `dnsFilteringProfileCreate`, `dnsFilteringProfileUpdate`, `dnsFilteringProfileDelete`  
**Gateways**: `gatewayCreate`, `gatewayUpdate`, `gatewayDelete`  
**Groups**: `groupCreate`, `groupUpdate`, `groupDelete`  
**Remote Networks**: `remoteNetworkCreate`, `remoteNetworkUpdate`, `remoteNetworkDelete`  
**Resources**: `resourceCreate`, `resourceUpdate`, `resourceDelete`, `resourceAccessAdd`, `resourceAccessRemove`, `resourceAccessSet`  
**Kubernetes**: `kubernetesResourceCreate`, `kubernetesResourceUpdate`  
**Security Policies**: `securityPolicyUpdate`  
**Service Accounts**: `serviceAccountCreate`, `serviceAccountDelete`, `serviceAccountKeyCreate`  
**Serial Numbers**: `serialNumbersCreate`, `serialNumbersDelete`

## Configuration Values
- **Header**: `X-API-KEY` — required on all requests
- **Endpoint pattern**: `https://<network_name>.twingate.com/api/graphql/`

## Gotchas
- `remoteNetwork` query accepts either `id` OR `name` (both optional, not both required)
- `securityPolicyId: null` in updates resets to Default Policy (not unchanged); omitting leaves it unchanged
- `alias: null` clears the alias; omitting leaves it unchanged — distinct behaviors
- `tags: null` removes all tags; omitting leaves tags unchanged
- `resourceAccessSet` replaces **all** existing access; use `resource