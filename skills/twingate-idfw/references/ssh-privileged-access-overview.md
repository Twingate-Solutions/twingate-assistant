# Privileged Access for SSH Overview

## Page Title
Twingate Privileged Access for SSH Overview

## Summary
Twingate Privileged Access for SSH is a Layer 7 reverse proxy (Gateway) that adds zero trust SSH access controls without distributing SSH keys or changing user workflows. It enforces least-privileged access via short-lived certificates, records all sessions in asciicast v2 format on your own infrastructure, and integrates with standard `ssh` clients.

## Key Information
- **Early Access**: Free for up to 5 Resources; contact Twingate for additional pricing
- Users connect with standard `ssh` — no custom CLIs
- No SSH keys distributed to users; revoking Twingate access removes SSH access instantly
- Session recordings stored locally (never uploaded to Twingate); viewable at `twingate.com/sessionplayer`
- Gateway deployed in your environment (Kubernetes or VM), associated with a Remote Network
- One Gateway can serve multiple SSH Resources within the same Remote Network

## Prerequisites
- **Minimum Client versions**: macOS `2026.85`, Windows `2026.90`, Linux `2025.342`
- **Minimum Connector version**: `1.82.0` on all Connectors associated with SSH Resources
- Mobile clients (Android/iOS) **not supported**
- See "Installing Privileged Access for SSH" doc for full deployment prerequisites

## Components

### Gateway
- Terminates inbound SSH, authenticates to target via certificates, records sessions to `stderr` (asciicast v2)

### Certificate Authorities (managed in Settings > Certificate Authorities)
| CA Type | Purpose | Required |
|---------|---------|---------|
| X.509 CA | Secures Client ↔ Gateway connection | Every Gateway |
| SSH CA | Issues user/host certificates | Any SSH Resource |

### SSH CA Signing Modes
- **Local SSH CA**: CA private key on Gateway; simpler, good for getting started
- **HashiCorp Vault**: Uses Vault SSH secrets engine; recommended for production (keys off-disk, audit logging)

## Supported SSH Features
- ✅ Interactive shell, remote command execution, SFTP/rsync, TCP/IP port forwarding
- ❌ X11 forwarding, mobile clients

## User Configuration
To avoid TOFU prompts, sync SSH CA public key to `~/.ssh/known_hosts`:
1. Open Twingate Client
2. Go to **More > SSH Server Configuration Auto-Sync**
3. Enable auto-sync (keeps `~/.ssh/known_hosts` updated automatically)

## Gotchas
- Session logs written to Gateway `stderr` — you must configure forwarding to SIEM/object storage yourself
- File transfer and port forwarding data is **not recorded** in session logs
- Existing `authorized_keys` entries are unaffected; migration to CA-only access is manual
- Without SSH config sync, OpenSSH shows TOFU warning on first connection
- CAs are reusable across Gateways but must be configured per Gateway type

## Configuration Values
- Session log format: **asciicast v2** (on Gateway `stderr`)
- CA management location: **Admin Console > Settings > Certificate Authorities**

## Related Docs
- Installing Privileged Access for SSH (deployment guide)
- Remote development with Twingate SSH (VS Code, JetBrains, Cursor setup)
- Twingate community subreddit