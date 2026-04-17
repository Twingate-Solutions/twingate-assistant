# twingate-assistant

A Claude Code plugin that turns Claude Code into a Twingate ZTNA implementation specialist. Install it once and every session gains deep domain expertise — architecture design, deployment playbooks, IaC generation, troubleshooting, and current documentation awareness.

---

## Installation

```bash
# Add the Twingate Solutions marketplace (once)
/plugin marketplace add Twingate-Solutions/twingate-assistant

# Install the plugin
/plugin install twingate-assistant@twingate-solutions
```

That's it. The plugin loads automatically in future sessions.

### Local development / testing

```bash
git clone https://github.com/Twingate-Solutions/twingate-assistant.git
claude --plugin-dir ./twingate-assistant
```

---

## What It Does

Once loaded, the plugin provides:

- **10 domain skills** — loaded automatically when Twingate topics are detected, or explicitly with `/skill twingate-architect` etc.
- **6 specialist agents** — invoked as `use the twingate-se agent` for end-to-end deployment workflows
- **Auto-updating reference docs** — weekly summaries of the Twingate documentation, refreshed by a GitHub Action
- **Code-first discovery** — when IaC already exists in your repo, the plugin reads it before generating anything new

---

## Getting Started

### New deployment

Invoke the senior SE agent for an end-to-end guided workflow:

```text
Use the twingate-se agent to help me deploy Twingate to my AWS environment.
```

The agent runs a structured environment assessment, produces a network design, and generates IaC.

### Existing deployment

If you already have Twingate deployed, create a context file so the plugin understands your current topology without re-asking:

```text
Use the twingate-se agent to document my current Twingate deployment as twingate-context.md
```

This creates a structured context file (see [`docs/twingate-context-template.md`](docs/twingate-context-template.md) for the schema) that the plugin reads at the start of future sessions. Commit it to your repo — it replaces the need for a full environment assessment every time.

### Troubleshooting

```text
Use the twingate-troubleshoot skill. My users can't reach a resource that was working yesterday.
```

### IaC generation

```text
Use the aws-deployer agent to generate Terraform for two HA connectors in us-east-1.
```

---

## Skills

Skills are loaded automatically when Twingate topics are detected. You can also invoke them explicitly.

| Skill | Topics | Example trigger |
| --- | --- | --- |
| `twingate-architect` | Core ZTNA architecture, Remote Networks, Resources, design patterns | "Design a Twingate deployment for our multi-region AWS setup" |
| `twingate-connectors` | Connector deployment, HA, upgrades, metrics, logging | "How do I deploy connectors on ECS Fargate?" |
| `twingate-terraform` | Terraform provider, resource definitions, secrets management | "Generate Terraform for a new Remote Network and connector pair" |
| `twingate-pulumi` | Pulumi provider, TypeScript/Python/Go/C# IaC | "Add Twingate resources to our existing Pulumi stack" |
| `twingate-kubernetes` | Helm chart, Kubernetes operator, CRDs, traffic routing | "Deploy the Twingate connector to our EKS cluster" |
| `twingate-idfw` | Identity Firewall, SSH PAM, Kubernetes gateway, session recording | "Set up certificate-based SSH with session recording for contractors" |
| `twingate-identity` | IdP integration, SCIM, security policies, device trust, JIT | "Configure Okta SAML + SCIM with device trust enforcement" |
| `twingate-api` | GraphQL API, CLI tools, automation scripts | "Write a Python script to audit all resources and their group assignments" |
| `twingate-dns-security` | DNS filtering, exit networks, DNS-over-HTTPS | "Configure split-tunnel DNS filtering for our marketing group" |
| `twingate-troubleshoot` | Diagnostics, connector failures, access failures, policy issues | "Connector is showing DEAD_NO_RELAYS, how do I fix it?" |

---

## Agents

Agents are orchestrators that combine multiple skills for end-to-end workflows.

| Agent | Role | When to use |
| --- | --- | --- |
| `twingate-se` | Senior SE orchestrator — environment assessment, network design, full deployment | Starting any Twingate deployment or major change |
| `aws-deployer` | AWS deployment specialist — ECS, EC2, IAM, Secrets Manager | Deploying connectors on AWS infrastructure |
| `azure-deployer` | Azure deployment specialist — ACI, VMs, Key Vault, Entra ID | Deploying connectors on Azure infrastructure |
| `gcp-deployer` | GCP deployment specialist — Cloud Run, GCE, Secret Manager, Google Workspace | Deploying connectors on GCP infrastructure |
| `network-designer` | Remote network topology planner — resource strategy, security tiers, output tables | Planning a new Twingate network before writing IaC |
| `idfw-deployer` | Identity Firewall specialist — SSH PAM, Kubernetes gateway, Ansible, session recording | Implementing certificate-based SSH or kubectl proxy access |

### Invoking an agent

```text
Use the aws-deployer agent to help me set up HA connectors in us-west-2.
```

```text
Use the network-designer agent to plan our resource structure for three environments.
```

---

## Auto-Update Pipeline

Reference documentation in each skill's `references/` directory is kept current by a weekly GitHub Action:

1. Fetches the Twingate documentation sitemap
2. Crawls changed or new doc pages
3. Summarizes each page via the Claude API (Sonnet)
4. Writes summaries to the appropriate skill's `references/` directory
5. Opens a PR if anything changed

**Evergreen knowledge** (the `SKILL.md` files themselves — guidelines, decisions, routing rules) is never touched by the pipeline. It is hand-authored and reviewed manually.

To run the pipeline locally:

```bash
# No API key needed — uses Claude Code CLI:
python scripts/test_pipeline.py --claude-code --url https://www.twingate.com/docs/how-twingate-works

# Full production run (requires ANTHROPIC_API_KEY):
ANTHROPIC_API_KEY=your_key python scripts/update_references.py
```

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for full pipeline documentation.

---

## Architecture

```text
twingate-assistant/
├── .claude-plugin/
│   └── plugin.json              # Plugin manifest
├── skills/                      # 10 domain expertise skills
│   └── twingate-{domain}/
│       ├── SKILL.md             # Evergreen guidelines + identity (hand-authored)
│       └── references/          # Auto-generated doc summaries (pipeline-managed)
├── agents/                      # 6 orchestrating subagents
│   ├── twingate-se.md
│   ├── aws-deployer.md
│   ├── azure-deployer.md
│   ├── gcp-deployer.md
│   ├── network-designer.md
│   └── idfw-deployer.md
├── scripts/                     # Auto-update pipeline
│   ├── update_references.py     # Orchestrator
│   ├── fetch_sitemap.py         # Sitemap XML parser
│   ├── summarize_docs.py        # Claude API summarizer
│   ├── diff_docs.py             # New/removed doc detection
│   ├── doc_mapping.yaml         # Doc URL → skill routing
│   └── requirements.txt
├── .github/workflows/
│   └── update-docs.yml          # Weekly cron GitHub Action
└── docs/
    └── twingate-context-template.md  # Schema for per-repo context files
```

**Design principles:**

- Skills contain **evergreen expertise** (guidelines, anti-patterns, routing decisions) + **dynamic references** (auto-updated doc summaries). Technical facts live in `references/`, not in the skill body.
- Agents are **orchestrators**, not encyclopedias. They invoke skills; they don't duplicate skill content.
- GitHub repos (Terraform provider, Helm charts, Kubernetes operator) are **referenced at runtime**, not bundled. Skills instruct Claude Code to clone/inspect them when needed.
- The auto-update pipeline is **idempotent** — it opens no PR when nothing changes.

---

## Requirements

- Claude Code (any recent version)
- An `ANTHROPIC_API_KEY` GitHub Actions secret if you want the auto-update pipeline to run (not required to use the plugin)

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to add skills, update evergreen knowledge, extend the doc mapping, run the pipeline locally, and submit PRs.

---

## License

Apache 2.0 — see [LICENSE](LICENSE).
