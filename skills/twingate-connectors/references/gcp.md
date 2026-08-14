---
source: https://www.twingate.com/docs/gcp
type: docs
fetched: 2026-08-14
source_version: 033bb6bca98568302efbff23ca6cc1d5b1d86c71debadd62370b1bf0990a3f06
---

# Deploy a Connector on GCP

## Summary
Covers multiple deployment options for Twingate Connectors on Google Cloud Platform, including Compute Engine (manual and automated), GKE, and IaC approaches. Subnet must have outbound internet access for image downloads and Twingate connectivity.

## Key Information
- Multiple deployment paths: Compute Engine (manual/automated), GKE (Helm), IaC (Terraform/Pulumi/API)
- Docker-based deployment works on any 64-bit Linux Docker supports
- systemd service supported on: Ubuntu, Fedora, Debian, CentOS
- Access/refresh tokens are Connector-specific — cannot be shared between Connectors

## Prerequisites
- Subnet with outbound internet access
- Google Cloud CLI (for automated Compute Engine deployment)
- Twingate Admin Console access
- Remote Network already configured in Twingate

## Step-by-Step (Automated Compute Engine)
1. Admin Console → Remote Networks → select network → **Add Connector**
2. Click new Connector → deployment page → select **Google Cloud** option
3. Generate tokens (triggers re-authentication)
4. Fill in GCP environment details and configure optional features
5. Copy and run the generated command in Google Cloud CLI

## Configuration Values
- **min_ports_per_vm** — Cloud NAT setting; GCP default may be insufficient for smaller deployments sharing NAT with high-volume workloads; tune via GCP "Tune NAT configuration" docs

## Gotchas
- **Cloud NAT port exhaustion**: If Connector VM shares a NAT gateway with analytics/batch workloads, the default `min_ports_per_vm` may be too low — explicitly tune it
- Peer-to-peer connections should be enabled to stay within Fair Use Policy bandwidth limits
- Tokens are per-Connector; generating tokens for one Connector cannot be reused for another
- Stagger updates across multiple Connectors to avoid downtime

## Updates
- Connectors run as systemd service
- Update manually via Linux package manager or automate with a scheduled task
- Reference: Systemd Connector Update Guide

## Related Docs
- [Linux Connector Deployment](https://www.twingate.com/docs/linux)
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices)
- [GKE Helm Chart](https://www.twingate.com/docs/kubernetes)
- [Kubernetes Best Practices](https://www.twingate.com/docs/kubernetes-best-practices)
- [Peer-to-Peer Connections](https://www.twingate.com/docs/peer-to-peer)
- [Terraform / Pulumi / API Deployment](https://www.twingate.com/docs/deployment-automation)
- [Systemd Connector Update Guide](https://www.twingate.com/docs/systemd-update)
- GCP: [Tune NAT Configuration](https://cloud.google.com/nat/docs/tune-nat)