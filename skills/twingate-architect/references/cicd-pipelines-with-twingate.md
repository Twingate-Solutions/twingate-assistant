# Securing CI/CD Pipelines with Twingate

## Summary
Twingate Service Accounts enable Zero Trust access control for automated processes like CI/CD pipelines. The Linux and Windows clients support headless mode, allowing service account credentials to be used via command line in automated environments. This replaces legacy VPN and static firewall/IP allowlist approaches.

## Key Information
- Service Accounts are first-class citizens in Twingate's Zero Trust architecture
- Assign service accounts to existing Resources or create new ones in the admin console
- Headless mode: connect using service account credentials via single command line
- No firewall rule changes or IP allowlist modifications needed
- Keys can be rotated and revoked without network redeployment
- Pre-built example configs available for **CircleCI** and **GitHub Actions**
- Examples serve as templates for other CI/CD systems or custom automation

## Prerequisites
- **Enterprise plan** (Service Accounts require Enterprise tier)
- Latest Twingate Linux or Windows client (headless mode support)
- Service Account created in Twingate admin console
- Resources defined and assigned to the Service Account

## Step-by-Step (General Flow)
1. Create a Service Account in the Twingate admin console
2. Assign required Resources to the Service Account
3. Generate a Service Account Key
4. Store the key as a secret in your CI/CD platform (e.g., GitHub Actions secrets, CircleCI env vars)
5. Add a pipeline step to start Twingate client in headless mode using the key
6. Subsequent pipeline steps access protected Resources through the Twingate tunnel

## Configuration Values
- Headless mode initiated via single CLI command (specific flags in platform-specific docs)
- Service account key passed as credential to the client
- Reference the CircleCI and GitHub Actions example profiles linked from this page for exact syntax

## Gotchas
- Service Accounts are **Enterprise-only** — not available on lower-tier plans
- Must use the **latest** Linux or Windows client; older versions lack headless mode support
- Third-party SaaS CI/CD tools (e.g., GitHub Actions) are explicitly supported use cases
- Windows client also supports headless mode, not just Linux

## Related Docs
- [Service Accounts](https://www.twingate.com/docs/service-accounts)
- [CircleCI example configuration](https://www.twingate.com/docs/cicd-pipelines-with-twingate)
- [GitHub Actions example configuration](https://www.twingate.com/docs/cicd-pipelines-with-twingate)
- Twingate admin console — Resource and Service Account management