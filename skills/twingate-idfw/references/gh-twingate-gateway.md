---
source: https://github.com/Twingate/gateway
type: github
fetched: 2026-10-04
source_version: 5ed8e12fc806474700abd9988cc3a85861aa83ad
trust: official
---

# Twingate Gateway

## Summary
A Layer 7 reverse proxy deployed within your infrastructure as part of Twingate Identity Firewall. It propagates user identity to upstream services and provides auditing for Kubernetes API servers, SSH servers, and web applications. Acts as a reverse proxy that intercepts connections and injects identity context without requiring credentials on end-user machines.

## Key Information
- **Protocols supported:** Kubernetes, SSH, Web App (TLS upstream/downstream as of v1.1.0)
- **Deployment:** Self-hosted within your environment; Docker image available on DockerHub (`twingate/gateway`)
- **SSH CA options:** Local (file) CA or Vault-backed CA
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

## Internal Architecture

```
main.go → cmd/start.go → proxy.NewProxy() → proxy.Start()
  ├─> frontend.NewListener() (TLS + CONNECT auth, dispatch by GAT resource type)
  ├─> one frontend.ProtocolListener per enabled backend
  │     e.g. kubernetes.NewHandler(), webapp handler, ssh.NewProxy()
  └─> metrics.Start() (Prometheus)
```

### Key Packages
| Area | Path |
|---|---|
| Orchestrator | `internal/proxy/proxy.go` |
| Auth / CONNECT | `internal/frontend/connect.go` |
| Listener / dispatch | `internal/frontend/listener.go` |
| Server cert sourcing | `internal/frontend/cert/` |
| GAT JWT parsing | `internal/token/parser.go` |
| Shared HTTP proxy core | `internal/backend/httpproxy/proxy.go` |
| Kubernetes proxy | `internal/backend/kubernetes/handler.go` |
| Web app proxy | `internal/backend/webapp/handler.go` |
| SSH proxy | `internal/backend/ssh/proxy.go` |
| Session recording | `internal/sessionrecorder/` |
| Vault client | `internal/vault/` |
| Shared helpers | `internal/util/` (imports nothing else under `internal/`) |
| Helm chart | `deploy/gateway/` |

### Security Model
- **Frontend:** Every connection goes through TLS termination → CONNECT validation → JWT verification → Proof-of-Possession (client signs TLS EKM with private key matching the public key in the GAT).
- **K8s:** Gateway adds `Impersonate-User`/`Impersonate-Group` headers; RBAC enforced at the API server. Gateway service account needs only impersonation permission.
- **Web App:** Request headers rewritten from templates with GAT variables (JWT, username, groups, client geo); client identity headers (`X-Real-IP`, `X-Forwarded-*`) stripped to prevent