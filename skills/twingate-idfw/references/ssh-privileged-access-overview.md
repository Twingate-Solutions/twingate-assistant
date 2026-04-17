# Twingate Privileged Access for SSH — Overview

**Page Title:** Privileged Access for SSH  
**URL:** https://www.twingate.com/docs/ssh-privileged-access-overview

## Summary

Twingate Privileged Access for SSH is a Layer 7 zero trust SSH proxy that eliminates SSH key distribution by issuing short-lived certificates per connection. A Gateway component deployed in your environment terminates SSH sessions, propagates user identity, and records all sessions in asciicast v2 format on your own infrastructure. Currently in early access, free for up to five Resources.

## Key Information

- **Gateway**: Standalone Layer 7 reverse proxy — terminates inbound SSH, authenticates to targets via certificate, records sessions to `stderr` in asciicast v2
- **No bastion required** — Gateway replaces bastion host functionality
- **No SSH keys on devices** — users connect with standard `ssh` CLI; certificates are ephemeral per-session
- **Session recordings** stored locally (never sent to Twingate); viewable at `twingate.com/sessionplayer`
- One Gateway can serve multiple SSH Resources within the same Remote Network

## Prerequisites

- Twingate Client minimum versions: macOS 2026.85 / Windows 2026.90 / Linux 2025.342
- Mobile clients (Android, iOS) not supported
- Target servers must support certificate-based SSH auth (Linux or Windows Server with OpenSSH)
- CAs configured under **Settings > Certificate Authorities** in Admin Console

## Certificate Authorities

Two CA types required:

| CA Type | Purpose |
|---|---|
| X.509 CA | Secures Client ↔ Gateway TLS connection (required for every Gateway) |
| SSH CA | Issues short-lived user certs + host certs for Gateway identity verification |

**CA signing modes:**
- **Local SSH CA** — Gateway holds private key, signs directly. Suitable for dev/test.
- **HashiCorp Vault** — Vault SSH secrets engine signs certs. Recommended for production (keys off-disk, audit logging).

## Supported SSH Features

| Supported | Not Supported |
|---|---|
| Interactive shell | X11 forwarding |
| Remote command execution | User config (`~/.ssh/config` overrides) |
| SFTP / rsync | |
| TCP/IP port forwarding | |

## User Configuration

Enable **SSH Server Configuration Auto-Sync** in the Twingate Client (More menu) to sync the SSH CA public key to `~/.ssh/known_hosts` — avoids TOFU prompts on first connection.

## Gotchas

- File transfer and port forwarding data is **not recorded** in session logs
- Existing `authorized_keys` entries are unaffected — migration to Twingate-only is incremental
- Session logs are written to Gateway `stderr` — you must configure forwarding to SIEM/object storage for retention
- Multiple CAs of each type can be created and reused across Gateways

## Related Docs

- Installing Privileged Access for SSH (prerequisites, deployment)
- Remote development with Twingate SSH (VS Code, JetBrains, Cursor)
- Settings > Certificate Authorities (Admin Console)