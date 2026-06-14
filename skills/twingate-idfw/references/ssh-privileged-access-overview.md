# Twingate Privileged Access for SSH Overview

## Page Title
Privileged Access for SSH Overview

## Summary
Twingate Privileged Access for SSH adds zero-trust, application-layer access controls to SSH connections via a Layer 7 reverse proxy (Gateway) deployed in your environment. It eliminates SSH key distribution, enforces identity-based authentication using short-lived certificates, and provides full session recording stored on your own infrastructure.

## Key Information
- **Early Access**: Free for up to 5 Resources; contact Twingate for additional pricing
- Gateway is a standalone reverse proxy: terminates inbound SSH, authenticates to target servers via certificates, records sessions to `stderr` in asciicast v2 format
- No bastion host required; Gateway replaces bastion functionality
- Session logs written to Gateway `stderr`—never uploaded to Twingate; operator responsible for forwarding/retention
- Visualize recordings at `twingate.com/sessionplayer`
- Mobile clients (Android/iOS) not supported

## Prerequisites
- **Minimum Client versions**: macOS `2026.85`, Windows `2026.90`, Linux `2025.342`
- **Minimum Connector version**: `1.82.0` for all Connectors associated with SSH Resources
- Gateway deployed in environment (Kubernetes or VM)
- Gateway associated with a Remote Network in Admin Console

## Components

### Certificate Authorities (managed under Settings > Certificate Authorities)
| CA Type | Purpose | Required |
|---------|---------|----------|
| X.509 CA | Secures Client ↔ Gateway connection | Always |
| SSH CA | Issues user + host certificates | For SSH Resources |

### Gateway Certificate Signing Modes
- **Local SSH CA**: Gateway holds private key, signs directly. Simple deployments.
- **HashiCorp Vault**: Uses Vault SSH secrets engine. Recommended for production (keys off-disk, audit logging).

## Supported SSH Features
| Supported | Not Supported |
|-----------|--------------|
| Interactive shell | X11 forwarding |
| Remote command execution | |
| SFTP/rsync file transfer | |
| TCP/IP port forwarding | |

## User Configuration (Avoid TOFU Prompts)
1. Open Twingate Client
2. Go to **More** → **SSH Server Configuration Auto-Sync**
3. This syncs SSH CA public key to `~/.ssh/known_hosts` automatically

Without syncing, OpenSSH shows a TOFU warning on first connection.

## Gotchas
- File transfer and port forwarding traffic is **not** recorded in session logs
- Existing `authorized_keys` entries are unaffected—migration to CA-only is gradual
- A single Gateway can serve multiple SSH Resources within the same Remote Network
- Multiple CAs of each type can be created and reused across Gateways
- Windows Server supported only if OpenSSH is installed

## Related Docs
- [Installing Privileged Access for SSH](https://www.twingate.com/docs/installing-privileged-access-for-ssh) — prerequisites and deployment options
- Remote development with Twingate SSH (VS Code, JetBrains, Cursor)