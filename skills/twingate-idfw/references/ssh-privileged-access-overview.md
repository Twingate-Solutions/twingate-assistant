---
source: https://www.twingate.com/docs/ssh-privileged-access-overview
type: docs
fetched: 2026-11-13
source_version: b983b431ea2aacca4df5f4a809d5332470e3061027ae01328f56db411c785dc8
trust: official
---

# Privileged Access for SSH Overview

## Summary
Privileged Access for SSH is the SSH component of Twingate Identity Firewall. It places a Twingate Gateway (a Layer 7 reverse proxy) between users and SSH servers, so each session is tied to a Twingate identity, authenticated with a short-lived certificate, and recorded. It replaces bastion hosts and SSH key distribution.

## Key Information
- Status: Early Access; free for up to five Resources (contact Twingate for a trial).
- Users connect with standard `ssh`; no custom CLI and no SSH keys on devices.
- Revoking a user's Twingate access removes their SSH access.
- Servers need no public exposure or inbound firewall rules.
- Gateway is deployed in your environment (Kubernetes or VM) and tied to a Remote Network. One Gateway can serve multiple SSH Resources in the same Remote Network.
- **Flow:** Twingate authenticates the user via IdP → forwards identity to Gateway → Gateway authenticates to the target using a certificate from the SSH CA.
- **Certificate Authorities** (Admin Console: Settings > Certificate Authorities; multiple CAs allowed and reusable across Gateways):
  - X.509 CA: secures Client↔Gateway; required for every Gateway.
  - SSH CA: issues short-lived user certs and Gateway host certs; required for any SSH Resource.
- **SSH CA signing modes:** Local SSH CA (Gateway holds private key; good for starting out) or HashiCorp Vault SSH secrets engine (recommended for production; keys off-disk, audit logging).
- **Supported:** interactive shell, remote commands, `sftp`, `rsync`, TCP/IP port forwarding. **Not supported:** X11 forwarding.
- **Session recording:** asciicast v2, written to `stderr` by default (optionally a file), stored only on your infrastructure, never uploaded to Twingate. Captures terminal I/O and command output plus events like channel open/close. File transfer and port-forwarding data is not recorded. Playback: twingate.com/sessionplayer.
- Windows Server with OpenSSH is supported.

## Prerequisites
- Minimum Client versions: macOS 2026.85, Windows 2026.90, Linux 2025.342 (no Android/iOS).
- Connectors for SSH Resources: version 1.82.0 or later.
- A Gateway, an X.509 CA, and an SSH CA.
- The Linux account named in `ssh.gateway.username` must exist on every target server.

## Steps (user side)
1. Open the Twingate Client.
2. Under **More**, select **SSH Server Configuration Auto-Sync**. This syncs the SSH CA public key to `~/.ssh/known_hosts` and keeps it updated.
3. Connect: `ssh admin@home.int` (Resource address or alias, using the account name the Gateway signs in as).

## Configuration Values
- `ssh.gateway.username`: Linux account the Gateway uses to sign in to target servers.
- Log output: `stderr` by default; configurable to a file.

## Gotchas
- Without auto-sync, OpenSSH shows a TOFU warning on first connection.
- You are responsible for forwarding and retaining logs (SIEM/object storage).
- Existing `authorized_keys` entries are unaffected; the Gateway just adds the SSH CA as trusted, so you can migrate gradually.
- Port forwarding and file transfer content is not recorded.

## Related Docs
- Installing Privileged Access for SSH (prerequisites and deployment)
- Remote Development with VS Code (VS Code Remote SSH over Privileged Access)
- Twingate Identity Firewall