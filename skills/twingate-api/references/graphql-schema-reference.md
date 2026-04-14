# Twingate GraphQL Schema Reference

Hand-authored static reference. Not auto-generated. Last reviewed: 2026-04.

---

## 1. Endpoint and Auth

**Endpoint:** `https://{network}.twingate.com/api/graphql`

All requests are HTTP POST. `{network}` is the tenant subdomain (same as the admin console).

**Required headers:**
```
X-API-KEY: <token>
Content-Type: application/json
```

**Token permission levels:**

| Level | Scope |
|---|---|
| Read | All queries (list and get) |
| Write | Queries + create/update/delete for resources, networks, groups, users, devices |
| Provision | Write + `connectorGenerateTokens`, `serviceAccountKeyCreate`, `serviceAccountKeyRevoke`, `serviceAccountKeyDelete` |

Generate tokens from **Admin Console → Settings → API**. Store in environment variables — never in source code.

---

## 2. Pagination Pattern

All list fields use Relay cursor pagination.

**Arguments:**
- `first: Int` — page size (forward pagination)
- `after: String` — cursor from previous page's `pageInfo.endCursor`
- `last: Int` — page size (backward pagination)
- `before: String` — cursor from previous page's `pageInfo.startCursor`

**Loop until `pageInfo.hasNextPage` is false.**

```graphql
query ListResources($after: String) {
  resources(first: 50, after: $after) {
    edges {
      node {
        id
        name
        address { value }
      }
    }
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
```

Pseudocode:
```
after = null
loop:
  result = query(after=after)
  collect result.edges[].node
  if result.pageInfo.hasNextPage == false: break
  after = result.pageInfo.endCursor
```

---

## 3. Mutation Payload Pattern

Every mutation returns a payload of this shape:

```graphql
{
  ok: Boolean!
  error: {
    errorCode: String!
    message: String!
  }
  entity: <ObjectType>   # null when ok is false
}
```

**Always check `ok` before reading `entity`.** When `ok` is false, `entity` is null; read `error.errorCode` and `error.message` for the failure reason.

Common `errorCode` values: `NOT_FOUND`, `ALREADY_EXISTS`, `INVALID_INPUT`, `PERMISSION_DENIED`, `RATE_LIMIT_EXCEEDED`.

---

## 4. Key Object Types

### Resource

| Field | Type | Description |
|---|---|---|
| id | ID! | Opaque NodeID |
| name | String! | Display name |
| address | Address! | `{ value: String! }` — FQDN, CIDR, wildcard, or IP |
| remoteNetwork | RemoteNetwork! | Parent remote network |
| groups | GroupConnection! | Groups that have access (paginated) |
| protocols | Protocols | Port/protocol restrictions |
| isActive | Boolean! | Whether the resource is enabled |
| isBrowserShortcutEnabled | Boolean! | Browser shortcut feature flag |
| alias | String | Optional alias hostname |
| securityPolicy | SecurityPolicy | Assigned security policy (nullable) |

**Protocols shape:**
```
protocols {
  allowIcmp: Boolean!
  tcp { policy: PortRestrictionPolicy!, ports { start: Int!, end: Int! } }
  udp { policy: PortRestrictionPolicy!, ports { start: Int!, end: Int! } }
}
```

---

### RemoteNetwork

| Field | Type | Description |
|---|---|---|
| id | ID! | Opaque NodeID |
| name | String! | Display name |
| isActive | Boolean! | Whether the network is enabled |
| location | NetworkLocation! | Enum — deployment location |
| type | String | Network type string |
| connectors | ConnectorConnection! | Connectors in this network (paginated) |
| resources | ResourceConnection! | Resources in this network (paginated) |

---

### Connector

| Field | Type | Description |
|---|---|---|
| id | ID! | Opaque NodeID |
| name | String! | Display name |
| remoteNetwork | RemoteNetwork! | Parent remote network |
| state | ConnectorState! | Health state enum |
| statusUpdatedAt | String | ISO 8601 timestamp of last state change |
| hasStatusNotificationsEnabled | Boolean! | Whether status alerts are on |
| hostname | String | Connector host's hostname (if reported) |
| privateIps | [String!] | Private IP addresses |
| publicIps | [String!] | Public IP addresses |
| version | String | Client version string |

---

### Group

| Field | Type | Description |
|---|---|---|
| id | ID! | Opaque NodeID |
| name | String! | Display name |
| type | GroupType! | MANUAL, SYNCED, or SYSTEM |
| isActive | Boolean! | Whether the group is enabled |
| createdAt | String! | ISO 8601 creation timestamp |
| resources | ResourceConnection! | Resources this group can access (paginated) |
| users | UserConnection! | Users in this group (paginated) |
| securityPolicy | SecurityPolicy | Assigned security policy (nullable) |

---

### User

| Field | Type | Description |
|---|---|---|
| id | ID! | Opaque NodeID |
| firstName | String | First name |
| lastName | String | Last name |
| email | String! | Email address (unique identifier) |
| state | UserState! | ACTIVE or DISABLED |
| role | UserRole! | ADMIN, DEVOPS, SUPPORT, or MEMBER |
| createdAt | String! | ISO 8601 creation timestamp |
| avatarUrl | String | Profile image URL |
| type | String | User type string |
| groups | GroupConnection! | Groups the user belongs to (paginated) |

---

### Device

| Field | Type | Description |
|---|---|---|
| id | ID! | Opaque NodeID |
| name | String! | Device display name |
| udid | String | Unique device identifier |
| serialNumber | String | Hardware serial number |
| userAgent | String | OS/client user agent string |
| osVersion | String | Operating system version |
| clientVersion | String | Twingate client version |
| lastConnectedAt | String | ISO 8601 timestamp of last connection |
| isTrusted | Boolean! | Device trust status |
| isActive | Boolean! | Whether the device is active |
| user | User | Owning user (nullable) |
| deviceType | String | Platform type string |

---

### ServiceAccount

| Field | Type | Description |
|---|---|---|
| id | ID! | Opaque NodeID |
| name | String! | Display name |
| createdAt | String! | ISO 8601 creation timestamp |
| resources | ResourceConnection! | Resources accessible to this service account (paginated) |
| keys | ServiceAccountKeyConnection! | Keys for this account (paginated) |

---

### ServiceAccountKey

| Field | Type | Description |
|---|---|---|
| id | ID! | Opaque NodeID |
| name | String! | Key display name |
| createdAt | String! | ISO 8601 creation timestamp |
| expiresAt | String | ISO 8601 expiry timestamp (null = no expiry) |
| status | ServiceAccountKeyStatus! | ACTIVE, REVOKED, or EXPIRED |
| revokedAt | String | ISO 8601 revocation timestamp (null if not revoked) |

---

### SecurityPolicy

| Field | Type | Description |
|---|---|---|
| id | ID! | Opaque NodeID |
| name | String! | Policy display name |

---

### AccessRequest

| Field | Type | Description |
|---|---|---|
| id | ID! | Opaque NodeID |
| user | User! | Requesting user |
| resource | Resource! | Requested resource |
| requestedAt | String! | ISO 8601 request timestamp |
| status | AccessRequestStatus! | PENDING, APPROVED, or REJECTED |
| expiresAt | String | Requested expiry (nullable) |
| approvedAt | String | ISO 8601 approval timestamp (nullable) |
| rejectedAt | String | ISO 8601 rejection timestamp (nullable) |

---

### PageInfo

| Field | Type | Description |
|---|---|---|
| hasNextPage | Boolean! | True if more pages exist after this one |
| hasPreviousPage | Boolean! | True if more pages exist before this one |
| startCursor | String | Cursor for the first edge in this page |
| endCursor | String | Cursor for the last edge — use as `after` on next call |

---

## 5. Enums

### ConnectorState
| Value | Meaning |
|---|---|
| `ALIVE` | Connector is connected and healthy |
| `DEAD_NO_HEARTBEAT` | No heartbeat received — connector may be starting or stopped |
| `DEAD_HEARTBEAT_TOO_OLD` | Last heartbeat is beyond the stale threshold |
| `DEAD_NO_RELAYS` | Connector cannot reach any relay |

### NetworkLocation
| Value | Meaning |
|---|---|
| `AWS` | Amazon Web Services |
| `AZURE` | Microsoft Azure |
| `GOOGLE_CLOUD` | Google Cloud Platform |
| `ON_PREMISE` | On-premises data center |
| `OTHER` | Any other location |

### UserRole
| Value | Meaning |
|---|---|
| `ADMIN` | Full admin access |
| `DEVOPS` | Connector management, limited admin |
| `SUPPORT` | Read-only admin console access |
| `MEMBER` | End user — no admin console access |

### UserState
| Value | Meaning |
|---|---|
| `ACTIVE` | User is active and can authenticate |
| `DISABLED` | User is disabled — cannot authenticate |

### GroupType
| Value | Meaning |
|---|---|
| `MANUAL` | Manually managed group |
| `SYNCED` | SCIM-synchronized group from IdP |
| `SYSTEM` | System-managed group (e.g., Everyone) |

### PortRestrictionPolicy
| Value | Meaning |
|---|---|
| `ALLOW_ALL` | No port restriction — all ports allowed |
| `RESTRICTED` | Only the specified port ranges are allowed |

### ServiceAccountKeyStatus
| Value | Meaning |
|---|---|
| `ACTIVE` | Key is valid and usable |
| `REVOKED` | Key has been explicitly revoked |
| `EXPIRED` | Key passed its expiry date |

### AccessRequestStatus
| Value | Meaning |
|---|---|
| `PENDING` | Awaiting approval or rejection |
| `APPROVED` | Access was granted |
| `REJECTED` | Access was denied |

---

## 6. Queries

```graphql
resources(first: Int, after: String, filter: ResourceFilterInput): ResourceConnection!
```
List all resources. Paginate with `first`/`after`. Filter by name or remote network.

```graphql
resource(id: ID!): Resource
```
Get a single resource by ID. Returns null if not found.

```graphql
remoteNetworks(first: Int, after: String): RemoteNetworkConnection!
```
List all remote networks.

```graphql
remoteNetwork(id: ID!): RemoteNetwork
```
Get a single remote network by ID.

```graphql
connectors(first: Int, after: String): ConnectorConnection!
```
List all connectors across all remote networks.

```graphql
connector(id: ID!): Connector
```
Get a single connector by ID including current state.

```graphql
groups(first: Int, after: String, filter: GroupFilterInput): GroupConnection!
```
List all groups. Supports name filter.

```graphql
group(id: ID!): Group
```
Get a single group by ID including its users and resources.

```graphql
users(first: Int, after: String, filter: UserFilterInput): UserConnection!
```
List all users. Filter by email, role, or state.

```graphql
user(id: ID!): User
```
Get a single user by ID.

```graphql
devices(first: Int, after: String): DeviceConnection!
```
List all enrolled devices.

```graphql
device(id: ID!): Device
```
Get a single device by ID.

```graphql
serviceAccounts(first: Int, after: String): ServiceAccountConnection!
```
List all service accounts.

```graphql
serviceAccount(id: ID!): ServiceAccount
```
Get a single service account by ID including its keys.

```graphql
securityPolicies(first: Int, after: String): SecurityPolicyConnection!
```
List all security policies.

```graphql
securityPolicy(id: ID!): SecurityPolicy
```
Get a single security policy by ID.

```graphql
accessRequests(first: Int, after: String, filter: AccessRequestFilterInput): AccessRequestConnection!
```
List access requests. Filter by status (`PENDING`, `APPROVED`, `REJECTED`).

---

## 7. Mutations

### Resource

```graphql
resourceCreate(input: ResourceCreateInput!): ResourcePayload!
```
Create a new resource. Required input fields: `name`, `address { value }`, `remoteNetworkId`.

```graphql
resourceUpdate(id: ID!, input: ResourceUpdateInput!): ResourcePayload!
```
Update a resource. All input fields are optional — only provided fields are changed.

```graphql
resourceDelete(id: ID!): OkErrorPayload!
```
Delete a resource. Returns `{ ok, error }` only (no entity).

```graphql
resourceAccessAdd(resourceId: ID!, principalIds: [ID!]!): ResourcePayload!
```
Grant access to a resource for one or more groups or service accounts (by ID).

```graphql
resourceAccessRemove(resourceId: ID!, principalIds: [ID!]!): ResourcePayload!
```
Revoke access to a resource from one or more groups or service accounts.

---

### Network

```graphql
remoteNetworkCreate(input: RemoteNetworkCreateInput!): RemoteNetworkPayload!
```
Create a remote network. Required: `name`, `location` (NetworkLocation enum).

```graphql
remoteNetworkUpdate(id: ID!, input: RemoteNetworkUpdateInput!): RemoteNetworkPayload!
```
Update a remote network's name or location.

```graphql
remoteNetworkDelete(id: ID!): OkErrorPayload!
```
Delete a remote network. Will fail if the network still has connectors or resources.

---

### Connector

```graphql
connectorCreate(input: ConnectorCreateInput!): ConnectorPayload!
```
Register a new connector. Required: `remoteNetworkId`. Optional: `name`, `hasStatusNotificationsEnabled`. Does not produce credentials — call `connectorGenerateTokens` next.

```graphql
connectorUpdate(id: ID!, input: ConnectorUpdateInput!): ConnectorPayload!
```
Update connector metadata (name, notifications flag).

```graphql
connectorDelete(id: ID!): OkErrorPayload!
```
Delete a connector registration. The running connector process will stop authenticating.

```graphql
connectorGenerateTokens(connectorId: ID!): ConnectorTokensPayload!
```
Generate a new access token and refresh token for a connector. **Requires Provision-level token.** Rotates credentials — the existing connector must be restarted with the new tokens. Returns `{ ok, error, connectorTokens { accessToken, refreshToken } }`.

---

### Group

```graphql
groupCreate(input: GroupCreateInput!): GroupPayload!
```
Create a group. Required: `name`. Optional: `userIds`, `resourceIds`, `securityPolicyId`.

```graphql
groupUpdate(id: ID!, input: GroupUpdateInput!): GroupPayload!
```
Update a group. Can add/remove users (`addedUserIds`, `removedUserIds`), add/remove resources, change security policy.

```graphql
groupDelete(id: ID!): OkErrorPayload!
```
Delete a group. SYNCED groups managed by SCIM cannot be deleted via API.

---

### User

```graphql
userUpdate(id: ID!, input: UserUpdateInput!): UserPayload!
```
Update a user's role or state. Input fields: `role` (UserRole), `state` (UserState).

```graphql
userDelete(id: ID!): OkErrorPayload!
```
Delete a user from the tenant.

---

### Device

```graphql
deviceUpdate(id: ID!, input: DeviceUpdateInput!): DevicePayload!
```
Update device trust status. Primary use: set `isTrusted: true` or `isTrusted: false`.

---

### Service Account

```graphql
serviceAccountCreate(input: ServiceAccountCreateInput!): ServiceAccountPayload!
```
Create a service account. Required: `name`. Optional: `resourceIds`.

```graphql
serviceAccountUpdate(id: ID!, input: ServiceAccountUpdateInput!): ServiceAccountPayload!
```
Update a service account (name, add/remove resources).

```graphql
serviceAccountDelete(id: ID!): OkErrorPayload!
```
Delete a service account and revoke all its keys.

```graphql
serviceAccountKeyCreate(serviceAccountId: ID!, input: ServiceAccountKeyCreateInput!): ServiceAccountKeyPayload!
```
Create a new key for a service account. **Requires Provision-level token.** Input: `name` (String!), `expirationTime` (Int — days until expiry; omit for no expiry). Returns the key value once — store it immediately, it cannot be retrieved again.

```graphql
serviceAccountKeyRevoke(keyId: ID!): OkErrorPayload!
```
Revoke a key immediately. The key can no longer be used but the record is retained. **Requires Provision-level token.**

```graphql
serviceAccountKeyDelete(keyId: ID!): OkErrorPayload!
```
Delete a revoked key record. The key must be in REVOKED state first. **Requires Provision-level token.**

---

### Access

```graphql
accessRequestApprove(id: ID!, input: AccessRequestApproveInput): AccessRequestPayload!
```
Approve a pending access request. Optional input: `expiresAt` (ISO 8601 — grant time-limited access).

```graphql
accessRequestReject(id: ID!, input: AccessRequestRejectInput): AccessRequestPayload!
```
Reject a pending access request. Optional input: `comment` (String).

---

## 8. Input Types

### ProtocolsInput
```graphql
input ProtocolsInput {
  allowIcmp: Boolean
  tcp: ProtocolInput
  udp: ProtocolInput
}
```
Omit a field to leave that protocol at its current setting.

### ProtocolInput
```graphql
input ProtocolInput {
  policy: PortRestrictionPolicy!
  ports: [PortRangeInput!]
}
```
Use `policy: ALLOW_ALL` with an empty `ports` array to allow all ports. Use `policy: RESTRICTED` with explicit ranges to restrict.

### PortRangeInput
```graphql
input PortRangeInput {
  start: Int!
  end: Int!
}
```
Both `start` and `end` are inclusive. Single-port restriction: `{ start: 443, end: 443 }`.

**Example — restrict resource to HTTPS only:**
```graphql
protocols: {
  allowIcmp: false
  tcp: {
    policy: RESTRICTED
    ports: [{ start: 443, end: 443 }]
  }
  udp: {
    policy: ALLOW_ALL
    ports: []
  }
}
```
