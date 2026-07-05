# Twingate Kubernetes Access Gateway - Wiki Home

## Page Title
Twingate Gateway - Home Wiki

## Summary
The Twingate Gateway is an open-source Layer 7 reverse proxy deployed within your environment that extends Zero Trust controls by propagating user identity to upstream services (Kubernetes, SSH, web apps, databases). It integrates with existing Twingate deployments and keeps all audit data local to your infrastructure.

## Key Information
- **Type**: Open-source Layer 7 reverse proxy (self-hosted)
- **Purpose**: Identity propagation + auditing for Zero Trust / PAM workflows
- **Supported protocols**: Kubernetes (GA), SSH (GA), Web App (coming soon), Database (coming soon)
- **Kubernetes features**: Identity propagation, RBAC integration, `kubectl` session recording
- **SSH features**: Identity propagation, session recording, shell/exec/SFTP/port forwarding
- **Session recording format**: Asciicast v2; replay at `https://www.twingate.com/sessionplayer`
- **Audit logs**: Exported to `stdout`; pipe to SIEM or storage solution of choice
- **Data residency**: All logs and recordings stay within your infrastructure — never uploaded to Twingate
- **External communication**: Only fetches Twingate's public key for identity verification

## Prerequisites
- Existing Twingate deployment
- Private network access to target infrastructure (Kubernetes cluster, SSH servers)
- Kubernetes environment for Gateway deployment (implied by repo name)

## Available Documentation Sections
- How It Works (architecture overview)
- Kubernetes: Overview, Quick Start Guide, Installation, Troubleshooting, Known Issues
- SSH: Overview, Quick Start Guide, Installation, Operations, Monitoring, Session Recordings
- Development: Developers guide

## Configuration Values
- **Logs**: `stdout` (stream to external SIEM)
- **Session player URL**: `https://www.twingate.com/sessionplayer`

## Gotchas
- Gateway is fully isolated — no Twingate cloud connectivity for logs/recordings; you own storage and retention
- Web App and Database support not yet available (listed as "Coming Soon")
- Only external call made is fetching Twingate's public key; firewall rules must allow this outbound request

## Related Docs
- [How It Works](https://github.com/Twingate/kubernetes-access-gateway/wiki/How-It-Works)
- [Kubernetes Quick Start](https://github.com/Twingate/kubernetes-access-gateway/wiki/Kubernetes-Quick-Start-Guide)
- [SSH Quick Start](https://github.com/Twingate/kubernetes-access-gateway/wiki/SSH-Quick-Start-Guide)
- [Twingate Identity Firewall](https://www.twingate.com) (product context)
- Asciicast v2 format spec (for session recording integration)