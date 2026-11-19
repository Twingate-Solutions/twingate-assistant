---
source: https://github.com/Twingate/gateway
type: github
fetched: 2026-11-19
source_version: 25d6db672a1028e528dc149642dcf20fb0408c51
trust: official
---

# Twingate Gateway

## Summary
The Twingate Gateway is a Layer 7 reverse proxy deployed within your environment as part of Twingate Privileged Access Management (PAM), formerly referred to as Identity Firewall. It propagates user identity to upstream services and provides auditing for Kubernetes API servers, SSH servers, and web applications. Free for up to five resources (Kubernetes, SSH, or Web App).

## Key Information
- Written in Go (1.27.4); distributed as a Docker image via [Docker Hub](https://hub.docker.com/r/twingate/gateway). License: MPL-2.0
- Supported protocols: Kubernetes, SSH, Web App; Databases listed as coming soon
- Kubernetes: identity propagation, RBAC integration, `kubectl` session recording
- SSH: certificate-based authentication, CA management, shell/exec/SFTP/port-forwarding support
- Web App: identity injected as HTTP request headers, HTTP request auditing
- Recent changes: HTTP/2 support for Kubernetes and Web App backends; the `TwingateGateway` address can be set in the Helm chart; SSH connections still being set up are now closed on shutdown; protocol client TLS handshake is now performed in the HTTP backends
- Earlier fix: audit redirected requests from the HTTP mux router
- Code layout: the HTTP backends share `internal/backend/httpproxy/` (TLS with the protocol client when the GAT requires it, HTTP/2 for TLS clients, 421 for requests whose hostname does not resolve to the connection's upstream host, audit middleware)

## Prerequisites
- A Twingate account with PAM (Identity Firewall) enabled
- Docker or a container orchestration platform (e.g., Kubernetes) to run the gateway image
- Network access from the gateway container to upstream services (K8s API server, SSH hosts, or internal web apps)

## Usage / Step-by-Step
Quick-start guides are maintained in the repo wiki:
- Kubernetes: [Kubernetes Quick Start Guide](https://github.com/Twingate/gateway/wiki/Kubernetes-Quick-Start-Guide)
- SSH: [SSH Quick Start Guide](https://github.com/Twingate/gateway/wiki/SSH-Quick-Start-Guide)
- Web App: [Web App Quick Start Guide](https://github.com/Twingate/gateway/wiki/Web-App-Quick-Start-Guide)

Pull the image from Docker Hub and follow the relevant quick-start guide for your protocol. No inline install script is documented in the repo README.

For development, Go is pinned in `.tool-versions` (install with `asdf install golang 1.27.4`).

## Configuration Values
Specific environment variables, CLI flags, and API parameters are documented in the [wiki](https://github.com/Twingate/gateway/wiki). Check the protocol-specific overview pages for upstream connection settings and identity propagation options. The gateway address can be set through the Helm chart.

## Gotchas
- Free tier is limited to five resources; additional resources require contacting Twingate for pricing
- The gateway must be deployed inside your environment (not as a SaaS service); network routing to upstream targets must be configured separately
- Redirected HTTP requests through the mux router were not audited in older releases; upgrade if audit completeness is a requirement
- HTTP backends return 421 when the request hostname does not match the connection's upstream host

## Related Docs
- [Wiki home](https://github.com/Twingate/gateway/wiki)
- [How It Works](https://github.com/Twingate/gateway/wiki/How-It-Works)
- [Developer Guide](https://github.com/Twingate/gateway/wiki/Developers)
- [Twingate PAM product docs](https://www.twingate.com/docs/identity-firewall)
- [Twingate community forum](https://forum.twingate.com/)
- [Support tickets](https://help.twingate.com/)