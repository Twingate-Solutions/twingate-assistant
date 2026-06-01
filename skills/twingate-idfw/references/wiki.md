# Twingate Kubernetes Access Gateway - Wiki Home

## Page Title
Twingate Gateway - Wiki Home

## Summary
The Twingate Gateway is an open-source Layer 7 reverse proxy deployed within your environment that extends Zero Trust controls with identity propagation and auditing. It integrates with existing Twingate deployments to provide identity-aware access to Kubernetes clusters, SSH servers, and (upcoming) web apps and databases. All audit data stays within your infrastructure—nothing is sent to Twingate.

## Key Information
- **Type**: Open-source Layer 7 reverse proxy (self-hosted)
- **Purpose**: Identity propagation + session recording/auditing for downstream services
- **Currently supported protocols**: Kubernetes, SSH
- **Upcoming protocols**: Web App, Database (PostgreSQL, MySQL)
- **External communication**: Only fetches Twingate's public key for identity verification
- **Audit logs**: Written to `stdout`; route to any SIEM or storage solution
- **Session recordings**: Captured in Asciicast v2 format; replay at `https://www.twingate.com/sessionplayer`
- **Data residency**: Logs and recordings never leave your infrastructure

## Supported Protocol Features

| Protocol | Identity Propagation | RBAC Integration | Session Recording |
|----------|---------------------|-----------------|-------------------|
| Kubernetes | ✅ | ✅ | ✅ (`kubectl`) |
| SSH | ✅ | N/A | ✅ (shell, exec, SFTP, port forwarding) |

## Prerequisites
- Existing Twingate deployment
- Kubernetes or SSH target infrastructure accessible via Twingate private network

## Key Capabilities
- **No double authentication**: Identity passed through to upstream services
- **No plaintext credentials** stored on end-user machines
- **Unified policy engine**: Single control plane for network + application access
- **Forensic compliance**: Session recording with replay support

## Configuration Values
- Logs exported to: `stdout`
- Session recording format: Asciicast v2
- Session replay URL: `https://www.twingate.com/sessionplayer`

## Gotchas
- Gateway is **completely isolated**—only external call is fetching Twingate's public key
- You are responsible for log aggregation/storage pipeline from `stdout`
- Web App and Database support are not yet available

## Related Docs
- [How It Works](https://github.com/Twingate/kubernetes-access-gateway/wiki/How-It-Works)
- Kubernetes: Overview, Quick Start Guide, Installation, Troubleshooting, Known Issues
- SSH: Overview, Quick Start Guide, Installation, Operations, Monitoring, Session Recordings
- [Twingate Identity Firewall](https://www.twingate.com) (product context)