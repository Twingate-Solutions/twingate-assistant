# Securing CI/CD Pipelines with Twingate

## Summary
Twingate provides Service Accounts to enable Zero Trust access control for automated CI/CD pipelines and unattended processes. This replaces legacy VPN or direct network deployment approaches with centrally managed, headless client connections using service account credentials.

## Key Information
- Service Accounts are first-class citizens in Twingate's Zero Trust architecture
- Linux and Windows clients support **headless mode** — connect via single command line
- No firewall rule or IP allowlist changes needed when modifying access
- Keys can be rotated and revoked without network redeployment
- Pre-built example profiles available for **CircleCI** and **GitHub Actions**
- Examples serve as templates for any CI/CD or custom automation

## Prerequisites
- **Enterprise plan** required for Service Accounts
- Latest Twingate Linux or Windows client (supports headless mode)
- Service Account created and configured in Twingate Admin Console
- Resources defined and access assigned to the Service Account

## Step-by-Step
1. Create a Service Account in the Twingate Admin Console
2. Assign access to required Resources (existing or new)
3. Generate service account key/credentials
4. Install Twingate Linux or Windows client in your pipeline environment
5. Invoke Twingate client in headless mode using service account credentials (single command)
6. Pipeline jobs execute with access to protected resources via Twingate

## Configuration Values
- Headless mode invocation: single CLI command with service account credentials (see CircleCI/GitHub Actions example profiles for exact flags)
- Credentials should be stored as **secrets/environment variables** in your CI/CD platform

## Gotchas
- Service Accounts are **Enterprise-only** — not available on lower-tier plans
- Must use the **latest** client version; older clients do not support headless mode
- Windows and Linux supported; no mention of macOS headless support
- Third-party SaaS CI/CD systems (e.g., GitHub Actions) require storing Twingate credentials as platform secrets

## Related Docs
- [Service Accounts](https://www.twingate.com/docs/service-accounts) (referenced but separate page)
- [CircleCI integration example](https://www.twingate.com/docs/circleci)
- [GitHub Actions integration example](https://www.twingate.com/docs/github-actions)