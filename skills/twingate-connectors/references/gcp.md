# Deploy a Connector on GCP

## Summary
Covers deployment options for Twingate Connectors on Google Cloud Platform, including Compute Engine (manual and automated), GKE, and IaC approaches. Subnets must have outbound internet access for container image downloads and Twingate connectivity.

## Key Information
- Multiple deployment methods: Compute Engine (manual/automated), GKE (Helm), IaC (Terraform/Pulumi/API)
- Docker-based deployment works on any 64-bit Linux distro Docker supports
- systemd service supported on: Ubuntu, Fedora, Debian, CentOS
- Access and refresh tokens are **per-Connector** — cannot be shared between Connectors
- Updates run via systemd; stagger updates across Connectors to avoid downtime

## Prerequisites
- Subnet with outbound internet access (for container image pull + Twingate connection)
- If using Cloud NAT: review `min_ports_per_vm` setting — GCP defaults may be insufficient for smaller deployments
- Remote Network already configured in Twingate Admin Console

## Step-by-Step: Automated Compute Engine Deployment
1. Admin Console → Remote Networks → select Remote Network → **Add Connector**
2. Click new Connector → deployment page → select **Google Cloud** option
3. Generate tokens (requires re-authentication)
4. Fill out GCP environment configuration (step 3 on deployment page)
5. Copy generated CLI command (step 5) → run in Google Cloud CLI

## Configuration Values
| Setting | Notes |
|---|---|
| `min_ports_per_vm` | Cloud NAT setting; tune if sharing NAT with high-volume workloads |
| Access token | Connector-specific, generated in Admin Console |
| Refresh token | Connector-specific, generated in Admin Console |

## Deployment Options Summary
| Method | Reference |
|---|---|
| Compute Engine (manual) | Linux Connector deployment docs |
| Compute Engine (automated) | Steps above via Admin Console |
| GKE | Official Twingate Helm chart + K8s Best Practices Guide |
| Terraform/Pulumi/API | Deployment automation docs |

## Gotchas
- Cloud NAT `min_ports_per_vm` default is tuned for large fleets — may be too low for small GCP deployments sharing a NAT gateway with analytics/batch workloads
- Tokens are Connector-specific; generating tokens for one Connector won't work for another
- Peer-to-peer connections should be enabled to stay within Fair Use Policy bandwidth limits

## Related Docs
- [Connector Best Practices](https://www.twingate.com/docs/connector-best-practices) — hardware recommendations for GCP
- [Linux Connector Deployment](https://www.twingate.com/docs/linux)
- [Twingate Helm Chart](https://www.twingate.com/docs/kubernetes)
- [Kubernetes Best Practices](https://www.twingate.com/docs/kubernetes-best-practices)
- [Systemd Connector Update Guide](https://www.twingate.com/docs/systemd-connector-update)
- [Support Peer-to-Peer Connections](https://www.twingate.com/docs/peer-to-peer)
- [GCP Tune NAT Configuration](https://cloud.google.com/nat/docs/tune-nat)