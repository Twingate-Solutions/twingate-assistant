---
source: https://github.com/Twingate/gateway
type: github
fetched: 2026-11-08
source_version: 8e42cae457ab55240eaf15e60ee2fb7e7bc378b3
trust: official
---

# Twingate Gateway

## Summary
The Twingate Gateway is a Layer 7 reverse proxy deployed within your environment as part of Twingate Identity Firewall. It propagates user identity to upstream services and provides auditing for Kubernetes API servers, SSH servers, and web applications. Free for up to five resources (Kubernetes, SSH, or Web App).

## Key Information
- Written in Go; distributed as a Docker image via [Docker Hub](https://hub.docker.com/r/twingate/gateway)
- Supported protocols: Kubernetes, SSH, Web App; Databases listed as coming soon
- Kubernetes: identity propagation, RBAC integration, `kubectl` session recording
- SSH: certificate-based authentication, CA management, shell/exec/SFTP/port-forwarding support
- Web App: identity injected as HTTP request headers, HTTP request auditing
- Latest fix: audit redirected requests from HTTP mux router (v current release)

## Prerequisites
- A Twingate account with Identity Firewall enabled
- Docker or a container orchestration platform (e.g., Kubernetes) to run the gateway image
- Network access from the gateway container to upstream services (K8s API server, SSH hosts, or internal web apps)

## Usage / Step-by-Step
Quick-start guides are maintained in the repo wiki:
- Kubernetes: [Kubernetes Quick Start Guide](https://github.com/Twingate/gateway/wiki/Kubernetes-Quick-Start-Guide)
- SSH: [SSH Quick Start Guide](https://github.com/Twingate/gateway/wiki/SSH-Quick-Start-Guide)
- Web App: [Web App Quick Start Guide](https://github.com/Twingate/gateway/wiki/Web-App-Quick-Start-Guide)

Pull the image from Docker Hub and follow the relevant quick-start guide for your protocol. No inline install script is documented in the repo README.

## Configuration Values
Specific environment variables, CLI flags, and API parameters are documented in the [wiki](https://github.com/Twingate/gateway/wiki). Check the protocol-specific overview pages for upstream connection settings and identity propagation options.

## Gotchas
- Free tier is limited to five resources; additional resources require contacting Twingate for pricing
- The gateway must be deployed inside your environment (not as a SaaS service); network routing to upstream targets must be configured separately
- Redirected HTTP requests through the mux router were not being audited prior to the latest release — upgrade if audit completeness is a requirement

## Related Docs
- [Wiki home](https://github.com/Twingate/gateway/wiki)
- [How It Works](https://github.com/Twingate/gateway/wiki/How-It-Works)
- [Developer Guide](https://github.com/Twingate/gateway/wiki/Developers)
- [Twingate Identity Firewall product docs](https://www.twingate.com/docs/identity-firewall)
- [Twingate community forum](https://forum.twingate.com/)
- [Support tickets](https://help.twingate.com/)