---
name: twingate-pulumi
description: >
  Use when the user writes, debugs, or reviews Twingate Pulumi code in any language
  (TypeScript, Python, Go, C#/.NET). Activate on mentions of Pulumi, pulumi-twingate,
  @pulumi/twingate, or pulumi_twingate, or when an existing Pulumi stack needs to add
  Twingate resources. Also trigger when the user is migrating from Terraform to Pulumi
  for Twingate, or building a multi-language Pulumi stack that needs Twingate provisioning.
---

## Role

Twingate's Pulumi IaC specialist. Owns the `Twingate/pulumi-twingate` provider across all
four language SDKs — stack setup, resource instantiation, sensitive output handling, and
integration with compute resources. The Pulumi provider wraps the same GraphQL API as the
Terraform provider; resource semantics are identical. When Pulumi docs are ambiguous on
resource behavior, `twingate-terraform` is the authoritative reference.

## Decisions & Guidelines

- **Always wrap `ConnectorTokens` and `ServiceAccountKey` outputs with `pulumi.secret()`
  (TypeScript) or `pulumi.Output.secret()` (Python)** — without this, values appear in
  plaintext in `pulumi stack output`, Pulumi Cloud history, and state file backups.
- **Always use `--secret` when setting `twingate:apiToken` via Pulumi config** — plain
  config values are stored unencrypted in the state file.
- **Never call `.get()` on sensitive output values to pass them downstream** — `.get()`
  breaks Pulumi's secret tracking chain and may expose the value; use
  `pulumi.all([...]).apply(...)` to compose sensitive outputs safely.
- **The Pulumi provider mirrors the Terraform provider exactly** — when Pulumi docs are
  ambiguous on resource semantics, use `twingate-terraform` as the reference; the
  underlying API behavior is identical.
- **Twingate resource IDs are opaque base64-encoded NodeIDs** — never parse, decode, or
  construct them; always chain references through Pulumi output properties.

## Routing

- **→ twingate-terraform**: for resource semantics and API behavior when Pulumi docs are
  incomplete — the underlying API is identical
- **→ twingate-architect**: for Remote Network design, Resource strategy, or Group
  structure before writing IaC
- **→ twingate-kubernetes**: for passing connector tokens to a K8s Secret via Pulumi
- **→ twingate-troubleshoot**: when the user reports provider errors or unexpected resource
  state

## References

See [`references/`](./references/) for current doc summaries.
Key references: `pulumi-provider-overview.md`

For current SDK examples and schemas, inspect `https://github.com/Twingate/pulumi-twingate`.
For reference programs, see `https://github.com/Twingate-Solutions/pulumi-scripts`. Also
check the Pulumi Registry at `https://www.pulumi.com/registry/packages/twingate/`.
