---
source: https://www.twingate.com/docs/gcp
type: docs
fetched: 2026-11-13
source_version: 3ce9d3ba07f82416b8ac9e73122ddc5b65f0ce92a91da052ad10bc9b70b30529
trust: official
---

# How to Deploy a Connector on GCP

## Summary
Twingate Connectors can be deployed on Google Cloud via Compute Engine (manual or automated through the Admin Console), GKE (Helm chart), or Infrastructure as Code (Terraform, Pulumi, Twingate API). The Connector needs outbound Internet access to pull its container image and reach Twingate.

## Key Information
- **Compute Engine (custom VM):** Follow the general Linux Connector deployment instructions.
  - Docker-based deployment works on any 64-bit Linux distribution Docker supports.
  - The `systemd` service is supported on Ubuntu, Fedora, Debian, and CentOS.
- **Automated Compute Engine deployment:** The Admin Console generates a command that creates a Compute Engine instance with the Connector pre-installed. You run it in the Google Cloud CLI.
- **GKE:** Use the official Twingate Helm chart. See the Kubernetes Best Practices Guide if using Twingate for K8s.
- **IaC:** Terraform, Pulumi, or the Twingate API.
- **Peer-to-peer connections:** Recommended for better user experience and to stay within the Fair Use Policy on bandwidth.
- **Updates:** Connectors on GCP run as a `systemd` service. Update manually with the Linux package manager, or automate with a scheduled task. Stagger updates across Connectors to avoid downtime.

## Prerequisites
- Twingate Admin Console access and an existing Remote Network.
- A subnet with outbound Internet access (to download the Connector image and reach Twingate).
- Google Cloud CLI (for the automated deployment command).
- Review Twingate's Connector Best Practices, including hardware recommendations for Google Cloud.

## Step-by-Step (Automated Compute Engine Deployment)
1. In the Admin Console, go to **Remote Networks**, select the target Remote Network, scroll down, and click **Add Connector**.
2. Click the new Connector. On the deployment page, select the **Google Cloud** option at the top.
3. In step 2, click the button to generate tokens (you'll re-authenticate and be returned to the page).
4. In step 3, enter your Google Cloud environment details and configure any optional features.
5. In step 5, copy the launch command and run it in the Google Cloud CLI.

## Configuration Values
- **Cloud NAT `min_ports_per_vm`:** Review this setting on the NAT gateway if the Connector VM uses Cloud NAT and shares it with services that make high volumes of parallel outbound connections (analytics, batch workloads). GCP's default is tuned for large fleets and may be insufficient for smaller deployments. See "Tune NAT configuration" in the GCP docs.
- **Access and refresh tokens:** Generated in the Admin Console, required for deployment.

## Gotchas
- Tokens are unique to each Connector and cannot be shared between Connectors.
- A subnet without outbound Internet access will cause deployment to fail.
- Shared Cloud NAT gateways can exhaust ports under heavy parallel outbound traffic.
- Updating all Connectors at once can cause downtime, so stagger the updates.

## Related Docs
- Linux Connector deployment
- Best Practices for Connectors
- Peer-to-peer connection support
- Fair Use Policy
- Twingate Helm chart / Kubernetes Best Practices Guide
- Terraform, Pulumi, and Twingate API deployment automation
- Systemd Connector Update Guide
- GCP: Tune NAT configuration