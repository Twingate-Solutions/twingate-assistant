# Twingate Kubernetes Access Gateway - Wiki Home

## Page Title
Twingate Gateway - Home/Overview

## Summary
The Twingate Gateway is an open-source Layer 7 reverse proxy deployed within your environment that enables identity propagation and auditing for Zero Trust access. It extends existing Twingate deployments to support Kubernetes, SSH, and (upcoming) web/database protocols. All audit data remains entirely within your infrastructure.

## Key Information
- **Type**: Open-source Layer 7 reverse proxy
- **Purpose**: Identity propagation + session recording/auditing
- **Currently supported protocols**: Kubernetes, SSH
- **Upcoming protocols**: Web App, Database (PostgreSQL, MySQL)
- **Deployment model**: Self-hosted within your environment
- **External communication**: Only fetches Twingate's public key for identity verification
- **Audit logs**: Exported to `stdout`; never sent to Twingate
- **Session recording format**: Asciicast v2
- **Session replay URL**: `https://www.twingate.com/sessionplayer`

## Prerequisites
- Existing Twingate deployment
- Kubernetes or SSH infrastructure to protect
- SIEM or log aggregation solution (recommended for audit logs)

## Core Capabilities
| Feature | Description |
|---|---|
| Identity Propagation | Passes user identity to upstream services; eliminates double auth and plaintext credentials |
| Session Recording | Records and replays sessions for forensic/compliance review |
| Unified Policy | Single policy engine for network + application access |

## Architecture Notes
- Gateway is **fully isolated** within customer environment
- Leverages Twingate private networking (infrastructure not exposed to public internet)
- Access policies use identity, device posture, and contextual signals
- Kubernetes integration: supports `kubectl`, RBAC, session recording
- SSH integration: supports shell, exec, SFTP, port forwarding

## Available Documentation (Wiki Sections)
- **How It Works** - Architecture overview
- **Kubernetes**: Overview, Quick Start Guide, Installation, Troubleshooting, Known Issues
- **SSH**: Overview, Quick Start Guide, Installation, Operations, Monitoring, Session Recordings
- **Development**: Developers guide

## Gotchas
- Session recordings and audit logs are **never uploaded to Twingate** — you are responsible for retention and storage
- Web App and Database support are not yet available ("Coming Soon")
- Gateway is a separate component from core Twingate — requires its own deployment

## Related Docs
- [Kubernetes Overview](https://github.com/Twingate/kubernetes-access-gateway/wiki/Kubernetes-Overview)
- [Kubernetes Quick Start](https://github.com/Twingate/kubernetes-access-gateway/wiki/Kubernetes-Quick-Start-Guide)
- [SSH Overview](https://github.com/Twingate/kubernetes-access-gateway/wiki/SSH-Overview)
- [How It Works](https://github.com/Twingate/kubernetes-access-gateway/wiki/How-It-Works)
- [Twingate Identity Firewall](https://www.twingate.com)