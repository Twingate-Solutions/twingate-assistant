<!-- manual-reference: do-not-overwrite -->
# Automation paths

For every task, pick the path from `meta.assist_level` and `meta.scripting`, then generate what's
needed **at the time of the work, from the state file**. The plugin ships no complete deployment
scripts — each environment is different, and a pre-built script goes stale.

## Choosing a path

| Path | Use when | Who executes |
|---|---|---|
| Admin console | `assist_level: handhold`/`checklist`, small tenants, one-off steps, anything the API can't do | Admin, with click paths from the owning skill's references |
| Claude runs API calls | Claude Code or Cowork with a local shell, `assist_level: automate`, token in an env var | Claude, after showing the exact plan and getting an explicit yes |
| Generated Python | Admin wants a repeatable script, or Claude can't run commands in this environment | Admin (or Claude with approval) |
| Generated PowerShell | Only when `environment.windows_only: yes` **and** the admin chose PowerShell when asked | Admin (or Claude with approval) |
| Terraform / Pulumi | `meta.scripting` is terraform/pulumi, or `meta.existing_iac` is set | Admin's pipeline; the plan output is the approval artifact |

## API calls (Claude-run or generated)

- Load **twingate-api**. Grep its references for the exact query/mutation in the schema file and
  start from its recipes. Never write a query or mutation shape from memory.
- Token scopes by phase: Read for discovery and read-back; Read+Write for creating networks,
  resources and access; Provision (connector tokens, service-account keys) stays with a human on
  the connector host. Confirm current scope names in twingate-api.
- The token lives in an env var (`TWINGATE_API_KEY`), never in chat, scripts, or the state file.
- Before any mutation: show a table of exactly what will be created (name, address, network,
  ports, groups), get an explicit yes, log it in `decisions`. Approval for one batch does not
  carry over to the next.
- Idempotency: read first, skip what already exists (match networks by name, resources by
  address within a network), never modify or delete existing objects unless the admin asks.
- After every write: read back through the API and diff against the state file; record mismatches
  as open questions; set `twingate_id`s from the read-back, not from assumptions.
- Generated Python: standard library only (`urllib.request`, `json`) so it runs anywhere with no
  installs; pagination and 429 handling as in the twingate-api recipes.

## Terraform / Pulumi

- If `meta.existing_iac` is set, **add Twingate to the admin's existing code**: read their repo
  layout, provider/backend conventions, and naming first; add the Twingate provider and resources
  alongside, rather than producing a parallel standalone module.
- Load **twingate-terraform** or **twingate-pulumi** for provider version, resource names and
  arguments. For cloud-specific connector hosting, delegate per `agent-delegation.md`.
- Generate from the confirmed catalog only (`inferred` items excluded). Group IDs come from the
  state file's `groups` (synced groups are referenced, not created).
- The `terraform plan` / `pulumi preview` output is the approval artifact — log approval in
  `decisions` before `apply`.

## Connectors

Connector deployment is platform-specific and needs Provision-scope tokens. Load
**twingate-connectors** and grep its references for the platform (docker, systemd, hyper-v, ecs,
aci, helm…) — reference implementations exist for many platforms; search before writing a new
one. Cloud platforms: delegate to the matching deployer agent. Connector tokens are generated and
used on the host by the admin, never pasted into chat or stored.

## Check what the API can do first

Some objects are console-only or only partly exposed (for example, security-policy rules). Grep
the twingate-api schema for the object before promising automation; if the API can't do it, the
task becomes an admin-console task with click paths from the owning skill.

## What not to automate

- Assigning groups to the Twingate app inside the IdP — the admin does that in the IdP.
- Creating MANUAL groups to stand in for missing synced groups — only if the admin explicitly
  chooses it, recorded in `decisions`.
- Anything destructive (delete, access replacement) unless the admin asks for it specifically.
