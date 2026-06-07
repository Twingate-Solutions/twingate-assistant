# Twingate Kubernetes Access Gateway - Wiki Home

## Page Title
Twingate Gateway - Wiki Home

## Summary
The Twingate Gateway is an open-source Layer 7 reverse proxy deployed within your environment that enables identity propagation and auditing for Zero Trust access. It extends existing Twingate deployments to support Kubernetes, SSH, and (upcoming) web/database protocols. All audit data remains within your infrastructure—nothing is sent to Twingate.

## Key Information
- **Type**: Open-source Layer 7 reverse proxy (self-hosted)
- **Purpose**: Identity propagation + session recording + privileged access auditing
- **Currently supported protocols**: Kubernetes, SSH
- **Coming soon**: Web App, Database (PostgreSQL, MySQL)
- **Isolation**: Gateway has no external communication except fetching Twingate's public key for identity verification
- **Logs**: Exported to `stdout`; stream to any SIEM or storage solution
- **Session recordings**: Captured in Asciicast v2 format; replay at `https://www.twingate.com/sessionplayer`

## Prerequisites
- Existing Twingate deployment
- Kubernetes or SSH target infrastructure
- Access to deploy workloads within your environment

## Supported Protocol Features

| Protocol | Identity Propagation | RBAC Integration | Session Recording |
|----------|---------------------|-----------------|-------------------|
| Kubernetes | ✅ | ✅ | ✅ (`kubectl`) |
| SSH | ✅ | N/A | ✅ (shell, exec, SFTP, port forwarding) |
| Web App | 🔜 | — | — |
| Database | 🔜 | — | — |

## Architecture Notes
- Gateway stays entirely within private network; infrastructure never exposed to public internet
- Access policies use identity, device posture, and contextual signals
- Eliminates double authentication and plaintext credentials on end-user machines

## Gotchas
- Session recordings and audit logs **never leave your environment**—you must configure your own log export pipeline
- Web App and Database support are not yet available
- Must have existing Twingate deployment before implementing the Gateway

## Related Docs
- [How It Works](https://github.com/Twingate/kubernetes-access-gateway/wiki/How-It-Works)
- [Kubernetes Overview](https://github.com/Twingate/kubernetes-access-gateway/wiki/Kubernetes-Overview)
- [Kubernetes Quick Start Guide](https://github.com/Twingate/kubernetes-access-gateway/wiki/Kubernetes-Quick-Start-Guide)
- [Kubernetes Installation](https://github.com/Twingate/kubernetes-access-gateway/wiki/Kubernetes-Installation)
- [SSH Overview](https://github.com/Twingate/kubernetes-access-gateway/wiki/SSH-Overview)
- [SSH Quick Start Guide](https://github.com/Twingate/kubernetes-access-gateway/wiki/SSH-Quick-Start-Guide)
- [SSH Installation](https://github.com/Twingate/kubernetes-access-gateway/wiki/SSH-Installation)
- [Session Recordings](https://github.com/Twingate/kubernetes-access-gateway/wiki/Session-Recordings)
- Asciicast web player: `https://www.twingate.com/sessionplayer`