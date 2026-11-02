---
source: https://github.com/Twingate/gateway
type: github
fetched: 2026-11-01
source_version: d9ac90a34029c7d9c935087125539edc22f3fa48
trust: official
---

# Twingate Gateway

## Summary
The Twingate Gateway is an open-source Layer 7 reverse proxy that runs inside your environment as part of Twingate Identity Firewall. It propagates user identity to upstream services and provides auditing for Kubernetes API servers, SSH servers, and web applications. It eliminates the need for plaintext credentials on end-user machines by handling authentication at the proxy layer.

## Key Information
- Written in Go; distributed as a Docker image (`twingate/gateway` on Docker Hub)
- Supports three protocols: Kubernetes (kubectl/RBAC), SSH (certificate-based auth, shell/exec/SFTP/port forwarding), and Web App (header injection + HTTP auditing)
- Database support is listed as coming soon
- Free tier covers up to five Kubernetes, SSH, or Web App resources
- Latest release fixed auditing of redirected requests from the HTTP mux router

## Prerequisites
- A Twingate account with Identity Firewall enabled
- Docker or a Kubernetes environment to run the gateway container
- Network access between the gateway and your upstream services (Kubernetes API server, SSH host, or internal web app)

## Usage / Step-by-Step
Protocol-specific quick start guides are maintained in the project wiki:
- **Kubernetes:** github.com/Twingate/gateway/wiki/Kubernetes-Quick-Start-Guide
- **SSH:** github.com/Twingate/gateway/wiki/SSH-Quick-Start-Guide
- **Web App:** github.com/Twingate/gateway/wiki/Web-App-Quick-Start-Guide

For local development and release process details, see the Developer Guide: github.com/Twingate/gateway/wiki/Developers

## Configuration Values
Configuration details are protocol-specific and documented in the wiki. No environment variables or CLI flags are documented in the README itself; refer to the relevant quick start guide for your protocol.

## Gotchas
- The gateway must be deployed **inside** your environment (not externally); it is a self-hosted component
- Identity propagation only works when traffic reaches the gateway through Twingate's network; direct access bypasses identity attribution
- Redirected HTTP requests were not being audited prior to the latest release (now fixed)

## Related Docs
- [Wiki (all topics)](https://github.com/Twingate/gateway/wiki)
- [How It Works](https://github.com/Twingate/gateway/wiki/How-It-Works)
- [Twingate Identity Firewall docs](https://www.twingate.com/docs/identity-firewall)
- [Demo video](https://youtu.be/kLE9txLo8Kg?si=iUrjzFuILMwnWCVI&t=1038)
- [Support forum](https://forum.twingate.com/)
- [Docker Hub image](https://hub.docker.com/r/twingate/gateway)