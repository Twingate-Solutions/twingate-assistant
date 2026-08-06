---
source: https://github.com/Twingate-Solutions/pulumi-scripts
type: github
fetched: 2026-08-06
source_version: dafb9df9c650cc52c93cc95f4aaee813bbe1127a
---

<!-- triage: unassigned -->

# pulumi-scripts

## Repo Title
Twingate Pulumi Quick Start Scripts

## Summary
A collection of infrastructure-as-code scripts for deploying Twingate components using Pulumi, organized by target environment. Provides quick start templates to automate Twingate connector and resource provisioning across cloud providers.

## Key Information
- Scripts are organized by environment (e.g., AWS, GCP, Azure)
- Uses Pulumi as the IaC framework
- Targets Twingate connector deployments and network resource configuration
- Minimal documentation in the README itself; content lives in subdirectories

## Prerequisites
- [Pulumi CLI](https://www.pulumi.com/docs/install/) installed
- A Twingate account with admin access
- Twingate API key
- Cloud provider credentials appropriate to the target environment (AWS, GCP, Azure, etc.)
- Node.js, Python, or other Pulumi-supported runtime depending on the script

## Usage / Step-by-Step
1. Clone the repository:
   ```bash
   git clone https://github.com/Twingate-Solutions/pulumi-scripts.git
   ```
2. Navigate to the subdirectory for your target environment.
3. Review the local README or script comments for environment-specific instructions.
4. Install dependencies (varies by runtime, e.g., `npm install` or `pip install -r requirements.txt`).
5. Configure required environment variables or Pulumi config values (see below).
6. Run the deployment:
   ```bash
   pulumi up
   ```

## Configuration Values
Exact values vary by script; common expected parameters include:

| Variable | Description |
|---|---|
| `TWINGATE_API_KEY` | Twingate API key for authenticating with the Twingate API |
| `TWINGATE_NETWORK` | Your Twingate network name (e.g., `mycompany`) |
| Cloud provider credentials | AWS `AWS_ACCESS_KEY_ID`/`AWS_SECRET_ACCESS_KEY`, GCP service account, etc. |

Set via Pulumi config:
```bash
pulumi config set twingate:apiKey <value> --secret
pulumi config set twingate:network <value>
```

## Gotchas
- The main README contains no setup instructions; check subdirectory READMEs for actual usage details.
- API keys should be stored as Pulumi secrets (`--secret` flag), not plain config values.
- Pulumi stack state must be managed (locally or via Pulumi Cloud) before running scripts.
- Cloud provider permissions must be sufficient to create the resources defined in each script (VMs, networking, IAM roles, etc.).
- No versioning or release tags visible; scripts may drift from current Twingate API behavior.

## Related Docs
- [Twingate API Reference](https://docs.twingate.com/reference/api-overview)
- [Twingate Pulumi Provider](https://www.pulumi.com/registry/packages/twingate/)
- [Pulumi Getting Started](https://www.pulumi.com/docs/get-started/)
- [Twingate Connector Deployment](https://docs.twingate.com/docs/connectors)