# Securing CI/CD Pipelines with Twingate

## Summary
Twingate Service Accounts enable Zero Trust access control for automated processes like CI/CD pipelines, replacing legacy VPN and static firewall rules. The Linux and Windows clients support headless mode, allowing service account credentials to be used via command line in automated workflows.

## Key Information
- Service Accounts are first-class citizens in Twingate's Zero Trust architecture
- Assign service accounts to existing Resources or define new ones via admin console
- Headless mode allows single command-line connection using service account credentials
- No firewall rule changes needed when modifying access — manage via admin console only
- Keys can be rotated and revoked without network disruption
- Pre-built example configs available for **CircleCI** and **GitHub Actions**
- Examples serve as templates for any CI/CD or custom automation platform

## Prerequisites
- **Enterprise plan** required for Service Accounts
- Latest Linux or Windows Twingate client (headless mode support)
- Service Account created and configured in Twingate admin console
- Service Account assigned to relevant Resources

## Implementation Steps
1. Create a Service Account in the Twingate admin console
2. Assign the Service Account access to required Resources
3. Configure the Twingate client in headless mode using service account credentials (single CLI command)
4. Integrate the headless startup command into your CI/CD pipeline step
5. Use CircleCI or GitHub Actions example configs as templates if applicable

## Configuration Values
- **Headless mode**: Initiated via CLI flag on Linux/Windows client (see platform-specific client docs)
- **Service Account credentials**: Generated in admin console; used as CLI arguments or environment secrets in pipeline config

## Gotchas
- Service Accounts are **Enterprise plan only** — not available on lower tiers
- Only **Linux and Windows** clients support headless mode; macOS is not mentioned
- Third-party SaaS CI/CD tools (e.g., GitHub Actions) require the Twingate client to be installed as a step within the runner environment
- Access rules and key rotation are managed centrally — ensure pipeline secrets stay synchronized when keys are rotated

## Related Docs
- [Service Accounts](https://www.twingate.com/docs/service-accounts) — setup and management
- [CircleCI Integration Example](https://www.twingate.com/docs/circleci)
- [GitHub Actions Integration Example](https://www.twingate.com/docs/github-actions)
- Twingate Linux Client (headless mode documentation)
- Twingate Windows Client (headless mode documentation)