# Infrastructure Access Use Case

## Page Title
Twingate Infrastructure Access Use Case

## Summary
Twingate provides secure, zero-trust access to on-premises and cloud infrastructure without exposing resources publicly. It supports programmatic configuration via Terraform, Pulumi, and Admin API, and integrates with Kubernetes and CI/CD pipelines. Deployment requires no network reconfiguration and completes in under 15 minutes.

## Key Information
- No public exposure required — eliminates need for jump servers or bastion hosts
- Single lightweight Connector component deployed within the target network
- Simultaneous multi-cloud and multi-environment access supported
- Kubernetes support: GKE, EKS, microK8s via Twingate Kubernetes Operator
- Service accounts enable machine-to-machine (M2M) automated access
- Least-privilege model: per-resource access with custom policies and groups

## Prerequisites
- Twingate account with Admin access
- Network host available for Connector deployment
- For Kubernetes: GKE, EKS, or compatible cluster
- For CI/CD: Service account credentials configured in Twingate

## Configuration Approaches

### IaC / Automation
| Tool | Reference |
|------|-----------|
| Terraform | Getting Started with Terraform and Twingate |
| Pulumi | Getting Started with Pulumi and Twingate |
| Admin API | Programmatic management of resources/groups |

### CI/CD Integration
- CircleCI and GitHub Actions supported
- GitHub Codespaces private resource access supported
- Service accounts used for automated/non-human access

### Kubernetes Deployment Options
- Route traffic **from** a cluster using Twingate Client
- Access **private** resources inside a cluster
- Access **publicly exposed** resources in a cluster
- Manage cluster via `kubectl` securely

## Gotchas
- Connector must be deployed **inside** the target network — it is not a cloud-hosted proxy
- Kubernetes Operator is separate from standard Connector deployment; use it for cluster integration
- CI/CD workflows require Service Accounts, not user credentials — configure these explicitly
- Multi-environment access (dev/staging) requires separate Connectors per network segment

## Related Docs
- Getting Started with Terraform and Twingate
- Getting Started with Pulumi and Twingate
- How to Secure CI/CD Pipelines (CircleCI & GitHub Actions)
- How to Secure Machine-to-machine Communication Using Service Accounts
- Twingate Kubernetes Operator
- How to Securely Manage Kubernetes using kubectl
- Best Practices for Securing Access to Non-production Environments
- How to Add MFA to All Protocols (SSH, RDP, SQL, etc.)
- Using Private DNS with Twingate