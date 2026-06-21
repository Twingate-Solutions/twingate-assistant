# Deploy a Connector on GCP

## Summary
Covers multiple deployment options for Twingate Connectors on Google Cloud Platform including Compute Engine, GKE, and IaC methods. Requires outbound internet access from the subnet. Supports Docker-based and systemd service deployments.

## Key Information
- Multiple deployment paths: Compute Engine (manual or automated), GKE (Helm chart), IaC (Terraform/Pulumi/API)
- Docker deployment works on any 64-bit Linux distro Docker supports
- systemd service supported on: Ubuntu, Fedora, Debian, CentOS
- Access and refresh tokens are **per-Connector** — cannot be shared between Connectors

## Prerequisites
- Subnet with outbound internet access (for container image download and Twingate connectivity)
- If using Cloud NAT: review `min_ports_per_vm` setting on NAT gateway (GCP default may be insufficient for smaller deployments)
- Google Cloud CLI (for automated Compute Engine deployment)
- Twingate Admin Console access

## Step-by-Step: Automated Compute Engine Deployment
1. Admin Console → Remote Networks → select Remote Network → **Add Connector**
2. Click the new Connector → deployment page → select **Google Cloud** option
3. Scroll to Step 2 → generate tokens (requires re-authentication)
4. Scroll to Step 3 → fill in GCP environment details and configure optional features
5. Scroll to Step 5 → copy and run the launch command in Google Cloud CLI

## Configuration Values
| Setting | Notes |
|---|---|
| `min_ports_per_vm` | Cloud NAT setting; tune if sharing NAT with high-volume workloads |
| Access token | Connector-specific, generated in Admin Console |
| Refresh token | Connector-specific, generated in Admin Console |

## Deployment Options Summary
| Method | Guide |
|---|---|
| Compute Engine (manual) | Linux Connector deployment instructions |
| Compute Engine (automated) | Steps above |
| GKE | Official Twingate Helm chart |
| Terraform/Pulumi/API | IaC deployment docs |

## Updates
- Connectors run as a **systemd service**
- Update manually via Linux package manager or automated scheduled task
- **Stagger updates** across multiple Connectors to avoid downtime
- See: Systemd Connector Update Guide

## Gotchas
- Cloud NAT `min_ports_per_vm` default is tuned for large fleets — may cause issues in smaller deployments
- Tokens are Connector-specific and non-shareable; generate separately for each Connector
- Subnet must have outbound internet access — verify before deploying

## Related Docs
- [Best Practices for Connectors](https://www.twingate.com/docs/connector-best-practices)
- [Kubernetes Best Practices Guide](https://www.twingate.com/docs/k8s-best-practices)
- [Systemd Connector Update Guide](https://www.twingate.com/docs/systemd-connector-update)
- [Support peer-to-peer connections](https://www.twingate.com/docs/peer-to-peer)
- [GCP Tune NAT configuration](https://cloud.google.com/nat/docs/tune-nat)