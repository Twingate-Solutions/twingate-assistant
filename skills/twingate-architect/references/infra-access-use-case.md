# Infrastructure Access Use Case

## Page Title
Infrastructure Access Use Case

## Summary
Twingate provides secure access to on-premises and cloud infrastructure without exposing resources publicly. It supports programmatic configuration via Terraform, Pulumi, and Admin API, and integrates with CI/CD pipelines and Kubernetes environments.

## Key Information
- No public exposure required — eliminates jump servers, Bastion hosts, and VPN servers
- Deployment time: under 15 minutes with a single lightweight Connector host
- No network reconfiguration needed
- Supports simultaneous access to multiple clouds or environments (dev, staging, prod)
- Kubernetes support: GKE, Amazon EKS, microK8s, Kubernetes Operator available

## Prerequisites
- A Twingate account with Admin access
- A host within the target network for Connector deployment
- For IaC: Terraform or Pulumi installed; Twingate provider configured
- For Kubernetes: GKE, EKS, or compatible cluster

## Configuration Options
| Method | Reference |
|--------|-----------|
| Terraform | Twingate Terraform provider |
| Pulumi | Twingate Pulumi integration |
| Admin API | Programmatic management |
| Kubernetes Operator | Cluster-native resource management |

## Use Case Guides

**IaC / Automation**
- Getting Started with Pulumi and Twingate
- Getting Started with Terraform and Twingate

**CI/CD**
- Secure CI/CD Pipelines (CircleCI & GitHub Actions)
- Secure Access from GitHub Codespaces
- Machine-to-machine communication via Service Accounts

**Kubernetes**
- Route traffic from a Kubernetes cluster using Twingate Client
- Securely access private resources in a Kubernetes cluster
- Securely access publicly exposed resources in a Kubernetes cluster
- Manage Kubernetes using `kubectl` securely

**Development Environments**
- Best practices for non-production environment access
- MFA for all protocols (SSH, RDP, SQL, zOS, etc.)
- Private DNS with Twingate

## Gotchas
- Service Accounts must be configured for automated/machine-to-machine workflows — user credentials should not be used in CI/CD contexts
- Kubernetes Operator is a separate integration path from deploying a Connector inside a cluster
- "Unified access" to multiple environments requires separate Connectors per network/environment

## Related Docs
- Twingate Kubernetes Operator
- Service Accounts (machine-to-machine)
- Admin API reference
- Private DNS configuration
- Terraform and Pulumi provider docs