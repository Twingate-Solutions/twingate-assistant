# Twingate Kubernetes Access Gateway - Wiki Home

## Summary
The Twingate Gateway is an open-source Layer 7 reverse proxy deployed within your environment that extends Zero Trust controls via identity propagation and auditing. It supports Kubernetes, SSH, and Web App protocols with session recording capabilities. All audit data remains within your infrastructure and is never sent to Twingate.

## Key Information
- **Type**: Open-source Layer 7 reverse proxy
- **Part of**: Twingate Identity Firewall (Zero Trust + PAM)
- **Supported protocols**: Kubernetes, SSH, Web App, Database (coming soon)
- **Identity propagation**: Passes user identity to upstream services, eliminating double authentication and stored plaintext credentials
- **Session recording format**: Asciicast v2, replayable at `https://www.twingate.com/sessionplayer`
- **Log output**: `stdout` only — stream to SIEM or storage solution of choice
- **External communication**: Only fetches Twingate's public key for identity verification; no other outbound data

## Supported Protocol Features

| Protocol | Identity Propagation | Session Recording | Notes |
|----------|---------------------|-------------------|-------|
| Kubernetes | ✅ RBAC integration | ✅ kubectl commands | GA |
| SSH | ✅ | ✅ shell, exec, SFTP, port forwarding | GA |
| Web App | ✅ via injected headers | ✅ auditing | GA |
| Database | Coming Soon | Coming Soon | PostgreSQL, MySQL planned |

## Architecture Notes
- Deployed **within your environment** (not Twingate's cloud)
- Leverages Twingate private networking — infrastructure stays off public internet
- Access policies use identity, device posture, and contextual signals
- Audit logs and session recordings **never leave your infrastructure**

## Available Documentation Sections
- How It Works (architecture overview)
- Per-protocol: Overview, Quick Start Guide, Installation
- Kubernetes Troubleshooting & Known Issues
- Operations: Monitoring, Session Recordings
- Reference: Migration guide
- Development: Developers guide

## Gotchas
- Gateway is completely isolated — only outbound call is fetching Twingate's public key
- Session recordings must be self-managed; Twingate does not store or have access to them
- Database support is not yet available

## Related Docs
- [How It Works](https://github.com/Twingate/kubernetes-access-gateway/wiki/How-It-Works)
- [Kubernetes Quick Start](https://github.com/Twingate/kubernetes-access-gateway/wiki/Kubernetes-Quick-Start-Guide)
- [SSH Quick Start](https://github.com/Twingate/kubernetes-access-gateway/wiki/SSH-Quick-Start-Guide)
- [Web App Quick Start](https://github.com/Twingate/kubernetes-access-gateway/wiki/Web-App-Quick-Start-Guide)
- [Session Recordings Operations](https://github.com/Twingate/kubernetes-access-gateway/wiki/Session-Recordings)
- Asciicast player: `https://www.twingate.com/sessionplayer`