# twingate-assistant

A Claude Code plugin that gives Claude Code deep Twingate ZTNA expertise — architecture design, deployment playbooks, IaC generation, and troubleshooting. Once installed, every Claude Code session can act as a Twingate solutions engineer: it assesses your environment, designs Remote Networks, generates Terraform or Pulumi, and walks you through deployments on AWS, Azure, GCP, or Kubernetes.

---

## Install

In Claude Code, add the marketplace and install the plugin:

```bash
/plugin marketplace add Twingate-Solutions/twingate-assistant
/plugin install twingate-assistant@twingate-solutions
```

That's all. The plugin loads automatically in every future Claude Code session.

To update later, re-run the same `/plugin install` command — it pulls the latest version.

---

## Use it

The plugin adds two things to Claude Code:

- **Skills** — domain expertise that loads automatically when relevant topics come up (e.g. mention "connector" and `twingate-connectors` activates).
- **Agents** — orchestrators you invoke explicitly by name for end-to-end workflows.

### Plan a new deployment

```text
Use the twingate-se agent to help me deploy Twingate to my AWS environment.
```

The senior SE agent runs a structured environment assessment, produces a network design, and generates IaC.

### Document an existing deployment

If Twingate is already in place, create a context file once so future sessions skip re-asking:

```text
Use the twingate-se agent to document my current Twingate deployment as twingate-context.md.
```

Commit the resulting file. Future sessions will pick it up automatically. Template: [`docs/twingate-context-template.md`](docs/twingate-context-template.md).

### Troubleshoot

```text
Use the twingate-troubleshoot skill. My users can't reach a resource that was working yesterday.
```

### Generate IaC for a specific cloud

```text
Use the aws-deployer agent to generate Terraform for two HA connectors in us-east-1.
```

```text
Use the azure-deployer agent to deploy connectors as Azure Container Instances with Entra ID auth.
```

---

## Skills

Skills load automatically when Twingate topics are detected, or you can invoke explicitly with `/skill <name>`.

| Skill | What it covers |
| --- | --- |
| `twingate-architect` | Core ZTNA architecture, Remote Networks, Resources, design patterns |
| `twingate-connectors` | Connector deployment, HA, upgrades, metrics, logging |
| `twingate-terraform` | Terraform provider, resource definitions, secrets management |
| `twingate-pulumi` | Pulumi provider — TypeScript, Python, Go, C# |
| `twingate-kubernetes` | Helm chart, Kubernetes operator, CRDs, traffic routing |
| `twingate-idfw` | Identity Firewall — SSH PAM, Kubernetes gateway, session recording |
| `twingate-identity` | IdP integration, SCIM, security policies, device trust, JIT |
| `twingate-api` | GraphQL API, CLI tools, automation scripts |
| `twingate-dns-security` | DNS filtering, exit networks, DNS-over-HTTPS |
| `twingate-troubleshoot` | Diagnostics — connector failures, access failures, policy issues |

---

## Agents

Agents orchestrate multiple skills for end-to-end workflows. Invoke them by name.

| Agent | When to use |
| --- | --- |
| `twingate-se` | Starting any Twingate deployment or major change — environment assessment, network design, end-to-end deployment |
| `aws-deployer` | Deploying connectors on AWS (ECS, EC2, IAM, Secrets Manager) |
| `azure-deployer` | Deploying connectors on Azure (ACI, VMs, Key Vault, Entra ID) |
| `gcp-deployer` | Deploying connectors on GCP (Cloud Run, GCE, Secret Manager, Google Workspace) |
| `network-designer` | Planning a new Twingate network before writing IaC — resource strategy, security tiers, output tables |
| `idfw-deployer` | Implementing certificate-based SSH PAM or kubectl proxy access |

Example invocations:

```text
Use the aws-deployer agent to help me set up HA connectors in us-west-2.
```

```text
Use the network-designer agent to plan our resource structure for three environments.
```

---

## How it stays current

Each skill has a `references/` directory of summarized Twingate documentation. A weekly GitHub Action refreshes those summaries from the live docs site, so the plugin always reflects current Twingate behavior. No action needed on your end — just re-run `/plugin install` occasionally to pull updates.

---

## Forking, customizing, contributing

Want to fork this plugin and customize it for your own organization, run the pipeline against your own docs, or extend it for a Twingate-adjacent product? See [`docs/MAINTAINING.md`](docs/MAINTAINING.md).

Want to contribute back upstream? See [`CONTRIBUTING.md`](CONTRIBUTING.md).

---

## License

Apache 2.0 — see [LICENSE](LICENSE).
