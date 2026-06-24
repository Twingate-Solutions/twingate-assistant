# Twingate Kubernetes Access Gateway - Wiki Home

## Page Title
Twingate Gateway - Home/Overview Wiki

## Summary
The Twingate Gateway is an open-source Layer 7 reverse proxy deployed within your environment that enables identity propagation and auditing for Zero Trust access control. It extends existing Twingate deployments to support Kubernetes, SSH, and (upcoming) web/database protocols. All audit data remains within your infrastructure—nothing is sent to Twingate.

## Key Information
- **Type**: Open-source Layer 7 reverse proxy (self-hosted)
- **Purpose**: Identity propagation + session recording/auditing
- **Supported protocols**: Kubernetes (GA), SSH (GA), Web App (coming soon), Database (coming soon)
- **Kubernetes features**: RBAC integration, kubectl session recording, identity propagation to API server
- **SSH features**: Shell, exec, SFTP, port forwarding support with session recording
- **Audit logs**: Exported to `stdout`; stream to any SIEM or storage solution
- **Session recordings**: Captured in Asciicast v2 format
- **Session replay URL**: `https://www.twingate.com/sessionplayer`
- **External communication**: Only fetches Twingate's public key for identity verification; fully isolated otherwise

## Prerequisites
- Existing Twingate deployment
- Kubernetes cluster (for K8s use case) or SSH server (for SSH use case)
- Private network infrastructure (Gateway leverages Twingate private networking)

## Architecture Notes
- Gateway sits as reverse proxy between Twingate clients and upstream services
- Access policies use identity, device posture, and contextual signals
- Eliminates need for plaintext credentials on end-user machines
- No double authentication required for upstream services

## Configuration Values
- Logs: `stdout` (pipe to SIEM of choice)
- Session recording format: Asciicast v2

## Gotchas
- Gateway is **completely isolated**—audit logs and session recordings stay in your infrastructure and are never uploaded to Twingate
- Web App and Database protocol support are not yet available
- Requires an existing Twingate deployment; this is an extension, not a standalone product

## Related Docs
- [How It Works](https://github.com/Twingate/kubernetes-access-gateway/wiki/How-It-Works)
- Kubernetes: Overview, Quick Start Guide, Installation, Troubleshooting, Known Issues
- SSH: Overview, Quick Start Guide, Installation, Operations, Monitoring, Session Recordings
- [Twingate Asciicast Session Player](https://www.twingate.com/sessionplayer)
- Development/Developers wiki page