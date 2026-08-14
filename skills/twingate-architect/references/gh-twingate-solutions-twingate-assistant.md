---
source: https://github.com/Twingate-Solutions/twingate-assistant
type: github
fetched: 2026-08-14
source_version: c40147a5198ba8b84faeb9e5e1f8c6b2bb75c94c
---

# twingate-assistant

## Summary
A Claude Code plugin that gives Claude Code Twingate ZTNA implementation expertise — architecture design, deployment playbooks, IaC generation, and troubleshooting. Once installed, any Claude Code session can act as a Twingate solutions engineer: assess an environment, design Remote Networks, generate Terraform or Pulumi, and walk through connector deployments on AWS, Azure, GCP, or Kubernetes.

## Key Information
- Distributed as a Claude Code plugin via the `twingate-solutions` marketplace, not a runtime service — no MCP server, no live API calls.
- Adds **skills** (10 domain modules, auto-load on topic detection) and **agents** (6 orchestrators, invoked explicitly by name).
- Skills: `twingate-architect`, `-connectors`, `-terraform`, `-pulumi`, `-kubernetes`, `-idfw`, `-identity`, `-api`, `-dns-security`, `-troubleshoot`.
- Agents: `twingate-se` (primary orchestrator), `aws-deployer`, `azure-deployer`, `gcp-deployer`, `network-designer`, `idfw-deployer`.
- Each skill carries a `references/` directory of summarized docs refreshed weekly by a GitHub Action pulling from the Twingate docs site, help center, and four public GitHub orgs (`Twingate`, `Twingate-Solutions`, `Twingate-Labs`, `Twingate-Community`).
- License: Apache 2.0.

## Prerequisites
- Claude Code with plugin/marketplace support.
- A Twingate tenant for real deployment work (the plugin generates guidance and code; it does not provision).

## Usage / Step-by-Step
1. Add the marketplace: `/plugin marketplace add Twingate-Solutions/twingate-assistant`
2. Install: `/plugin install twingate-assistant@twingate-solutions`
3. Skills load automatically when relevant; invoke agents by name, e.g. *"Use the twingate-se agent to deploy Twingate to my AWS environment."*
4. Document an existing deployment once with the `twingate-se` agent to produce `twingate-context.md`, then commit it — future sessions read it automatically. Template: `docs/twingate-context-template.md`.
5. Update later by re-running the same `/plugin install` command.

## Configuration Values
- No CLI flags, env vars, or API parameters for end users — the plugin is invoked through Claude Code slash commands and natural-language agent/skill triggers.
- `/skill <name>` explicitly loads a skill; agents are triggered by naming them in a prompt.
- Pipeline configuration (doc routing, source list) lives in the repo's `scripts/doc_mapping.yaml` and matters only to forkers/maintainers.

## Gotchas
- The plugin produces expertise and code; it performs no live provisioning or API calls against a tenant.
- Reference summaries are only as current as the last weekly Action run — re-run `/plugin install` to pull updates.
- Skills auto-activate on keyword detection; agents do not — they must be named explicitly.
- Committing the generated `twingate-context.md` is what makes future sessions skip re-assessment; without it, each session re-asks.

## Related Docs
- `docs/twingate-context-template.md` — deployment context template.
- `docs/MAINTAINING.md` — forking, customizing, running the pipeline against your own docs.
- `CONTRIBUTING.md` — contributing upstream.
- `LICENSE` — Apache 2.0.