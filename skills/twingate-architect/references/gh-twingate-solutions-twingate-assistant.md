---
source: https://github.com/Twingate-Solutions/twingate-assistant
type: github
fetched: 2026-08-30
source_version: 3f3875138e9b7b5e813e68abc491a1dd4f304907
---

# twingate-assistant

## Summary
A Claude Code plugin that adds Twingate ZTNA domain expertise to Claude Code sessions via auto-loading skills and explicit agents. It covers architecture design, IaC generation (Terraform/Pulumi), cloud-specific deployments, and troubleshooting across AWS, Azure, GCP, and Kubernetes.

## Key Information
- Plugin type: Claude Code marketplace plugin
- Provides two mechanism types: **Skills** (auto-load on topic detection) and **Agents** (explicit invocation for end-to-end workflows)
- IaC support: Terraform and Pulumi (TypeScript, Python, Go, C#)
- Cloud targets: AWS, Azure, GCP, Kubernetes
- Weekly GitHub Action refreshes skill knowledge from Twingate docs, help center, and public Twingate GitHub orgs
- License: Apache 2.0

## Prerequisites
- Claude Code installed and configured
- Access to Claude Code plugin marketplace

## Installation

```bash
/plugin marketplace add Twingate-Solutions/twingate-assistant
/plugin install twingate-assistant@twingate-solutions
```

To update: re-run the same `/plugin install` command.

## Usage

### Agents (invoke explicitly by name)

| Agent | Purpose |
|---|---|
| `twingate-se` | Environment assessment, network design, end-to-end deployment |
| `aws-deployer` | Connectors on AWS (ECS, EC2, IAM, Secrets Manager) |
| `azure-deployer` | Connectors on Azure (ACI, VMs, Key Vault, Entra ID) |
| `gcp-deployer` | Connectors on GCP (Cloud Run, GCE, Secret Manager) |
| `network-designer` | Network planning before IaC — resource strategy, security tiers |
| `idfw-deployer` | SSH PAM or kubectl proxy (certificate-based) |

```text
Use the twingate-se agent to help me deploy Twingate to my AWS environment.
Use the aws-deployer agent to generate Terraform for two HA connectors in us-east-1.
Use the network-designer agent to plan our resource structure for three environments.
```

### Skills (auto-load or invoke with `/skill <name>`)

| Skill | Covers |
|---|---|
| `twingate-architect` | Core ZTNA architecture, Remote Networks, design patterns |
| `twingate-connectors` | Connector deployment, HA, upgrades, logging |
| `twingate-terraform` | Terraform provider, resource definitions, secrets |
| `twingate-pulumi` | Pulumi provider across languages |
| `twingate-kubernetes` | Helm, operator, CRDs, traffic routing |
| `twingate-idfw` | SSH PAM, Kubernetes gateway, session recording |
| `twingate-identity` | IdP, SCIM, device trust, JIT, security policies |
| `twingate-api` | GraphQL API, CLI, automation |
| `twingate-dns-security` | DNS filtering, exit networks, DNS-over-HTTPS |
| `twingate-troubleshoot` | Connector failures, access failures, policy issues |

### Document an existing deployment
```text
Use the twingate-se agent to document my current Twingate deployment as twingate-context.md.
```
Commit `twingate-context.md` — future sessions pick it up automatically. Template at `docs/twingate-context-template.md`.

## Configuration Values
None required. No environment variables or API keys configured in the plugin itself. Cloud-specific IaC generation uses whatever credentials are present in your environment.

## Gotchas
- Skills activate automatically when Twingate topics are detected; no explicit invocation needed, but you can force with `/skill <name>`
- The `twingate-context.md` file must be committed to your repo for future sessions to auto-detect it
- Knowledge currency depends on the weekly refresh action; pull plugin updates periodically with `/plugin install`

## Related Docs
- Context template: `docs/twingate-context-template.md`
- Forking/customization guide: `docs/MAINTAINING.md`
- Contribution guide: `CONTRIBUTING.md`