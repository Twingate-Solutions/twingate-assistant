---
source: https://github.com/Twingate-Solutions/twingate-assistant
type: github
fetched: 2026-11-13
source_version: 8be7e41c20d189b40bb5959d642e8cc151737608
trust: official
---

# twingate-assistant

## Summary
A Claude Code plugin that gives Claude Code Twingate ZTNA expertise: architecture design, deployment playbooks, IaC generation (Terraform/Pulumi), and troubleshooting. Once installed, it loads in every Claude Code session through skills (auto-activated by topic) and agents (invoked by name). It covers AWS, Azure, GCP, and Kubernetes deployments.

## Key Information
- **Skills** load automatically when relevant topics come up, or explicitly via `/skill <name>`. Available skills: `twingate-onboarding`, `twingate-architect`, `twingate-connectors`, `twingate-terraform`, `twingate-pulumi`, `twingate-kubernetes`, `twingate-idfw`, `twingate-identity`, `twingate-api`, `twingate-dns-security`, `twingate-troubleshoot`.
- **Agents** are invoked by name: `twingate-se` (assessment, design, end-to-end deployment), `aws-deployer`, `azure-deployer`, `gcp-deployer`, `deployment-reviewer` (read-only plan review), `network-designer`, `idfw-deployer` (certificate-based SSH PAM, kubectl proxy).
- `twingate-onboarding` runs a guided, multi-session rollout. It accepts diagrams, screenshots, transcripts, firewall/VPN exports, cloud inventory, and IdP group lists. It proposes a design, waits for approval, then either produces an admin task list or builds via API, Python, or Terraform.
- Each skill has a `references/` directory of summarized Twingate docs, refreshed weekly by a GitHub Action from the Twingate docs site, help center, and the Twingate, Twingate-Solutions, Twingate-Labs, and Twingate-Community GitHub orgs.
- License: Apache 2.0.

## Prerequisites
- Claude Code with plugin marketplace support.

## Usage / Step-by-Step
1. Add the marketplace: `/plugin marketplace add Twingate-Solutions/twingate-assistant`
2. Install: `/plugin install twingate-assistant@twingate-solutions`
3. Start a session and prompt, for example:
   - "Help me deploy Twingate. Here's our network diagram."
   - "Use the twingate-se agent to help me deploy Twingate to my AWS environment."
   - "Use the twingate-troubleshoot skill. My users can't reach a resource that was working yesterday."
   - "Use the aws-deployer agent to generate Terraform for two HA connectors in us-east-1."
   - "Use the azure-deployer agent to deploy connectors as Azure Container Instances with Entra ID auth."
4. To document an existing deployment, ask the `twingate-se` agent to write `twingate-context.md` and commit it so future sessions skip re-asking. Template: `docs/twingate-context-template.md`.
5. To update, re-run the `/plugin install` command.

## Configuration Values
- No env vars or CLI flags documented.
- `twingate-deployment/deployment.yaml`: onboarding progress file, used to resume across sessions.
- `twingate-context.md`: optional committed context file describing an existing deployment.

## Gotchas
- `twingate-deployment/deployment.yaml` contains internal network details; keep it out of public repos.
- Updates are not automatic on your side; re-run `/plugin install` to pull the latest references.
- The onboarding skill gets your approval before anything is built; the `deployment-reviewer` agent is read-only.

## Related Docs
- `docs/MAINTAINING.md`: forking, customizing, running the pipeline against your own docs
- `CONTRIBUTING.md`: contributing upstream
- `docs/twingate-context-template.md`: context file template
- `LICENSE`