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

## When to Verify

This skill body contains automation patterns and guidelines, not the schema.
**Before writing any API code or answering questions involving any of the
following, read `references/graphql-schema-reference.md` first** — this is
the authoritative type and field reference and must be consulted for every
non-trivial query or mutation:

- Exact query/mutation names, argument names, or argument types
- Field names on response objects (including nested fields and pagination structures)
- Enum values for any field (e.g., resource protocol enums, address-type enums)
- Input type structure for create/update mutations
- Whether a given field exists, is nullable, or is deprecated

For **CLI tooling** (Python `tg-cli`, JavaScript `tg-cli`, OpenClaw),
read the corresponding CLI reference before suggesting commands — flag
names and subcommand structure differ between tools.

Do not answer schema or CLI questions from training-data memory — the
schema evolves and CLI tools have version-specific syntax.

## Routing

- **→ twingate-terraform / twingate-pulumi**: when the user wants persistent IaC management rather than API scripting — IaC provides drift detection, audit trail, and lifecycle management that raw API scripts do not
- **→ twingate-architect**: for understanding what resources, remote networks, groups, and connectors are before writing API automation against them
- **→ twingate-connectors**: for `connectorGenerateTokens` context — token provisioning is an API operation, but the Connector deployment specifics (runtime env vars, restart behavior) live in twingate-connectors

## References

`references/` contains the static GraphQL schema (hand-maintained, authoritative)
and current Twingate doc summaries refreshed weekly. **Consult these before
answering fact-shaped questions.**

| If the user asks about… | Read first |
|---|---|
| Query/mutation signatures, field names, enum values, input types | `graphql-schema-reference.md` (authoritative) |
| API overview, authentication, getting started | `api-overview.md`, `api.md`, `getting-started-with-the-api.md` |
| Exploring the API, sample queries | `exploring-the-apis.md` |
| Python CLI (`tg-cli`) | `introduction-to-the-python-cli.md` |
| JavaScript CLI (`tg-cli`) | `introduction-to-tg-cli-javascript.md` |
| OpenClaw automation tool (general, Docker Compose, DigitalOcean) | `openclaw.md`, `openclaw-docker-compose.md`, `openclaw-digitalocean.md` |
| CI/CD pipeline patterns | `example-cicd-configurations.md` |
| General automation script examples | `general-scripts.md` |

For comprehensive coverage, see [`references/`](./references/) for the full
set of doc summaries. **Default to checking the schema** — never write a
query or mutation from memory; field names and enum values change.
