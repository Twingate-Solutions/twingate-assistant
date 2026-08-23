---
source: https://github.com/Twingate/gateway
type: github
fetched: 2026-08-23
source_version: 2e7b9e69bf3febcd6bb13f018732773846aa784d
---

<!-- triage: unassigned -->

# Twingate Gateway

## Summary
A Layer 7 reverse proxy deployed within your environment as part of Twingate Identity Firewall. It propagates user identity to upstream services and provides auditing for Kubernetes API servers, SSH servers, and web applications. Free for up to five Kubernetes, SSH, or Web App resources.

## Key Information
- Supports **Kubernetes** (RBAC integration, `kubectl` session recording) and **SSH** (certificate-based auth, CA management, shell/exec/SFTP/port forwarding); Web App support is coming soon
- Eliminates plaintext credentials on end-user machines via identity propagation
- Provides session recording and replay for forensic/compliance use
- Docker image published to [Docker Hub](https://hub.docker.com/r/twingate/gateway)
- CI via GitHub Actions; coverage tracked via Codecov
- Current release: **v1.0.0** (breaking changes from v0.21; see [migration guide](https://github.com/Twingate/gateway/wiki/Migration-0.21-to-1.0))

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
- **v1.0.0 introduces breaking changes** from v0.21; upgrade requires following the [migration guide](https://github.com/Twingate/gateway/wiki/Migration-0.21-to-1.0)
- Web App protocol support is listed as "Coming Soon" — not yet available
- Free tier is limited to **five** Kubernetes, SSH, or Web App resources; additional resources require contacting Twingate for pricing
- The gateway must be deployed **inside** your environment (not externally); it is not a cloud-hosted service
- Account-specific issues should go to Twingate support, not GitHub Issues

## Technical Details
- **Language**: Go 1.26.6
- **Build**: goreleaser, Docker buildx (v4.3.0), kind (testing)
- **Linting**: golangci-lint v2.11.1
- **Testing**: testify, helm-unittest
- Entry point: `main.go → cmd/start.go → proxy.NewProxy() → proxy.Start()`

## Related Docs
- [Wiki (main)](https://github.com/Twingate/gateway/wiki)
- [How It Works](https://github.com/Twingate/gateway/wiki/How-It-Works)
- [Kubernetes Overview](https://github.com/Twingate/gateway/wiki/Kubernetes-Overview)
- [SSH Overview](https://github.com/Twingate/gateway/wiki/SSH-Overview)
- [Developer Guide](https://github.com/Twingate/gateway/wiki/Developers)
- [Migration Guide (v0.21 → v1.0)](https://github.com/Twingate/gateway/wiki/Migration-0.21-to-1.0