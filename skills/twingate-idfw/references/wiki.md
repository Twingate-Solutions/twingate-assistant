# Twingate Kubernetes Access Gateway - Wiki Home

## Page Title
Twingate Gateway - Wiki Home

## Summary
The Twingate Gateway is an open-source Layer 7 reverse proxy deployed within your environment that extends Zero Trust controls by propagating user identity to upstream services. It supports Kubernetes and SSH protocols (web app and database support coming soon). All audit data remains entirely within your infrastructure.

## Key Information
- **Type**: Open-source Layer 7 reverse proxy (self-hosted)
- **Purpose**: Identity propagation + session recording + auditing for internal services
- **Supported protocols**: Kubernetes (GA), SSH (GA), Web App (coming soon), Database (coming soon)
- **Identity verification**: Fetches Twingate's public key externally; no other outbound communication
- **Audit logs**: Written to `stdout` — pipe to SIEM or storage solution
- **Session recordings**: Captured in Asciicast v2 format; replay at `https://www.twingate.com/sessionplayer`
- **Isolation**: Gateway has no connection back to Twingate cloud except public key fetch

## Prerequisites
- Existing Twingate deployment
- Private network infrastructure (Gateway keeps services off public internet)

## Supported Use Cases

| Protocol | Features |
|----------|----------|
| Kubernetes | Identity propagation, RBAC integration, `kubectl` session recording |
| SSH | Identity propagation, session recording, shell/exec/SFTP/port forwarding |

## Architecture Notes
- Leverages Twingate private networking — upstream services remain hidden from internet
- Access policies use identity, device posture, and contextual signals
- Eliminates need for plaintext credentials on end-user machines
- No double authentication required for upstream services

## Gotchas
- Audit logs and session recordings **never leave your environment** — you are responsible for log retention and storage
- Session recordings require external replay tool (`https://www.twingate.com/sessionplayer`) — the recordings themselves stay local
- Web App and Database protocol support not yet available

## Related Docs
- [How It Works](https://github.com/Twingate/kubernetes-access-gateway/wiki/How-It-Works)
- [Kubernetes Overview](https://github.com/Twingate/kubernetes-access-gateway/wiki/Kubernetes-Overview)
- [Kubernetes Quick Start](https://github.com/Twingate/kubernetes-access-gateway/wiki/Kubernetes-Quick-Start-Guide)
- [Kubernetes Installation](https://github.com/Twingate/kubernetes-access-gateway/wiki/Kubernetes-Installation)
- [SSH Overview](https://github.com/Twingate/kubernetes-access-gateway/wiki/SSH-Overview)
- [SSH Quick Start](https://github.com/Twingate/kubernetes-access-gateway/wiki/SSH-Quick-Start-Guide)
- [SSH Installation](https://github.com/Twingate/kubernetes-access-gateway/wiki/SSH-Installation)
- [Troubleshooting](https://github.com/Twingate/kubernetes-access-gateway/wiki/Troubleshooting)
- [Session Recordings](https://github.com/Twingate/kubernetes-access-gateway/wiki/Session-Recordings)