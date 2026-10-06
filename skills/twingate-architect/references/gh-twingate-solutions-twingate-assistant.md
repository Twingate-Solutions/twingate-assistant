---
source: https://github.com/Twingate-Solutions/twingate-assistant
type: github
fetched: 2026-10-04
source_version: 926dd6fc7b18cb597af8bfab8ddda0e7895c2427
trust: official
---

# twingate-assistant

A Claude Code plugin that provides Twingate ZTNA domain expertise via skills and agents. It supports architecture design, IaC generation (Terraform/Pulumi), deployment workflows across AWS/Azure/GCP/Kubernetes, and troubleshooting. Skills activate automatically on relevant topics; agents are invoked explicitly for end-to-end workflows.

## Key Information

- Adds two extension types: **Skills** (auto-loaded on topic detection) and **Agents** (explicitly invoked by name)
- Skills cover: architecture, connectors, Terraform, Pulumi, Kubernetes, Identity Firewall, IdP/SCIM, GraphQL API, DNS security, troubleshooting
- Agents cover: SE assessment/design (`twingate-se`), cloud deployers (AWS/Azure/GCP), network design, IDFW deployment
- A weekly GitHub Action refreshes skill reference docs from the Twingate docs site, help center, and public Twingate GitHub orgs
- Licensed under Apache 2.0

## Prerequisites

- Claude Code with plugin/marketplace support
- No Twingate API credentials required at install time (credentials are gathered during agent workflows)

## Usage / Step-by-Step

**Install:**

```
/plugin marketplace add Twingate-Solutions/twingate-assistant
/plugin install twingate-assistant@twingate-solutions
```

**Plan a new deployment:**
```
Use the twingate-se agent to help me deploy Twingate to my AWS environment.
```

**Document an existing deployment:**
```
Use the twingate-se agent to document my current Twingate deployment as twingate-context.md.
```
Commit the resulting file; future sessions pick it up automatically. See `docs/twingate-context-template.md` for the template.

**Troubleshoot an access issue:**
```
Use the twingate-troubleshoot skill. My users can't reach a resource that was working yesterday.
```

**Generate cloud-specific IaC:**
```
Use the aws-deployer agent to generate Terraform for two HA connectors in us-east-1.
Use the azure-deployer agent to deploy connectors as Azure Container Instances with Entra ID auth.
```

## Configuration Values

No environment variables or CLI flags are required to install or load the plugin. Individual agent workflows gather environment-specific values (cloud region, credentials, IdP details) interactively during the session.

## Gotchas

- Skills activate automatically when Twingate topics are mentioned, but can also be invoked explicitly with `/skill <name>` if needed
- To stay current with Twingate changes, periodically re-run `/plugin install twingate-assistant@twingate-solutions` — the weekly Action updates the repo but does not push to your local install automatically
- Context file (`twingate-context.md`) must be committed to the repo root for future sessions to detect it automatically

## Related Docs

- Context file template: `docs/twingate-context-template.md`
- Forking/customization guide: `docs/MAINTAINING.md`
- Contribution guide: `CONTRIBUTING.md`
- Twingate public docs: referenced and summarized in each skill's `references/` directory