<!-- manual-reference: do-not-overwrite -->
# Twingate GraphQL Recipes

Copy-and-adapt snippets for common onboarding operations. Verified against
`graphql-schema.graphql` (2026-11). Field reference: `graphql-schema-reference.md`.

## Rules

1. **Snippets are illustrative.** Grep `graphql-schema.graphql` to confirm every field and
   argument before running — the schema changes.
2. **Never hardcode tokens.** Read `TWINGATE_API_KEY` / `TWINGATE_NETWORK` from the environment.
3. **Always check `ok`.** On `ok: false`, surface `error` (a plain String) and stop. Also check the
   top-level `errors` array for schema/validation failures.
4. **Always paginate** every list, and nested lists when their `pageInfo.hasNextPage` is true.
5. **Show the admin a plan and get explicit approval before any mutation.** List exactly what will
   be created/changed (names, IDs, groups, protocols) first. Reads need no approval.
6. **Prefer a Read-scoped token for reads.** Use Write only for mutations; Provision only for
   `connectorGenerateTokens` / service account keys.
7. Mutations take **flat arguments** (no `input:` object).

---

## Shared helpers

### Python (stdlib only)

```python
import json, os, time, urllib.error, urllib.request

NETWORK = os.environ["TWINGATE_NETWORK"]          # tenant subdomain, e.g. "acme"
API_KEY = os.environ["TWINGATE_API_KEY"]          # never hardcode
URL = f"https://{NETWORK}.twingate.com/api/graphql/"


def gql(query: str, variables: dict | None = None, retries: int = 5) -> dict:
    """POST a GraphQL request; retry on 429 honouring Retry-After; raise on GraphQL errors."""
    body = json.dumps({"query": query, "variables": variables or {}}).encode()
    for attempt in range(retries):
        req = urllib.request.Request(URL, data=body, method="POST", headers={
            "X-API-KEY": API_KEY, "Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                payload = json.load(resp)
        except urllib.error.HTTPError as exc:
            if exc.code == 429 and attempt < retries - 1:
                time.sleep(float(exc.headers.get("Retry-After") or 2 ** attempt))
                continue
            raise
        if payload.get("errors"):
            raise RuntimeError(payload["errors"])
        return payload["data"]
    raise RuntimeError("rate limited: retries exhausted")


def paginate(query: str, root: str, variables: dict | None = None) -> list[dict]:
    """Collect every node of top-level connection `root`. Query must take $after."""
    nodes, after = [], None
    while True:
        conn = gql(query, {**(variables or {}), "after": after})[root]
        nodes += [edge["node"] for edge in conn["edges"]]
        if not conn["pageInfo"]["hasNextPage"]:
            return nodes
        after = conn["pageInfo"]["endCursor"]


def mutate(query: str, variables: dict, field: str) -> dict:
    """Run a mutation (only after admin approval) and enforce the ok/error contract."""
    result = gql(query, variables)[field]
    if not result["ok"]:
        raise RuntimeError(f"{field} failed: {result['error']}")
    return result
```

Usage: `groups = paginate(LIST_GROUPS, "groups")`.

### curl pattern

```bash
curl -sS -X POST "https://${TWINGATE_NETWORK}.twingate.com/api/graphql/" \
  -H "X-API-KEY: ${TWINGATE_API_KEY}" -H "Content-Type: application/json" \
  -d '{"query":"query($after:String){ groups(first:50, after:$after){ pageInfo{hasNextPage endCursor} edges{node{id name}} } }","variables":{"after":null}}'
```

curl does not paginate or retry — loop on `endCursor` and back off on HTTP 429 yourself.

---

## Reads

### List groups (with member count)

```graphql
query ListGroups($after: String) {
  groups(first: 50, after: $after) {
    pageInfo { hasNextPage endCursor }
    edges { node {
      id name type isActive
      users { totalCount }
      securityPolicy { id name }
    } }
  }
}
```
Optional: `groups(first: 50, after: $after, filter: { type: { in: [MANUAL] } })`.

### List remote networks

```graphql
query ListRemoteNetworks($after: String) {
  remoteNetworks(first: 50, after: $after) {
    pageInfo { hasNextPage endCursor }
    edges { node {
      id name networkType location isActive
      connectors { totalCount }
      resources { totalCount }
    } }
  }
}
```

### Find a remote network by name

```graphql
query FindRemoteNetwork($name: String!) {
  remoteNetwork(name: $name) { id name networkType location isActive }
}
```
Returns `null` when absent. Case-insensitive alternative:
`remoteNetworks(first: 10, filter: { name: { ieq: $name } })`.

### List connectors with state and remote network

```graphql
query ListConnectors($after: String) {
  connectors(first: 50, after: $after) {
    pageInfo { hasNextPage endCursor }
    edges { node {
      id name state version hostname lastHeartbeatAt publicIP privateIPs
      remoteNetwork { id name }
    } }
  }
}
```
Only unhealthy: add `filter: { state: { in: [DEAD_NO_HEARTBEAT, DEAD_HEARTBEAT_TOO_OLD, DEAD_NO_RELAYS] } }`.

### List resources with address, network, protocols and access

```graphql
query ListResources($after: String) {
  resources(first: 50, after: $after) {
    pageInfo { hasNextPage endCursor }
    edges { node {
      __typename id name alias isActive
      address { type value }
      remoteNetwork { id name }
      protocols {
        allowIcmp
        tcp { policy ports { start end } }
        udp { policy ports { start end } }
      }
      securityPolicy { id name }
      access(first: 50) {
        totalCount
        pageInfo { hasNextPage endCursor }
        edges {
          securityPolicy { id name }
          expiresAt
          node {
            __typename
            ... on Group { id name }
            ... on ServiceAccount { id name }
          }
        }
      }
    } }
  }
}
```
`access` replaces the deprecated `groups` / `serviceAccounts` fields. If a resource's
`access.pageInfo.hasNextPage` is true, page it with `resource(id:) { access(first: 50, after: ...) }`.
Scope to one network: `filter: { remoteNetworkId: { eq: $rnId } }`.

---

## Writes (plan → approval → run → check `ok`)

### Create a remote network

```graphql
mutation CreateRemoteNetwork($name: String!, $location: RemoteNetworkLocation) {
  remoteNetworkCreate(name: $name, location: $location) {
    ok error
    entity { id name location networkType }
  }
}
```
Variables: `{"name": "AWS us-east-1 Prod", "location": "AWS"}`. Check first with
*Find a remote network by name* to stay idempotent.

### Create a resource with protocols and groups

```graphql
mutation CreateResource($name: String!, $address: String!, $rn: ID!,
                        $groupIds: [ID], $protocols: ProtocolsInput) {
  resourceCreate(name: $name, address: $address, remoteNetworkId: $rn,
                 groupIds: $groupIds, protocols: $protocols) {
    ok error
    entity { id name address { value } }
  }
}
```
Variables:
```json
{
  "name": "Prod Postgres", "address": "db.prod.internal", "rn": "<remoteNetworkId>",
  "groupIds": ["<groupId>"],
  "protocols": {
    "allowIcmp": false,
    "tcp": {"policy": "RESTRICTED", "ports": [{"start": 5432, "end": 5432}]},
    "udp": {"policy": "RESTRICTED", "ports": []}
  }
}
```
`protocols` needs all three keys if passed; omit it to allow all ports. `RESTRICTED` with `[]`
blocks that protocol entirely.

### Grant access with a security policy (`resourceAccessAdd`)

```graphql
mutation AddAccess($resourceId: ID!, $access: [AccessInput!]!) {
  resourceAccessAdd(resourceId: $resourceId, access: $access) {
    ok error
    entity { id name }
  }
}
```
Variables: `{"resourceId": "<id>", "access": [{"principalId": "<groupId>", "securityPolicyId": "<policyId>"}]}`.
Adds or reconfigures edges without touching others. **Do not** use `resourceAccessSet` for this —
it removes every principal not in the list. Look up policy IDs with
`securityPolicy(name: "...") { id }` or `securityPolicies(first: 50)`.

### Checking the result

```python
res = mutate(CREATE_RESOURCE, variables, "resourceCreate")   # raises on ok == false
resource_id = res["entity"]["id"]
```
Report `error` verbatim to the admin; do not retry a failed mutation blindly (it may be a
duplicate name or invalid ID, not a transient fault). Only HTTP 429 is safe to auto-retry.
