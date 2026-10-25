---
source: https://www.twingate.com/docs/ssh-privileged-access-overview
type: docs
fetched: 2026-10-25
source_version: d313a2e079aabd07e4eb0215bec4dc229d88f63ca0cbeb3cf0182d6eb6b49e39
trust: official
---

# Privileged Access for SSH Overview

## Page Title
Twingate Privileged Access for SSH Overview

## Summary
Twingate Privileged Access for SSH is a Layer 7 reverse proxy (Gateway) deployed in your environment that adds zero trust SSH access controls without distributing SSH keys to users. It issues short-lived certificates per connection, records all sessions in asciicast v2 format on your infrastructure, and requires no workflow changes for end users.

## Key Information
- **Early Access**: Free for up to 5 Resources; contact Twingate to start trial
- No SSH keys distributed to devices; access revocation is instant via Twingate identity
- Session recordings stored locally (never uploaded to Twingate) in asciicast v2 format, written to Gateway `stderr`
- Visualize recordings at `twingate.com/sessionplayer`
- Existing `authorized_keys` entries are unaffected; migration is incremental

## Prerequisites
- **Client minimum versions**: macOS 2026.85, Windows 2026.90, Linux 2025.342
- **Connector minimum version**: 1.82.0 (all Connectors tied to SSH Resources)
- Mobile clients (Android, iOS) not supported
- Target: Linux servers or Windows Server with OpenSSH installed

## Components

### Gateway
- Standalone Layer 7 reverse proxy deployed in your environment (Kubernetes or VM)
- Associated with a Remote Network; one Gateway serves multiple SSH Resources
- Terminates inbound SSH, authenticates to target via certificate, records session

### Certificate Authorities (managed in Admin Console → Settings > Certificate Authorities)
| Type | Purpose | Required |
|------|---------|----------|
| X.509 CA | Secures Client↔Gateway connection | Always |
| SSH CA | Issues short-lived user/host certificates | For SSH Resources |

### SSH CA Signing Modes
- **Local SSH CA**: Gateway holds private key; simpler, good for getting started
- **HashiCorp Vault**: Uses Vault SSH secrets engine; recommended for production (keys off-disk, audit logging)

## Supported SSH Features
- ✅ Interactive shell, remote command execution, `sftp`/`rsync`, TCP/IP port forwarding
- ❌ X11 forwarding, mobile clients, file transfer/port forwarding data in recordings

## Configuration Values
- Session logs: written to Gateway `stderr`
- Known hosts sync path: `~/.ssh/known_hosts`
- Session format: asciicast v2

## Step-by-Step: Avoid TOFU Prompts (User Setup)
1. Open Twingate Client
2. Navigate to **More** → **SSH Server Configuration Auto-Sync**
3. This syncs SSH CA public key to `~/.ssh/known_hosts` and keeps it updated

## Gotchas
- Without SSH config auto-sync, OpenSSH shows TOFU warning on first connection
- File transfer and port forwarding data is **not** captured in session recordings
- You are responsible for forwarding/retaining Gateway logs (SIEM, object storage)
- HashiCorp Vault integration is recommended for production; local CA keeps private key on disk

## Related Docs
- [Installing Privileged Access for SSH](https://www.twingate.com/docs/) — prerequisites and deployment options
- Remote development guide (VS Code, JetBrains, Cursor)
- Twingate community subreddit