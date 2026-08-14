---
source: https://www.twingate.com/docs/infra-access-use-case
type: docs
fetched: 2026-08-14
source_version: 0eab85eb3698d1ae6d08e3d2d79ea2c4f564cf35e1716b4d19de243a1ff502db
---

# Infrastructure Access Use Case

## Page Title
Twingate Infrastructure Access Use Case

## Summary
Twingate provides secure access to on-premises and cloud infrastructure without public internet exposure, replacing jump servers and Bastion hosts. It supports programmatic configuration via Terraform, Pulumi, and Admin API for DevOps automation. Deployment takes under 15 minutes with no network reconfiguration required.

## Key Information
- No public internet exposure required — eliminates need for jump servers or Bastion hosts
- Deployment time: under 15 minutes, single lightweight Connector on one host
- Supports simultaneous access to multiple clouds and environments (dev, staging, etc.)
- Kubernetes support: GKE, Amazon EKS, microK8s; Twingate Kubernetes Operator available
- Least-privilege access via granular resource-level permissions and group policies

## Prerequisites
- Twingate account with Admin access
- A host within target network for Connector deployment
- For IaC: Terraform or Pulumi provider configured
- For CI/CD: Service accounts or machine identity configured in Twingate

## Primary Use Cases & Related Guides

### Automation / IaC
- Terraform: *Getting Started with Terraform and Twingate*
- Pulumi: *Getting Started with Pulumi and Twingate*
- Admin API for programmatic management

### CI/CD Pipelines
- CircleCI & GitHub Actions: *How to Secure CI/CD Pipelines*
- GitHub Codespaces: *How to Enable Secure Access to Resources from GitHub Codespaces*
- Machine-to-machine: *How to Secure Machine-to-machine Communication Using Service Accounts*

### Kubernetes
- Route traffic from cluster: *How to Route Traffic from a Kubernetes Cluster Using the Twingate Client*
- Access private resources: *How to Securely Access Private Resources in a Kubernetes Cluster*
- Access public resources securely: *How to Securely Access Publicly Exposed Resources in a Kubernetes Cluster*
- Kubectl management: *How to Securely Manage Kubernetes using kubectl*

### Development Environments
- Non-production best practices: *Best Practices for Securing Access to Non-production Environments*
- MFA for all protocols (SSH, RDP, SQL, zOS): *How to Add Multi-Factor Authentication to all Protocols*
- Private DNS usage guide available

## Configuration Values
- No specific env vars or CLI flags on this page; see linked IaC and API docs for specifics

## Gotchas
- No network reconfiguration needed, but Connector host must have outbound connectivity to Twingate control plane
- Service accounts required for automated/machine-to-machine workflows (not user accounts)
- Kubernetes Operator is a separate integration component from the standard Connector

## Related Docs
- Twingate Kubernetes Operator
- Twingate Admin API
- Terraform Provider docs
- Pulumi Provider docs
- CircleCI integration guide