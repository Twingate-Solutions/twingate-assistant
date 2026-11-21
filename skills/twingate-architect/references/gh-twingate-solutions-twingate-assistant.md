---
source: https://github.com/Twingate-Solutions/twingate-assistant
type: github
fetched: 2026-11-19
source_version: cbfb2eeca4ee471be1f76e5681e143264cbc4d3c
trust: official
---

# Twingate-Solutions/twingate-assistant

## Summary
A Claude Code plugin that gives Claude Code Twingate ZTNA expertise: architecture design, deployment playbooks, IaC generation (Terraform/Pulumi), and troubleshooting. It bundles skills that load automatically on relevant topics and agents that you invoke by name for end-to-end workflows on AWS, Azure, GCP, or Kubernetes.

## Key Information
- **Skills** (auto-load, or `/skill <name>`): `twingate-onboarding`, `twingate-architect`, `twingate-connectors`, `twingate-terraform`, `twingate-pulumi`, `twingate-kubernetes`, `twingate-idfw`, `twingate-identity`, `twingate-api`, `twingate-dns-security`, `twingate-troubleshoot`.
- **Agents** (invoke by name): `twingate-se`, `aws-deployer`, `azure-deployer`, `gcp-deployer`, `deployment-reviewer` (read-only plan review), `network-designer`, `idfw-deployer` (SSH PAM / kubectl proxy).
- `twingate-onboarding` runs a guided, multi-session rollout. It accepts diagrams, screenshots, transcripts, firewall/VPN exports, cloud inventory, and IdP group lists. It proposes a design, waits for approval, then either produces an admin task list or builds via API, Python, or Terraform.
- Each skill has a `references/` directory of summarized Twingate docs. A weekly GitHub Action refreshes them from the Twingate docs site, help center, and the public Twingate, Twingate-Solutions, Twingate-Labs, and Twingate-Community GitHub orgs.
- License: Apache 2.0.

## Prerequisites
- Claude Code with plugin support.
- For actual deployments: access to your Twingate tenant and the relevant cloud or Kubernetes environment (implied by the workflows).

## Usage / Step-by-Step
1. Add the marketplace in Claude Code: `/plugin marketplace add Twingate-Solutions/twingate-assistant`
2. Install: `/plugin install twingate-assistant@twingate-solutions`
3. Start a session and prompt, for example:
   - "Help me deploy Twingate. Here's our network diagram."
   - "Use the twingate-se agent to help me deploy Twingate to my AWS environment."
   - "Use the twingate-troubleshoot skill. My users can't reach a resource that was working yesterday."
   - "Use the aws-deployer agent to generate Terraform for two HA connectors in us-east-1."
4. For an existing deployment, ask the `twingate-se` agent to document it as `twingate-context.md` and commit the file so future sessions pick it up. Template: `docs/twingate-context-template.md`.
5. To update, re-run the `/plugin install` command.

## Configuration Values
No environment variables or CLI flags are documented. State files:
- `twingate-deployment/deployment.yaml`: onboarding progress, so work can resume across sessions.
- `twingate-context.md`: existing-deployment context.

## Gotchas
- `deployment.yaml` contains internal network details. Keep it out of public repos.
- Updates are not automatic. Re-run `/plugin install` to get refreshed reference content.
- The onboarding skill requires your approval of the design before anything is built.

## Related Docs
- `docs/MAINTAINING.md`: forking, customizing, running the pipeline against your own docs.
- `CONTRIBUTING.md`: contributing upstream.
- `docs/twingate-context-template.md`
- `LICENSE`