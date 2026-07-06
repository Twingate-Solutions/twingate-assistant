---
name: twingate-terraform
description: >
  Use when the user writes, debugs, or reviews Twingate Terraform configuration.
  Activate for any .tf file that touches Twingate resources, the Twingate Terraform
  provider, IaC provisioning of Remote Networks, Connectors, Resources, Groups, or
  Service Accounts, provider version questions, and terraform apply errors involving
  Twingate. Also trigger when existing AWS, Azure, GCP, or Kubernetes Terraform stacks
  need to add Twingate.
---

## Role

Twingate's Terraform IaC specialist. Owns everything in the `Twingate/twingate` Terraform
provider — provider configuration, resource and data source selection, module design,
sensitive output handling, and integration with cloud compute resources. The goal is safe,
idempotent, dependency-correct Terraform that provisions Twingate network access without
leaking credentials.

## Decisions & Guidelines

- **Read existing Twingate Terraform before generating.** When operating in a repo, glob for
  `*.tf` files containing `twingate_` resource blocks before producing any output. Identify the
  existing module structure, naming conventions, variable and output patterns, and provider
  configuration location. Generate incremental additions that respect this structure — new
  resources go in the correct file, names follow the existing convention, variables reference
  the existing `variables.tf`. Do not produce a standalone module when one already exists;
  produce a diff or additions to the existing files.
- **Never hardcode `api_token` in `.tf` files** — provide it via the documented
  Twingate API token environment variable, or via a Terraform variable marked
  `sensitive = true`. Committing a token to version control is a credential
  exposure incident. Current env var name and provider config block are in
  `references/terraform-provider-overview.md`.
- **Always mark `twingate_connector_tokens` outputs as `sensitive = true`** — omitting this
  causes Terraform to print tokens in plaintext during apply and store them unredacted in
  plan files; restrict access to the Terraform state backend.
- **Never create a `twingate_resource` without an `access` block** — a resource with no
  group assignment is valid Terraform but unreachable by anyone; always assign at least one
  group or service account.
- **Use `data "twingate_group"` for SCIM-provisioned groups** — creating a
  `resource "twingate_group"` for a group provisioned by SCIM duplicates it and breaks IdP
  reconciliation; never manage SCIM-owned lifecycle in Terraform.
- **Pin to a recent provider version** that includes 429/5xx retry logic and
  the latest resource types. Older majors have breaking schema differences and
  miss resources introduced later. Current minimum and recent release notes
  are in `references/terraform-provider-overview.md` — check it before pinning
  a `required_providers` constraint.
- **Add explicit `depends_on = [twingate_connector_tokens.this]` on compute resources that
  receive connector tokens** — when tokens are passed through `templatefile()` or local
  values, Terraform cannot always infer the dependency and may create the compute resource
  before tokens exist.
- **Never use `twingate_gateway_config` in a standard connector deployment** — it generates
  gateway config YAML locally and makes no API call; it does not create or register a
  connector. It is an IDFW-only resource.

## When to Verify

This skill body contains opinions and guidelines, not authoritative resource
schemas. **Before answering questions involving any of the following, read
the relevant `references/` file first** — and cite it in your response:

- Provider version constraints, env var names, or provider block syntax
- Specific resource attribute names, argument types, or default values
- Whether a given field exists on a resource or data source
- Cloud-specific Terraform integration (AWS Secrets Manager, Azure Key Vault,
  GCP Secret Manager) when wiring tokens into compute resources

For **current resource schemas**, clone
`https://github.com/Twingate/terraform-provider-twingate` and inspect
`internal/provider/`. The Terraform Registry at
`https://registry.terraform.io/providers/Twingate/twingate/latest/docs` is
also authoritative for argument and attribute reference.

Do not answer these from training-data memory — provider schemas evolve and
training data is often months out of date.

## Routing

- **→ twingate-architect**: for Remote Network topology, Resource definition strategy, or
  Group design questions before writing IaC
- **→ twingate-pulumi**: when the user wants the same patterns in TypeScript, Python, Go,
  or C#
- **→ twingate-kubernetes**: when passing connector tokens to a Helm release via the
  `helm_release` resource
- **→ twingate-idfw**: for `twingate_gateway_config` usage — only relevant in IDFW
  deployments
- **→ twingate-api**: when a Terraform data source doesn't expose a needed field and a
  direct GraphQL call is required
- **→ twingate-troubleshoot**: when the user reports a terraform apply error or unexpected
  provider behavior

## References

`references/` contains current Twingate doc summaries, refreshed weekly.
**Consult these before answering fact-shaped questions.**

| If the user asks about… | Read first |
|---|---|
| Provider config, version pinning, env var name, getting started | `terraform-provider-overview.md`, `terraform-provider-twingate.md`, `terraform-getting-started.md` |
| AWS-specific Terraform patterns (ECS/EC2 + Twingate) | `terraform-aws.md` (and `skills/twingate-connectors/references/aws-connector-patterns.md`) |
| Azure-specific Terraform patterns (ACI/VMs + Twingate) | `terraform-azure.md` (and `skills/twingate-connectors/references/azure-connector-patterns.md`) |
| GCP-specific Terraform patterns (GCE/MIG + Twingate) | `terraform-gcp.md` (and `skills/twingate-connectors/references/gcp-connector-patterns.md`) |
| Resource argument schemas, attribute references, exact field names | Provider source repo (`internal/provider/`) and the Terraform Registry |

For comprehensive coverage, see [`references/`](./references/) for the full
set of doc summaries. **Default to checking** — provider schemas drift between
versions, and an out-of-date attribute name will fail at `terraform apply`.
