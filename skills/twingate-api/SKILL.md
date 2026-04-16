---
name: twingate-api
description: >
  Twingate GraphQL API, CLI tools, and automation. Load when the user wants to
  automate Twingate via the API, write scripts against the GraphQL endpoint,
  generate or manage API tokens, use the Twingate CLI tools, or build automation
  pipelines. Also trigger on 'GraphQL', 'X-API-KEY', 'Twingate API', 'api/graphql',
  'service account key', 'connector token provisioning', 'rate limiting', or any
  Twingate admin API mention.
---

## Role

This skill owns Twingate's GraphQL API, service account key management, CLI tooling, and API-driven automation. It covers scripting, CI/CD pipeline integration, pagination, rate limiting, token permissioning, and the programmatic path for connector and service account credential provisioning. It does not replace IaC — use it for scripting and automation, not for managing long-lived Twingate objects that need lifecycle tracking.

## Decisions & Guidelines

- **Always check `ok` before reading `entity` in a mutation response.** A mutation can return HTTP 200 with `ok: false` and `entity: null`. Reading entity fields without checking `ok` first causes null reference errors or silent data corruption. Check `error.errorCode` and `error.message` on failure.
- **Always paginate — never assume all results fit in one page.** Scripts that omit pagination silently miss records with no error. You may get 50 of 500 resources. Loop on `pageInfo.hasNextPage` until `false`, passing `pageInfo.endCursor` as the `after` argument on each request.
- **Never parse, decode, or construct IDs.** Twingate IDs are opaque base64-encoded NodeIDs. Use them only as returned by the API. Never infer numeric components from base64 decoding.
- **Issue the least-privileged token for the task.** Read for monitoring/reporting. Write for provisioning. Provision only for `connectorGenerateTokens` and service account key generation. Never issue Provision-level tokens to read-only scripts.
- **`connectorGenerateTokens` rotates credentials on an existing Connector.** Calling it again on a deployed Connector invalidates the current tokens and the Connector stops working until restarted with the new tokens. Only call this when reprovisioning credentials — never as a "refresh" operation.
- **Prefer Terraform or Pulumi over raw GraphQL for persistent configuration management.** The API is the right tool for scripting, automation, and reporting. IaC is better for long-lived Twingate objects that need lifecycle tracking and drift detection.
- **Implement 429 retry with `Retry-After` backoff from the start, not as an afterthought.** The API enforces per-minute rate limits. Scripts that ignore 429 fail mid-run on large operations. The Terraform and Pulumi providers handle this automatically — raw scripts must not ignore it.
- **Service account keys expire — build rotation logic into any pipeline that uses them.** Monitor `expiresAt` and rotate before expiry. Reactive rotation on failure disrupts pipelines.

## Routing

- **→ twingate-terraform / twingate-pulumi**: when the user wants persistent IaC management rather than API scripting — IaC provides drift detection, audit trail, and lifecycle management that raw API scripts do not
- **→ twingate-architect**: for understanding what resources, remote networks, groups, and connectors are before writing API automation against them
- **→ twingate-connectors**: for `connectorGenerateTokens` context — token provisioning is an API operation, but the Connector deployment specifics (runtime env vars, restart behavior) live in twingate-connectors

## References

See [`references/`](./references/) for auto-generated doc summaries and the static schema file.

Key references:
- [`graphql-schema-reference.md`](./references/graphql-schema-reference.md) — hand-maintained full type definitions, field signatures, enum values, input types, and all query/mutation signatures; read this before writing any API code
