# Privileged Access for SSH Overview

## Page Title
Twingate Privileged Access for SSH Overview

## Summary
Twingate Privileged Access for SSH is a Layer 7 reverse proxy (Gateway) that adds zero trust SSH access controls without distributing SSH keys to users. It provides short-lived certificate-based auth, full session recording in asciicast v2 format stored on your infrastructure, and works with standard `ssh` clients. Currently early access, free for up to 5 Resources.

## Key Information
- Gateway acts as SSH reverse proxy: terminates inbound sessions, authenticates to targets via certificates, records sessions
- No SSH keys on user devices; short-lived certificates issued per connection
- Session recordings exported to Gateway `stderr` in asciicast v2 format — never sent to Twingate
- One Gateway serves multiple SSH Resources within same Remote Network
- Visualize recordings at `twingate.com/sessionplayer`

## Prerequisites
- Minimum Client versions: macOS `2026.85`, Windows `2026.90`, Linux `2025.342`
- Minimum Connector version: `1.82.0` (all Connectors associated with SSH Resources)
- Mobile clients (Android/iOS) not supported
- Deployment target: Kubernetes cluster or VM

## Components

### Certificate Authorities (configured in Settings > Certificate Authorities)
| CA Type | Purpose | Required |
|---------|---------|----------|
| X.509 CA | Secures Client ↔ Gateway connection | Always |
| SSH CA | Issues user/host certificates | For SSH Resources |

### Gateway Signing Modes
- **Local SSH CA**: CA private key on Gateway; simpler, good for getting started
- **HashiCorp Vault**: Uses Vault SSH secrets engine; recommended for production (keys off-disk, audit logging)

## Supported SSH Features
| Feature | Supported |
|---------|-----------|
| Interactive shell | ✅ |
| Remote command execution | ✅ |
| SFTP / rsync | ✅ |
| TCP/IP port forwarding | ✅ |
| X11 forwarding | ❌ |

## User Configuration (Avoiding TOFU Prompts)
1. Open Twingate Client
2. Go to **More** → **SSH Server Configuration Auto-Sync**
3. This syncs SSH CA public key to `~/.ssh/known_hosts` and keeps it updated

Without this step, OpenSSH shows TOFU warning on first connection.

## Gotchas
- File transfer and port forwarding data is **not** recorded in session logs
- Existing `authorized_keys` entries are unaffected when adding SSH CA — migration is optional
- You are responsible for forwarding/retaining session logs (SIEM, object storage)
- Session recording captures terminal I/O for interactive shells; also logs channel open/close events
- Windows Server supported if OpenSSH is installed

## Related Docs
- [Installing Privileged Access for SSH](https://www.twingate.com/docs/installing-privileged-access-for-ssh) — prerequisites and deployment options
- Remote development guide (VS Code, JetBrains, Cursor)
- Twingate community subreddit