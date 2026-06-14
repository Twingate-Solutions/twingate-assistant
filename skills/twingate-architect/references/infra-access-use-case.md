# Infrastructure Access Use Case

## Page Title
Infrastructure Access Use Case

## Summary
Twingate provides secure access to on-premises and cloud infrastructure without public internet exposure, replacing jump servers and Bastion hosts. It supports programmatic configuration via Terraform, Pulumi, and Admin API, and integrates with Kubernetes and CI/CD workflows.

## Key Information
- No public internet exposure required — eliminates need for jump servers or Bastion hosts
- Deployment time: under 15 minutes with a single lightweight Connector host
- No network reconfiguration or VPN server setup needed
- Supports simultaneous access to multiple clouds or environments (dev, staging, prod)
- Kubernetes support: GKE, Amazon EKS, microK8s, Kubernetes Operator available
- Service accounts enable machine-to-machine (M2M) access for automated pipelines

## Prerequisites
- Twingate account with Admin access
- Connector deployed within target network
- For Kubernetes: GKE, EKS, or compatible cluster
- For CI/CD: Service account configured in Twingate

## Configuration Approaches
| Method | Use Case |
|--------|----------|
| Terraform provider | IaC automation of resources/groups |
| Pulumi provider | IaC automation (alternative to Terraform) |
| Admin API | Programmatic management |
| Kubernetes Operator | Cluster-native Twingate integration |

## Use Case Guides (Linked)

**Automation:**
- Pulumi + Twingate
- Terraform + Twingate
- Admin API

**CI/CD:**
- CircleCI & GitHub Actions pipeline security
- GitHub Codespaces private resource access
- Machine-to-machine via Service Accounts

**Kubernetes:**
- Route traffic from a Kubernetes cluster using Twingate Client
- Access private resources in a Kubernetes cluster
- Access publicly exposed resources in a Kubernetes cluster
- Manage Kubernetes via `kubectl` securely

**Dev Environments:**
- Non-production environment best practices
- MFA for all protocols (SSH, RDP, SQL, zOS)
- Private DNS with Twingate

## Gotchas
- Connector must be deployed inside the target network segment — it is not a VPN server
- Kubernetes Operator is a separate integration from standard Connector deployment
- Service accounts are required for automated/headless CI/CD access (no user login flow)
- Private DNS configuration is separate and must be explicitly set up for hostname-based resource access

## Related Docs
- [Terraform Integration](https://www.twingate.com/docs/terraform)
- [Pulumi Integration](https://www.twingate.com/docs/pulumi)
- [Admin API](https://www.twingate.com/docs/api)
- [Kubernetes Operator](https://www.twingate.com/docs/kubernetes-operator)
- [CircleCI & GitHub Actions](https://www.twingate.com/docs/ci-cd)
- [Service Accounts](https://www.twingate.com/docs/service-accounts)
- [Private DNS](https://www.twingate.com/docs/private-dns)