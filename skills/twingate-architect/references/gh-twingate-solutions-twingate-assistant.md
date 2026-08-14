---
source: https://github.com/Twingate-Solutions/twingate-assistant
type: github
fetched: 2026-08-14
source_version: c83dcea985caf06e9892cc31a7b9c505d827b2ba
---

# twingate-assistant

## Summary
A Claude Code plugin that provides Twingate ZTNA domain expertise through skills (auto-loaded context modules) and agents (explicit orchestration workflows). It handles architecture design, IaC generation (Terraform/Pulumi), and troubleshooting for AWS, Azure, GCP, and Kubernetes deployments.

## Key Information
- Plugin type: Claude Code marketplace plugin
- IaC support: Terraform, Pulumi (TypeScript, Python, Go, C#)
- Cloud targets: AWS (ECS, EC2), Azure (ACI, VMs), GCP (Cloud Run, GCE), Kubernetes (Helm, operator)
- Documentation refresh: Weekly GitHub Action pulls from Twingate docs, help center, and public Twingate GitHub orgs
- License: Apache 2.0

## Prerequisites
- Claude Code with plugin marketplace access
- No Twingate account required to install; credentials/API keys needed for actual deployments

## Installation

```bash
/plugin marketplace add Twingate-Solutions/twingate-assistant
/plugin install twingate-assistant@twingate-solutions
```

Re-run the install command to update.

## Usage

### Agents (invoke explicitly by name)

| Agent | Purpose |
|---|---|
| `twingate-se` | Full deployment lifecycle: assessment → design → IaC |
| `aws-deployer` | AWS connector deployment |
| `azure-deployer` | Azure connector deployment |
| `gcp-deployer` | GCP connector deployment |
| `network-designer` | Network planning before writing IaC |
| `idfw-deployer` | SSH PAM / kubectl proxy via Identity Firewall |

```text
Use the twingate-se agent to help me deploy Twingate to my AWS environment.
Use the aws-deployer agent to generate Terraform for two HA connectors in us-east-1.
Use the network-designer agent to plan our resource structure for three environments.
```

### Skills (auto-load on relevant topics, or invoke with `/skill <name>`)

`twingate-architect`, `twingate-connectors`, `twingate-terraform`, `twingate-pulumi`, `twingate-kubernetes`, `twingate-idfw`, `twingate-identity`, `twingate-api`, `twingate-dns-security`, `twingate-troubleshoot`

### Persisting deployment context

```text
Use the twingate-se agent to document my current Twingate deployment as twingate-context.md.
```

Commit the output file. Future sessions pick it up automatically, skipping re-assessment. Template: `docs/twingate-context-template.md`.

## Configuration Values
None defined at the plugin level. Cloud-specific agents will prompt for environment-specific values (region, resource group, project ID, etc.) during workflow execution.

## Gotchas
- Skills activate automatically on topic detection; you may get Twingate-specific guidance without explicitly invoking a skill
- The `twingate-context.md` file must be committed to the repo root for auto-detection in future sessions
- Updates require manually re-running `/plugin install`; the weekly doc refresh updates the plugin source but not your local install until you reinstall

## Related Docs
- Context template: [`docs/twingate-context-template.md`](docs/twingate-context-template.md)
- Maintenance/forking guide: [`docs/MAINTAINING.md`](docs/MAINTAINING.md)
- Contribution guide: [`CONTRIBUTING.md`](CONTRIBUTING.md)
- Twingate Terraform provider: referenced in `twingate-terraform` skill
- Twingate GraphQL API: referenced in `twingate-api` skill