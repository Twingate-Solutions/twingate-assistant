# Secure CI/CD Pipelines with Twingate

## Summary
Twingate Service Accounts enable Zero Trust access control for automated processes like CI/CD pipelines, replacing legacy VPN and static firewall configurations. Clients support headless mode for programmatic connection using service account credentials via command line.

## Key Information
- Service Accounts are first-class citizens in Twingate's Zero Trust architecture
- Linux and Windows clients support headless mode for unattended/automated use
- Access rules can be modified, keys rotated/revoked without firewall or IP allowlist changes
- Pre-built example configs available for CircleCI and GitHub Actions
- Usable as templates for any CI/CD platform or custom automation

## Prerequisites
- Enterprise plan (Service Accounts require Enterprise tier)
- Latest Twingate Linux or Windows client installed in pipeline environment
- Service Account created and configured in Twingate admin console
- Resources defined and assigned to the Service Account

## Step-by-Step
1. Create a Service Account in the Twingate admin console
2. Assign required Resources to the Service Account
3. Generate Service Account key/credentials
4. Install Twingate Linux or Windows client in your pipeline environment
5. Invoke Twingate client in headless mode using Service Account credentials (single command)
6. Pipeline jobs can now access protected resources via Twingate tunnel

## Configuration Values
- Headless mode invocation: single CLI command with service account credentials (see CircleCI/GitHub Actions example configs in linked docs)
- No specific env var names documented on this page — refer to CircleCI and GitHub Actions example pages for exact parameter names

## Gotchas
- Service Accounts are **Enterprise plan only** — not available on lower tiers
- Must use the **latest** Linux or Windows client; older versions do not support headless mode
- Windows and Linux supported; no mention of macOS headless support
- Third-party SaaS pipeline tools (e.g., GitHub Actions) require the client to be installed/run as a step within the pipeline job

## Related Docs
- [Service Accounts](https://www.twingate.com/docs/service-accounts) — setup and management
- [CircleCI example configuration](https://www.twingate.com/docs/circleci)
- [GitHub Actions example configuration](https://www.twingate.com/docs/github-actions)