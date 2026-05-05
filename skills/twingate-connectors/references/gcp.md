# Deploy a Connector on GCP

## Summary
Covers multiple deployment options for Twingate Connectors on Google Cloud Platform including Compute Engine (manual and automated), GKE, and IaC approaches. Subnet must have outbound internet access for image download and Twingate connectivity.

## Key Information
- Supports Docker-based deployment on any 64-bit Linux distro with Docker
- systemd service supported on: Ubuntu, Fedora, Debian, CentOS
- Access/refresh tokens are Connector-specific — cannot be shared between Connectors
- Peer-to-peer connections recommended for bandwidth Fair Use Policy compliance

## Prerequisites
- Subnet with outbound internet access
- Google Cloud CLI (for automated Compute Engine deployment)
- Twingate Admin Console access with Remote Network configured

## Deployment Options

### Automated Compute Engine
1. Admin Console → Remote Networks → select network → Add Connector
2. Click new Connector → select **Google Cloud** option on deployment page
3. Generate tokens (requires re-authentication)
4. Fill in GCP environment details and optional features
5. Copy and run the generated command in Google Cloud CLI

### Other Deployment Methods
- **Manual Compute Engine**: Follow standard [Linux Connector deployment](https://www.twingate.com/docs/linux)
- **GKE**: Use official Twingate Helm chart; see Kubernetes Best Practices Guide
- **IaC**: Terraform, Pulumi, or Twingate API

## Configuration Values
| Setting | Notes |
|---------|-------|
| `min_ports_per_vm` | Cloud NAT setting — increase if sharing NAT with high-volume workloads |

## Gotchas
- **Cloud NAT port exhaustion**: GCP default `min_ports_per_vm` is tuned for large fleets; small deployments sharing NAT with batch/analytics workloads may need this increased
- Tokens generated per Connector — cannot reuse across multiple Connectors
- Stagger updates across multiple Connectors to avoid downtime

## Updates
- Connectors run as systemd service
- Update manually via Linux package manager or automate with a scheduled task
- Reference: Systemd Connector Update Guide

## Related Docs
- [Linux Connector Deployment](https://www.twingate.com/docs/linux)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [Twingate Helm Chart (GKE)](https://www.twingate.com/docs/kubernetes)
- [Kubernetes Best Practices](https://www.twingate.com/docs/kubernetes-best-practices)
- [Peer-to-peer connections](https://www.twingate.com/docs/peer-to-peer)
- [GCP Tune NAT Configuration](https://cloud.google.com/nat/docs/tune-nat)
- [Terraform/Pulumi/API deployment](https://www.twingate.com/docs/deployment-automation)