---
source: https://github.com/Twingate/gateway
type: github
fetched: 2026-10-28
source_version: 02278747114351db1c960c6a59c0970962a95922
trust: official
---

# Twingate Gateway

## Summary
The Twingate Gateway is a Layer 7 reverse proxy deployed within your own environment as part of Twingate Identity Firewall. It propagates user identity to upstream services and provides auditing for Kubernetes API servers, SSH servers, and web applications. Session recording, RBAC integration, and certificate-based auth are supported.

## Key Information
- Distributed as a Docker image: `twingate/gateway` on Docker Hub
- Supports Kubernetes, SSH, and Web App protocols
- SSH: certificate-based auth, CA management (local or Vault-backed), full channel support (shell, exec, SFTP, port forwarding)
- Kubernetes: identity propagation, RBAC integration, `kubectl` session recording
- Web App: identity propagation via injected request headers, HTTP request auditing
- Databases: coming soon
- Free tier: up to 5 Kubernetes, SSH, or Web App resources

## Prerequisites
- A Twingate account with Identity Firewall enabled
- Docker or Kubernetes environment to run the Gateway container
- For Vault-backed SSH CA: a configured Vault SSH secrets engine role
- For SSH host certificates via Vault: the Gateway host CA role must permit resource addresses/aliases (e.g., `allowed_domains=*`)

## Usage / Step-by-Step

See the wiki for full guides:
- Kubernetes: [Quick Start Guide](https://github.com/Twingate/gateway/wiki/Kubernetes-Quick-Start-Guide)
- SSH: [Quick Start Guide](https://github.com/Twingate/gateway/wiki/SSH-Quick-Start-Guide)
- Web App: [Quick Start Guide](https://github.com/Twingate/gateway/wiki/Web-App-Quick-Start-Guide)

## Configuration Values (v2.x)
- `ssh.ca.local` — local/manual SSH CA config (renamed from `ssh.ca.manual`)
- `ssh.ca.vault.role` — Vault SSH CA role (top-level fallback)
- `ssh.ca.vault.gatewayHostCA.role` — Vault role specifically for Gateway host CA signing
- `log.sessionRecording` — session recording config (renamed from `auditLog`)
- `upstreamTrustedCABundles` — upstream CA bundles (renamed from `cas` / `upstreamCABundles`)
- TLS `tls_mode` enum replaces former boolean `tls` fields
- Multiple static downstream TLS certificates supported
- Automated downstream certificate issuance supported (cert-manager with ACME, Vault, local, and GCP Private CA issuers)

## Gotchas
- **v2.0.0 introduces breaking changes.** See the [v1 → v2 migration guide](https://github.com/Twingate/gateway/wiki/Migration-1.0-to-2.0) before upgrading.
- `ssh.ca.manual` renamed to `ssh.ca.local`; `auditLog` renamed to `log.sessionRecording`; `certificateConfigMapName` replaced by `certificateSecretName`; `--debug` flag removed.
- Vault token auth method for Vault SSH CA has been removed.
- Dev release tags now include a UTC build timestamp: `v1.2.3-dev-abc1234-20260101120000`.

## Related Docs
- [Wiki home](https://github.com/Twingate/gateway/wiki)
- [How It Works](https://github.com/Twingate/gateway/wiki/How-It-Works)
- [Web App Overview](https://github.com/Twingate/gateway/wiki/Web-App-Overview)
- [Developer Guide](https://github.com/Twingate/gateway/wiki/Developers)
- [Twingate Forum](https://forum.twingate.com/)
- [Support](https://help.twingate.com/)