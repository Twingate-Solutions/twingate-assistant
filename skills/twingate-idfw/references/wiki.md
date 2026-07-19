# Twingate Kubernetes Access Gateway - Wiki Home

## Page Title
Twingate Gateway - Wiki Home

## Summary
The Twingate Gateway is an open-source Layer 7 reverse proxy deployed within your environment that provides identity propagation, Zero Trust access controls, and session recording for Kubernetes, SSH, and (upcoming) web/database protocols. It extends existing Twingate deployments without exposing infrastructure to the public internet. All audit data remains within your infrastructure.

## Key Information
- **Type**: Open-source Layer 7 reverse proxy (self-hosted)
- **Part of**: Twingate Identity Firewall product
- **Currently supported protocols**: Kubernetes, SSH
- **Coming soon**: Web App, Database (PostgreSQL, MySQL)
- **External communication**: Only fetches Twingate's public key for identity verification
- **Audit logs**: Exported to `stdout` only; never sent to Twingate
- **Session recording format**: Asciicast v2
- **Session replay**: `https://www.twingate.com/sessionplayer`

## Supported Protocols

| Protocol | Features |
|----------|----------|
| Kubernetes | Identity propagation, RBAC integration, `kubectl` session recording |
| SSH | Identity propagation, session recording, shell/exec/SFTP/port forwarding |
| Web App | Coming soon |
| Database | Coming soon |

## Prerequisites
- Existing Twingate deployment
- Private network infrastructure (Gateway leverages Twingate private networking)

## Gotchas
- Gateway is **completely isolated** within your environment — logs/recordings are never uploaded to Twingate
- No built-in log storage; must pipe `stdout` to external SIEM or storage solution
- Session recordings are in Asciicast v2 format — requires compatible player or the Twingate web player

## Related Docs
- [How It Works](https://github.com/Twingate/kubernetes-access-gateway/wiki/How-It-Works)
- Kubernetes: Overview, Quick Start Guide, Installation, Troubleshooting, Known Issues
- SSH: Overview, Quick Start Guide, Installation, Operations, Monitoring, Session Recordings
- [Developers](https://github.com/Twingate/kubernetes-access-gateway/wiki/Developers)