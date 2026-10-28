---
source: https://github.com/Twingate-Solutions/twingate-assistant
type: github
fetched: 2026-10-28
source_version: c6bab839a8fdaf24e1df44936db1aa8a3536f984
trust: official
---

# Twingate Assistant (Claude Code Plugin)

A Claude Code plugin that provides Twingate ZTNA expertise via automatically-loaded skills and explicitly-invoked agents. Covers architecture design, IaC generation (Terraform/Pulumi), cloud-specific connector deployment, and troubleshooting across AWS, Azure, GCP, and Kubernetes.

## Key Information

- Delivers expertise through two mechanisms: **Skills** (auto-load on topic detection) and **Agents** (explicitly invoked for end-to-end workflows)
- Skills cover: architecture, connectors, Terraform, Pulumi, Kubernetes, Identity Firewall, IdP/SCIM, GraphQL API, DNS security, troubleshooting
- Agents cover: general SE workflows, AWS/Azure/GCP deployers, network design, and Identity Firewall deployment
- Reference docs in each skill's `references/` directory are refreshed weekly via GitHub Actions from Twingate's docs site, help center, and public GitHub orgs
- License: Apache 2.0

## Prerequisites

- Claude Code with plugin/marketplace support

## Installation

Install via Claude Code commands:

```
/plugin marketplace add Twingate-Solutions/twingate-assistant
/plugin install twingate-assistant@twingate-solutions
```

To update, re-run the same `/plugin install` command.

## Usage

### Invoke an agent explicitly

```text
Use the twingate-se agent to help me deploy Twingate to my AWS environment.
Use the aws-deployer agent to generate Terraform for two HA connectors in us-east-1.
Use the azure-deployer agent to deploy connectors as Azure Container Instances with Entra ID auth.
Use the network-designer agent to plan our resource structure for three environments.
```

### Invoke a skill explicitly

```text
Use the twingate-troubleshoot skill. My users can't reach a resource that was working yesterday.
```

### Document an existing deployment (one-time setup)

```text
Use the twingate-se agent to document my current Twingate deployment as twingate-context.md.
```

Commit the resulting file; future sessions pick it up automatically. Template at `docs/twingate-context-template.md`.

## Agents Reference

| Agent | Purpose |
|---|---|
| `twingate-se` | Environment assessment, network design, end-to-end deployment |
| `aws-deployer` | ECS, EC2, IAM, Secrets Manager |
| `azure-deployer` | ACI, VMs, Key Vault, Entra ID |
| `gcp-deployer` | Cloud Run, GCE, Secret Manager, Google Workspace |
| `network-designer` | Resource strategy and security tier planning pre-IaC |
| `idfw-deployer` | Certificate-based SSH PAM or kubectl proxy |

## Gotchas

- Skills activate automatically on keyword detection but can also be invoked explicitly with `/skill <name>`
- The weekly refresh pipeline pulls from public Twingate GitHub orgs and docs; forking requires running the pipeline against your own sources (see `docs/MAINTAINING.md`)
- Re-run `/plugin install` periodically to pull refreshed skill content

## Related Docs

- Customization and pipeline maintenance: [`docs/MAINTAINING.md`](docs/MAINTAINING.md)
- Deployment context template: [`docs/twingate-context-template.md`](docs/twingate-context-template.md)
- Contribution guide: [`CONTRIBUTING.md`](CONTRIBUTING.md)