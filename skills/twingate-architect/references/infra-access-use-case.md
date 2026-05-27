# Infrastructure Access Use Case

## Page Title
Infrastructure Access Use Case

## Summary
Twingate provides secure, zero-trust access to on-premises and cloud infrastructure without public internet exposure. It supports programmatic configuration via Terraform, Pulumi, and Admin API, and integrates with Kubernetes and CI/CD pipelines.

## Key Information
- No public exposure required — eliminates need for jump servers or bastion hosts
- Deployment time: ~15 minutes, single connector host, no network reconfiguration
- Supports simultaneous multi-cloud and multi-environment access
- Kubernetes support: GKE, EKS, microK8s via Twingate Kubernetes Operator
- Service accounts enable machine-to-machine (M2M) access for automated workflows

## Prerequisites
- Twingate account with Admin access
- Network host available for Connector deployment
- For IaC: Terraform or Pulumi installed; Twingate provider configured
- For Kubernetes: GKE/EKS/microK8s cluster; Twingate Kubernetes Operator

## Use Case Categories & Related Guides

### Automation / IaC
- Terraform integration: Getting Started with Terraform and Twingate
- Pulumi integration: Getting Started with Pulumi and Twingate
- Admin API for programmatic management

### CI/CD Workflows
- CircleCI & GitHub Actions pipeline security
- GitHub Codespaces access to private resources
- Service accounts for M2M communication

### Kubernetes
- Route traffic from cluster using Twingate Client
- Securely access private resources in Kubernetes
- Securely access publicly exposed resources in Kubernetes
- Manage Kubernetes via `kubectl` securely

### Development Environments
- Non-production environment access best practices
- MFA for all protocols (SSH, RDP, SQL, zOS, etc.)
- Private DNS configuration

## Configuration Values
- **Connector**: Lightweight, deployed on single host within target network
- **Granular permissions**: Resource-level access policies + group assignments
- **Service accounts**: Used for automated/non-human access (CI/CD agents)

## Gotchas
- Networks remain hidden from internet — ensure Connector has proper outbound connectivity
- Least privilege requires explicit resource definitions; default is no access
- Kubernetes Operator is separate from standard Client deployment — choose correct approach per use case
- Multi-environment access (dev/staging) requires separate Connectors per environment network

## Related Docs
- Twingate Kubernetes Operator
- Admin API reference
- Terraform provider docs
- Pulumi provider docs
- CircleCI integration guide
- Private DNS with Twingate