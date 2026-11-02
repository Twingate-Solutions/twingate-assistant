---
source: https://github.com/Twingate-Solutions/twingate-assistant
type: github
fetched: 2026-11-01
source_version: c8f5b735594515fff6ef5aff27018dadd7af0995
trust: official
---

# Twingate Assistant (Claude Code Plugin)

A Claude Code plugin that provides Twingate ZTNA domain expertise via skills and agents. It covers architecture design, connector deployment, IaC generation (Terraform/Pulumi), troubleshooting, and cloud-specific deployment workflows across AWS, Azure, GCP, and Kubernetes.

## Key Information

- Delivers expertise through two mechanisms: **Skills** (auto-load on topic detection) and **Agents** (explicit invocation for end-to-end workflows)
- Skills cover: architecture, connectors, Terraform, Pulumi, Kubernetes, Identity Firewall, IdP/SCIM, GraphQL API, DNS security, troubleshooting
- Agents cover: SE assessment, AWS/Azure/GCP deployer, network designer, IDFW deployer
- Reference docs are refreshed weekly via GitHub Action from Twingate docs, help center, and public Twingate GitHub orgs
- Licensed under Apache 2.0

## Prerequisites

- Claude Code with plugin marketplace access
- A Twingate account and relevant cloud credentials (varies by deployment target)

## Installation

Install via Claude Code plugin commands:

```
/plugin marketplace add Twingate-Solutions/twingate-assistant
/plugin install twingate-assistant@twingate-solutions
```

To update: re-run the same `/plugin install` command.

## Usage

### Invoke an agent

```text
Use the twingate-se agent to help me deploy Twingate to my AWS environment.
Use the aws-deployer agent to generate Terraform for two HA connectors in us-east-1.
Use the azure-deployer agent to deploy connectors as Azure Container Instances with Entra ID auth.
Use the network-designer agent to plan our resource structure for three environments.
```

### Document an existing deployment

```text
Use the twingate-se agent to document my current Twingate deployment as twingate-context.md.
```

Commit the resulting file; future sessions load it automatically. Template: `docs/twingate-context-template.md`.

### Invoke a skill explicitly

```text
Use the twingate-troubleshoot skill. My users can't reach a resource that was working yesterday.
```

Skills also activate automatically when relevant topics are mentioned (e.g., mentioning "connector" activates `twingate-connectors`).

## Agents Reference

| Agent | Purpose |
|---|---|
| `twingate-se` | Full deployment assessment, network design, IaC generation |
| `aws-deployer` | ECS, EC2, IAM, Secrets Manager connector deployment |
| `azure-deployer` | ACI, VMs, Key Vault, Entra ID connector deployment |
| `gcp-deployer` | Cloud Run, GCE, Secret Manager, Google Workspace deployment |
| `network-designer` | Pre-IaC network planning, resource strategy, security tiers |
| `idfw-deployer` | Certificate-based SSH PAM or kubectl proxy access |

## Gotchas

- Skills load automatically but can also be called explicitly with `/skill <name>` if not triggering on their own
- Reference knowledge is updated weekly server-side; pull plugin updates periodically with `/plugin install` to get the latest summaries
- The `twingate-context.md` file (if created) must be committed to the repo to persist across sessions

## Related Docs

- Context file template: [`docs/twingate-context-template.md`](docs/twingate-context-template.md)
- Forking/customizing: [`docs/MAINTAINING.md`](docs/MAINTAINING.md)
- Contributing: [`CONTRIBUTING.md`](CONTRIBUTING.md)