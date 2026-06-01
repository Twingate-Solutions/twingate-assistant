# Infrastructure Access Use Case

## Page Title
Twingate Infrastructure Access Use Case

## Summary
Twingate provides zero-trust secure access to on-premises and cloud infrastructure without public internet exposure. It replaces jump servers/bastion hosts with a lightweight connector model deployable in under 15 minutes. Supports programmatic configuration via Terraform, Pulumi, and Admin API.

## Key Information
- No public internet exposure required — eliminates bastion hosts and jump servers
- Single lightweight Connector component per network, no network reconfiguration needed
- Supports simultaneous multi-cloud and multi-environment access
- Kubernetes support: GKE, EKS, microK8s via Twingate Kubernetes Operator
- Service accounts enable machine-to-machine and CI/CD automation access
- Granular, least-privilege permissions per resource via groups and policies

## Prerequisites
- Twingate account with Admin access
- Connector deployed within target network
- For Kubernetes: GKE, EKS, or compatible cluster; Twingate Kubernetes Operator

## Use Case Guides (Actionable Links)

**Automation/IaC:**
- Pulumi integration
- Terraform integration
- Admin API for programmatic management

**CI/CD:**
- CircleCI & GitHub Actions pipeline security
- GitHub Codespaces private resource access
- Machine-to-machine via Service Accounts

**Kubernetes:**
- Route traffic from Kubernetes cluster using Twingate Client
- Access private resources in Kubernetes cluster
- Access publicly exposed resources in Kubernetes cluster
- Manage Kubernetes via `kubectl` securely

**Dev Environments:**
- Non-production environment access best practices
- MFA for all protocols (SSH, RDP, SQL, zOS)
- Private DNS configuration

## Configuration Values
| Method | Reference |
|--------|-----------|
| IaC | Terraform provider, Pulumi provider |
| API | Twingate Admin API |
| Kubernetes | Twingate Kubernetes Operator (Helm-based) |

## Gotchas
- Connector must be deployed inside the target network segment — it cannot reach resources outside its network boundary
- CI/CD services require Service Accounts (not user accounts) for automated access
- Multiple environments (dev/staging) require separate Connectors per network

## Related Docs
- Terraform Getting Started
- Pulumi Getting Started
- Admin API reference
- Twingate Kubernetes Operator
- Service Accounts documentation
- Private DNS with Twingate
- Non-production environment best practices