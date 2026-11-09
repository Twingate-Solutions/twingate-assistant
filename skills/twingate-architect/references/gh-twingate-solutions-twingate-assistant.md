---
source: https://github.com/Twingate-Solutions/twingate-assistant
type: github
fetched: 2026-11-08
source_version: 5721351e61e74625d63fe0792c77aa9795a4d373
trust: official
---

# Twingate Assistant (Claude Code Plugin)

A Claude Code plugin that provides Twingate ZTNA domain expertise via skills and agents. It covers architecture design, connector deployment, IaC generation (Terraform/Pulumi), IdP integration, troubleshooting, and cloud-specific deployers for AWS, Azure, and GCP.

## Key Information

- Adds **Skills** (auto-activate on topic detection) and **Agents** (explicitly invoked by name) to Claude Code sessions
- Supports IaC output via Terraform and Pulumi; cloud targets include AWS, Azure, GCP, and Kubernetes
- Deployment progress persists to `twingate-deployment/deployment.yaml` — contains internal network details, keep out of public repos
- A weekly GitHub Action refreshes skill reference docs from Twingate docs, help center, and public Twingate GitHub orgs
- License: Apache 2.0

## Prerequisites

- Claude Code with plugin marketplace support
- A Twingate account (for actual deployments)
- Cloud credentials if using cloud-deployer agents

## Installation

Install via Claude Code plugin commands:

```
/plugin marketplace add Twingate-Solutions/twingate-assistant
/plugin install twingate-assistant@twingate-solutions
```

Re-run `/plugin install` to update to the latest version.

## Usage

**New deployment walkthrough:**
```
Help me deploy Twingate. Here's our network diagram.
```

**SE agent assessment and design:**
```
Use the twingate-se agent to help me deploy Twingate to my AWS environment.
```

**Document an existing deployment (run once, commit result):**
```
Use the twingate-se agent to document my current Twingate deployment as twingate-context.md.
```
Template: `docs/twingate-context-template.md`

**Troubleshoot:**
```
Use the twingate-troubleshoot skill. My users can't reach a resource that was working yesterday.
```

**Cloud-specific IaC:**
```
Use the aws-deployer agent to generate Terraform for two HA connectors in us-east-1.
Use the azure-deployer agent to deploy connectors as Azure Container Instances with Entra ID auth.
```

## Available Skills

| Skill | Coverage |
|---|---|
| `twingate-onboarding` | End-to-end guided deployment |
| `twingate-architect` | ZTNA architecture, Remote Networks, design patterns |
| `twingate-connectors` | Connector deployment, HA, upgrades, metrics |
| `twingate-terraform` | Terraform provider and resource definitions |
| `twingate-pulumi` | Pulumi provider (TypeScript, Python, Go, C#) |
| `twingate-kubernetes` | Helm chart, operator, CRDs |
| `twingate-idfw` | SSH PAM, Kubernetes gateway, session recording |
| `twingate-identity` | IdP, SCIM, device trust, JIT |
| `twingate-api` | GraphQL API, CLI, automation |
| `twingate-dns-security` | DNS filtering, exit networks, DoH |
| `twingate-troubleshoot` | Connector/access/policy diagnostics |

## Available Agents

| Agent | Purpose |
|---|---|
| `twingate-se` | Full deployment or major change orchestration |
| `aws-deployer` | AWS connector deployment (ECS, EC2, IAM, Secrets Manager) |
| `azure-deployer` | Azure connector deployment (ACI, VMs, Key Vault, Entra ID) |
| `gcp-deployer` | GCP connector deployment (Cloud Run, GCE, Secret Manager) |
| `deployment-reviewer` | Read-only plan review before building |
| `network-designer` | Network planning before writing IaC |
| `idfw-deployer` | Certificate-based SSH PAM or kubectl proxy |

## Gotchas

- `twingate-deployment/deployment.yaml` stores internal network details — do not commit to public repositories
- Skills auto-activate based on topic detection; explicit invocation uses `/skill <name>`
- The onboarding skill is multi-session; progress is saved to the YAML file and resumed automatically

## Related Docs