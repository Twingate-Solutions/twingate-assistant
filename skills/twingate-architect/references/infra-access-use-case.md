# Infrastructure Access Use Case

## Page Title
Twingate Infrastructure Access Use Case

## Summary
Twingate provides zero-trust network access for engineers and DevOps teams to securely reach on-premises and cloud infrastructure without public exposure. It eliminates the need for jump servers or VPNs while supporting programmatic configuration via Terraform, Pulumi, and Admin API.

## Key Information
- No public-facing endpoints required — resources remain hidden from the internet
- Deployment time: under 15 minutes with a single lightweight Connector host
- No network reconfiguration or VPN server setup needed
- Supports simultaneous access to multiple clouds or environments (dev, staging, prod)
- Kubernetes support: GKE, EKS, microK8s via Twingate Kubernetes Operator

## Prerequisites
- Twingate account with Admin access
- A host within the target network to deploy the Connector
- For IaC: Terraform or Pulumi installed; Twingate provider configured
- For CI/CD: Service account credentials for automated pipelines

## Use Case Guides (Step-by-Step References)

### Automation/IaC
- Pulumi integration → *Getting Started with Pulumi and Twingate*
- Terraform integration → *Getting Started with Terraform and Twingate*
- API-driven config → *Automating configuration with Twingate*

### CI/CD Pipelines
- CircleCI & GitHub Actions → *How to Secure CI/CD Pipelines*
- GitHub Codespaces → *How to Enable Secure Access from GitHub Codespaces*
- Machine-to-machine → *How to Secure Machine-to-machine Communication Using Service Accounts*

### Kubernetes
- Route traffic from cluster → Twingate Client guide
- Access private resources in cluster → dedicated guide
- Access publicly exposed resources in cluster → dedicated guide
- `kubectl` secure management → dedicated guide

### Development Environments
- Non-production access best practices
- MFA for all protocols (SSH, RDP, SQL, zOS)
- Private DNS usage with Twingate

## Configuration Values
- **Service Accounts**: Used for automated/machine-to-machine access (CI/CD pipelines)
- **Kubernetes Operator**: Provides cluster-to-Twingate integration
- **Admin API**: Programmatic resource and access control management
- **Groups + Policies**: Granular per-resource permissions (least privilege)

## Gotchas
- Each network segment requires its own Connector deployed on a host within that network
- CI/CD services need narrowly scoped Service Account permissions — avoid over-provisioning
- Kubernetes deployments have multiple distinct use cases (routing traffic *from* vs. accessing resources *within* a cluster) — consult the appropriate guide

## Related Docs
- Twingate Kubernetes Operator
- Admin API reference
- Terraform provider docs
- Pulumi provider docs
- Private DNS with Twingate
- MFA for all protocols guide
- Non-production environment best practices