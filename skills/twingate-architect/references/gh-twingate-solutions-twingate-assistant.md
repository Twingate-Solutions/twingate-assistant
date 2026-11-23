---
source: https://github.com/Twingate-Solutions/twingate-assistant
type: github
fetched: 2026-11-22
source_version: de80d45fa22206874fd7cbfd951c49f61c643d36
trust: official
---

# twingate-assistant

## Summary
A Claude Code plugin that adds Twingate ZTNA expertise to Claude Code sessions. It provides skills (auto-loaded domain knowledge) and agents (explicitly invoked orchestrators) for architecture design, deployment walkthroughs, IaC generation (Terraform, Pulumi), and troubleshooting on AWS, Azure, GCP, or Kubernetes.

## Key Information
- **Skills** load automatically when relevant topics come up, or can be invoked with `/skill <name>`.
  - `twingate-onboarding`, `twingate-architect`, `twingate-connectors`, `twingate-terraform`, `twingate-pulumi`, `twingate-kubernetes`, `twingate-pam`, `twingate-identity`, `twingate-api`, `twingate-dns-security`, `twingate-troubleshoot`
- **Agents** are invoked by name:
  - `twingate-se`: environment assessment, network design, end-to-end deployment
  - `aws-deployer`, `azure-deployer`, `gcp-deployer`: cloud-specific connector deployment
  - `deployment-reviewer`: read-only plan review (unconfirmed items, broad access, missing connector HA)
  - `network-designer`: network planning before IaC
  - `pam-deployer`: Twingate Gateway (SSH with short-lived certificates, identity-aware kubectl, web-app identity injection)
- `twingate-onboarding` accepts diagrams (image, draw.io, Visio), screenshots, transcripts, firewall/VPN exports, cloud inventory, and IdP group lists. It proposes a design, gets approval, then either gives you a task list or builds via API, Python, or Terraform.
- Each skill has a `references/` directory of summarized Twingate docs, refreshed weekly by a GitHub Action from the Twingate docs site, help center, and several public Twingate GitHub orgs.
- License: Apache 2.0.

## Prerequisites
- Claude Code with plugin support.

## Usage / Step-by-Step
1. Add the marketplace: `/plugin marketplace add Twingate-Solutions/twingate-assistant`
2. Install: `/plugin install twingate-assistant@twingate-solutions`
3. Prompt Claude Code, for example:
   - `Help me deploy Twingate. Here's our network diagram.`
   - `Use the twingate-se agent to help me deploy Twingate to my AWS environment.`
   - `Use the twingate-troubleshoot skill. My users can't reach a resource that was working yesterday.`
   - `Use the aws-deployer agent to generate Terraform for two HA connectors in us-east-1.`
4. For an existing deployment, ask the `twingate-se` agent to document it as `twingate-context.md`, then commit the file so future sessions pick it up.
5. To update, re-run the `/plugin install` command.

## Configuration Values
No environment variables or CLI flags are documented. Files used:
- `twingate-deployment/deployment.yaml`: onboarding progress, resumable across sessions.
- `twingate-context.md`: context file for an existing deployment.

## Gotchas
- `deployment.yaml` contains internal network details; keep it out of public repos.
- The `twingate-idfw` skill is now `twingate-pam` and the `idfw-deployer` agent is now `pam-deployer` (renamed following Twingate's product rename to Privileged Access Management). Update prompts or scripts that use the old names.
- Updates are pulled only when you re-run `/plugin install`.

## Related Docs
- `docs/twingate-context-template.md`: context file template
- `docs/MAINTAINING.md`: forking, customizing, running the pipeline against your own docs
- `CONTRIBUTING.md`: contributing upstream
- `LICENSE`