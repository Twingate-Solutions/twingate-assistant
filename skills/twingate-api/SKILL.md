---
name: twingate-api
description: |
  Twingate GraphQL API, CLI tools, and automation. Use this skill when the user
  wants to automate Twingate via the API, write scripts, use the GraphQL endpoint,
  generate API tokens, or use the Twingate CLI tools. Also trigger on 'GraphQL',
  'X-API-KEY', 'Twingate API', or any admin API mention.
---

# Twingate API

## When to Use This Skill

Trigger this skill when the user:

- Asks how to use the Twingate GraphQL API or wants the API endpoint URL
- Wants to automate resource, group, connector, or user management via script or pipeline
- Needs to generate or manage API tokens, service account keys, or connector tokens programmatically
- Is writing a script, GitHub Action, or CI/CD step that calls the Twingate API
- Asks about pagination, rate limiting, or error handling with the Twingate API
- Mentions `X-API-KEY`, `graphql`, `api/graphql`, or any Twingate admin API endpoint
- Wants to use the Twingate CLI (`tg-cli` or the Python CLI)
- Is building IaC with the Terraform or Pulumi provider and needs to understand the underlying API
- Needs to approve or reject access requests programmatically
- Wants to create, provision, or revoke service account keys

## Quick Reference

| Concern | Value |
|---|---|
| Endpoint | `https://{network}.twingate.com/api/graphql` |
| Auth header | `X-API-KEY: <token>` |
| Protocol | GraphQL over HTTPS (POST) |
| Content-Type | `application/json` |
| Pagination style | Relay cursor (`first`/`after`, `last`/`before`) |
| Rate limit response | HTTP 429 with `Retry-After` header |
| All IDs | Opaque base64-encoded NodeIDs — never parse |
| Mutation response | `{ ok, error { errorCode, message }, entity }` — always check `ok` first |

**Token permission levels:**
| Level | Permits |
|---|---|
| Read | List and get operations (queries only) |
| Write | Create, update, delete resources, networks, groups, users |
| Provision | Generate connector tokens, create and revoke service account keys |

Always issue the least-privileged token for the task. A monitoring script needs Read only. A provisioning pipeline needs Provision. Never use a Provision-level token in an application that only needs to read.

## Evergreen Knowledge

### Endpoint and Authentication

The GraphQL endpoint is `https://{network}.twingate.com/api/graphql` where `{network}` is the tenant subdomain — the same one used to reach the admin console. All requests are POST with a JSON body.

Authentication uses the `X-API-KEY` header. Generate tokens from the admin console under **Settings → API**. There is no OAuth, no Basic auth, no session cookie — it is always the API key header. Treat API keys as secrets: store them in environment variables or a secrets manager, never in source code or config files.

### Token Permission Levels

Three token levels exist — always issue the minimum level needed:

- **Read** — list and get queries. Use for monitoring, reporting, and audit scripts.
- **Write** — creates, updates, and deletes for resources, remote networks, groups, and user management. Use for provisioning workflows that manage the Twingate configuration.
- **Provision** — everything in Write, plus the ability to call `connectorGenerateTokens` and create/revoke service account keys. Use only in infrastructure provisioning pipelines. This level can produce credentials that grant network access, so scope its use carefully.

### Pagination

All list fields use Relay cursor-based pagination. Never assume all results fit in one page — always paginate.

**Pattern:**
- Use `first` (and optionally `after`) for forward pagination.
- After each page, check `pageInfo.hasNextPage`.
- If `true`, pass `pageInfo.endCursor` as the `after` argument on the next call.
- Repeat until `hasNextPage` is `false`.

Example — paginated resource list:

```graphql
query ListResources($after: String) {
  resources(first: 50, after: $after) {
    edges {
      node {
        id
        name
        address {
          value
        }
        isActive
      }
    }
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
```

```python
import os
import requests

ENDPOINT = f"https://{os.environ['TG_NETWORK']}.twingate.com/api/graphql"
HEADERS = {"X-API-KEY": os.environ["TG_API_KEY"], "Content-Type": "application/json"}

QUERY = """
query ListResources($after: String) {
  resources(first: 50, after: $after) {
    edges { node { id name address { value } isActive } }
    pageInfo { hasNextPage endCursor }
  }
}
"""

def list_all_resources() -> list[dict]:
    """Return all resources, handling pagination."""
    resources = []
    after = None
    while True:
        resp = requests.post(
            ENDPOINT,
            headers=HEADERS,
            json={"query": QUERY, "variables": {"after": after}},
        )
        resp.raise_for_status()
        data = resp.json()["data"]["resources"]
        resources.extend(edge["node"] for edge in data["edges"])
        if not data["pageInfo"]["hasNextPage"]:
            break
        after = data["pageInfo"]["endCursor"]
    return resources
```

### Mutation Response Pattern

Every mutation returns a payload with three fields:

```graphql
{
  ok        # Boolean — true if the operation succeeded
  error {
    errorCode   # Machine-readable code (e.g., "NOT_FOUND", "ALREADY_EXISTS")
    message     # Human-readable description
  }
  entity    # The created/updated object — only valid when ok is true
}
```

**Always check `ok` before reading `entity`.** If `ok` is false, `entity` may be null. Read `error.errorCode` and `error.message` to understand the failure.

Example — create a resource with error handling:

```python
MUTATION = """
mutation CreateResource($input: ResourceCreateInput!) {
  resourceCreate(input: $input) {
    ok
    error { errorCode message }
    entity {
      id
      name
    }
  }
}
"""

def create_resource(name: str, address: str, remote_network_id: str) -> str:
    """Create a resource and return its ID. Raises on failure."""
    resp = requests.post(
        ENDPOINT,
        headers=HEADERS,
        json={
            "query": MUTATION,
            "variables": {
                "input": {
                    "name": name,
                    "address": {"value": address},
                    "remoteNetworkId": remote_network_id,
                }
            },
        },
    )
    resp.raise_for_status()
    result = resp.json()["data"]["resourceCreate"]
    if not result["ok"]:
        err = result["error"]
        raise RuntimeError(f"resourceCreate failed [{err['errorCode']}]: {err['message']}")
    return result["entity"]["id"]
```

### IDs

All IDs in the Twingate API are opaque base64-encoded NodeIDs (e.g., `UmVzb3VyY2U6MTIz`). They are not meaningful — never parse, decode, or construct them. Use IDs exactly as returned by the API or as copied from admin console URLs. Pass them verbatim to mutation input fields.

### Rate Limits

The API enforces per-minute rate limits. When a limit is exceeded, the response is HTTP 429 with a `Retry-After` header indicating how many seconds to wait before retrying.

The Terraform and Pulumi providers handle 429 retries automatically in recent versions. Python and shell scripts must implement their own retry logic. Use exponential backoff with jitter: start at the `Retry-After` value, add random jitter, cap at a reasonable maximum.

```python
import time
import random

def post_with_retry(payload: dict, max_retries: int = 5) -> dict:
    """POST to the GraphQL endpoint with 429 retry and backoff."""
    for attempt in range(max_retries):
        resp = requests.post(ENDPOINT, headers=HEADERS, json=payload)
        if resp.status_code == 429:
            retry_after = int(resp.headers.get("Retry-After", 5))
            sleep_for = retry_after + random.uniform(0, 2)
            time.sleep(sleep_for)
            continue
        resp.raise_for_status()
        return resp.json()
    raise RuntimeError("Exceeded max retries due to rate limiting")
```

### Connector Token Provisioning

`connectorGenerateTokens(connectorId: ID!)` is the programmatic path for obtaining the access and refresh tokens needed to deploy a Connector. This is what IaC tools (Terraform, Pulumi) call after `connectorCreate` to retrieve deployable credentials.

The mutation requires a **Provision-level token**. The returned tokens are sensitive — treat them exactly like passwords. Do not log them, do not store them in plaintext, and pass them to Connectors via environment variables or secrets management.

```graphql
mutation ProvisionConnector($connectorId: ID!) {
  connectorGenerateTokens(connectorId: $connectorId) {
    ok
    error { errorCode message }
    connectorTokens {
      accessToken
      refreshToken
    }
  }
}
```

The `accessToken` and `refreshToken` are passed to the Connector deployment (e.g., as `TWINGATE_ACCESS_TOKEN` and `TWINGATE_REFRESH_TOKEN` environment variables in Docker or systemd).

### Service Accounts

Service accounts are headless, machine identities for programmatic or server-to-Twingate access. They are not tied to a human user and do not require SSO. Use them for:

- CI/CD pipelines that need access to internal resources via the Twingate Client in service mode
- Server-to-server access patterns where a machine needs to reach a Twingate Resource
- Any non-human principal that requires long-lived, managed credentials

Service account keys are created with `serviceAccountKeyCreate`, which accepts an `expirationTime` in days. Keys expire automatically, so build rotation into your pipeline. Revoke keys with `serviceAccountKeyRevoke` when they are no longer needed. Monitor key expiry via the `serviceAccount` query and its `keys.edges.node.expiresAt` field.

### Key Queries

| Query | Description |
|---|---|
| `resources(first, after, filter)` | List resources with pagination |
| `resource(id: ID!)` | Get a single resource by ID |
| `remoteNetworks(first, after)` | List remote networks |
| `remoteNetwork(id: ID!)` | Get a single remote network |
| `connectors(first, after)` | List connectors |
| `connector(id: ID!)` | Get a single connector and its state |
| `groups(first, after, filter)` | List groups |
| `group(id: ID!)` | Get a single group |
| `users(first, after, filter)` | List users |
| `user(id: ID!)` | Get a single user |
| `devices(first, after)` | List devices |
| `device(id: ID!)` | Get a single device |
| `serviceAccounts(first, after)` | List service accounts |
| `serviceAccount(id: ID!)` | Get a single service account and its keys |
| `securityPolicies(first, after)` | List security policies |
| `securityPolicy(id: ID!)` | Get a single security policy |
| `accessRequests(first, after, filter)` | List access requests (pending, approved, rejected) |

### Key Mutations

| Mutation | Level | Description |
|---|---|---|
| `resourceCreate(input)` | Write | Create a new resource |
| `resourceUpdate(id, input)` | Write | Update a resource |
| `resourceDelete(id)` | Write | Delete a resource |
| `resourceAccessAdd(resourceId, principalIds)` | Write | Grant groups or service accounts access to a resource |
| `resourceAccessRemove(resourceId, principalIds)` | Write | Revoke access |
| `remoteNetworkCreate(input)` | Write | Create a remote network |
| `remoteNetworkUpdate(id, input)` | Write | Update a remote network |
| `remoteNetworkDelete(id)` | Write | Delete a remote network |
| `connectorCreate(input)` | Write | Create a connector (returns ID for token generation) |
| `connectorUpdate(id, input)` | Write | Update connector metadata |
| `connectorDelete(id)` | Write | Delete a connector |
| `connectorGenerateTokens(connectorId)` | Provision | Generate access+refresh tokens for a connector |
| `groupCreate(input)` | Write | Create a group |
| `groupUpdate(id, input)` | Write | Update a group (add/remove users, change policy) |
| `groupDelete(id)` | Write | Delete a group |
| `userUpdate(id, input)` | Write | Update user role or state |
| `userDelete(id)` | Write | Delete a user |
| `deviceUpdate(id, input)` | Write | Update device trust status |
| `serviceAccountCreate(input)` | Write | Create a service account |
| `serviceAccountUpdate(id, input)` | Write | Update a service account |
| `serviceAccountDelete(id)` | Write | Delete a service account |
| `serviceAccountKeyCreate(serviceAccountId, input)` | Provision | Create a service account key |
| `serviceAccountKeyRevoke(keyId)` | Provision | Revoke a key immediately |
| `serviceAccountKeyDelete(keyId)` | Provision | Delete a revoked key |
| `accessRequestApprove(id, input)` | Write | Approve a pending access request |
| `accessRequestReject(id, input)` | Write | Reject a pending access request |

### CLI Tools

Two CLI tools are available for scripting common Twingate operations without writing raw GraphQL:

- **tg-cli** (JavaScript) — available on GitHub. Covers most resource, group, and connector operations. Install via npm.
- **Twingate Python CLI** — available on GitHub. Wraps the GraphQL API with command-line subcommands.

Fetch the current GitHub repos at runtime to get installation instructions and command references — do not rely on cached repository URLs in this skill file.

### Static Schema Reference

The complete hand-maintained GraphQL schema reference is at `./references/graphql-schema-reference.md`. Read it for full type definitions, field signatures, enum values, input types, and all query/mutation signatures before writing any API code.

## Current Documentation

Reference files in `./references/` are auto-generated by the update pipeline and contain summaries of current Twingate API documentation. Read them for up-to-date syntax, token generation steps, and API changes.

If a reference file is missing or appears outdated, fetch the canonical doc directly:

```
curl -s https://www.twingate.com/docs/api
curl -s https://www.twingate.com/docs/twingate-api-token
curl -s https://www.twingate.com/docs/api-reference-resources
curl -s https://www.twingate.com/docs/api-reference-groups
curl -s https://www.twingate.com/docs/api-reference-connectors
curl -s https://www.twingate.com/docs/api-reference-remote-networks
```

Key doc slugs for this skill:
- `api` — API overview, endpoint, authentication
- `twingate-api-token` — generating and managing API tokens, permission levels
- `api-reference-resources` — resource query and mutation signatures
- `api-reference-groups` — group management via API
- `api-reference-connectors` — connector creation and token generation
- `api-reference-remote-networks` — remote network management

## Common Patterns

**Bulk resource audit**
Query `resources` with full pagination, collecting each resource's name, address, remote network, active state, and assigned groups. Export to CSV or push to a SIEM. Use a Read-level token. Handle pagination carefully — large tenants may have hundreds of resources across many pages.

**Connector provisioning pipeline (IaC)**
Call `connectorCreate` (Write) to register the connector in Twingate, then call `connectorGenerateTokens` (Provision) to get credentials. Pass `accessToken` and `refreshToken` to the Connector runtime (Docker env vars, Kubernetes secret, systemd environment file). Never log the tokens. This is the exact sequence the Terraform provider follows internally.

**Group sync from external directory**
Query the external directory (e.g., LDAP, HR system), compare against `groups` from the API, and reconcile via `groupCreate`, `groupUpdate` (to add/remove users), or `groupDelete`. This pattern is typically only needed when SCIM is not available. Prefer SCIM over a custom sync script — it is real-time and does not require you to manage the sync loop.

**Service account key rotation**
Query `serviceAccount(id)` to retrieve the current key's `expiresAt`. If within a rotation window (e.g., 7 days of expiry), call `serviceAccountKeyCreate` to generate a new key, update the consuming system with the new key, then call `serviceAccountKeyRevoke` on the old key. Build this as a scheduled job.

**Automated access request approval**
Poll `accessRequests` with a `PENDING` filter. For each pending request, evaluate against your organization's policy (e.g., auto-approve during business hours for certain groups). Call `accessRequestApprove` or `accessRequestReject` accordingly. Log all decisions with the request ID and approving entity.

## Anti-Patterns and Gotchas

**Issuing Provision-level tokens for read-only tasks**
A Provision token can generate Connector credentials and service account keys. Issuing it to a monitoring or reporting script is unnecessary privilege escalation. Always use Read tokens for query-only workloads.

**Not paginating**
The API returns a limited page of results by default. Scripts that omit pagination silently miss records — you may get 50 of 500 resources with no error. Always check `pageInfo.hasNextPage` and loop until exhausted.

**Parsing or constructing IDs**
IDs are opaque. Base64-decoding a Twingate ID to extract a numeric component and constructing other IDs from it is unsupported and will break. Use IDs only as received from the API.

**Reading `entity` without checking `ok`**
A mutation can return HTTP 200 with `ok: false` and `entity: null`. If you access `entity` fields without first confirming `ok` is true, you will get null reference errors or silent data corruption. Always check `ok` first.

**Ignoring 429 responses in scripts**
The API enforces rate limits. Scripts that do not handle 429 will fail mid-run on large operations. Implement retry with `Retry-After` backoff from the start, not as an afterthought.

**Storing API keys in source code or config files**
API keys are long-lived secrets. Committing them to a repository or embedding them in a YAML config file is a credential leak. Use environment variables, GitHub Actions secrets, HashiCorp Vault, or AWS Secrets Manager.

**Using `connectorGenerateTokens` on an already-deployed connector**
Calling `connectorGenerateTokens` again on an existing connector rotates the tokens. The existing Connector process will stop working until it is restarted with the new tokens. Only call this mutation when you intend to reprovision credentials.

**Assuming the GraphQL API and Terraform provider fields always match 1:1**
The Terraform provider sometimes abstracts or renames fields relative to the raw GraphQL schema. If you are working in both, verify the field name against the static schema reference (`./references/graphql-schema-reference.md`) and the provider docs separately.

## Related Skills

- [twingate-architect](../twingate-architect/SKILL.md) — architectural context for understanding what resources, remote networks, groups, and connectors are and how they relate
- [twingate-terraform](../twingate-terraform/SKILL.md) — Terraform provider uses the same API under the hood; recommend IaC over raw API for persistent configuration management
- [twingate-connectors](../twingate-connectors/SKILL.md) — `connectorGenerateTokens` is the API path for connector credential provisioning; see this skill for Connector deployment specifics
- [twingate-identity](../twingate-identity/SKILL.md) — user, group, device, and security policy management all have API counterparts covered in this skill
