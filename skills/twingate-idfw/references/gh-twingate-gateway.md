---
source: https://github.com/Twingate/gateway
type: github
fetched: 2026-09-20
source_version: 00d7ae3b047bf16b9390b2d73ac35463e0660369
---

# Twingate Gateway

## Summary
A Layer 7 reverse proxy deployed within your infrastructure as part of Twingate Identity Firewall. It propagates user identity to upstream services and provides auditing for Kubernetes API servers, SSH servers, and web applications. Acts as a reverse proxy that intercepts connections and injects identity context without requiring credentials on end-user machines.

## Key Information
- **Protocols supported:** Kubernetes, SSH, Web App (TLS upstream/downstream as of v1.1.0)
- **Deployment:** Self-hosted within your environment; Docker image available on DockerHub (`twingate/gateway`)
- **SSH CA options:** Vault-backed CA or manual CA
- **Session recording:** Supported for Kubernetes (`kubectl`) and SSH sessions
- **Audit logging:** All activity attributed to specific user identities; SSH channel request outcomes logged
- **Free tier:** Up to 5 Kubernetes, SSH, or Web App resources

## Prerequisites
- A Twingate account with Identity Firewall enabled
- GAT (Gateway Access Token) for authenticating the gateway to Twingate
- For Kubernetes: access to a private Kubernetes cluster
- For SSH with Vault CA: a configured Vault SSH secrets engine role
- Docker or compatible container runtime

## Usage / Step-by-Step
1. Pull the Docker image: `docker pull twingate/gateway`
2. Configure the gateway via config file or environment variables (see wiki Quick Start guides)
3. For Kubernetes: follow [Kubernetes Quick Start Guide](https://github.com/Twingate/gateway/wiki/Kubernetes-Quick-Start-Guide)
4. For SSH: follow [SSH Quick Start Guide](https://github.com/Twingate/gateway/wiki/SSH-Quick-Start-Guide)
5. Point Twingate resources at the gateway's address

## Configuration Values
| Key | Description |
|---|---|
| `ssh.ca.vault.role` | Default Vault SSH CA role |
| `ssh.ca.vault.gatewayHostCA.role` | Override role specifically for gateway host CA |
| GAT token | Required; validated via payload `type` claim (v1.1.0+) |

Refer to the [wiki](https://github.com/Twingate/gateway/wiki) for full configuration reference.

## Gotchas
- **v1.1.0 breaking change (Vault-backed SSH CA):** SSH host certificates now include resource addresses and aliases as principals. The Vault role for the gateway host CA must permit these via `allowed_domains=*` (or explicitly listed hostnames with `allow_bare_domains=true`).
- **Zero-downtime migration path for Vault CA:** Add `allowed_domains=*` before upgrading; remove `allow_empty_principals=true` only after confirming no rollback needed.
- **Manual CA deployments:** No migration steps required for v1.1.0.
- GAT token type is now validated from the payload claim — ensure tokens are of the correct type.
- Web App TLS support (upstream and downstream) is new in v1.1.0 and may require additional configuration.

## Related Docs
- [Wiki (main)](https://github.com/Twingate/gateway/wiki)
- [How It Works](https://github.com/Twingate/gateway/wiki/How-It-Works)
- [Kubernetes Overview](https://github.com/Twingate/gateway/wiki/Kubernetes-Overview)
- [SSH Overview](https://github.com/Twingate/gateway/wiki/SSH-Overview)
- [Developer Guide](https://github.com/Twingate/gateway/wiki/Developers)
- [DockerHub](https://hub.docker.com/r/twingate/gateway)
- [Twingate Forum](https://forum.twingate.com/)