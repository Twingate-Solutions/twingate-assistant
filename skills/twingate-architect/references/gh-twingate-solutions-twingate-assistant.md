---
source: https://github.com/Twingate-Solutions/twingate-assistant
type: github
fetched: 2026-10-18
source_version: 3a80b52ac223e46322e5db115c5f6c1a27356ad0
trust: official
---

# Twingate Assistant (Claude Code Plugin)

A Claude Code plugin that provides Twingate ZTNA expertise via automatically-loaded skills and explicitly-invoked agents. It covers architecture design, connector deployment, IaC generation (Terraform/Pulumi), and troubleshooting across AWS, Azure, GCP, and Kubernetes.

## Key Information

- Distributed as a Claude Code plugin (`Twingate-Solutions/twingate-assistant`)
- Two components: **Skills** (auto-activate on topic detection) and **Agents** (explicit invocation for end-to-end workflows)
- IaC support: Terraform and Pulumi (TypeScript, Python, Go, C#)
- Reference docs in each skill's `references/` directory; refreshed weekly via GitHub Actions from official Twingate documentation and GitHub orgs
- License: Apache 2.0

## Prerequisites

- Claude Code with plugin/marketplace support
- No Twingate API credentials required at install time (needed at deploy/generate time depending on workflow)

## Installation

Install via Claude Code plugin commands:

```
/plugin marketplace add Twingate-Solutions/twingate-assistant
/plugin install twingate-assistant@twingate-solutions
```

To update, re-run the same `/plugin install` command.

## Usage

### Invoke an agent (explicit)

```
Use the twingate-se agent to help me deploy Twingate to my AWS environment.
Use the aws-deployer agent to generate Terraform for two HA connectors in us-east-1.
Use the azure-deployer agent to deploy connectors as Azure Container Instances with Entra ID auth.
Use the network-designer agent to plan our resource structure for three environments.
```

### Document an existing deployment (one-time setup)

```
Use the twingate-se agent to document my current Twingate deployment as twingate-context.md.
```

Commit the resulting file; future sessions pick it up automatically. Template: `docs/twingate-context-template.md`.

### Invoke a skill (explicit)

```
Use the twingate-troubleshoot skill. My users can't reach a resource that was working yesterday.
```

Skills also activate automatically when relevant topics are mentioned.

## Available Skills

| Skill | Coverage |
|---|---|
| `twingate-architect` | ZTNA architecture, Remote Networks, design patterns |
| `twingate-connectors` | Connector deployment, HA, upgrades, metrics |
| `twingate-terraform` | Terraform provider, resource definitions |
| `twingate-pulumi` | Pulumi provider (TypeScript, Python, Go, C#) |
| `twingate-kubernetes` | Helm, operator, CRDs, traffic routing |
| `twingate-idfw` | SSH PAM, Kubernetes gateway, session recording |
| `twingate-identity` | IdP, SCIM, device trust, JIT |
| `twingate-api` | GraphQL API, CLI, automation |
| `twingate-dns-security` | DNS filtering, exit networks, DoH |
| `twingate-troubleshoot` | Connector, access, and policy diagnostics |

## Available Agents

| Agent | Use case |
|---|---|
| `twingate-se` | Full deployment assessment and design |
| `aws-deployer` | ECS, EC2, IAM, Secrets Manager |
| `azure-deployer` | ACI, VMs, Key Vault, Entra ID |
| `gcp-deployer` | Cloud Run, GCE, Secret Manager |
| `network-designer` | Pre-IaC network and resource planning |
| `idfw-deployer` | Certificate-based SSH PAM / kubectl proxy |

## Gotchas

- Skills activate automatically by topic detection; explicit invocation is available but not always required
- The `twingate-context.md` file is optional but prevents repeated environment re-assessment across sessions
- Reference docs refresh weekly automatically; pull plugin updates manually with `/plugin install` to get skill/agent changes

## Related Docs

- Context template: `docs/twingate-context-template.md`
- Maintenance/forking guide: `docs/MAINTAINING.md`
- Contribution guide: `CONTRIBUTING.md`
- Twingate official docs: [twin