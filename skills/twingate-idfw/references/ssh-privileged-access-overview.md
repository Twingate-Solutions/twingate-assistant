# Twingate Privileged Access for SSH – Overview

## Page Title
Privileged Access for SSH Overview

## Summary
Twingate Privileged Access for SSH adds zero-trust, Layer 7 access controls to SSH sessions via a Gateway (reverse proxy) deployed in your environment. It eliminates SSH key distribution, enforces identity-based authentication using short-lived certificates, and records all sessions in asciicast v2 format on your own infrastructure.

## Key Information
- **Early Access**: Free for up to 5 Resources; contact Twingate for additional pricing
- Session recordings stored locally (never sent to Twingate); viewable at `twingate.com/sessionplayer`
- No bastion host required; Gateway replaces it
- Users connect with standard `ssh` — no custom CLI
- File transfer (`sftp`, `rsync`) and port forwarding supported; X11 forwarding is **not** supported
- File transfer and port forwarding data is **not** recorded

## Prerequisites
- Connector version ≥ `1.82.0` on all Connectors associated with SSH Resources
- Minimum Client versions:
  - macOS: `2026.85`
  - Windows: `2026.90`
  - Linux: `2025.342`
- Mobile clients (Android/iOS) not supported
- Gateway deployed to Kubernetes cluster or VM within target Remote Network

## Components

### Gateway
- Layer 7 reverse proxy; terminates inbound SSH, authenticates to target server, records sessions to `stderr`
- One Gateway can serve multiple SSH Resources within the same Remote Network

### Certificate Authorities (managed under Settings > Certificate Authorities)
| CA Type | Purpose | Required For |
|---------|---------|--------------|
| X.509 CA | Secures Client↔Gateway connection | Every Gateway |
| SSH CA | Issues short-lived user/host certs | Any SSH Resource |

### SSH CA Signing Modes
- **Local SSH CA**: Gateway holds private key; signs directly. Good for getting started.
- **HashiCorp Vault**: Uses Vault SSH secrets engine. Recommended for production (keys off-disk, audit logging).

## Configuration Values
- CAs: multiple CAs per type allowed; reusable across Gateways
- Session log format: `asciicast v2` written to `stderr` on Gateway
- Known hosts sync: `~/.ssh/known_hosts` (auto-synced via Twingate Client)

## Step-by-Step: Avoid TOFU Prompts (User Setup)
1. Open Twingate Client
2. Navigate to **More** → **SSH Server Configuration Auto-Sync**
3. Enables automatic sync of SSH CA public key to `~/.ssh/known_hosts`

## Gotchas
- Existing `authorized_keys` entries are unaffected; migration to CA-only access is manual
- Without SSH config auto-sync, users see TOFU warning on first connection
- Session recording does **not** capture file transfer or port forwarding data
- Logs are your responsibility to forward/retain (forward to SIEM or object storage)
- Windows Server supported only with OpenSSH installed

## Related Docs
- [Installing Privileged Access for SSH](https://www.twingate.com/docs/installing-privileged-access-for-ssh) – prerequisites and deployment options
- Remote development with Twingate SSH (VS Code, JetBrains, Cursor)
- Twingate session player: `twingate.com/sessionplayer`