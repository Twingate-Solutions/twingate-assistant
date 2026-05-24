# Privileged Access for SSH Overview

## Page Title
Twingate Privileged Access for SSH Overview

## Summary
Twingate Privileged Access for SSH is a Layer 7 zero trust access control system for SSH connections that uses short-lived certificates instead of SSH keys. A Gateway component (reverse proxy) handles identity propagation, certificate-based auth to target servers, and session recording. Currently in early access, free for up to 5 Resources.

## Key Information
- No SSH keys distributed to users; certificates are short-lived and per-connection
- Revoking Twingate access immediately removes SSH access
- Session recordings stored in **asciicast v2 format** on your own infrastructure (never uploaded to Twingate)
- Standard `ssh` command works — no custom CLI required
- Gateway is a standalone Layer 7 reverse proxy deployed in your environment (Kubernetes or VM)
- One Gateway can serve multiple SSH Resources within the same Remote Network

## Prerequisites
- Minimum Client versions: macOS `2026.85`, Windows `2026.90`, Linux `2025.342`
- Minimum Connector version: `1.82.0` (all Connectors associated with SSH Resources)
- Mobile clients (Android/iOS) **not supported**
- Gateway must be associated with a Remote Network in Twingate Admin Console

## Components

### Certificate Authorities (managed under Settings > Certificate Authorities)
| Type | Purpose | Required |
|------|---------|----------|
| X.509 CA | Secures Client ↔ Gateway connection | Always |
| SSH CA | Issues user/host certificates | For SSH Resources |

### Gateway Signing Modes
- **Local SSH CA** — Gateway holds private key; simpler setup
- **HashiCorp Vault** — Uses Vault SSH secrets engine; recommended for production (keys off-disk, audit logging)

## Supported SSH Features
| Supported | Not Supported |
|-----------|--------------|
| Interactive shell | X11 forwarding |
| Remote command execution | |
| SFTP, rsync | |
| TCP/IP port forwarding | |

## Configuration Values
- CAs created/managed in: **Admin Console → Settings → Certificate Authorities**
- Session logs written to: `stderr` on the Gateway
- SSH CA public key synced to: `~/.ssh/known_hosts`

## User SSH Config Sync (avoid TOFU prompts)
1. Open Twingate Client
2. Go to **More → SSH Server Configuration Auto-Sync**
3. Enables automatic sync of SSH CA public key to `~/.ssh/known_hosts`

## Gotchas
- Without SSH config sync, OpenSSH shows TOFU warning on first connection
- File transfer and port forwarding data is **not recorded** in session logs
- Existing `authorized_keys` entries are unaffected when adding SSH CA — migration is incremental
- Session log retention and forwarding (SIEM, object storage) is your responsibility
- Windows Server supported only with OpenSSH installed

## Related Docs
- [Installing Privileged Access for SSH](https://www.twingate.com/docs/ssh-privileged-access-install) — prerequisites and deployment
- [Remote development with Twingate SSH](https://www.twingate.com/docs/ssh-remote-dev) — VS Code, JetBrains, Cursor setup
- Session player: `twingate.com/sessionplayer`