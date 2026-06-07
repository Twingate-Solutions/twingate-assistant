# Privileged Access for SSH Overview

## Page Title
Twingate Privileged Access for SSH Overview

## Summary
Twingate Privileged Access for SSH is a Layer 7 zero trust proxy that handles SSH session authentication via short-lived certificates, eliminating SSH key distribution. It records all sessions in asciicast v2 format stored on your own infrastructure, with no workflow changes for end users.

## Key Information
- **Early Access**: Free for up to 5 Resources; contact Twingate for additional pricing
- Gateway acts as Layer 7 reverse proxy — terminates inbound SSH, authenticates to target via certificate, records session
- No SSH keys distributed to users; certificate-based auth only
- Session recordings exported to `stderr` on Gateway in asciicast v2 format — never sent to Twingate
- Visualize recordings at `twingate.com/sessionplayer`
- One Gateway can serve multiple SSH Resources within the same Remote Network

## Prerequisites
- Minimum Client versions: macOS `2026.85`, Windows `2026.90`, Linux `2025.342`
- Minimum Connector version: `1.82.0` on all Connectors associated with SSH Resources
- Mobile clients (Android/iOS) **not supported**
- Gateway deployed to Kubernetes cluster or VM

## Components

### Certificate Authorities (managed in Settings > Certificate Authorities)
| CA Type | Purpose | Required |
|---------|---------|---------|
| X.509 CA | Secures Client ↔ Gateway connection | Always |
| SSH CA | Issues user + host certificates | For SSH Resources |

### Gateway CA Signing Modes
- **Local SSH CA**: CA private key on Gateway; simpler, good for getting started
- **HashiCorp Vault**: Uses Vault SSH secrets engine; recommended for production (keys off-disk, audit logging)

## Supported Features
**Supported:** Interactive shell, remote command execution, SFTP/rsync, TCP/IP port forwarding  
**Not supported:** X11 forwarding, mobile clients

## User Configuration (Avoiding TOFU Prompts)
1. Open Twingate Client
2. Under **More**, select **SSH Server Configuration Auto-Sync**
3. This syncs SSH CA public key to `~/.ssh/known_hosts` and keeps it updated

Without this step, OpenSSH shows TOFU warning on first connection.

## Gotchas
- Existing `authorized_keys` entries are **unaffected** — SSH CA is added as an additional trusted CA; migration is gradual
- File transfer and port forwarding data is **not** recorded in session logs
- Session logs are written to `stderr` — you must configure forwarding to SIEM/object storage yourself
- Windows Server requires OpenSSH installed; same setup process applies
- CAs can be reused across multiple Gateways

## Configuration Values
- Session log format: `asciicast v2` on Gateway `stderr`
- CA management: Admin Console → **Settings > Certificate Authorities**

## Related Docs
- [Installing Privileged Access for SSH](https://www.twingate.com/docs/) — prerequisites and deployment options
- Remote development guide (VS Code, JetBrains, Cursor)
- Twingate community subreddit