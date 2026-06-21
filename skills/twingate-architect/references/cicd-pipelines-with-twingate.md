# Secure CI/CD Pipelines with Twingate

## Summary
Twingate Service Accounts enable Zero Trust access control for automated processes like CI/CD pipelines, replacing legacy VPN and static firewall approaches. The Twingate Linux and Windows clients support headless mode, allowing service account credentials to be used via command line in automated workflows.

## Key Information
- Service Accounts are first-class citizens in Twingate's Zero Trust architecture
- Headless client mode enables non-interactive authentication via single command
- Access rules modified centrally—no firewall changes or IP allowlist updates needed
- Keys can be rotated and revoked without network redeployment
- Pre-built example configurations available for CircleCI and GitHub Actions
- Examples serve as templates for any CI/CD system or custom automation

## Prerequisites
- Enterprise plan subscription (Service Accounts are Enterprise-only)
- Latest Twingate Linux or Windows client (headless mode support required)
- Service Account created in Twingate admin console
- Resources defined and assigned to the Service Account

## Step-by-Step (General)
1. Create a Service Account in the Twingate admin console
2. Assign relevant Resources to the Service Account
3. Generate a Service Account key
4. Store the key as a secret in your CI/CD platform (e.g., GitHub Actions secret, CircleCI env var)
5. Add a pipeline step to start Twingate client in headless mode using the key
6. Subsequent pipeline steps access protected resources through the Twingate tunnel

## Configuration Values
- Headless mode initiated via **command line** (single command—see CircleCI and GitHub Actions example docs for exact flags)
- Service Account key stored as CI/CD secret/environment variable (platform-specific)

## Gotchas
- Service Accounts require **Enterprise plan**—not available on lower tiers
- Must use **latest** Linux or Windows client; older versions lack headless support
- macOS client headless support not mentioned—verify before using in macOS-based runners
- Third-party SaaS CI/CD systems (e.g., GitHub-hosted runners) require the client to be installed as part of the pipeline step

## Related Docs
- [Service Accounts](https://www.twingate.com/docs/service-accounts) — setup and management
- [CircleCI example configuration](https://www.twingate.com/docs/circleci)
- [GitHub Actions example configuration](https://www.twingate.com/docs/github-actions)
- Twingate Admin Console — Resource and access rule management