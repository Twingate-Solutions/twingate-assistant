---
source: https://github.com/Twingate-Solutions/twingate-assistant
type: github
fetched: 2026-09-20
source_version: b9e09d3fba4cbdafa6e3642723870eedbe70953d
---

# twingate-assistant

## Summary
A Claude Code plugin that embeds Twingate ZTNA expertise into Claude Code sessions. It provides skills (auto-loading domain knowledge) and agents (explicit orchestrators) for designing, deploying, and troubleshooting Twingate environments. Supports IaC generation via Terraform/Pulumi across AWS, Azure, GCP, and Kubernetes.

## Key Information
- Plugin type: Claude Code marketplace plugin
- Delivers two primitives: **Skills** (auto-activate on topic detection) and **Agents** (explicit invocation for workflows)
- 10 skills covering architecture, connectors, IaC, Kubernetes, identity, API, DNS, and troubleshooting
- 6 agents covering full deployment workflows per cloud provider plus network design and IDFW
- Weekly GitHub Action refreshes embedded docs from Twingate's docs site, help center, and public GitHub orgs
- License: Apache 2.0

## Prerequisites
- Claude Code with plugin/marketplace support
- No Twingate API credentials required by the plugin itself (credentials needed for actual deployments)

## Installation

```bash
/plugin marketplace add Twingate-Solutions/twingate-assistant
/plugin install twingate-assistant@twingate-solutions
```

Re-run `/plugin install` to update to the latest version.

## Usage / Step-by-Step

**New deployment:**
```text
Use the twingate-se agent to help me deploy Twingate to my AWS environment.
```

**Document existing deployment (run once, commit result):**
```text
Use the twingate-se agent to document my current Twingate deployment as twingate-context.md.
```

**Troubleshoot access issues:**
```text
Use the twingate-troubleshoot skill. My users can't reach a resource that was working yesterday.
```

**Generate cloud-specific IaC:**
```text
Use the aws-deployer agent to generate Terraform for two HA connectors in us-east-1.
```

**Plan network structure before writing IaC:**
```text
Use the network-designer agent to plan our resource structure for three environments.
```

## Configuration Values
- `twingate-context.md` — optional context file committed to repo; auto-detected by future sessions to skip re-assessment
- Template: `docs/twingate-context-template.md`

## Skills Reference

| Skill | Covers |
|---|---|
| `twingate-architect` | Core ZTNA, Remote Networks, design patterns |
| `twingate-connectors` | Deployment, HA, upgrades, metrics |
| `twingate-terraform` | Terraform provider, secrets management |
| `twingate-pulumi` | TypeScript, Python, Go, C# |
| `twingate-kubernetes` | Helm, operator, CRDs |
| `twingate-idfw` | SSH PAM, kubectl proxy, session recording |
| `twingate-identity` | IdP/SCIM, device trust, JIT |
| `twingate-api` | GraphQL, CLI, automation |
| `twingate-dns-security` | DNS filtering, exit networks, DoH |
| `twingate-troubleshoot` | Connector/access/policy diagnostics |

## Agents Reference

| Agent | Use case |
|---|---|
| `twingate-se` | Full deployment orchestration, environment assessment |
| `aws-deployer` | ECS, EC2, IAM, Secrets Manager |
| `azure-deployer` | ACI, VMs, Key Vault, Entra ID |
| `gcp-deployer` | Cloud Run, GCE, Secret Manager |
| `network-designer` | Pre-IaC network planning |
| `idfw-deployer` | Certificate-based SSH PAM / kubectl proxy |

## Gotchas
- Skills auto-activate on keyword detection — explicit invocation via `/skill <name>` is optional but available
- The `twingate-context.md` file must be committed to the repo to persist across sessions; without it, the SE agent will re-ask environmental questions each session
- Weekly doc refresh happens automatically in the upstream repo; to get updates you must re-run `/plugin install`

## Related Docs
- [`docs/twingate-context-template.md`](