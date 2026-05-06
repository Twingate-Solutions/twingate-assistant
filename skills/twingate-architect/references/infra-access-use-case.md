# Infrastructure Access Use Case

## Page Title
Twingate Infrastructure Access Use Case

## Summary
Twingate provides secure, zero-trust access to on-premises and cloud infrastructure without exposing resources publicly. It replaces jump servers, bastion hosts, and VPNs with a lightweight connector-based approach deployable in under 15 minutes.

## Key Information
- No public internet exposure required for protected resources
- Networks remain hidden while allowing access to authorized users/services
- Supports simultaneous access to multiple clouds or environments
- Programmatic management via Terraform, Pulumi, and Admin API
- Kubernetes operator available for cluster integration

## Prerequisites
- Twingate account with Admin access
- Network where Connector can be deployed (single host)
- No network reconfiguration required

## Use Cases Covered

### CI/CD Workflows
- CircleCI and GitHub Actions pipeline security
- GitHub Codespaces resource access
- Machine-to-machine communication via Service Accounts

### Kubernetes Deployments
- Supported platforms: GKE, Amazon EKS, microK8s
- Traffic routing from Kubernetes clusters
- Accessing private and public resources in clusters
- `kubectl` secure management

### Development Environments
- Non-production environment access controls
- MFA for all protocols (SSH, RDP, SQL, zOS)
- Private DNS integration

## Configuration Values
- **IaC**: Terraform provider, Pulumi provider
- **API**: Admin API for automated management
- **Operator**: Twingate Kubernetes Operator

## Step-by-Step (High Level)
1. Deploy Twingate Connector on single host within target network
2. Define Resources (individual IPs, hostnames, or CIDR ranges)
3. Create Groups with least-privilege access policies
4. Assign users/service accounts to Groups
5. For CI/CD: configure Service Accounts for machine-to-machine access
6. For Kubernetes: deploy Twingate Kubernetes Operator

## Gotchas
- Service Accounts required for automated/machine-to-machine workflows (not regular user accounts)
- Kubernetes operator needed for seamless cluster integration — manual connector deployment has limitations
- Multiple environments (dev/staging) can be accessed simultaneously, but require separate Connectors per network segment

## Related Docs
- [Getting Started with Terraform and Twingate](https://www.twingate.com/docs/terraform)
- [Getting Started with Pulumi and Twingate](https://www.twingate.com/docs/pulumi)
- [Twingate Kubernetes Operator](https://www.twingate.com/docs/kubernetes-operator)
- [How to Secure CI/CD Pipelines](https://www.twingate.com/docs/cicd-pipelines)
- [Machine-to-machine via Service Accounts](https://www.twingate.com/docs/service-accounts)
- [Private DNS with Twingate](https://www.twingate.com/docs/private-dns)
- [Best Practices for Non-production Environments](https://www.twingate.com/docs/non-production-environments)