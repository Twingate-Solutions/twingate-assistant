---
source: https://github.com/Twingate-Solutions/twingate-assistant
type: github
fetched: 2026-11-15
source_version: eea776952f5d266726ab55265754d83b6d1bfb67
trust: official
---

# twingate-assistant

## Summary
A Claude Code plugin from Twingate-Solutions that gives Claude Code Twingate ZTNA expertise: architecture design, deployment playbooks, IaC generation (Terraform/Pulumi), and troubleshooting. Once installed, it loads in every Claude Code session through skills (auto-activated by topic) and agents (invoked by name).

## Key Information
- **Skills** load automatically when relevant topics come up, or explicitly via `/skill <name>`:
  - `twingate-onboarding`: guided multi-session rollout
  - `twingate-architect`
  - `twingate-connectors`
  - `twingate-terraform`
  - `twingate-pulumi`
  - `twingate-kubernetes`
  - `twingate-idfw`
  - `twingate-identity`
  - `twingate-api`
  - `twingate-dns-security`
  - `twingate-troubleshoot`
- **Agents** are invoked explicitly by name:
  - `twingate-se`: assessment, design, and end-to-end deployment
  - `aws-deployer`, `azure-deployer`, `gcp-deployer`
  - `deployment-reviewer`: read-only plan review
  - `network-designer`
  - `idfw-deployer`: SSH PAM and kubectl proxy access
- Each skill has a `references/` directory of summarized Twingate docs. A weekly GitHub Action refreshes it from the Twingate docs, help center, and the Twingate, Twingate-Solutions, Twingate-Labs, and Twingate-Community GitHub orgs.
- License: Apache 2.0.

## Prerequisites
- Claude Code with plugin support.
- For deployment work, access to your cloud environment (AWS, Azure, GCP, or Kubernetes) and a Twingate account.

## Usage / Step-by-Step
1. Install inside Claude Code:
   - `/plugin marketplace add Twingate-Solutions/twingate-assistant`
   - `/plugin install twingate-assistant@twingate-solutions`
2. Start a guided deployment: "Help me deploy Twingate. Here's our network diagram." The onboarding skill accepts diagrams (image, draw.io, Visio), screenshots, transcripts, firewall/VPN exports, cloud inventory, or IdP group lists. It asks questions, proposes a design, and waits for approval before building. It then gives you a task list or builds via API, Python, or Terraform.
3. Plan with the SE agent: "Use the twingate-se agent to help me deploy Twingate to my AWS environment."
4. Document an existing deployment: "Use the twingate-se agent to document my current Twingate deployment as twingate-context.md." Commit the file so future sessions pick it up. Template: `docs/twingate-context-template.md`.
5. Troubleshoot: "Use the twingate-troubleshoot skill. My users can't reach a resource that was working yesterday."
6. Generate cloud IaC, for example: "Use the aws-deployer agent to generate Terraform for two HA connectors in us-east-1."
7. Update by re-running the `/plugin install` command.

## Configuration Values
No environment variables or CLI flags are documented. Onboarding progress is saved to `twingate-deployment/deployment.yaml`.

## Gotchas
- `twingate-deployment/deployment.yaml` contains internal network details. Keep it out of public repos.
- Updates are not automatic on your side. Re-run `/plugin install` to pull the latest references.
- Onboarding is multi-session. Nothing is built until you approve the design.

## Related Docs
- `docs/twingate-context-template.md`
- `docs/MAINTAINING.md` (forking, customizing, running the pipeline on your own docs)
- `CONTRIBUTING.md`
- `LICENSE`