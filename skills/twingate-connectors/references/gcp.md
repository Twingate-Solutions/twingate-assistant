# Deploy a Connector on GCP

## Summary
Covers multiple deployment methods for Twingate Connectors on Google Cloud Platform including Compute Engine (manual and automated), GKE, and IaC options. Subnet must have outbound internet access for image download and Twingate connectivity.

## Key Information
- Multiple deployment paths: Compute Engine (manual/automated), GKE (Helm), IaC (Terraform/Pulumi/API)
- Docker-based deployment works on any 64-bit Linux distro Docker supports
- systemd service supported on: Ubuntu, Fedora, Debian, CentOS
- Access/refresh tokens are Connector-specific — cannot be shared between Connectors
- Peer-to-peer connections recommended for performance and Fair Use Policy compliance

## Prerequisites
- Subnet with outbound internet access
- Google Cloud CLI (for automated Compute Engine deployment)
- If using Cloud NAT: review `min_ports_per_vm` setting if NAT is shared with high-volume workloads

## Step-by-Step: Automated Compute Engine Deployment
1. Admin Console → Remote Networks → select Remote Network → Add Connector
2. Click new Connector → deployment page → select **Google Cloud** option
3. Generate tokens (requires re-authentication)
4. Fill in GCP environment details and configure optional features
5. Copy generated command → run in Google Cloud CLI

## Configuration Values
| Setting | Notes |
|---|---|
| `min_ports_per_vm` | Cloud NAT setting; GCP default may be insufficient for small deployments |
| Access token | Per-Connector, generated in Admin Console |
| Refresh token | Per-Connector, generated in Admin Console |

## Deployment Options
| Method | Reference |
|---|---|
| Manual Linux/Docker | General Linux Connector docs |
| Automated Compute Engine | Steps above |
| GKE | Official Twingate Helm chart |
| Terraform/Pulumi/API | Deployment automation docs |

## Gotchas
- Cloud NAT `min_ports_per_vm` default is tuned for large fleets — may be too low for smaller GCP deployments sharing NAT with analytics/batch workloads
- Tokens cannot be reused across multiple Connectors
- systemd updates: stagger across Connectors to avoid downtime

## Updating
- Connectors run as systemd service
- Update manually via Linux package manager or automate with a scheduled task
- Reference: Systemd Connector Update Guide

## Related Docs
- [Best Practices for Connectors](#)
- [GCP Tune NAT Configuration](https://cloud.google.com/nat/docs/tune-nat)
- [Kubernetes Best Practices Guide](#)
- [Twingate Helm Chart](#)
- [Deployment Automation (Terraform/Pulumi/API)](#)
- [Systemd Connector Update Guide](#)
- [Support Peer-to-Peer Connections](#)