---
source: https://github.com/Twingate/gateway
type: github
fetched: 2026-09-06
source_version: 104af64beb4f1b44640f6ea9a0b0c0300cca5e27
---

<!-- triage: unassigned -->

# Twingate Gateway

## Summary
A Layer 7 reverse proxy deployed within your environment as part of Twingate Identity Firewall. It propagates user identity to upstream services and provides auditing for Kubernetes API servers, SSH servers, and web applications. Free for up to five Kubernetes, SSH, or Web App resources.

## Key Information
- Supports **Kubernetes** (RBAC integration, `kubectl` session recording), **SSH** (certificate-based auth, CA management, shell/exec/SFTP/port forwarding), and **Web App** resources (upstream and downstream TLS support added in v1.1.0)
- Eliminates plaintext credentials on end-user machines via identity propagation
- Provides session recording and replay for forensic/compliance use
- Docker image published to [Docker Hub](https://hub.docker.com/r/twingate/gateway)
- CI via GitHub Actions; coverage tracked via Codecov
- Current release: **v1.1.0** (breaking change to SSH host certificate principals; see migration notes below)

## Prerequisites
- A Twingate account with Identity Firewall enabled
- Docker or a Kubernetes cluster to deploy the gateway container
- Network access between the gateway and upstream services (Kubernetes API server or SSH server)

## Usage / Step-by-Step
1. Pull the Docker image: `docker pull twingate/gateway`
2. Follow the protocol-specific quick start guide:
   - [Kubernetes Quick Start](https://github.com/Twingate/gateway/wiki/Kubernetes-Quick-Start-Guide)
   - [SSH Quick Start](https://github.com/Twingate/gateway/wiki/SSH-Quick-Start-Guide)
3. Deploy the gateway within your environment (sidecar, standalone container, or Kubernetes pod)
4. Configure the gateway to point to the upstream service
5. Route client traffic through the gateway instead of directly to the upstream service

## Configuration Values
> Specific env vars and CLI flags are documented in the [Wiki](https://github.com/Twingate/gateway/wiki). Common configuration areas include:

| Area | Details |
|---|---|
| Upstream target | Address/port of the Kubernetes API server or SSH server |
| TLS/certificates | CA and certificate config for SSH certificate-based auth |
| Twingate API credentials | Token/credentials for identity resolution |
| Listening address | Port the gateway proxy listens on |
| Helm: Remote Network | Twingate Remote Network can now be specified via Helm values |

## Gotchas
- **v1.1.0 changes SSH host certificate principals**: SSH host certificates now include resource addresses and aliases. When using a Vault-backed SSH CA, the role (configured via `ssh.ca.vault.gatewayHostCA.role` or top-level `ssh.ca.vault.role`) must permit the relevant hostnames. Migrate without downtime by first adding `allowed_domains=*` with `allow_empty_principals=true`, then upgrading, then removing `allow_empty_principals=true`. Deployments using a manual CA need no change.
- **v1.0.0 introduces breaking changes** from v0.21; upgrade requires following the [migration guide](https://github.com/Twingate/gateway/wiki/Migration-0.21-to-1.0)
- Free tier is limited to **five** Kubernetes, SSH, or Web App resources; additional resources require contacting Twingate for pricing
- The gateway must be deployed **inside** your environment (not externally); it is not a cloud-hosted service
- Account-specific issues should go to Twingate support, not GitHub Issues

## Technical Details
- **Language**: Go 1.27.0
- **Build**: goreleaser, Docker buildx (v4.3.0), kind (testing)
- **Linting**: golangci-lint v2.13.1
- **Testing**: testify, helm-unittest
- Entry point: `main.go → cmd/start.go → proxy.NewProxy() → proxy.Start()`
- Gateway identifies itself to Twingate via a `User-Agent` header on outbound requests

## Related Docs
- [Wiki (main)](https://github.com/Twingate/gateway/wiki)
- [How It Works](https://github.com/Twingate/gateway/wiki/How-It-Works