---
source: https://github.com/Twingate-Solutions/twingate-assistant
type: github
fetched: 2026-08-06
source_version: b7b660375457ea1541b225910bb12d342150e290
---

<!-- triage: unassigned -->

# Twingate Assistant

## Summary
A Claude Code plugin that adds Twingate ZTNA domain expertise to Claude Code sessions. It provides skills (auto-loading domain knowledge) and agents (explicit orchestrators) for designing, deploying, and troubleshooting Twingate across AWS, Azure, GCP, and Kubernetes. Documentation summaries are refreshed weekly from live Twingate docs via GitHub Actions.

## Key Information
- Plugin type: Claude Code marketplace plugin
- Provides 10 skills + 6 agents covering architecture, IaC, IdP, DNS, troubleshooting
- IaC support: Terraform and Pulumi
- Cloud targets: AWS, Azure, GCP, Kubernetes
- License: Apache 2.0
- Updated via weekly GitHub Action; re-run install to pull updates

## Prerequisites
- Claude Code with plugin marketplace access
- No Twingate credentials required at install time (required when generating actual configs)

## Installation

```bash
/plugin marketplace add Twingate-Solutions/twingate-assistant
/plugin install twingate-assistant@twingate-solutions
```

Re-run the install command to update.

## Usage

**New deployment:**
```text
Use the twingate-se agent to help me deploy Twingate to my AWS environment.
```

**Document existing deployment (run once, commit result):**
```text
Use the twingate-se agent to document my current Twingate deployment as twingate-context.md.
```

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

| Skill | Covers |
|---|---|
| `twingate-architect` | Remote Networks, Resources, design patterns |
| `twingate-connectors` | Deployment, HA, upgrades, metrics |
| `twingate-terraform` | Terraform provider, secrets management |
| `twingate-pulumi` | TypeScript, Python, Go, C# providers |
| `twingate-kubernetes` | Helm, operator, CRDs |
| `twingate-idfw` | SSH PAM, kubectl gateway, session recording |
| `twingate-identity` | IdP/SCIM, device trust, JIT |
| `twingate-api` | GraphQL API, CLI, automation |
| `twingate-dns-security` | DNS filtering, exit networks, DoH |
| `twingate-troubleshoot` | Connector/access/policy diagnostics |

Skills activate automatically on relevant topics or via `/skill <name>`.

## Agents Reference

| Agent | Use case |
|---|---|
| `twingate-se` | Full deployment lifecycle, environment assessment |
| `aws-deployer` | ECS, EC2, IAM, Secrets Manager |
| `azure-deployer` | ACI, VMs, Key Vault, Entra ID |
| `gcp-deployer` | Cloud Run, GCE, Secret Manager |
| `network-designer` | Pre-IaC network planning, resource strategy |
| `idfw-deployer` | Certificate-based SSH PAM, kubectl proxy |

## Gotchas
- Skills load automatically but can be invoked explicitly — useful when auto-detection doesn't trigger
- Commit `twingate-context.md` to your repo so future sessions skip re-assessment; template at `docs/twingate-context-template.md`
- Weekly doc refresh happens in the upstream repo; you must re-run `/plugin install` to pull those updates locally
- Forks require running the refresh pipeline against your own docs source; see `docs/MAINTAINING.md`

## Related Docs
- Context template: `docs/twingate-context-template.md`
- Maintenance/forking guide: `docs/MAINTAINING.md`
- Contributing: `CONTRIBUTING.md`
- [Twingate official docs](https://www.twingate.com/docs)