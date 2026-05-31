# Securing CI/CD Pipelines with Twingate

## Summary
Twingate Service Accounts enable Zero Trust access control for automated processes like CI/CD pipelines, replacing legacy VPN or direct network deployment approaches. The Twingate Linux and Windows clients support headless mode for service account authentication via command line, enabling integration with CI/CD systems.

## Key Information
- Service Accounts are first-class citizens in Twingate's Zero Trust architecture
- Headless mode allows connection via single command line using service account credentials
- Access rules can be modified, keys rotated/revoked without firewall or IP allowlist changes
- Pre-built example configurations available for CircleCI and GitHub Actions
- Service Accounts require **Enterprise plan**

## Prerequisites
- Twingate Enterprise plan subscription
- Latest Twingate Linux or Windows client (headless mode support required)
- Service Account created in Twingate admin console
- Resources defined and assigned to the Service Account in admin console

## Step-by-Step
1. Create a Service Account in the Twingate admin console
2. Assign required Resources to the Service Account
3. Generate Service Account credentials/keys
4. Configure CI/CD pipeline to invoke Twingate client in headless mode using credentials
5. Reference CircleCI or GitHub Actions example profiles as templates for your pipeline

## Configuration Values
- Headless mode invocation: single command line with service account credentials (exact CLI flags in linked CircleCI/GitHub Actions examples)
- Credentials should be stored as CI/CD secrets/environment variables (not hardcoded)

## Gotchas
- **Enterprise plan only** — Service Accounts not available on lower tiers
- Must use the **latest** Linux or Windows client; older versions may not support headless mode
- macOS client headless support not mentioned — Linux/Windows only
- Key rotation requires updating credentials in pipeline secret stores manually

## Related Docs
- [Service Accounts](https://www.twingate.com/docs/service-accounts) — setup and management
- [CircleCI integration example](https://www.twingate.com/docs/circleci)
- [GitHub Actions integration example](https://www.twingate.com/docs/github-actions)