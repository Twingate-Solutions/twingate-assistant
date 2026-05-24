# Deploy a Connector on GCP

## Summary
Covers multiple deployment options for Twingate Connectors on Google Cloud Platform, including Compute Engine (manual and automated), GKE, and IaC methods. Requires outbound internet access from the subnet. Peer-to-peer connections are recommended for bandwidth efficiency.

## Key Information
- Multiple deployment paths: Compute Engine (manual/automated), GKE (Helm), IaC (Terraform/Pulumi/API)
- Docker-based deployment works on any 64-bit Linux Docker supports
- systemd service supported on Ubuntu, Fedora, Debian, CentOS
- Access/refresh tokens are Connector-specific; cannot be shared between Connectors

## Prerequisites
- Subnet with outbound internet access (for image download + Twingate connectivity)
- If using Cloud NAT: review `min_ports_per_vm` setting if NAT is shared with high-volume workloads
- Twingate Admin Console access
- Google Cloud CLI (for automated Compute Engine deployment)

## Step-by-Step: Automated Compute Engine Deployment
1. Admin Console → Remote Networks → select Remote Network → **Add Connector**
2. Click new Connector → deployment page → select **Google Cloud** option
3. Scroll to step 2 → **Generate Tokens** (re-authentication required)
4. Scroll to step 3 → fill in GCP environment details and configure optional features
5. Scroll to step 5 → copy and run the launch command in Google Cloud CLI

## Configuration Values
| Setting | Notes |
|---|---|
| `min_ports_per_vm` | Cloud NAT setting; GCP default may be insufficient in small deployments |
| Access token | Connector-specific, generated per Connector |
| Refresh token | Connector-specific, generated per Connector |

## Deployment Options Summary
| Method | Reference |
|---|---|
| Manual Linux/Compute Engine | Linux Connector deployment docs |
| Automated Compute Engine | Steps above |
| GKE | Official Twingate Helm chart |
| Terraform / Pulumi / API | IaC deployment docs |

## Updates
- Connectors run as a `systemd` service
- Update manually via Linux package manager or automate with a scheduled task
- Stagger updates across multiple Connectors to avoid downtime
- See: Systemd Connector Update Guide

## Gotchas
- Cloud NAT `min_ports_per_vm` default is tuned for large fleets; may be too low for smaller deployments sharing NAT with high-parallel-connection workloads
- Tokens are per-Connector — generating tokens for one Connector cannot be reused for another
- Subnet must have outbound internet access; private-only subnets will fail

## Related Docs
- Best Practices for Connectors
- Connector Hardware Recommendations (GCP)
- Kubernetes Best Practices Guide
- Systemd Connector Update Guide
- Peer-to-peer connections guide
- Twingate Helm chart
- Terraform / Pulumi / API deployment