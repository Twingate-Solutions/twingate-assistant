## Connector Deployment Automation

Options for automating Twingate Connector deployment, from full Terraform IaC to semi-automated scripting.

**Full Automation — Terraform Provider:**
- Use the Twingate Terraform provider to provision Connectors, Resources, and Remote Networks as code
- See /docs/terraform-getting-started

**API-Based Automation:**
- Twingate Admin API supports programmatic Connector provisioning and token generation
- See /docs/api-overview

**Semi-Automated (manual tokens + scripted deploy):**
- Generate tokens manually from the Admin Console (Manual deployment option)
- Use the tokens in your deployment scripts/pipelines
- Constraints:
  - Each Connector requires its own unique token pair — tokens cannot be reused
  - Each new Connector must be provisioned separately (Admin Console or API)

**Deployment Parameters Reference:**
- Image: `docker.io/twingate/connector:latest`
- `TWINGATE_NETWORK` = your account subdomain (e.g., `acme` for `acme.twingate.com`)
- `TWINGATE_ACCESS_TOKEN` = Connector-specific auth token (treat as a secret, never commit)
- `TWINGATE_REFRESH_TOKEN` = Connector-specific refresh token (treat as a secret)
- `--restart=unless-stopped` (Docker) or equivalent in other container environments
- `TWINGATE_DNS` (optional) = custom DNS server for Resource resolution
- Container name: match the name from the Admin Console for traceability

**Example:**
- Helm chart reference: github.com/Twingate/helm-charts

**Related Docs:**
- /docs/terraform-getting-started -- Full Terraform IaC setup
- /docs/api-overview -- Admin API for programmatic provisioning
- /docs/connector-best-practices -- Token and deployment rules
