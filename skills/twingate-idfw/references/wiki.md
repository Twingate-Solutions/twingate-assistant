# Twingate Kubernetes Access Gateway - Wiki Home

## Page Title
Twingate Gateway - Wiki Home

## Summary
The Twingate Gateway is an open-source Layer 7 reverse proxy deployed within your environment that enables identity propagation and auditing for Zero Trust access. It extends existing Twingate deployments to support Kubernetes, SSH, and (soon) web apps and databases. All audit data stays within your infrastructure—nothing is sent to Twingate.

## Key Information
- **Type**: Open-source Layer 7 reverse proxy
- **Purpose**: Identity propagation + session recording + access auditing
- **Deployment**: Self-hosted within your environment
- **External communication**: Only fetches Twingate's public key for identity verification
- **Logs**: Exported to `stdout`; stream to any SIEM
- **Session recordings**: Captured in Asciicast v2 format
- **Session replay URL**: `https://www.twingate.com/sessionplayer`

## Supported Protocols

| Protocol | Status | Features |
|----------|--------|---------|
| Kubernetes | GA | Identity propagation, RBAC integration, `kubectl` session recording |
| SSH | GA | Identity propagation, session recording, shell/exec/SFTP/port forwarding |
| Web App | Coming Soon | Identity-aware reverse proxying |
| Database | Coming Soon | PostgreSQL, MySQL identity propagation |

## Prerequisites
- Existing Twingate deployment
- Private network infrastructure (Gateway keeps resources off public internet)

## Architecture Notes
- Gateway is fully isolated within your environment
- Identity verification uses Twingate's public key (only external dependency)
- Audit logs and session recordings never leave your infrastructure

## Gotchas
- Gateway is completely isolated—no telemetry or recordings sent to Twingate
- Must integrate with existing SIEM/storage for log retention (no built-in persistence beyond `stdout`)
- Web App and Database protocol support not yet available

## Related Docs
- How It Works (architecture overview)
- Kubernetes: Overview, Quick Start Guide, Installation, Troubleshooting, Known Issues
- SSH: Overview, Quick Start Guide, Operations, Monitoring, Session Recordings
- Development/Developers guide