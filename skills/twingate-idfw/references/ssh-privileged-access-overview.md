# Privileged Access for SSH Overview

## Page Title
Twingate Privileged Access for SSH Overview

## Summary
Twingate Privileged Access for SSH is a Layer 7 reverse proxy (Gateway) that adds zero trust access controls to SSH connections. It eliminates SSH key distribution by issuing short-lived certificates per connection, while recording all sessions in asciicast v2 format stored on your own infrastructure. Currently in early access, free for up to five Resources.

## Key Information
- **No SSH keys on devices** — Gateway authenticates using CA-issued short-lived certificates
- **Full session auditing** — asciicast v2 format, stored on your infrastructure only, never uploaded to Twingate
- **No workflow changes** — standard `ssh` client, no custom CLIs
- **No bastion host needed** — Gateway replaces bastion functionality
- **Session player** available at `twingate.com/sessionplayer`

## Prerequisites
- Minimum Client versions: macOS `2026.85`, Windows `2026.90`, Linux `2025.342`
- Minimum Connector version: `1.82.0` for all Connectors associated with SSH Resources
- Mobile clients (Android/iOS) **not supported**
- Deploy Gateway into your environment (Kubernetes or VM)

## Components

### Gateway
- Layer 7 reverse proxy — terminates inbound SSH, authenticates to target via certificate, records session to `stderr`
- One Gateway can serve multiple SSH Resources within the same Remote Network

### Certificate Authorities (managed under Settings > Certificate Authorities)
| CA Type | Purpose | Required |
|---------|---------|----------|
| X.509 CA | Secures Client ↔ Gateway connection | Every Gateway |
| SSH CA | Issues user/host certificates | Any SSH Resource |

### SSH CA Signing Modes
- **Local SSH CA** — Gateway holds private key, signs directly; suitable for dev/simple setups
- **HashiCorp Vault** — Uses Vault SSH secrets engine; recommended for production (keys off-disk, audit logs)

## Supported SSH Features
| Feature | Supported |
|---------|-----------|
| Interactive shell | ✅ |
| Remote command execution | ✅ |
| sftp / rsync | ✅ |
| TCP/IP port forwarding | ✅ |
| X11 forwarding | ❌ |
| File transfer/port forward recording | ❌ |

## Step-by-Step: Avoid TOFU Prompts (User Setup)
1. Open Twingate Client
2. Go to **More** → **SSH Server Configuration Auto-Sync**
3. This syncs SSH CA public key to `~/.ssh/known_hosts` automatically

## Configuration Values
- Session logs written to: `stderr` on the Gateway
- Log format: asciicast v2
- CA management: Admin Console → **Settings > Certificate Authorities**

## Gotchas
- Existing `authorized_keys` entries are **unaffected** — migration to Twingate-only access is optional/gradual
- Without SSH config sync, OpenSSH will show TOFU warning on first connection
- File transfer and port forwarding data is **not recorded** in session logs
- Private keys stay off-disk only if using HashiCorp Vault mode

## Related Docs
- [Installing Privileged Access for SSH](https://www.twingate.com/docs/installing-privileged-access-for-ssh) — prerequisites and deployment
- Remote development guide (VS Code, JetBrains, Cursor)
- Twingate community subreddit