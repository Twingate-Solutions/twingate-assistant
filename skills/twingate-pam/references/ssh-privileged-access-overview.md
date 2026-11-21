---
source: https://www.twingate.com/docs/ssh-privileged-access-overview
type: docs
fetched: 2026-11-19
source_version: eb24fec26fcf362a6cbb2fbd589efa8adffc9539ca854648f93aed3f9bf3b36e
trust: official
---

# Privileged Access for SSH Overview

## Summary
Privileged Access for SSH is the SSH component of Twingate Privileged Access Management. A Twingate Gateway (Layer 7 reverse proxy) sits between users and SSH servers, tying each session to a Twingate identity, authenticating with short-lived certificates, and recording sessions on your own infrastructure. It replaces bastion hosts and SSH key distribution. Status: Early Access, free for up to five Resources.

## Key Information
- Users connect with standard `ssh`; no custom CLI and no SSH keys on devices.
- Revoking a user's Twingate access removes SSH access.
- SSH servers need no public exposure or inbound firewall rules.
- Gateway is deployed in Kubernetes or a VM and associated with one Remote Network; one Gateway can serve multiple SSH Resources in that network.
- **Two CA types** (managed in Admin Console under Settings > Certificate Authorities; multiple CAs allowed and reusable across Gateways):
  - X.509 CA: secures Client-to-Gateway connection. Required for every Gateway.
  - SSH CA: issues short-lived user certs and Gateway host certs. Required for any SSH Resource.
- **SSH CA signing modes:** Local SSH CA (Gateway holds private key; good for getting started) or HashiCorp Vault SSH secrets engine (recommended for production; keys off-disk, audit logging).
- **Supported:** interactive shell, remote commands, file transfer (`sftp`, `rsync`), TCP/IP port forwarding. **Not supported:** X11 forwarding.
- **Session recording:** asciicast v2 format, written to `stderr` by default (can be configured to write to a file). Never uploaded to Twingate. Captures terminal I/O and command output plus SSH events (channel open/close). File transfer and port forwarding data is not recorded. Playback via twingate.com/sessionplayer.
- Windows Server with OpenSSH is supported as a target.

## Prerequisites
- Client minimum versions: macOS 2026.85, Windows 2026.90, Linux 2025.342. Mobile (Android/iOS) is unsupported.
- Connectors for SSH Resources: version 1.82.0 or later.
- Gateway, X.509 CA, and SSH CA (see the install guide for full prerequisites).
- The Linux account named in `ssh.gateway.username` must exist on every target server.

## Step-by-Step (Client setup)
1. Open the Twingate Client.
2. Under **More**, select **SSH Server Configuration Auto-Sync**. This syncs the SSH CA public key to `~/.ssh/known_hosts` and keeps it updated.
3. Connect: `ssh admin@home.int` (use the Resource address or alias and the Gateway's configured account name).

## Configuration Values
- `ssh.gateway.username`: Linux account the Gateway uses to sign in to target servers.
- Log output: `stderr` by default; file output configurable on the Gateway.

## Gotchas
- Without auto-sync, OpenSSH shows a TOFU warning on first connection.
- You are responsible for forwarding and retaining logs (SIEM or object storage); Twingate has no access to session content.
- Existing `authorized_keys` entries are unaffected; the Gateway adds the SSH CA as a trusted CA, so migration can be gradual.
- The username users type must match the account the Gateway signs in as.

## Related Docs
- Installing Privileged Access for SSH (prerequisites, deployment)
- Remote Development with VS Code (Remote SSH over Privileged Access for SSH)
- Twingate Privileged Access Management overview