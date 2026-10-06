---
source: https://www.twingate.com/docs/cicd-pipelines-with-twingate
type: docs
fetched: 2026-10-04
source_version: 6ea3816c624ccfbf9c772c616ffee8d276d54b509520658b67aaa105671c5a30
trust: official
---

# How to Secure CI/CD Pipelines with Twingate

## Summary
Twingate provides Service Accounts to enable Zero Trust access control for automated processes like CI/CD pipelines. Clients support headless mode for service account authentication via command line, replacing VPN or static firewall rules.

## Key Information
- Service Accounts are first-class citizens in Twingate's Zero Trust architecture
- Linux and Windows clients support **headless mode** for unattended/programmatic authentication
- Access rules can be modified, keys rotated/revoked without firewall or IP allowlist changes
- Pre-built configuration profiles available for **CircleCI** and **GitHub Actions**
- Other CI/CD systems can use those profiles as templates

## Prerequisites
- **Enterprise plan** subscription (Service Accounts are Enterprise-only)
- Latest Twingate Linux or Windows client installed
- Service Account created in Twingate admin console
- Resources defined and assigned to the Service Account in admin console

## Step-by-Step
1. Create a Service Account in the Twingate admin console
2. Assign relevant Resources to the Service Account
3. Generate a Service Account Key
4. Install the Twingate client in your pipeline environment
5. Invoke the client in headless mode using the Service Account credentials (single command)
6. Pipeline steps can then reach protected resources as authorized

## Configuration Values
- Headless mode is invoked via **command line** (single command — see CircleCI/GitHub Actions example profiles in Twingate docs)
- Service Account Key should be stored as a **CI/CD secret/environment variable** (not hardcoded)

## Gotchas
- Service Accounts are **Enterprise-only** — not available on lower-tier plans
- Keys must be explicitly rotated/revoked when access should be removed; no automatic expiry is implied
- Third-party SaaS CI runners (e.g., GitHub-hosted Actions runners) require the client to be installed as a pipeline step each run
- Windows and Linux clients support headless mode; **macOS headless support is not mentioned**

## Related Docs
- [Twingate Service Accounts](https://www.twingate.com/docs/service-accounts)
- [CircleCI integration example](https://www.twingate.com/docs/circleci)
- [GitHub Actions integration example](https://www.twingate.com/docs/github-actions)
- Twingate Admin Console — Resource and Group management