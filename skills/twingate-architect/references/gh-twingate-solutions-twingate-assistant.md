---
source: https://github.com/Twingate-Solutions/twingate-assistant
type: github
fetched: 2026-08-09
source_version: 671f5961f3b91cd8669028a9b94223d745ba5707
---

# twingate-assistant

## Summary
A Claude Code plugin that adds Twingate ZTNA domain expertise to Claude Code sessions. It provides skills (auto-loading domain knowledge) and agents (explicit orchestrators) for designing, deploying, and troubleshooting Twingate across AWS, Azure, GCP, and Kubernetes. Generates Terraform and Pulumi IaC as part of deployment workflows.

## Key Information
- Plugin type: Claude Code marketplace plugin
- License: Apache 2.0
- Skills activate automatically on topic detection or via `/skill <name>`
- Agents must be invoked explicitly by name
- Documentation summaries refresh weekly via GitHub Action from Twingate's docs, help center, and public GitHub orgs

## Prerequisites
- Claude Code installed and running
- Access to Claude Code plugin marketplace

## Usage / Step-by-Step

**Install:**
```bash
/plugin marketplace add Twingate-Solutions/twingate-assistant
/plugin install twingate-assistant@twingate-solutions
```

**Update:** Re-run the same `/plugin install` command.

**Invoke an agent:**
```text
Use the twingate-se agent to help me deploy Twingate to my AWS environment.
Use the aws-deployer agent to generate Terraform for two HA connectors in us-east-1.
```

**Invoke a skill explicitly:**
```text
Use the twingate-troubleshoot skill. My users can't reach a resource that was working yesterday.
```

**Persist deployment context across sessions:**
```text
Use the twingate-se agent to document my current Twingate deployment as twingate-context.md.
```
Commit the resulting file; future sessions pick it up automatically. Template at `docs/twingate-context-template.md`.

## Configuration Values
None required. No environment variables, API keys, or CLI flags needed for the plugin itself. Cloud-specific agents (AWS, Azure, GCP) will guide credential and secrets configuration as part of their workflows.

## Available Skills

| Skill | Coverage |
|---|---|
| `twingate-architect` | Core ZTNA architecture, Remote Networks, design patterns |
| `twingate-connectors` | Connector deployment, HA, upgrades, logging |
| `twingate-terraform` | Terraform provider, resource definitions |
| `twingate-pulumi` | Pulumi provider (TS, Python, Go, C#) |
| `twingate-kubernetes` | Helm, operator, CRDs |
| `twingate-idfw` | SSH PAM, Kubernetes gateway, session recording |
| `twingate-identity` | IdP, SCIM, device trust, JIT |
| `twingate-api` | GraphQL API, CLI, automation |
| `twingate-dns-security` | DNS filtering, exit networks, DoH |
| `twingate-troubleshoot` | Connector/access/policy diagnostics |

## Available Agents

| Agent | Use case |
|---|---|
| `twingate-se` | Full deployment planning and environment assessment |
| `aws-deployer` | ECS, EC2, IAM, Secrets Manager |
| `azure-deployer` | ACI, VMs, Key Vault, Entra ID |
| `gcp-deployer` | Cloud Run, GCE, Secret Manager, Google Workspace |
| `network-designer` | Pre-IaC network and resource planning |
| `idfw-deployer` | Certificate-based SSH PAM or kubectl proxy |

## Gotchas
- Skills auto-load on keyword detection; explicit invocation is available but often unnecessary
- The `twingate-context.md` file must be committed to the repo for future sessions to find it automatically
- Plugin updates are not automatic—run `/plugin install` periodically to pull refreshed documentation summaries

## Related Docs
- Context template: `docs/twingate-context-template.md`
- Maintenance/forking guide: `docs/MAINTAINING.md`
- Contribution guide: `CONTRIBUTING.md`
- Twingate docs: referenced internally via weekly-refreshed skill summaries