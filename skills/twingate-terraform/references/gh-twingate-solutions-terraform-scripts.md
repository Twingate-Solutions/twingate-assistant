---
source: https://github.com/Twingate-Solutions/terraform-scripts
type: github
fetched: 2026-11-13
source_version: 4422725637c974130f2016a2d2b399a8eff00f5f
trust: official
---

# terraform-scripts (Twingate-Solutions)

## Summary
Terraform quickstarts that deploy Twingate Connectors and a private demo resource on AWS, GCP, and Azure. Each folder is a standalone root module, organized by cloud and deployment type (VM, container, Kubernetes). The project is an example provided as-is, with no support or warranty, and was developed with help from an LLM-based coding assistant.

## Key Information
- Licensed under Apache 2.0, including its "AS IS" and limitation-of-liability terms.
- Intended as a reference to build from, not a supported product. Review and test before any critical or production use.
- Modules:
  - AWS: `aws/ec2`, `aws/ecs`, `aws/eks`
  - GCP: `gcp/gce`, `gcp/gce-container`, `gcp/gke`
  - Azure: `azure/vm`, `azure/aci`, `azure/aks`
  - Twingate-only: `twingate-specific-examples/groups`
- Each module has its own README with per-module prerequisites.
- Validation is credential-free: `terraform fmt`, `validate`, `tflint`, and `terraform test` with mocked providers, run in Docker.
- CI runs the same validation image on push and pull request (`.github/workflows/validate.yml`).

## Prerequisites
- Terraform >= 1.9
- Cloud CLI credentials for the target cloud (AWS, GCP, or Azure)
- A Twingate API token with Read, Write & Provision permissions
- Docker (only for running the validation suite)

## Usage / Step-by-Step
1. Change into a module: `cd <cloud>/<deployment>`
2. Copy the example variables file: `cp terraform.tfvars.example terraform.tfvars`
3. Set `tg_network` in `terraform.tfvars` (plus `gcp_project_id` for `gcp/*` modules).
4. Export the token: `export TWINGATE_API_TOKEN="<token>"`
5. Run `terraform init`, then `terraform apply`.
6. Clean up with `terraform destroy`.

Validation:
- All modules: `docker compose -f ci/compose.yaml run --rm validate`
- One module: `docker compose -f ci/compose.yaml run --rm validate aws/ec2`

## Configuration Values
- `TWINGATE_API_TOKEN` (env var): Twingate API token with Read, Write & Provision.
- `tg_network` (tfvars): Twingate network name to deploy into.
- `gcp_project_id` (tfvars): required for GCP modules only.

## Gotchas
- No support or warranty; the code is not guaranteed.
- Mocked tests check configuration, schema, and logic only. They do not exercise cloud APIs, so apply in a sandbox account before relying on a module.
- Each folder is a separate root module with its own state; run Terraform from within the specific module directory.
- Per-module prerequisites differ, so check each module's README.

## Related Docs
- Module READMEs, e.g. `aws/ec2/README.md`, `gcp/gke/README.md`, `azure/aks/README.md`
- `twingate-specific-examples/groups/README.md`
- `LICENSE` (Apache 2.0)
- `.github/workflows/validate.yml`