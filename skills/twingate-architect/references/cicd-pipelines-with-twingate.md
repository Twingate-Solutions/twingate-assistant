# Securing CI/CD Pipelines with Twingate

## Summary
Twingate provides Service Accounts to enable Zero Trust access control for automated processes like CI/CD pipelines. This replaces legacy VPN connections and static firewall/IP allowlist configurations with centrally managed, revocable credentials that work in headless (unattended) mode.

## Key Information
- Service Accounts are first-class citizens in Twingate's Zero Trust architecture
- Linux and Windows clients support **headless mode** for unattended/automated use
- Single command-line invocation to connect using service account credentials
- Access rules can be modified, keys rotated/revoked without firewall or network changes
- Pre-built example configs available for **CircleCI** and **GitHub Actions**
- Examples can be adapted as templates for any CI/CD system or custom automation

## Prerequisites
- **Enterprise plan** required for Service Accounts
- Latest Twingate Linux or Windows client (headless mode support)
- Service Account created in Twingate admin console
- Resources defined and assigned to the Service Account

## Step-by-Step (High Level)
1. Create a Service Account in the Twingate admin console
2. Assign access to required Resources (existing or new)
3. Generate Service Account key/credentials
4. Install Twingate client in CI/CD environment
5. Invoke Twingate in headless mode using service account credentials (single command)
6. Execute pipeline steps that require access to protected resources

## Configuration Values
- Headless mode: invoked via CLI with service account credentials (exact flags detailed in CircleCI/GitHub Actions example pages)
- Credentials typically injected as environment secrets in CI/CD platform

## Gotchas
- Service Accounts are **Enterprise plan only** — not available on lower tiers
- Must use the **latest** Linux/Windows client; older versions may not support headless mode
- Third-party SaaS CI/CD tools (e.g., GitHub Actions) require the client to be installed as a step in the pipeline runner environment

## Related Docs
- [Service Accounts](https://www.twingate.com/docs/service-accounts) (implied)
- [CircleCI integration example](https://www.twingate.com/docs/circleci)
- [GitHub Actions integration example](https://www.twingate.com/docs/github-actions)