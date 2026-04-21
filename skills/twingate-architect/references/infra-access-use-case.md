## Page Title
Infrastructure Access

## Summary
Use case overview for securing engineer and DevOps access to technical infrastructure. Networks remain hidden from the internet — no jump servers, bastion hosts, or public endpoints required. Supports programmatic configuration, CI/CD service accounts, and Kubernetes integration.

## Key Information
- No public exposure — Connector hides the network; no bastion or jump server needed
- Deploys in under 15 minutes; no VPN server setup or network reconfiguration
- **IaC**: Terraform provider and Pulumi provider for automating resources, groups, and policies
- **Admin API**: full programmatic management of all Twingate objects
- Least-privilege: per-resource policies and group-based access control
- **CI/CD**: service accounts with service keys for automated pipeline access (CircleCI, GitHub Actions)
- **Kubernetes**: deployable in GKE, EKS, microK8s; Kubernetes Operator manages Twingate resources as CRDs
- Simultaneous multi-cloud and multi-environment (dev/staging/prod) access supported

## Prerequisites
- Connector deployed in each target network or environment
- Service accounts configured for CI/CD pipelines (separate from user identity)

## Step-by-Step
Not applicable on this page — see linked guides for each scenario.

## Configuration Values
None on this page.

## Gotchas
- Service accounts use service keys, not user credentials — manage separately from IdP-based user accounts
- Kubernetes Operator requires a separate installation step and manages Twingate resources as Kubernetes CRDs
- "Unified access" across multiple environments works only if Connectors are deployed in each environment

## Related Docs
- `/docs/terraform-getting-started` — Terraform provider setup
- `/docs/pulumi-getting-started` — Pulumi provider setup
- `/docs/cicd-pipelines-with-twingate` — CI/CD pipeline integration
- `/docs/k8s` — Kubernetes Operator overview
- `/docs/services` — service accounts
- `/docs/access-control-for-staging-environments` — non-production environment best practices
