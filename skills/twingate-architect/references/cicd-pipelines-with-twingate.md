---
source: https://www.twingate.com/docs/cicd-pipelines-with-twingate
type: docs
fetched: 2026-08-14
source_version: af5cbc236cdf88b7b6c5f15f7e56727b2705e0c6a3e326f0be3ec3c8ff13e0df
---

# Secure CI/CD Pipelines with Twingate

## Summary
Twingate Service Accounts enable Zero Trust access control for automated processes like CI/CD pipelines, replacing legacy VPN and static firewall configurations. Service accounts integrate with Twingate's existing access model and support headless client modes for unattended authentication via command line.

## Key Information
- Service Accounts are first-class citizens in Twingate's Zero Trust architecture
- Linux and Windows clients support **headless mode** for service account authentication
- Access rules can be modified, keys rotated/revoked without firewall or IP allowlist changes
- Pre-built example profiles available for **CircleCI** and **GitHub Actions**
- Examples serve as templates for other CI/CD systems or custom automation

## Prerequisites
- **Enterprise plan** required for Service Accounts
- Latest Twingate Linux or Windows client (headless mode support)
- Existing Twingate network with defined Resources

## Implementation Steps
1. Create a Service Account in the Twingate Admin Console
2. Assign the Service Account access to relevant Resources
3. Configure headless mode using service account credentials via CLI
4. Integrate the CLI command into your pipeline (single command invocation)
5. Reference CircleCI or GitHub Actions example profiles as templates

## Configuration Values
- Headless mode activated via **single command line** using service account credentials (see platform-specific docs for flags)
- Credentials managed through Twingate Admin Console (key rotation/revocation available)

## Gotchas
- Service Accounts are **Enterprise plan only** — not available on lower tiers
- Headless mode requires the **latest** client version; older clients do not support it
- Windows client also supports headless mode, not just Linux
- Third-party SaaS pipeline tools (e.g., GitHub Actions) are explicitly supported use cases

## Related Docs
- [Service Accounts](https://www.twingate.com/docs/service-accounts)
- [CircleCI Integration Example](https://www.twingate.com/docs/circleci)
- [GitHub Actions Integration Example](https://www.twingate.com/docs/github-actions)
- Twingate Linux Client (headless mode)
- Twingate Windows Client (headless mode)