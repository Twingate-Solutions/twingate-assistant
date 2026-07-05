# Twingate GraphQL API Reference

## Page Title
Twingate GraphQL API Reference

## Summary
Complete GraphQL schema reference for Twingate's API, covering all queries and mutations for managing network resources, users, devices, connectors, and access controls. API uses cursor-based pagination for list operations. All requests require an API token from the admin console.

## Key Information
- **API Type**: GraphQL
- **Endpoint**: `https://<network-name>.twingate.com/api/graphql/`
- **Auth**: Header `X-API-KEY: <token>` required on all requests
- **Pagination**: Cursor-based (`before`, `after`, `first`, `last` args on all list queries)
- **Response pattern**: Mutations return `{ ok, error, entity }` pattern; queries return typed objects or Connection types

## Prerequisites
- API token from Twingate admin console
- Network name (subdomain) for your Twingate account

## Configuration Values

**Headers:**
```
X-API-KEY: <YOUR_TOKEN_HERE>
```

## Available Queries
| Query | Returns | Filter Support |
|-------|---------|---------------|
| `accessRequest(id)` | AccessRequest | — |
| `accessRequests` | AccessRequestConnection | `AccessRequestFilterInput` |
| `connector(id)` / `connectors` | Connector/Connection | `ConnectorFilterInput` |
| `device(id)` / `devices` | Device/Connection | `DeviceFilterInput` |
| `devicePosture(id)` | DevicePosture | — |
| `dnsFilteringProfile(id)` / `dnsFilteringProfiles` | Profile/Metadata | — |
| `gateway(id)` / `gateways` | Gateway/Connection | — |
| `group(id)` / `groups` | Group/Connection | `GroupFilterInput` |
| `remoteNetwork(id\|name)` / `remoteNetworks` | RemoteNetwork/Connection | `RemoteNetworkFilterInput` |
| `resource(id)` / `resources` | Resource/Connection | `ResourceFilterInput` |
| `securityPolicy(id\|name)` / `securityPolicies` | SecurityPolicy/Connection | `SecurityPolicyFilterField` |
| `serviceAccount(id)` / `serviceAccounts` | ServiceAccount/Connection | `ServiceAccountFilterInput` |
| `user(id)` / `users` | User/Connection | `UserFilterInput` |
| `serialNumbers` | SerialNumberConnection | `SerialNumberFilterInput` |

## Available Mutations
| Mutation | Description |
|----------|-------------|
| `accessRequestApprove/Reject(id)` | Approve or reject access requests |
| `connectorCreate/Update/Delete` | Manage connectors |
| `connectorGenerateTokens(connectorId)` | Generate connector tokens |
| `deviceArchive/Unarchive/Block/Unblock/Update` | Manage device state and trust |
| `dnsFilteringProfileCreate/Update/Delete` | Manage DNS filtering |
| `gatewayCreate/Update/Delete` | Manage gateways |
| `groupCreate/Update/Delete` | Manage groups with user/resource assignments |
| `kubernetesResourceCreate/Update` | Manage Kubernetes resources |
| `remoteNetworkCreate/Update/Delete` | Manage remote networks |
| `resourceCreate/Update/Delete` | Manage network resources |
| `resourceAccessAdd/Remove/Set` | Manage resource access |
| `securityPolicyUpdate` | Assign groups to security policies |
| `serviceAccountCreate/Delete` + key CRUD | Manage service accounts |
| `serialNumbersCreate/Delete` | Manage device serial numbers |

## Gotchas
- `resourceAccessSet` **replaces all existing access** — use `resourceAccessAdd/Remove` for incremental changes
- `groupUpdate` supports both full replacement (`resourceIds`, `userIds`) and incremental (`addedResourceIds`, `removedResourceIds`) — don't mix
- Setting `securityPolicyId: null` on resource/group resets to Default Policy (not no policy)
- Setting `alias: null` explicitly clears the alias; omitting leaves it unchanged
- `serviceAccountKeyCreate`