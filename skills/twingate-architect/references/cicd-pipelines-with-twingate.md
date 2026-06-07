# Securing CI/CD Pipelines with Twingate

## Summary
Twingate Service Accounts enable Zero Trust access control for automated CI/CD pipelines and unattended processes. They replace legacy VPN/firewall approaches by providing headless client modes that connect using service account credentials via command line, manageable through the Twingate admin console.

## Key Information
- Service Accounts are first-class citizens in Twingate's Zero Trust architecture
- Linux and Windows clients support **headless mode** for non-interactive/automated use
- Single command-line invocation to establish connection with service account credentials
- Access rules (resources, keys) managed centrally without firewall/IP allowlist changes
- Keys can be rotated and revoked instantly
- Pre-built example configs available for **CircleCI** and **GitHub Actions**

## Prerequisites
- **Enterprise plan** required for Service Accounts
- Latest Twingate Linux or Windows client installed in pipeline environment
- Service Account created and configured in Twingate admin console
- Resources defined and assigned to the Service Account

## Step-by-Step
1. Create a Service Account in the Twingate admin console
2. Assign required Resources to the Service Account
3. Generate service account key/credentials
4. Store credentials as secrets in your CI/CD platform (e.g., GitHub Actions secrets, CircleCI env vars)
5. Add Twingate client installation step to pipeline
6. Invoke Twingate client in headless mode with service account credentials
7. Run pipeline steps that access protected resources
8. (Optional) Teardown/disconnect at end of pipeline run

## Configuration Values
- Headless mode: invoked via **command line** (specific flags in platform-specific docs)
- Credentials stored as **environment variables/secrets** in CI/CD platform
- Reference CircleCI and GitHub Actions example profiles for exact syntax

## Gotchas
- Service Accounts are **Enterprise plan only** — not available on lower tiers
- Must use **latest** Linux/Windows client — older versions lack headless mode support
- macOS client headless support not mentioned — likely unsupported
- Third-party SaaS pipeline runners (e.g., GitHub-hosted runners) require the client to be installed fresh each run
- Key rotation/revocation is instant — ensure pipelines use current credentials to avoid unexpected failures

## Related Docs
- [Service Accounts](https://www.twingate.com/docs/service-accounts)
- [CircleCI example configuration](https://www.twingate.com/docs/circleci)
- [GitHub Actions example configuration](https://www.twingate.com/docs/github-actions)
- Twingate Admin Console — Resource and Service Account management
- Linux Client documentation (headless mode flags)
- Windows Client documentation (headless mode flags)