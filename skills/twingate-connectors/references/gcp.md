## Deploy Connector on GCP

Multiple deployment options for Twingate Connectors on Google Cloud Platform: Compute Engine VM, automated GCE deployment, GKE, and IaC.

**Compute Engine (manual Linux VM):**
- Follow standard Linux Connector deployment instructions (Docker or systemd)
- Recommended instance: e2-small (sufficient for hundreds of users under typical usage)

**Automated Compute Engine Deployment:**
- Admin Console → Connector → Google Cloud option → Generate Tokens → fill GCP environment info → copy and run the Google Cloud CLI command

**GKE Deployment:**
- Use the official Twingate Helm chart; see Kubernetes Best Practices Guide

**IaC:**
- Terraform, Pulumi, or Twingate API

**Gotchas:**
- Subnet requires outbound internet access for image pull and Twingate connectivity
- **Cloud NAT:** if the Connector VM shares a Cloud NAT gateway with high-volume outbound services, review `min_ports_per_vm` — GCP default may be insufficient for smaller deployments (see GCP "Tune NAT configuration" docs)
- Tokens are Connector-specific — do not share between Connector instances
- Updates use the systemd update process (Linux package manager or scheduled task); stagger across Connectors

**Related Docs:**
- /docs/connectors-on-linux -- Linux deployment details
- /docs/connector-best-practices -- Hardware recommendations and network requirements
- /docs/upgrading-connectors -- Connector update process
