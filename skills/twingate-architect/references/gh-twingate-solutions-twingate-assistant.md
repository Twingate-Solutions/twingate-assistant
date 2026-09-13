---
source: https://github.com/Twingate-Solutions/twingate-assistant
type: github
fetched: 2026-09-13
source_version: 4f51316b31cdd04cea17b1ac0d1d5e0d1f47ac5d
---

# twingate-assistant

## Summary
A Claude Code plugin that provides Twingate ZTNA domain expertise via skills (auto-loaded context) and agents (explicit orchestrators). It covers architecture design, IaC generation (Terraform/Pulumi), connector deployment across AWS/Azure/GCP/Kubernetes, and troubleshooting. Documentation summaries are refreshed weekly via GitHub Actions.

## Key Information
- Plugin type: Claude Code marketplace plugin
- Provides 10 skills and 6 agents
- IaC support: Terraform and Pulumi (TypeScript, Python, Go, C#)
- Cloud targets: AWS (ECS/EC2), Azure (ACI/VMs), GCP (Cloud Run/GCE), Kubernetes (Helm/Operator)
- Weekly automated doc refresh from Twingate docs, help center, and public Twingate GitHub orgs
- License: Apache 2.0

## Prerequisites
- Claude Code with plugin marketplace access
- No Twingate API credentials required for the plugin itself (credentials needed when deploying actual infrastructure)

## Installation
```bash
/plugin marketplace add Twingate-Solutions/twingate-assistant
/plugin install twingate-assistant@twingate-solutions
```
To update: re-run the same `/plugin install` command.

## Usage

| Use case | Invocation |
|---|---|
| New deployment | `Use the twingate-se agent to help me deploy Twingate to my AWS environment.` |
| Document existing setup | `Use the twingate-se agent to document my current Twingate deployment as twingate-context.md.` |
| Troubleshoot | `Use the twingate-troubleshoot skill. My users can't reach a resource.` |
| AWS HA connectors | `Use the aws-deployer agent to generate Terraform for two HA connectors in us-east-1.` |
| Azure ACI | `Use the azure-deployer agent to deploy connectors as Azure Container Instances with Entra ID auth.` |

## Skills (auto-load on topic detection, or invoke with `/skill <name>`)

| Skill | Covers |
|---|---|
| `twingate-architect` | Core ZTNA architecture, Remote Networks, design patterns |
| `twingate-connectors` | Connector deployment, HA, upgrades, metrics |
| `twingate-terraform` | Terraform provider, resource definitions, secrets |
| `twingate-pulumi` | Pulumi provider (TypeScript, Python, Go, C#) |
| `twingate-kubernetes` | Helm chart, operator, CRDs, traffic routing |
| `twingate-idfw` | SSH PAM, Kubernetes gateway, session recording |
| `twingate-identity` | IdP/SCIM, device trust, security policies, JIT |
| `twingate-api` | GraphQL API, CLI, automation |
| `twingate-dns-security` | DNS filtering, exit networks, DoH |
| `twingate-troubleshoot` | Connector/access/policy diagnostics |

## Agents

| Agent | Use when |
|---|---|
| `twingate-se` | Starting any deployment or major change |
| `aws-deployer` | Deploying on AWS |
| `azure-deployer` | Deploying on Azure |
| `gcp-deployer` | Deploying on GCP |
| `network-designer` | Planning resource structure before writing IaC |
| `idfw-deployer` | Certificate-based SSH PAM or kubectl proxy |

## Gotchas
- Skills load automatically when relevant topics are detected; explicit invocation is optional but available
- Commit `twingate-context.md` after generating it — subsequent sessions pick it up to avoid re-asking environment questions
- Plugin content updates weekly via CI, but you must re-run `/plugin install` to pull the updated version into your Claude Code environment

## Related Docs
- Context template: [`docs/twingate-context-template.md`](docs/twingate-context-template.md)
- Customization/fork guide: [`docs/MAINTAINING.md`](docs/MAINTAINING.md)
- Contribution guide: [`CONTRIBUTING.md`](CONTRIBUTING.md)