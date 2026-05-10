# Infrastructure Access Use Case

## Page Title
Twingate Infrastructure Access Use Case

## Summary
Twingate provides secure, zero-trust access to on-premises and cloud infrastructure without public exposure via bastion hosts or VPNs. It supports programmatic configuration through Terraform, Pulumi, and an Admin API, and integrates with Kubernetes and CI/CD pipelines.

## Key Information
- No public internet exposure required — eliminates jump servers/bastion hosts
- Deployment time: under 15 minutes with a single lightweight Connector host
- No network reconfiguration or VPN server setup needed
- Supports simultaneous access to multiple clouds/environments
- Kubernetes Operator available for GKE, EKS, microK8s integrations

## Prerequisites
- A Twingate account with Admin access
- A host within the target network to deploy the Connector
- For IaC: Terraform or Pulumi installed; Twingate Admin API credentials

## Use Case Categories & Related Guides

### Automation / IaC
- Terraform integration: `Getting Started with Terraform and Twingate`
- Pulumi integration: `Getting Started with Pulumi and Twingate`
- Admin API for programmatic management

### CI/CD Workflows
- CircleCI & GitHub Actions: `How to Secure CI/CD Pipelines`
- GitHub Codespaces: `How to Enable Secure Access to Resources from Github Codespaces`
- Machine-to-machine: `How to Secure Machine-to-machine Communication Using Service Accounts`

### Kubernetes
- `How to Route Traffic from a Kubernetes Cluster Using the Twingate Client`
- `How to Securely Access Private Resources in a Kubernetes Cluster`
- `How to Securely Access Publicly Exposed Resources in a Kubernetes Cluster`
- `How to Securely Manage Kubernetes using kubectl`

### Development Environments
- `Best Practices for Securing Access to Non-production Environments`
- `How to Add MFA to all Protocols (ssh, RDP, SQL, zOS, etc.)`
- `Using Private DNS with Twingate`

## Configuration Values
| Method | Reference |
|--------|-----------|
| IaC | Terraform provider, Pulumi provider |
| API | Twingate Admin API |
| K8s | Twingate Kubernetes Operator |

## Gotchas
- Connector must be deployed **inside** the target network — it initiates outbound connections, so no inbound firewall rules needed
- Least-privilege access requires explicit Resource and Group configuration — no implicit broad access
- CI/CD service access should use **Service Accounts**, not user credentials

## Related Docs
- Twingate Terraform Provider
- Twingate Pulumi Provider
- Admin API Reference
- Twingate Kubernetes Operator
- Service Accounts documentation
- Private DNS with Twingate