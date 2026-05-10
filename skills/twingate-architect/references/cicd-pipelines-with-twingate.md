# Securing CI/CD Pipelines with Twingate

## Summary
Twingate Service Accounts enable Zero Trust access control for automated CI/CD pipelines and unattended processes. They replace legacy VPN and static firewall rules by providing centralized, revocable access credentials manageable from the Twingate admin console.

## Key Information
- Service Accounts are first-class citizens in Twingate's Zero Trust architecture
- Linux and Windows clients support **headless mode** for non-interactive authentication
- Access rules can be modified, and keys rotated/revoked without network config changes
- Pre-built examples available for **CircleCI** and **GitHub Actions**
- Examples serve as templates for any CI/CD platform or custom automation

## Prerequisites
- **Enterprise plan** required for Service Accounts
- Latest Twingate Linux or Windows client (headless mode support)
- Twingate admin console access to configure resources and assign Service Account permissions

## Implementation Steps
1. Create a Service Account in the Twingate admin console
2. Assign the Service Account access to required Resources
3. Generate Service Account keys/credentials
4. Configure your CI/CD pipeline to invoke the Twingate client in headless mode using a single command line
5. Store credentials as secrets in your CI/CD platform (e.g., GitHub Actions secrets, CircleCI environment variables)
6. Reference provided CircleCI or GitHub Actions example configs as templates

## Configuration Values
- Headless mode invocation: single CLI command (platform-specific; see CircleCI/GitHub Actions example docs)
- Credentials passed via environment variables or secrets store in CI/CD platform

## Gotchas
- Service Accounts are **Enterprise plan only** — not available on lower tiers
- Must use the **latest** client version; older clients do not support headless mode
- Third-party SaaS pipeline tools (e.g., GitHub Actions) require the Twingate client to be installed/started as a step within the pipeline job

## Related Docs
- [Service Accounts](https://www.twingate.com/docs/service-accounts)
- [CircleCI example configuration](https://www.twingate.com/docs/circleci)
- [GitHub Actions example configuration](https://www.twingate.com/docs/github-actions)