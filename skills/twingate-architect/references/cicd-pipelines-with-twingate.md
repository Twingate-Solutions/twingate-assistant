# Securing CI/CD Pipelines with Twingate

## Summary
Twingate Service Accounts enable Zero Trust access control for automated processes like CI/CD pipelines, replacing legacy VPN or direct network deployment approaches. Clients run in headless mode using service account credentials via command line, integrating with pipeline tools like GitHub Actions and CircleCI.

## Key Information
- Service Accounts are first-class citizens in Twingate's Zero Trust architecture
- Linux and Windows clients support headless mode for unattended/automated use
- Access rules, key rotation, and revocation managed centrally—no firewall/IP allowlist changes needed
- Pre-built example configs available for CircleCI and GitHub Actions
- Examples serve as templates for any CI/CD or custom automation tool

## Prerequisites
- **Twingate Enterprise plan** (Service Accounts are Enterprise-only)
- Latest Twingate Linux or Windows client (headless mode support required)
- Service Account created and configured in Twingate admin console
- Resources defined and access granted to the Service Account

## Step-by-Step
1. Create a Service Account in the Twingate admin console
2. Assign access to required Resources (existing or new)
3. Generate Service Account key/credentials
4. Install latest Twingate Linux/Windows client in your pipeline environment
5. Invoke Twingate client in headless mode via single command using service account credentials
6. Pipeline jobs now have Zero Trust access to protected resources

## Configuration Values
- **Headless mode**: Single CLI command invocation (see CircleCI/GitHub Actions example configs for exact flags)
- **Credential injection**: Pass service account keys as environment variables/secrets in your pipeline tool

## Gotchas
- Service Accounts are **Enterprise plan only**—not available on lower tiers
- Must use the **latest** Linux or Windows client; older versions do not support headless mode
- macOS client headless support is not mentioned—assume Linux/Windows only
- Key rotation/revocation must be managed actively; no automatic expiry behavior described

## Related Docs
- [Service Accounts](https://www.twingate.com/docs/service-accounts) (referenced but separate page)
- [CircleCI example configuration](https://www.twingate.com/docs/circleci) (referenced)
- [GitHub Actions example configuration](https://www.twingate.com/docs/github-actions) (referenced)