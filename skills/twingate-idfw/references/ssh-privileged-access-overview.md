## Privileged Access for SSH (IDFW)

Twingate IDFW for SSH -- adds zero-trust controls to SSH sessions: identity propagation, short-lived per-connection certificates, and full session recording. Replaces SSH key distribution and bastion hosts.

**Status:**
- Early access, free for up to 5 Resources

**Architecture:**
- **Twingate Gateway** = Layer 7 reverse proxy deployed in your environment (K8s or VM)
- One Gateway can serve **multiple SSH Resources** within the same Remote Network
- User SSH client -> Twingate Client -> Connector -> **Gateway** -> target SSH server

**Authentication Flow:**
1. User initiates `ssh user@host` (host = private IP or FQDN, defined as a Twingate Resource)
2. Twingate Client tunnels to the Gateway
3. Gateway authenticates the user via IdP (Twingate session = IdP identity)
4. Gateway requests a **short-lived SSH user certificate** from the SSH CA
5. Gateway authenticates to the target SSH server using that certificate
6. SSH session proceeds normally; Gateway records all I/O

**No SSH Keys on Devices:**
- Users never see or manage SSH keys
- Revoking Twingate access removes SSH access immediately (no key cleanup)
- Existing `authorized_keys` entries on servers are unaffected -- migration is incremental

**Certificate Authorities (managed under Settings > Certificate Authorities):**

| CA Type | Purpose | Required For |
|---|---|---|
| **X.509 CA** | Secures Twingate Client <-> Gateway link | Every Gateway |
| **SSH CA** | Issues user certs (auth to servers) + host certs (Gateway identity) | Every SSH Resource on the Gateway |

**SSH CA Signing Modes:**

| Mode | Where Private Key Lives | Recommended For |
|---|---|---|
| **Local SSH CA** | On the Gateway itself | Getting started, simple deployments |
| **HashiCorp Vault** | In Vault's SSH secrets engine | **Production** -- keys off-disk, full audit logging on cert ops |

**Supported SSH Features:**
- Interactive shell
- Remote command execution
- File transfer (sftp, rsync)
- TCP/IP port forwarding

**Not Supported:**
- X11 forwarding

**User Configuration -- SSH Auto-Sync:**
- Twingate Client option (under **More**) -> **SSH Server Configuration Auto-Sync**
- Syncs the SSH CA public key to `~/.ssh/known_hosts` so the Gateway's host cert is trusted automatically
- Without this: TOFU prompts on first connection

**Client Versions (minimum for IDFW SSH):**
- macOS: 2026.85
- Windows: 2026.90
- Linux: 2025.342
- Mobile (iOS, Android): **NOT supported** for IDFW SSH

**Session Recording:**
- All sessions automatically recorded
- Format: **asciicast v2**
- Output: Gateway's **stderr** stream
- **Stays on customer infrastructure** -- never uploaded to Twingate
- Capture: terminal I/O for interactive shells + command output + SSH events (channel open/close)
- **Not** captured: file transfer payloads, port forwarding data
- Replay: `twingate.com/sessionplayer` (paste log or upload), or any asciicast player (`asciinema play`)

**Vs. Bastion Host:**
- Replaces a bastion completely while adding identity propagation, session recording, and zero-trust access controls

**Vs. Smallstep CA Pattern (/docs/ssh-smallstep):**
- IDFW is the newer, integrated alternative -- recommended for new deployments
- Smallstep pattern still works but requires running and maintaining a separate CA

**Windows Server:**
- Supported with OpenSSH installed

**Related Docs:**
- /docs/identity-firewall -- IDFW overview
- /docs/ssh-installation -- Gateway deployment guides (AWS / DigitalOcean / GCE / Vault)
- /docs/ssh-remote-development -- VS Code / JetBrains / Cursor IDE setup
