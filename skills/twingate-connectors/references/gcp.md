# Deploy a Connector on GCP

## Summary
Covers multiple deployment options for Twingate Connectors on Google Cloud Platform including Compute Engine, GKE, and IaC methods. Requires outbound internet access from the subnet. Supports Docker-based and systemd service installations.

## Key Information
- Multiple deployment paths: Compute Engine (manual/automated), GKE (Helm), IaC (Terraform/Pulumi/API)
- Docker-based deployment works on any 64-bit Linux distro Docker supports
- systemd service supported on: Ubuntu, Fedora, Debian, CentOS
- Access/refresh tokens are Connector-specific — cannot be shared between Connectors

## Prerequisites
- Subnet with outbound internet access (for container image download and Twingate connectivity)
- If using Cloud NAT: review `min_ports_per_vm` setting — GCP default may be insufficient for smaller deployments
- Twingate Admin Console access with a configured Remote Network

## Step-by-Step (Automated Compute Engine)
1. Admin Console → Remote Networks → select network → scroll down → **Add Connector**
2. Click new Connector → deployment page → select **Google Cloud** option
3. Scroll to step 2 → generate tokens (re-authentication required)
4. Scroll to step 3 → fill in GCP environment details and configure optional features
5. Scroll to step 5 → copy and run launch command in **Google Cloud CLI**

## Configuration Values
| Setting | Notes |
|---|---|
| `min_ports_per_vm` | Cloud NAT setting — increase if sharing NAT with high-volume workloads |
| Access token | Per-Connector, generated in Admin Console |
| Refresh token | Per-Connector, generated in Admin Console |

## Deployment Options
| Method | Reference |
|---|---|
| Manual Linux VM | Linux Connector deployment docs |
| Automated Compute Engine | Steps above |
| GKE | Official Twingate Helm chart |
| Terraform/Pulumi/API | IaC deployment docs |

## Updates
- Connectors run as a systemd service
- Update manually via Linux package manager or via scheduled task for automatic updates
- Stagger updates across multiple Connectors to avoid downtime
- Reference: Systemd Connector Update Guide

## Gotchas
- Cloud NAT `min_ports_per_vm` default is tuned for large fleets — may cause connectivity issues in smaller deployments
- Subnet **must** have outbound internet access; deployment fails otherwise
- Tokens are unique per Connector — generate separately for each
- Enable peer-to-peer connections to stay within Fair Use Policy bandwidth limits

## Related Docs
- Linux Connector Deployment
- Connector Best Practices (includes GCP hardware recommendations)
- Kubernetes Best Practices Guide
- Twingate Helm Chart
- Terraform / Pulumi / Twingate API (IaC)
- Systemd Connector Update Guide
- GCP: Tune NAT Configuration