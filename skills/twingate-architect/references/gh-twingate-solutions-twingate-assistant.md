---
source: https://github.com/Twingate-Solutions/twingate-assistant
type: github
fetched: 2026-08-23
source_version: 1c12d13260d61cf7101bdb071e7d5abd5acce0c6
---

# twingate-assistant

## Summary
A Claude Code plugin that embeds Twingate ZTNA domain expertise into Claude Code sessions. It provides skills (auto-loaded domain knowledge) and agents (explicit end-to-end workflow orchestrators) covering architecture design, IaC generation, and troubleshooting. Documentation is refreshed weekly via GitHub Actions from Twingate's public docs and GitHub orgs.

## Key Information
- Plugin type: Claude Code marketplace plugin
- IaC support: Terraform and Pulumi
- Cloud targets: AWS, Azure, GCP, Kubernetes
- License: Apache 2.0
- Auto-updates: Weekly GitHub Action refreshes skill reference docs
- Context persistence: Supports committing a `twingate-context.md` file to persist environment details across sessions

## Prerequisites
- Claude Code installed and configured
- Access to the Claude Code plugin marketplace
- (For IaC generation) Terraform or Pulumi CLI with appropriate cloud credentials

## Usage / Step-by-Step

**Install:**
```bash
/plugin marketplace add Twingate-Solutions/twingate-assistant
/plugin install twingate-assistant@twingate-solutions
```

**Update:** Re-run the same `/plugin install` command.

**Invoke an agent:**
```text
Use the twingate-se agent to help me deploy Twingate to my AWS environment.
Use the aws-deployer agent to generate Terraform for two HA connectors in us-east-1.
Use the network-designer agent to plan our resource structure for three environments.
```

**Persist environment context:**
```text
Use the twingate-se agent to document my current Twingate deployment as twingate-context.md.
```
Commit the resulting file; future sessions load it automatically.

**Invoke a skill explicitly:**
```bash
/skill twingate-troubleshoot
```

## Configuration Values

| Item | Value/Notes |
|---|---|
| Context template | `docs/twingate-context-template.md` |
| Maintenance docs | `docs/MAINTAINING.md` |
| Contribution docs | `CONTRIBUTING.md` |
| Skill references dir | `references/` inside each skill directory |

## Available Skills (auto-load on topic detection)
`twingate-architect`, `twingate-connectors`, `twingate-terraform`, `twingate-pulumi`, `twingate-kubernetes`, `twingate-idfw`, `twingate-identity`, `twingate-api`, `twingate-dns-security`, `twingate-troubleshoot`

## Available Agents (explicit invocation)
`twingate-se`, `aws-deployer`, `azure-deployer`, `gcp-deployer`, `network-designer`, `idfw-deployer`

## Gotchas
- Skills activate automatically on keyword detection — no explicit invocation needed in most cases, but you can force them with `/skill <name>`
- Environment context (`twingate-context.md`) must be committed to the repo to persist across sessions; it is not stored by the plugin itself
- Plugin updates require manually re-running `/plugin install` — no automatic in-session updates
- Reference docs are summaries, not live API calls; there is a lag between Twingate releasing changes and the weekly refresh running

## Skill Reference Notes (selected, as of 2026-08-16 refresh)

### twingate-api / GraphQL API
- Endpoint: `https://<network-name>.twingate.com/api/graphql/`; auth via `X-API-KEY` header
- Mutation responses return `ok`, `error`, and optionally `entity`
- `securityPolicyId: null` resets to Default Policy; omitting leaves unchanged — distinct behaviors
- `alias: null` clears alias; omitting leaves unchanged
- `tags: null` removes all tags; omitting leaves unchanged
- `resourceAccessSet` replaces **all** existing access entries
- `remoteNetwork` query accepts `id` OR `name`, not both required simultaneously

### twingate-api / JavaScript CLI (`tg`)
- Community-maintained; not supported by Twingate product engineering
- Binaries for Windows/Mac/Linux; extensible for Node/Deno
- IDs are base64-encoded GraphQL node IDs
- `connector create` returns `ACCESS_TOKEN` and `REFRESH_TOKEN