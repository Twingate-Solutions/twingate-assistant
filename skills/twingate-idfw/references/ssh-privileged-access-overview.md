# Privileged Access for SSH Overview

## Page Title
Twingate Privileged Access for SSH Overview

## Summary
Twingate Privileged Access for SSH is a Layer 7 reverse proxy (Gateway) solution that adds zero trust access controls to SSH connections. It eliminates SSH key distribution by using short-lived certificates, records all sessions in asciicast v2 format on your infrastructure, and requires no workflow changes for end users. Currently in early access, free for up to five Resources.

## Key Information
- **Gateway**: Standalone Layer 7 reverse proxy deployed in your environment (Kubernetes or VM); associated with a Remote Network
- **No SSH keys on devices**: Short-lived certificates issued per connection; revoking Twingate access immediately removes SSH access
- **Session recordings**: Written to `stderr` on Gateway in asciicast v2 format; never sent to Twingate; visualize at `twingate.com/sessionplayer`
- **One Gateway** can serve multiple SSH Resources within the same Remote Network
- **CA Types**: X.509 CA (Client↔Gateway TLS) and SSH CA (user/host certificates); managed under Settings > Certificate Authorities

## Prerequisites
- Minimum Client versions: macOS `2026.85`, Windows `2026.90`, Linux `2025.342`
- Minimum Connector version: `1.82.0` for all Connectors associated with SSH Resources
- Desktop only: macOS, Windows, Linux (no mobile support)

## Certificate Authority Modes
| Mode | Description | Use Case |
|------|-------------|----------|
| Local SSH CA | Gateway holds private key, signs directly | Getting started / simple deployments |
| HashiCorp Vault | Uses Vault SSH secrets engine | Production (keys off-disk, audit logging) |

## Supported SSH Features
**Supported:** Interactive shell, remote command execution, SFTP/rsync, TCP/IP port forwarding  
**Not supported:** X11 forwarding

## Step-by-Step: Avoid TOFU Prompts (Client Setup)
1. Open Twingate Client
2. Go to **More** → **SSH Server Configuration Auto-Sync**
3. This syncs SSH CA public key to `~/.ssh/known_hosts` and keeps it updated automatically

## Configuration Values
- Session logs output: `stderr` on the Gateway
- Session recording format: asciicast v2
- known_hosts sync target: `~/.ssh/known_hosts`

## Gotchas
- Existing `authorized_keys` entries are **not removed**; SSH CA public key is added as a trusted CA alongside them
- File transfer and port forwarding data is **not recorded** in session logs
- Without SSH config auto-sync, OpenSSH will show TOFU warning on first connection
- Session log retention/forwarding to SIEM is your responsibility; Twingate provides no storage
- Windows Server requires OpenSSH installed

## Related Docs
- [Installing Privileged Access for SSH](https://www.twingate.com/docs/) — prerequisites and deployment options
- [Remote development with Twingate SSH](https://www.twingate.com/docs/) — VS Code, JetBrains, Cursor setup
- Settings > Certificate Authorities (Admin Console)