# Deploy a Connector on GCP

## Summary
Covers multiple deployment options for Twingate Connectors on Google Cloud Platform, including Compute Engine (manual and automated), GKE, and IaC approaches. Subnets require outbound internet access for image downloads and Twingate connectivity.

## Key Information
- Docker-based deployment works on any 64-bit Linux distro Docker supports
- systemd service supported on Ubuntu, Fedora, Debian, and CentOS
- Access/refresh tokens are Connector-specific — cannot be shared between Connectors
- Peer-to-peer connections recommended for bandwidth Fair Use Policy compliance
- Updates via Linux package manager (manual) or scheduled task (automatic); stagger updates across Connectors to avoid downtime

## Prerequisites
- Subnet with outbound internet access
- Google Cloud CLI (for automated Compute Engine deployment)
- If using Cloud NAT: review `min_ports_per_vm` on NAT gateway (GCP default tuned for large fleets, may be insufficient for smaller deployments)

## Deployment Options

### Automated Compute Engine
1. Admin Console → Remote Networks → select network → Add Connector
2. Click new Connector → Deployment page → select **Google Cloud**
3. Generate tokens (requires re-authentication)
4. Fill in GCP environment details and configure optional features
5. Copy and run the generated command in Google Cloud CLI

### Manual Compute Engine
- Follow standard [Linux Connector deployment instructions](https://www.twingate.com/docs/linux)

### GKE
- Use the [official Twingate Helm chart](https://www.twingate.com/docs/helm)
- Review [Kubernetes Best Practices Guide](https://www.twingate.com/docs/kubernetes-best-practices) if using Twingate for K8s

### Infrastructure as Code
- Terraform, Pulumi, or Twingate API

## Configuration Values
| Setting | Notes |
|---|---|
| `min_ports_per_vm` | Cloud NAT setting — increase if sharing NAT with high-volume workloads |

## Gotchas
- **Cloud NAT**: Default `min_ports_per_vm` may be too low in small deployments sharing NAT with analytics/batch workloads
- **Token sharing**: Each Connector requires its own unique access and refresh tokens
- **Update risk**: Avoid updating all Connectors simultaneously — stagger to prevent downtime

## Related Docs
- [Linux Connector Deployment](https://www.twingate.com/docs/linux)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [Helm Chart / GKE](https://www.twingate.com/docs/helm)
- [Kubernetes Best Practices](https://www.twingate.com/docs/kubernetes-best-practices)
- [Peer-to-Peer Connections](https://www.twingate.com/docs/peer-to-peer)
- [Systemd Connector Update Guide](https://www.twingate.com/docs/systemd-update)
- [Terraform/Pulumi/API Deployment Automation](https://www.twingate.com/docs/deployment-automation)
- [GCP Tune NAT Configuration](https://cloud.google.com/nat/docs/tune-nat-configuration)