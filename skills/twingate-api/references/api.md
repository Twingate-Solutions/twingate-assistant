# Twingate GraphQL API Reference

## Page Title
Twingate GraphQL API Reference

## Summary
Twingate exposes a GraphQL API for programmatic management of all network resources, users, devices, connectors, and access controls. All requests require an API key header and target a tenant-specific endpoint. The API supports full CRUD operations via queries and mutations with cursor-based pagination.

## Key Information
- **API Type**: GraphQL (queries + mutations)
- **Pagination**: Cursor-based using `before`, `after`, `first`, `last` on all list queries
- **Response pattern**: Mutations return `{ ok: Boolean, error: String, entity: <Type> }`
- **IDs**: Base64-encoded (e.g., `"YWJjMTIzeHl6Nzg5"`)

## Prerequisites
- API token generated from the Twingate admin console
- Network name (tenant subdomain) for constructing the endpoint URL

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Endpoint | `https://<network-name>.twingate.com/api/graphql/` |
| Auth Header | `X-API-KEY: <YOUR_TOKEN_HERE>` |

## Available Queries
| Query | Description |
|-------|-------------|
| `accessRequest(id)` | Single access request |
| `accessRequests` | List with filter support |
| `connector(id)` / `connectors` | Connector(s) |
| `device(id)` / `devices` | Device(s) |
| `devicePosture(id)` | Device security posture |
| `group(id)` / `groups` | Group(s) |
| `remoteNetwork(id\|name)` / `remoteNetworks` | Remote network(s) |
| `resource(id)` / `resources` | Resource(s) |
| `securityPolicy(id\|name)` / `securityPolicies` | Security policies |
| `serviceAccount(id)` / `serviceAccounts` | Service accounts |
| `user(id)` / `users` | User(s) |
| `gateway(id)` / `gateways` | Gateways |
| `dnsFilteringProfile(id)` / `dnsFilteringProfiles` | DNS filtering |
| `certificateAuthority(id)` / `certificateAuthorities` | CAs |

## Available Mutations
| Mutation | Description |
|----------|-------------|
| `connectorCreate/Update/Delete/GenerateTokens` | Connector management |
| `resourceCreate/Update/Delete` | Resource management |
| `resourceAccessAdd/Remove/Set` | Access control |
| `groupCreate/Update/Delete` | Group management |
| `remoteNetworkCreate/Update/Delete` | Network management |
| `userCreate/Update/Delete` | User management |
| `serviceAccountCreate/Delete` + `serviceAccountKeyCreate/Delete` | Service accounts |
| `deviceUpdate/Archive/Unarchive/Block/Unblock` | Device management |
| `accessRequestApprove/Reject` | Access request handling |
| `gatewayCreate/Update/Delete` | Gateway management |
| `dnsFilteringProfileCreate/Update/Delete` | DNS filtering |
| `serialNumbersCreate/Delete` | Serial number management |
| `kubernetesResourceCreate/Update` | K8s resources |

## Gotchas
- `resourceAccessSet` **replaces all existing access** — use `resourceAccessAdd/Remove` for incremental changes
- `securityPolicyId: null` in updates resets to the default policy (not unchanged); omit the field to preserve existing
- `alias: null` explicitly clears the alias; omit to leave unchanged
- `serviceAccountKeyCreate` returns the `token` only at creation time — not retrievable afterward
- `expirationTime` for service account keys is 0–365 days (integer)
- DNS filtering queries return `None` when DNS filtering is not enabled on the tenant

## Related Docs
- Getting Started with the API guide (linked from page intro)
- Twingate Support: https://www.twingate.com/support