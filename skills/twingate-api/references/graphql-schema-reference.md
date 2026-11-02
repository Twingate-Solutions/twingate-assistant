<!-- manual-reference: do-not-overwrite -->
# Twingate GraphQL Schema Reference

Hand-authored curated guide. Not auto-generated. Last reviewed against the SDL: **2026-11**.

> **For exact signatures, grep `graphql-schema.graphql` in this directory; this file is a curated summary.**
> The `.graphql` file is the verbatim Admin API SDL and wins any disagreement with this page.
> Copy-and-adapt snippets for common operations live in `graphql-recipes.md`.

**Contents:** 1. Endpoint and Auth · 2. Scalars, IDs, interfaces · 3. Pagination · 4. Mutation
payload pattern · 5. Key object types · 6. Enums · 7. Queries · 8. Mutations (flat arguments) ·
9. Input types

Grep examples:

```
grep -n "resourceCreate(" -A 16 graphql-schema.graphql
grep -n "^input AccessInput" -A 26 graphql-schema.graphql
grep -n "^enum UserRole" -A 40 graphql-schema.graphql
```

---

## 1. Endpoint and Auth

**Endpoint:** `https://{network}.twingate.com/api/graphql/` (HTTP POST, trailing slash as in the docs).
`{network}` is the tenant subdomain (same as the Admin Console URL).

**Headers:**
```
X-API-KEY: <token>
Content-Type: application/json
```

Root types: `query: QueriesRoot`, `mutation: MutationsRoot`. No subscriptions.

**Token permission levels** (set when the token is created; not expressed in the SDL):

| Level | Scope |
|---|---|
| Read | All queries |
| Read & Write | Queries + create/update/delete on resources, networks, groups, users, devices, etc. |
| Read, Write & Provision | Write + `connectorGenerateTokens` and service account key operations |

Generate tokens from **Admin Console → Settings → API**. Store in environment variables — never in
source code. Rate limits and 429 handling: see `api-overview.md` (not part of the SDL).

---

## 2. Scalars, IDs, interfaces

- **`ID`** — opaque Relay NodeID. Never decode or construct; use as returned.
- **`DateTime`** — ISO 8601 string (all timestamps: `createdAt`, `updatedAt`, `expiresAt`, …).
- **`Node`** interface — everything with an `id`.
- **`Resource` is an interface**, implemented by `NetworkResource`, `KubernetesResource`,
  `SSHResource`, `WebAppResource`. `resources` / `resource(id)` return the interface — use inline
  fragments (`... on NetworkResource { routingMode }`) for type-specific fields. `routingMode` is
  **only** on `NetworkResource`, not on the interface.
- **`Taggable`** interface — `tags: [Tag!]!` where `Tag { key value }`.
- **`Principal` union** = `Group | ServiceAccount` (the node type of a resource's `access` edges).
- **`CertificateAuthority` union** = `X509CertificateAuthority | SSHCertificateAuthority`.

---

## 3. Pagination Pattern

Every list is a Relay connection. Arguments: `first: Int`, `after: String`, `last: Int`,
`before: String`, plus an optional `filter`. Every `*Connection` has:

```graphql
pageInfo { hasNextPage hasPreviousPage startCursor endCursor }
edges { cursor node { ... } }
totalCount   # Int! — present on every connection
```

Loop until `pageInfo.hasNextPage` is false, passing `endCursor` as `after`. **Nested
connections** (e.g. a resource's `access`, a group's `users`) are paginated independently — if a
nested `pageInfo.hasNextPage` is true, follow up with a per-object query.

```graphql
query ListResources($after: String) {
  resources(first: 50, after: $after) {
    pageInfo { hasNextPage endCursor }
    edges { node { id name address { type value } } }
  }
}
```

### Filters

`StringFilterOperatorInput`: `eq`, `ieq` (case-insensitive eq), `ne`, `startsWith`, `endsWith`,
`regexp`, `contains`, `in: [String!]`. Multiple operators are ANDed.

| Query | Filter input | Fields |
|---|---|---|
| `resources` | `ResourceFilterInput` | `name`, `remoteNetworkId { in, eq }`, `tags { and: [{ key, value { in, notIn, eq } }] }` |
| `remoteNetworks` | `RemoteNetworkFilterInput` | `name`, `networkType { in }` |
| `connectors` | `ConnectorFilterInput` | `name`, `state { in: [ConnectorState!] }` |
| `groups` | `GroupFilterInput` | `name`, `type { in }`, `isActive { eq }`, `originId` |
| `users` | `UserFilterInput` | `role { in }`, `firstName`, `lastName`, `email` |
| `devices` | `DeviceFilterInput` | `isTrusted { eq }`, `serialNumber`, `activeState { in }`, `userId { in }` |
| `serviceAccounts` | `ServiceAccountFilterInput` | `name` |
| `securityPolicies` | `SecurityPolicyFilterField` | `policyType { in }`, `name` |
| `accessRequests` | `AccessRequestFilterInput` | `userId { in }`, `resourceId { in }`, `status { in }` |
| `serialNumbers` | `SerialNumberFilterInput` | `serialNumber`, `hasMatchedDevices { eq }` |
| `Resource.access` | `AccessFilterInput` | `principalType { in: [GROUP, SERVICE_ACCOUNT] }` |

---

## 4. Mutation Payload Pattern

**All mutations take flat arguments — there are no `input:` wrapper objects.** Each returns a
`<Name>Mutation` payload:

```graphql
ok: Boolean!
error: String        # plain human-readable string; there is NO errorCode / message object
entity: <Type>       # nullable; absent on delete/approve/reject payloads
```

Exceptions: `connectorGenerateTokens` returns `connectorTokens { accessToken refreshToken }`
instead of `entity`; `serviceAccountKeyCreate` returns `entity` **and** `token: String`;
`serialNumbersCreate` returns `entities: [SerialNumber!]`.

**Always check `ok` before reading `entity`.** HTTP 200 with `ok: false` is a normal failure;
surface `error` verbatim. GraphQL-level failures (bad field/argument names, type errors) come back
as a top-level `errors` array instead — check both.

---

## 5. Key Object Types

### NetworkResource (implements Resource)

| Field | Type | Notes |
|---|---|---|
| id, name | ID!, String! | |
| createdAt, updatedAt | DateTime! | |
| address | ResourceAddress! | `{ type: AddressType! (IP \| DNS), value: String! }` |
| alias | String | |
| protocols | ResourceProtocols! | see below |
| isActive | Boolean! | |
| isVisible | Boolean! | shown in the Client's main list |
| isBrowserShortcutEnabled | Boolean! | |
| remoteNetwork | RemoteNetwork! | |
| access(filter, first, after…) | AccessConnection! | **current way** to read who has access |
| groups(…) / serviceAccounts(…) | connections | **deprecated** — use `access` |
| securityPolicy | SecurityPolicy | nullable |
| accessPolicy | AccessPolicy! | `{ mode: AccessMode!, durationSeconds: Int }` |
| approvalMode | AccessApprovalMode! | |
| approverGroups(…) | GroupConnection! | groups that can approve access requests |
| usageBasedAutolockDurationDays | Int | **deprecated** — use `accessPolicy` |
| routingMode | RoutingMode! | NetworkResource only |
| tags | [Tag!]! | |

**ResourceProtocols:** `allowIcmp: Boolean!`, `tcp: ResourceProtocol!`, `udp: ResourceProtocol!`;
`ResourceProtocol { policy: ProtocolPolicy!, ports: [PortRange!]! }`; `PortRange { start end }`
(inclusive, 1–65535). Ignore `ports` when `policy` is `ALLOW_ALL`.

**AccessEdge** (edges of `access`): `node: Principal!` (Group or ServiceAccount — use fragments),
`cursor`, `securityPolicy: SecurityPolicy`, `expiresAt: DateTime`, `accessPolicy: AccessPolicy`,
`approvalMode: AccessApprovalMode`, `usageBasedAutolockDurationDays` (deprecated).

**Gateway-backed resources** (`KubernetesResource`, `SSHResource`, `WebAppResource`) share the
Resource fields and add `gateway: Gateway!`, `downstream { port }`, `upstream { port }`.
WebApp adds `tlsMode` on both sides (`TLSServerMode` / `TLSClientMode`) and
`requestHeaderRewrites: [KeyValuePair!]!`. Kubernetes adds `clusterRef: String` (null = in-cluster
credentials); its `proxyAddress` / `certificateAuthorityCert` are deprecated.

### RemoteNetwork

| Field | Type | Notes |
|---|---|---|
| id, name | ID!, String! | |
| createdAt, updatedAt | DateTime! | |
| networkType | RemoteNetworkType! | `REGULAR` or `EXIT` (field is `networkType`, not `type`) |
| location | RemoteNetworkLocation! | |
| isActive | Boolean! | |
| resources(…), connectors(…), gateways(…) | connections | |

### Connector

| Field | Type | Notes |
|---|---|---|
| id, name | ID!, String! | |
| createdAt, updatedAt | DateTime! | |
| lastHeartbeatAt | DateTime | |
| hostname | String | |
| remoteNetwork | RemoteNetwork! | |
| state | ConnectorState! | |
| hasStatusNotificationsEnabled | Boolean! | |
| version | String | |
| publicIP | String | singular, capital `IP` |
| privateIPs | [String!]! | capital `IPs` |

### Gateway / Certificate Authorities

`Gateway { id address remoteNetwork x509CA: X509CertificateAuthority! sshCA: SSHCertificateAuthority }`.
`X509CertificateAuthority` / `SSHCertificateAuthority`: `{ id name fingerprint }`.

### Group

| Field | Type | Notes |
|---|---|---|
| id, name | ID!, String! | |
| createdAt, updatedAt | DateTime! | |
| originId | String | IdP origin identifier (synced groups) |
| isActive | Boolean! | |
| type | GroupType! | |
| users(…) | UserConnection! | `users { totalCount }` gives member count |
| resources(…) | ResourceConnection! | |
| securityPolicy | SecurityPolicy! | non-null |

### User

| Field | Type | Notes |
|---|---|---|
| id | ID! | |
| createdAt, updatedAt | DateTime! | |
| firstName, lastName | String! | |
| email | String | nullable |
| avatarUrl | String | |
| state | UserState! | |
| role | UserRole! | |
| type | UserType! | `MANUAL` (email invite) or `SYNCED` (IdP) |
| isAdmin | Boolean! | **deprecated** — use `role` |
| groups(…), devices(…) | connections | |

### Device

| Field | Type | Notes |
|---|---|---|
| id | ID! | |
| name, osVersion, hardwareModel, hostname, username, serialNumber, clientVersion, manufacturerName | String | all nullable |
| user | User! | |
| osName | DeviceOsName | |
| deviceType | DeviceType! | |
| activeState | DeviceActiveState! | |
| isTrusted | Boolean! | |
| lastSuccessfulLoginAt, lastFailedLoginAt | DateTime | |
| lastConnectedAt | DateTime | **deprecated** — no longer populated |
| internetSecurityConfiguration | String! | |

Posture detail is a separate query: `devicePosture(id: ID!): DevicePosture!` — per-check
`isSatisfied: PostureStatus` (hardDriveEncryption, screenLockPasscode, firewall, biometric,
antivirus, osVersion) and per-provider `TrustProviderVerification` (crowdstrike, jamf, iru,
inTune, sentinelOne, onePassword; `kandji` deprecated → `iru`), plus `manualVerification`.

### ServiceAccount / ServiceAccountKey

`ServiceAccount { id name createdAt updatedAt resources(…) keys(…) }`.
`ServiceAccountKey { id name createdAt updatedAt expiresAt revokedAt status serviceAccount }`.

### SecurityPolicy

`SecurityPolicy { id name createdAt updatedAt policyType: SecurityPolicyType! groups(…) }`.

### AccessRequest

`AccessRequest { id reason: String requestedAt: DateTime! user: User! resource: Resource! status }`.
(No `expiresAt` / `approvedAt` / `rejectedAt` fields.)

### Other types

`SerialNumber { id serialNumber createdAt matchedDevices: [Device!]! }`;
`DnsFilteringProfile { id name priority: Float! fallbackMethod groups(…) allowedDomains deniedDomains contentCategoryConfig securityCategoryConfig privacyCategoryConfig }`
(category configs are flat Boolean flags — grep `ContentCategoryConfig` for names).

---

## 6. Enums

| Enum | Values |
|---|---|
| `AddressType` | `IP`, `DNS` |
| `ProtocolPolicy` | `ALLOW_ALL`, `RESTRICTED` |
| `RemoteNetworkType` | `REGULAR`, `EXIT` |
| `RemoteNetworkLocation` | `AWS`, `AZURE`, `GOOGLE_CLOUD`, `ON_PREMISE`, `OTHER` |
| `ConnectorState` | `ALIVE`, `DEAD_NO_HEARTBEAT`, `DEAD_HEARTBEAT_TOO_OLD`, `DEAD_NO_RELAYS` |
| `GroupType` | `MANUAL`, `SYNCED`, `SYSTEM` |
| `UserState` | `PENDING`, `ACTIVE`, `DISABLED` |
| `UserStateUpdateInput` | `ACTIVE`, `DISABLED` (what `userDetailsUpdate` accepts) |
| `UserType` | `MANUAL`, `SYNCED` |
| `UserRole` | `ADMIN`, `SUPPORT`, `DEVOPS`, `INTERNET_SECURITY`, `HELPDESK`, `ACCESS_REVIEWER`, `BILLING`, `MEMBER` |
| `DeviceOsName` | `IPADOS`, `IOS`, `MAC_OS`, `ANDROID`, `CHROME_OS`, `WINDOWS`, `LINUX` |
| `DeviceType` | `GENERIC`, `DESKTOP`, `LAPTOP`, `TABLET`, `MOBILE` |
| `DeviceActiveState` | `ACTIVE`, `ARCHIVED`, `BLOCKED` |
| `SecurityPolicyType` | `RESOURCE`, `DEFAULT_RESOURCE` |
| `ServiceAccountKeyStatus` | `ACTIVE`, `REVOKED`, `EXPIRED` |
| `AccessMode` | `MANUAL`, `AUTO_LOCK`, `ACCESS_REQUEST` |
| `AccessApprovalMode` | `MANUAL`, `AUTOMATIC` |
| `PrincipalType` | `GROUP`, `SERVICE_ACCOUNT` |
| `RoutingMode` | `THROUGH_TWINGATE`, `BYPASS_TWINGATE` |
| `AccessRequestStatus` | `PENDING`, `APPROVED`, `REJECTED` |
| `TLSServerMode` | `TLS13`, `NONE` |
| `TLSClientMode` | `VERIFY_FULL`, `VERIFY_CA`, `INSECURE`, `NONE` |
| `DohFallbackMethod` | `AUTO`, `STRICT` |
| `PostureStatus` | `YES`, `NO`, `NOT_REQUIRED` |

**UserRole meanings (from SDL descriptions):** `ADMIN` full read-write; `SUPPORT` read-only
excluding Billing and Internet Security (shown as **Viewer** in the Admin Console from the week of
Oct 19 2026 — see `skills/twingate-identity/references/2026-10-admin-role-changes.md`); `DEVOPS`
Viewer + Network tab write; `INTERNET_SECURITY` Viewer + Internet Security write; `HELPDESK` Viewer +
MFA reset and device verification; `ACCESS_REVIEWER` resource requests only; `BILLING` billing only;
`MEMBER` no Admin Console access.

---

## 7. Queries (`QueriesRoot`)

All list queries take `before, after, first, last` plus the filter shown in §3.

| Query | Returns | Notes |
|---|---|---|
| `resources(filter: ResourceFilterInput)` | ResourceConnection! | nodes are the `Resource` interface |
| `resource(id: ID!)` | Resource | |
| `remoteNetworks(filter: RemoteNetworkFilterInput)` | RemoteNetworkConnection! | |
| `remoteNetwork(id: ID, name: String)` | RemoteNetwork | **lookup by ID or by name** |
| `connectors(filter: ConnectorFilterInput)` | ConnectorConnection! | |
| `connector(id: ID!)` | Connector | |
| `gateways` / `gateway(id: ID!)` | GatewayConnection! / Gateway | no filter |
| `certificateAuthorities` / `certificateAuthority(id: ID!)` | CertificateAuthorityConnection! / CertificateAuthority (union) | |
| `groups(filter: GroupFilterInput)` | GroupConnection! | |
| `group(id: ID!)` | Group | |
| `users(filter: UserFilterInput)` | UserConnection! | |
| `user(id: ID!)` | User | |
| `devices(filter: DeviceFilterInput)` | DeviceConnection! | |
| `device(id: ID!)` | Device | |
| `devicePosture(id: ID!)` | DevicePosture! | |
| `serviceAccounts(filter: ServiceAccountFilterInput)` | ServiceAccountConnection! | |
| `serviceAccount(id: ID!)` | ServiceAccount | |
| `serviceAccountKey(id: ID, name: String)` | ServiceAccountKey | by ID or name |
| `securityPolicies(filter: SecurityPolicyFilterField)` | SecurityPolicyConnection! | |
| `securityPolicy(id: ID, name: String)` | SecurityPolicy | by ID or name |
| `accessRequests(filter: AccessRequestFilterInput)` | AccessRequestConnection! | |
| `accessRequest(id: ID!)` | AccessRequest | |
| `serialNumbers(filter: SerialNumberFilterInput)` | SerialNumberConnection! | |
| `dnsFilteringProfiles` | [DnsFilteringProfileMetadata!] | `{ id name priority }`; null when DNS filtering is off; **not paginated** |
| `dnsFilteringProfile(id: ID!)` | DnsFilteringProfile | |
| `eventsSyncOidcProviderUrl` | String! | OIDC provider URL to register in a cloud provider for event sync |

---

## 8. Mutations (`MutationsRoot`) — flat arguments

`= x` shows the SDL default. `[ID]` lists without `!` are as written in the SDL.

### Remote networks

```graphql
remoteNetworkCreate(name: String!, location: RemoteNetworkLocation = OTHER,
                    networkType: RemoteNetworkType = REGULAR, isActive: Boolean = true)
remoteNetworkUpdate(id: ID!, name: String, location: RemoteNetworkLocation, isActive: Boolean)
remoteNetworkDelete(id: ID!)                       # payload: ok, error
```
`networkType` is set at create time only — `remoteNetworkUpdate` has no `networkType` argument.

### Connectors

```graphql
connectorCreate(remoteNetworkId: ID!, name: String, hasStatusNotificationsEnabled: Boolean = true)
connectorUpdate(id: ID!, name: String, hasStatusNotificationsEnabled: Boolean)
connectorDelete(id: ID!)
connectorGenerateTokens(connectorId: ID!)          # → connectorTokens { accessToken refreshToken }
```
`connectorCreate` does not return credentials; call `connectorGenerateTokens` next (Provision
token). Calling it on a deployed Connector rotates its credentials.

### Resources (network)

```graphql
resourceCreate(
  name: String!, address: String!, remoteNetworkId: ID!,
  alias: String, protocols: ProtocolsInput,          # null/omitted = all protocols & ports allowed
  groupIds: [ID] = [], securityPolicyId: ID,
  accessPolicy: AccessPolicyInput, approvalMode: AccessApprovalMode = MANUAL,
  approverGroupIds: [ID!] = [], isVisible: Boolean, isBrowserShortcutEnabled: Boolean,
  routingMode: RoutingMode, tags: [TagInput!]
)                                                    # entity: NetworkResource

resourceUpdate(
  id: ID!, name, address, remoteNetworkId, alias, protocols, isActive, isVisible,
  isBrowserShortcutEnabled, routingMode, securityPolicyId, accessPolicy, approvalMode, tags,
  groupIds: [ID],  addedGroupIds: [ID],  removedGroupIds: [ID],
  approverGroupIds: [ID!], addedApproverGroupIds: [ID!], removedApproverGroupIds: [ID!]
)                                                    # entity: NetworkResource
resourceDelete(id: ID!)
```

`address` is a plain `String` (IP, CIDR, FQDN or wildcard) — **not** `{ value }`.
`resourceUpdate` null-vs-omitted semantics (from SDL descriptions): `alias` omitted = unchanged,
null = cleared; `securityPolicyId` omitted = unchanged, null = reset to Default Policy; `tags`
omitted = unchanged, null = all removed; `accessPolicy`/`approvalMode` omitted or null = unchanged.
`groupIds` **replaces** the full group set; prefer `addedGroupIds` / `removedGroupIds`.

### Resource access (groups and service accounts)

```graphql
resourceAccessAdd(resourceId: ID!, access: [AccessInput!]!)     # add or reconfigure edges
resourceAccessSet(resourceId: ID!, access: [AccessInput!]!)     # REPLACES all existing access
resourceAccessRemove(resourceId: ID!, principalIds: [ID!]!)     # entity: Resource
```

- `resourceAccessAdd`: if an edge for that principal already exists, its properties are
  reconfigured — this is also how you change or remove an edge's security policy.
- `resourceAccessSet`: existing accesses not in the list **are removed**. Destructive; confirm first.
- `principalId` is a Group ID or Service Account ID. For service accounts, leave
  `securityPolicyId`, `expiresAt`, `accessPolicy`, `approvalMode` null.

### Groups

```graphql
groupCreate(name: String!, userIds: [ID] = [], resourceIds: [ID] = [], securityPolicyId: ID)
groupUpdate(id: ID!, name: String, isActive: Boolean, securityPolicyId: ID,
            userIds: [ID],     addedUserIds: [ID],     removedUserIds: [ID],
            resourceIds: [ID], addedResourceIds: [ID], removedResourceIds: [ID])
groupDelete(id: ID!)
```
`userIds` / `resourceIds` on update **replace** the full set; `added*` / `removed*` are
incremental. `groupCreate` with no `securityPolicyId` uses the default Resource Policy.

### Users

```graphql
userCreate(email: String!, firstName: String, lastName: String, role: UserRole = MEMBER)
userDetailsUpdate(id: ID!, firstName: String, lastName: String, state: UserStateUpdateInput)
userRoleUpdate(id: ID!, role: UserRole)
userResetMfa(id: ID!)
userDelete(id: ID!)
```
There is no single `userUpdate` — state/name and role are separate mutations.

### Devices

```graphql
deviceUpdate(id: ID!, isTrusted: Boolean!)
deviceArchive(id: ID!)   deviceUnarchive(id: ID!)
deviceBlock(id: ID!)     deviceUnblock(id: ID!)
```

### Service accounts and keys

```graphql
serviceAccountCreate(name: String!, resourceIds: [ID] = [])
serviceAccountUpdate(id: ID!, name: String, resourceIds: [ID],
                     addedResourceIds: [ID], removedResourceIds: [ID])
serviceAccountDelete(id: ID!)
serviceAccountKeyCreate(serviceAccountId: ID!, expirationTime: Int!, name: String)
                                                    # → entity + token (shown once)
serviceAccountKeyUpdate(id: ID!, name: String!)
serviceAccountKeyRevoke(id: ID!)                    # entity: ServiceAccountKey
serviceAccountKeyDelete(id: ID!)
```
`expirationTime` is **required**: days until expiry, 0–365 inclusive. Store `token` immediately —
it cannot be read back. Key mutations take `id`, not `keyId`.

### Security policies

```graphql
securityPolicyUpdate(id: ID!, groupIds: [ID], addedGroupIds: [ID], removedGroupIds: [ID])
```
Only group assignment is editable via the API — there is no create/delete, and policy rules
(MFA, device posture) are not exposed. Groups removed fall back to the default resource policy;
`groupIds` replaces the full set.

### Access requests

```graphql
accessRequestApprove(id: ID!)      # payload: ok, error (no entity)
accessRequestReject(id: ID!)
```
No expiry or comment arguments.

### Other mutation families (grep the `.graphql` for full signatures)

| Family | Mutations |
|---|---|
| Gateways | `gatewayCreate(address!, remoteNetworkId!, x509CAId!, sshCAId)`, `gatewayUpdate`, `gatewayDelete` |
| Certificate authorities | `x509CertificateAuthorityCreate(name!, certificate!)`, `x509CertificateAuthorityDelete`, `sshCertificateAuthorityCreate(name!, publicKey!)`, `sshCertificateAuthorityDelete` |
| Kubernetes resources | `kubernetesResourceCreate` / `Update` — resource args + `gatewayId` (optional), `clusterRef`, `downstream { port }`, `upstream { port }` |
| SSH resources | `sshResourceCreate` / `Update` — resource args (no `protocols`) + `gatewayId!`, `downstream`, `upstream` |
| Web app resources | `webAppResourceCreate` / `Update` — `gatewayId!`, `downstream: WebAppDownstreamInput!`, `upstream: WebAppUpstreamInput!`, `requestHeaderRewrites: [KeyValueInputObject!]` |
| DNS filtering | `dnsFilteringProfileCreate(name!)`, `dnsFilteringProfileUpdate(id!, name, priority: Float, fallbackMethod, allowedDomains, deniedDomains, groups: [String!], content/security/privacyCategoryConfig)`, `dnsFilteringProfileDelete` |
| Serial numbers | `serialNumbersCreate(serialNumbers: [String!]!)` → `entities`, `serialNumbersDelete(serialNumbers: [String!]!)` |

Note the gateway-resource mutations reuse the access-related args (`groupIds`, `securityPolicyId`,
`accessPolicy`, `approvalMode`, approver groups, `tags`), and `resourceAccessAdd/Set/Remove` work
on them too (they take any `Resource` ID).

---

## 9. Input Types

```graphql
input ProtocolsInput {           # ALL THREE fields are required when you pass protocols
  allowIcmp: Boolean!
  tcp: ProtocolInput!
  udp: ProtocolInput!
}
input ProtocolInput {
  policy: ProtocolPolicy!        # ALLOW_ALL | RESTRICTED
  ports: [PortRangeInput!]! = [] # used only when RESTRICTED; RESTRICTED + [] = NO ports allowed
}
input PortRangeInput { start: Int!  end: Int! }   # inclusive, 1–65535; start == end for one port

input AccessInput {
  principalId: ID!               # Group or Service Account
  securityPolicyId: ID           # omitted = unchanged; null = removed
  expiresAt: DateTime            # omitted = unchanged; null = removed
  accessPolicy: AccessPolicyInput
  approvalMode: AccessApprovalMode
}
input AccessPolicyInput { mode: AccessMode!  durationSeconds: Int }
input TagInput { key: String!  value: String! }
input KeyValueInputObject { key: String!  value: String! }
input KubernetesDownstreamInput { port: Int! }   # same shape: KubernetesUpstreamInput, SSH*Input
input WebAppDownstreamInput { port: Int!  tlsMode: TLSServerMode }
input WebAppUpstreamInput   { port: Int!  tlsMode: TLSClientMode }
```

**Example — HTTPS only, no UDP, no ICMP:**
```graphql
protocols: {
  allowIcmp: false
  tcp: { policy: RESTRICTED, ports: [{ start: 443, end: 443 }] }
  udp: { policy: RESTRICTED, ports: [] }
}
```
To allow everything, omit `protocols` entirely (or pass `ALLOW_ALL` for both with `allowIcmp: true`).
