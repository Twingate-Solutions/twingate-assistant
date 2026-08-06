---
source: https://github.com/Twingate-Solutions/terraform-scripts
type: github
fetched: 2026-08-06
source_version: 92cc225a6753f6906ec6cf9b2c7f6869586e669e
---

<!-- triage: unassigned -->

# terraform-scripts

## Summary
A collection of Terraform quick-start scripts and sandbox demos maintained by the Twingate SE team. Scripts are organized by deployment environment to simplify standing up Twingate infrastructure for testing or reference deployments.

## Key Information
- Maintained by Twingate Solutions Engineers as example/reference material
- Organized by target environment (e.g., AWS, GCP, Azure, etc.)
- Intended for demos, testing, and guided deployments — not hardened production configs
- Uses the [Twingate Terraform provider](https://registry.terraform.io/providers/Twingate/twingate/latest)

## Prerequisites
- Terraform installed (version requirements vary by module)
- A Twingate account with API access
- Twingate API key (generated from the Admin Console)
- Cloud provider credentials appropriate to the target environment (e.g., AWS credentials, GCP service account)

## Usage / Step-by-Step
1. Clone the repository:
   ```bash
   git clone https://github.com/Twingate-Solutions/terraform-scripts.git
   ```
2. Navigate to the desired environment directory.
3. Copy or rename `terraform.tfvars.example` to `terraform.tfvars` (if provided) and populate values.
4. Initialize Terraform:
   ```bash
   terraform init
   ```
5. Review the plan:
   ```bash
   terraform plan
   ```
6. Apply:
   ```bash
   terraform apply
   ```

## Configuration Values
| Variable | Description |
|---|---|
| `twingate_api_key` | API key from Twingate Admin Console |
| `twingate_network` | Your Twingate network/tenant name |
| Cloud-specific vars | Varies by environment (region, VPC ID, credentials, etc.) |

Values are typically set via `terraform.tfvars` or environment variables (e.g., `TF_VAR_twingate_api_key`).

## Gotchas
- Scripts are examples/demos — review before using in production; security hardening is not guaranteed
- Each environment subdirectory may have its own provider version pins and variable requirements; check the local `README` or `variables.tf` before running
- Twingate API keys should not be committed to version control; use environment variables or a secrets manager
- Connector deployments in cloud environments will incur cloud costs

## Related Docs
- [Twingate Terraform Provider – Registry](https://registry.terraform.io/providers/Twingate/twingate/latest/docs)
- [Twingate API Documentation](https://docs.twingate.com/docs/api-overview)
- [Twingate Connector Deployment](https://docs.twingate.com/docs/connectors)
- [Terraform Documentation](https://developer.hashicorp.com/terraform/docs)