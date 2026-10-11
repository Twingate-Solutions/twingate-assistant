---
source: https://github.com/Twingate-Solutions/twingate-assistant
type: github
fetched: 2026-10-11
source_version: 165600f3fcbf3ceab729a5691951b99a79e50e21
trust: official
---

# twingate-assistant

A Claude Code plugin that provides Twingate ZTNA domain expertise via automatically-loaded skills and explicitly-invoked agents. It supports environment assessment, network design, IaC generation (Terraform/Pulumi), and troubleshooting across AWS, Azure, GCP, and Kubernetes.

## Key Information

- Adds **10 skills** (auto-activate on topic detection) and **6 agents** (invoked explicitly by name)
- Generates Terraform and Pulumi configurations for connector deployments
- Covers connector HA, IdP/SCIM integration, Identity Firewall, DNS security, and GraphQL API automation
- Each skill includes a `references/` directory of summarized Twingate documentation
- A weekly GitHub Action refreshes references from Twingate docs, help center, and public Twingate GitHub orgs

## Prerequisites

- Claude Code with plugin marketplace access

## Installation

Add the marketplace source and install the plugin via Claude Code commands:

```
/plugin marketplace add Twingate-Solutions/twingate-assistant
/plugin install twingate-assistant@twingate-solutions
```

Re-run the install command to update to the latest version.

## Usage

### Plan a new deployment
```
Use the twingate-se agent to help me deploy Twingate to my AWS environment.
```

### Document an existing deployment
```
Use the twingate-se agent to document my current Twingate deployment as twingate-context.md.
```
Commit the resulting file; future sessions read it automatically. Template: `docs/twingate-context-template.md`.

### Troubleshoot
```
Use the twingate-troubleshoot skill. My users can't reach a resource that was working yesterday.
```

### Generate cloud-specific IaC
```
Use the aws-deployer agent to generate Terraform for two HA connectors in us-east-1.
Use the azure-deployer agent to deploy connectors as Azure Container Instances with Entra ID auth.
```

## Skills

| Skill | Covers |
|---|---|
| `twingate-architect` | ZTNA architecture, Remote Networks, design patterns |
| `twingate-connectors` | Connector deployment, HA, upgrades, metrics |
| `twingate-terraform` | Terraform provider, resource definitions, secrets |
| `twingate-pulumi` | Pulumi — TypeScript, Python, Go, C# |
| `twingate-kubernetes` | Helm chart, operator, CRDs, traffic routing |
| `twingate-idfw` | SSH PAM, Kubernetes gateway, session recording |
| `twingate-identity` | IdP, SCIM, device trust, JIT |
| `twingate-api` | GraphQL API, CLI, automation |
| `twingate-dns-security` | DNS filtering, exit networks, DoH |
| `twingate-troubleshoot` | Connector/access/policy diagnostics |

## Agents

| Agent | Use for |
|---|---|
| `twingate-se` | Full deployment planning and end-to-end design |
| `aws-deployer` | ECS, EC2, IAM, Secrets Manager |
| `azure-deployer` | ACI, VMs, Key Vault, Entra ID |
| `gcp-deployer` | Cloud Run, GCE, Secret Manager, Google Workspace |
| `network-designer` | Pre-IaC network and resource planning |
| `idfw-deployer` | Certificate-based SSH PAM or kubectl proxy |

## Gotchas

- Skills activate automatically but can also be invoked explicitly with `/skill <name>`
- A persistent `twingate-context.md` file prevents the SE agent from re-asking environment questions on every session — worth creating early
- Reference documentation is refreshed weekly via CI; run `/plugin install` periodically to pull those updates locally

## Related Docs

- Context template: `docs/twingate-context-template.md`
- Forking/customizing: `docs/MAINTAINING.md`
- Contributing: `CONTRIBUTING.md`
- License: Apache 2.0