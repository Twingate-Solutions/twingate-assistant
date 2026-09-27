---
source: https://github.com/Twingate-Solutions/twingate-assistant
type: github
fetched: 2026-09-27
source_version: 6531eee00fc55716b565689ecd3bd7d70a023799
---

# Twingate Assistant (Claude Code Plugin)

A Claude Code plugin that provides Twingate ZTNA expertise via skills and agents. It handles architecture design, IaC generation (Terraform/Pulumi), and troubleshooting for deployments on AWS, Azure, GCP, and Kubernetes.

## Key Information

- Distributed as a Claude Code plugin; no standalone binary or API key required
- Two primitives: **Skills** (auto-load on topic detection) and **Agents** (explicitly invoked orchestrators)
- Documentation summaries are refreshed weekly via GitHub Actions from Twingate docs, help center, and public Twingate GitHub orgs
- License: Apache 2.0

## Prerequisites

- Claude Code with plugin support
- No additional credentials or environment setup required for the plugin itself

## Installation

```bash
/plugin marketplace add Twingate-Solutions/twingate-assistant
/plugin install twingate-assistant@twingate-solutions
```

Re-run `/plugin install` to update.

## Usage

Invoke agents by name in any Claude Code session:

```text
Use the twingate-se agent to help me deploy Twingate to my AWS environment.
Use the aws-deployer agent to generate Terraform for two HA connectors in us-east-1.
Use the twingate-troubleshoot skill. My users can't reach a resource that was working yesterday.
```

Document an existing deployment once to avoid re-assessment in future sessions:

```text
Use the twingate-se agent to document my current Twingate deployment as twingate-context.md.
```

Commit `twingate-context.md`; sessions pick it up automatically. Template at `docs/twingate-context-template.md`.

## Agents

| Agent | Purpose |
|---|---|
| `twingate-se` | End-to-end deployment: environment assessment, network design, IaC |
| `aws-deployer` | Connectors on AWS (ECS, EC2, IAM, Secrets Manager) |
| `azure-deployer` | Connectors on Azure (ACI, VMs, Key Vault, Entra ID) |
| `gcp-deployer` | Connectors on GCP (Cloud Run, GCE, Secret Manager) |
| `network-designer` | Pre-IaC network planning, resource strategy, security tiers |
| `idfw-deployer` | Certificate-based SSH PAM or kubectl proxy access |

## Skills (auto-load or `/skill <name>`)

`twingate-architect`, `twingate-connectors`, `twingate-terraform`, `twingate-pulumi`, `twingate-kubernetes`, `twingate-idfw`, `twingate-identity`, `twingate-api`, `twingate-dns-security`, `twingate-troubleshoot`

## Gotchas

- Skills activate automatically when relevant keywords appear; explicit invocation via `/skill <name>` is optional but forces activation
- Without a committed `twingate-context.md`, the SE agent will re-run environment assessment at the start of each session
- Plugin updates are not automatic — re-run `/plugin install` to pull weekly doc refreshes

## Related Docs

- Context file template: `docs/twingate-context-template.md`
- Forking/customization guide: `docs/MAINTAINING.md`
- Contribution guide: `CONTRIBUTING.md`