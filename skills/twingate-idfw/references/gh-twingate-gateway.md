---
source: https://github.com/Twingate/gateway
type: github
fetched: 2026-10-11
source_version: 3407973bbfe357e1671cf2e34848c733ace803aa
trust: official
---

# Twingate Gateway

## Summary
The Twingate Gateway is a Layer 7 reverse proxy deployed within your own environment as part of Twingate Identity Firewall. It propagates user identity to upstream services and provides auditing for Kubernetes API servers, SSH servers, and web applications. Session recording, RBAC integration, and certificate-based auth are supported.

## Key Information
- Distributed as a Docker image: `twingate/gateway` on Docker Hub
- Supports Kubernetes, SSH, and Web App (TLS upstream/downstream as of v1.1.0) protocols
- SSH: certificate-based auth, CA management (manual or Vault-backed), full channel support (shell, exec, SFTP, port forwarding)
- Kubernetes: identity propagation, RBAC integration, `kubectl` session recording
- Free tier: up to 5 Kubernetes, SSH, or Web App resources

## Prerequisites
- A Twingate account with Identity Firewall enabled
- Docker or Kubernetes environment to run the Gateway container
- For Vault-backed SSH CA: a configured Vault SSH secrets engine role
- For SSH host certificates via Vault (v1.1.0+): the Gateway host CA role must permit resource addresses/aliases (e.g., `allowed_domains=*`)

## Usage / Step-by-Step

See the wiki for full guides:
- Kubernetes: [Quick Start Guide](https://github.com/Twingate/gateway/wiki/Kubernetes-Quick-Start-Guide)
- SSH: [Quick Start Guide](https://github.com/Twingate/gateway/wiki/SSH-Quick-Start-Guide)

**v1.1.0 Vault SSH CA migration (zero-downtime):**
1. Add `allowed_domains=*` to the Vault role while keeping `allow_empty_principals=true`
2. Upgrade the Gateway
3. Remove `allow_empty_principals=true` once rollback is no longer needed

## Configuration Values
- `ssh.ca.vault.role` — Vault SSH CA role (top-level fallback)
- `ssh.ca.vault.gatewayHostCA.role` — Vault role specifically for Gateway host CA signing
- Vault role options relevant to v1.1.0: `allowed_domains`, `allow_bare_domains`, `allow_subdomains`, `allow_empty_principals`

## Gotchas
- **v1.1.0 breaking change:** SSH host certificates now include resource addresses and aliases as principals. Vault-backed CA roles must explicitly allow those hostnames or use `allowed_domains=*`; deployments using a manual CA are unaffected.
- Skipping the migration steps before upgrading to v1.1.0 with Vault CA will cause host certificate signing to fail.

## Related Docs
- [Wiki home](https://github.com/Twingate/gateway/wiki)
- [How It Works](https://github.com/Twingate/gateway/wiki/How-It-Works)
- [Developer Guide](https://github.com/Twingate/gateway/wiki/Developers)
- [Twingate Forum](https://forum.twingate.com/)
- [Support](https://help.twingate.com/)