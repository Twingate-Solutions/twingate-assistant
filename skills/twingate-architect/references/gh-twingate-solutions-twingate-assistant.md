---
source: https://github.com/Twingate-Solutions/twingate-assistant
type: github
fetched: 2026-10-25
source_version: 2ea7f646bbca84be6a308e1d6bb6050f3405dad2
trust: official
---

# Twingate Assistant (Claude Code Plugin)

A Claude Code plugin that provides Twingate ZTNA expertise via skills and agents. It covers architecture design, connector deployment, IaC generation (Terraform/Pulumi), and troubleshooting across AWS, Azure, GCP, and Kubernetes.

## Key Information

- Delivered as **Skills** (auto-load on topic detection) and **Agents** (explicit invocation for end-to-end workflows)
- Skills cover: architecture, connectors, Terraform, Pulumi, Kubernetes, Identity Firewall, IdP/SCIM, GraphQL API, DNS security, troubleshooting
- Agents cover: general SE workflows, AWS/Azure/GCP connector deployment, network design, IDFW implementation
- Reference docs in each skill's `references/` directory are refreshed weekly via GitHub Actions from Twingate docs, help center, and public Twingate GitHub orgs
- License: Apache 2.0

## Prerequisites

- Claude Code with plugin marketplace support
- No Twingate account credentials required at install time (credentials/tokens needed at deployment time depending on IaC used)

## Installation

Install via Claude Code plugin commands:

```
/plugin marketplace add Twingate-Solutions/twingate-assistant
/plugin install twingate-assistant@twingate-solutions
```

To update: re-run the same `/plugin install` command.

## Usage

**Invoke an agent explicitly:**

```
Use the twingate-se agent to help me deploy Twingate to my AWS environment.
Use the aws-deployer agent to generate Terraform for two HA connectors in us-east-1.
Use the azure-deployer agent to deploy connectors as Azure Container Instances with Entra ID auth.
Use the network-designer agent to plan our resource structure for three environments.
```

**Invoke a skill explicitly:**

```
Use the twingate-troubleshoot skill. My users can't reach a resource that was working yesterday.
```

**Document an existing deployment (run once, commit the output):**

```
Use the twingate-se agent to document my current Twingate deployment as twingate-context.md.
```

A context template is available at `docs/twingate-context-template.md`. Committing the generated file allows future sessions to skip re-assessment.

## Agents

| Agent | Purpose |
|---|---|
| `twingate-se` | Environment assessment, network design, end-to-end deployment |
| `aws-deployer` | ECS, EC2, IAM, Secrets Manager connector deployment |
| `azure-deployer` | ACI, VMs, Key Vault, Entra ID connector deployment |
| `gcp-deployer` | Cloud Run, GCE, Secret Manager, Google Workspace |
| `network-designer` | Resource strategy and security tier planning before IaC |
| `idfw-deployer` | Certificate-based SSH PAM or kubectl proxy access |

## Gotchas

- Skills activate automatically on topic detection; explicit invocation (`/skill <name>`) is also supported but not required
- The weekly doc-refresh pipeline runs in the upstream repo — forks do not inherit this automatically; see `docs/MAINTAINING.md` to run it yourself
- Re-run `/plugin install` periodically to pull updated skill reference content into your Claude Code environment

## Related Docs

- Customization and pipeline maintenance: [`docs/MAINTAINING.md`](docs/MAINTAINING.md)
- Contribution guide: [`CONTRIBUTING.md`](CONTRIBUTING.md)
- Deployment context template: [`docs/twingate-context-template.md`](docs/twingate-context-template.md)