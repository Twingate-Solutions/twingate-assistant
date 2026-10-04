---
source: https://www.twingate.com/docs/infra-access-use-case
type: docs
fetched: 2026-10-04
source_version: 2f1ea120cc9aaca4d76bb79b7b9778a7ffc313fb2d2d1f1e261eb3a45810d191
trust: official
---

# Infrastructure Access Use Case

## Page Title
Infrastructure Access Use Case

## Summary
Twingate provides secure, zero-trust network access to technical infrastructure (on-prem and cloud) without public internet exposure. It supports programmatic configuration via Terraform, Pulumi, and an Admin API, and integrates with Kubernetes and CI/CD pipelines.

## Key Information
- No public exposure required — eliminates need for jump servers or Bastion hosts
- Deployment time: under 15 minutes with a single lightweight Connector host
- No network reconfiguration or VPN server setup needed
- Supports simultaneous access to multiple clouds/environments
- Kubernetes support: GKE, EKS, microK8s, and Twingate Kubernetes Operator available

## Prerequisites
- A Twingate account with admin access
- A host within the target network to deploy the Connector
- (For IaC) Terraform or Pulumi installed; Twingate Admin API credentials

## Configuration Values
| Method | Reference |
|---|---|
| Terraform | Twingate Terraform provider |
| Pulumi | Twingate Pulumi integration |
| Admin API | Programmatic management of resources/groups |

## Related Guides (with use cases)

**Automation/IaC**
- Getting Started with Pulumi and Twingate
- Getting Started with Terraform and Twingate

**CI/CD**
- How to Secure CI/CD Pipelines (CircleCI & GitHub Actions)
- How to Enable Secure Access from GitHub Codespaces
- How to Secure Machine-to-machine Communication Using Service Accounts

**Kubernetes**
- How to Route Traffic from a Kubernetes Cluster Using the Twingate Client
- How to Securely Access Private Resources in a Kubernetes Cluster
- How to Securely Access Publicly Exposed Resources in a Kubernetes Cluster
- How to Securely Manage Kubernetes using kubectl

**Dev Environments**
- Best Practices for Securing Access to Non-production Environments
- How to Add MFA to All Protocols (SSH, RDP, SQL, etc.)
- Using Private DNS with Twingate

## Gotchas
- This page is an overview/index only — no direct configuration steps; follow linked guides for implementation
- Kubernetes deployments require the Twingate Kubernetes Operator for cluster-level integration
- Service accounts are required for machine-to-machine (CI/CD) access, not user accounts

## Related Docs
- Twingate Terraform integration
- Twingate Pulumi integration
- Twingate Admin API
- Twingate Kubernetes Operator