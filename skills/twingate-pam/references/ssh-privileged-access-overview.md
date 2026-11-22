---
source: https://www.twingate.com/docs/ssh-privileged-access-overview
type: docs
fetched: 2026-11-22
source_version: d8199aead35587f37b9d7f8b2b8b67131a81e84f4b4b459aab58710da079b8b5
trust: official
---

# Privileged Access for SSH Overview

## Summary
Privileged Access for SSH is the SSH component of Twingate Privileged Access Management. It places a Twingate Gateway (a Layer 7 reverse proxy) between users and SSH servers, so each session is tied to a Twingate identity, authenticated with a short-lived certificate, and recorded. It replaces bastion hosts and SSH key distribution.

## Key Information
- Users connect with standard `ssh`; no custom CLI is needed.
- Twingate authenticates the user via their IdP and forwards the identity to the Gateway. The Gateway authenticates to the target server using an SSH CA-issued certificate.
- Revoking a user's Twingate access removes their SSH access.
- The Gateway runs in your environment (Kubernetes or VM) and is associated with a Remote Network. One Gateway can serve multiple SSH Resources in that network.
- **Supported:** interactive shell, remote commands, `sftp`/`rsync`, local (`-L`) and remote (`-R`) port forwarding.
- **Not supported:** X11 forwarding, and the Android and iOS clients.
- Windows Server with OpenSSH is supported.
- Existing `authorized_keys` entries are unaffected, so you can migrate gradually.
- **Certificate Authorities** (managed under Settings > Certificate Authorities in the Admin Console):
  - X.509 CA: secures Client-to-Gateway traffic. Required for every Gateway.
  - SSH CA: issues short-lived user certs and Gateway host certs. Required for any SSH Resource.
- **SSH CA signing modes:**
  - Local SSH CA: the Gateway holds the private key. Suited to simple setups.
  - HashiCorp Vault: recommended for production. Authenticates via token, AppRole, GCP, or AWS.
- **Session recording:**
  - Format is asciicast v2, written to `stderr` by default (can be configured to write to a file).
  - Recordings stay on your infrastructure and are never uploaded to Twingate.
  - You are responsible for forwarding (SIEM or object storage) and retention.
  - File transfer and port-forwarding data is not recorded.

## Prerequisites
- Minimum Client versions: macOS 2026.85, Windows 2026.90, Linux 2025.342.
- Connectors associated with SSH Resources must be on version 1.82.0 or later.
- An X.509 CA and an SSH CA configured for the Gateway.
- The Linux account named in `ssh.gateway.username` must exist on every target server.
- Availability: contact Twingate for a free trial.

## Step-by-Step (User Setup)
1. Open the Twingate Client.
2. Under **More**, select **SSH Server Configuration Auto-Sync**. This syncs the SSH CA public key to `~/.ssh/known_hosts` and keeps it updated.
3. Connect, for example: `ssh admin@home.int`

## Configuration Values
- `ssh.gateway.username`: the Linux account the Gateway signs in as on target servers.
- Gateway log output: `stderr` by default, or a file.

## Gotchas
- Without Auto-Sync, OpenSSH shows a TOFU warning on first connection.
- By default, the Gateway uses TOFU for target server host keys. For cryptographic verification from the first connection, sign each server's host key with the SSH CA.
- The username in the `ssh` command must be the account the Gateway signs in as.
- Local SSH CA keeps the private key on the Gateway. Use Vault for production.

## Related Docs
- Installing Privileged Access for SSH (https://www.twingate.com/docs/ssh-installation)
- Sign target server host keys (https://www.twingate.com/docs/ssh-installation#sign-target-server-host-keys)
- Session Recordings (https://www.twingate.com/docs/gateway-session-recordings)
- Remote Development with VS Code (https://www.twingate.com/docs/ssh-remote-development)
- Privileged Access Management (https://www.twingate.com/docs/privileged-access-management)
- Twingate session player (https://www.twingate.com/sessionplayer)