## Page Title
How to Secure CI/CD Pipelines with Twingate

## Summary
Explains how to use Twingate Service Accounts and headless Client mode to grant automated processes (CI/CD pipelines, unattended scripts) Zero Trust access to private resources. Service Accounts are a first-class Twingate entity; example configurations are provided for CircleCI and GitHub Actions.

## Key Information
- **Service Accounts**: Twingate entities for non-human automated access; managed in Admin Console alongside user accounts; same Group/Resource access model applies
- **Headless mode**: Linux and Windows Clients support a headless (non-interactive) mode for use in automation; authenticates with Service Account credentials via command line
- **Benefit over VPN**: no static firewall/IP allow list changes needed; access rules and keys can be rotated/revoked centrally without network reconfiguration
- **Example configs**: CircleCI and GitHub Actions example configuration profiles provided by Twingate
- **Plan requirement**: Service Accounts require Enterprise plan

## Prerequisites
- Enterprise plan
- Latest Linux or Windows Client (supports headless mode)
- Service Account created in Admin Console

## Step-by-Step
1. Create a Service Account in the Twingate Admin Console
2. Assign the Service Account to Groups that have access to the required Resources
3. Generate Service Account credentials (keys)
4. In CI/CD pipeline: install Twingate Client, authenticate using Service Account credentials in headless mode
5. Pipeline can now access private Resources during the job

## Configuration Values
- Headless mode: single command-line invocation with Service Account credentials
- See `/docs/example-cicd-configurations` for CircleCI and GitHub Actions YAML examples

## Gotchas
- Service Accounts are Enterprise-only -- not available on Starter or Teams plans
- Key rotation should be automated; revoked keys immediately lose access without firewall changes
- Headless mode is currently supported on Linux and Windows clients only

## Related Docs
- `/docs/example-cicd-configurations` -- CircleCI and GitHub Actions example configs
- `/docs/service-accounts-guide` -- Service Account setup and management
- `/docs/linux-headless` -- Linux headless Client documentation
- `/docs/windows-headless` -- Windows headless Client documentation
