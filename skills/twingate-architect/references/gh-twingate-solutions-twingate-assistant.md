---
source: https://github.com/Twingate-Solutions/twingate-assistant
type: github
fetched: 2026-09-06
source_version: 3f3875138e9b7b5e813e68abc491a1dd4f304907
---

# twingate-assistant

## Summary
A Claude Code plugin that embeds Twingate ZTNA domain expertise into Claude Code sessions. It provides skills (auto-loading domain knowledge) and agents (explicit orchestrators) for designing, deploying, and troubleshooting Twingate across AWS, Azure, GCP, and Kubernetes. Generates Terraform/Pulumi IaC and follows structured deployment workflows.

## Key Information
- Plugin type: Claude Code marketplace plugin
- Provides 10 skills (auto-activate on topic detection) and 6 agents (explicit invocation)
- Documentation summaries refresh weekly via GitHub Action from Twingate docs, help center, and public GitHub orgs
- License: Apache 2.0

## Prerequisites
- Claude Code installed and running
- Access to Claude Code plugin marketplace

## Installation
```bash
/plugin marketplace add Twingate-Solutions/twingate-assistant
/plugin install twingate-assistant@twingate-solutions
```
To update: re-run the same `/plugin install` command.

## Usage / Step-by-Step

**New deployment:**
```text
Use the twingate-se agent to help me deploy Twingate to my AWS environment.
```

**Document existing deployment (run once, commit result):**
```text
Use the twingate-se agent to document my current Twingate deployment as twingate-context.md.
```
Template available at `docs/twingate-context-template.md`. Future sessions pick up the committed file automatically.

**Troubleshoot:**
```text
Use the twingate-troubleshoot skill. My users can't reach a resource that was working yesterday.
```

**Cloud-specific IaC generation:**
```text
Use the aws-deployer agent to generate Terraform for two HA connectors in us-east-1.
Use the azure-deployer agent to deploy connectors as Azure Container Instances with Entra ID auth.
```

## Skills Reference

| Skill | Coverage |
|---|---|
| `twingate-architect` | Core ZTNA architecture, Remote Networks, design patterns |
| `twingate-connectors` | Connector deployment, HA, upgrades, metrics |
| `twingate-terraform` | Terraform provider, resource definitions, secrets |
| `twingate-pulumi` | Pulumi provider (TypeScript, Python, Go, C#) |
| `twingate-kubernetes` | Helm chart, operator, CRDs |
| `twingate-idfw` | SSH PAM, Kubernetes gateway, session recording |
| `twingate-identity` | IdP/SCIM, device trust, JIT, security policies |
| `twingate-api` | GraphQL API, CLI, automation |
| `twingate-dns-security` | DNS filtering, exit networks, DoH |
| `twingate-troubleshoot` | Connector/access/policy diagnostics |

## Agents Reference

| Agent | Use case |
|---|---|
| `twingate-se` | Full deployment lifecycle: assessment → design → IaC |
| `aws-deployer` | ECS, EC2, IAM, Secrets Manager |
| `azure-deployer` | ACI, VMs, Key Vault, Entra ID |
| `gcp-deployer` | Cloud Run, GCE, Secret Manager, Google Workspace |
| `network-designer` | Pre-IaC network planning, resource strategy, security tiers |
| `idfw-deployer` | Certificate-based SSH PAM or kubectl proxy |

## Gotchas
- Skills activate automatically on keyword detection; explicit invocation uses `/skill <name>` syntax, not natural language
- `twingate-context.md` must be committed to the repo root for future sessions to auto-detect it — it is not persisted otherwise
- Weekly doc refresh happens in the upstream repo; you must re-run `/plugin install` to pull those updates locally
- Forking requires separate maintenance of the refresh pipeline (see `docs/MAINTAINING.md`)

## Related Docs
- Context file template: `docs/twingate-context-template.md`
- Maintenance/fork guide: `docs/MAINTAINING.md`
- Contribution guide: `CONTRIBUTING.md`
- Twingate public GitHub orgs: `Twingate`, `Twingate-Solutions`,