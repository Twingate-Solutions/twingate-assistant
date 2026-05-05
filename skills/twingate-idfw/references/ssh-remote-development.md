## Remote Development with Twingate SSH (VS Code)

How to use VS Code Remote SSH against private SSH Resources reached through the Twingate Gateway -- no public IP, no VPN, no SSH key files.

**Prerequisites:**
- Twingate Client installed and running, meeting minimum versions for IDFW SSH:
  - macOS: 2026.85
  - Windows: 2026.90
  - Linux: 2025.342
- Privileged Access for SSH already deployed (Gateway + Connector + SSH Resource configured)
- User has Group access to the SSH Resource

**SSH Server Configuration Auto-Sync (do this first):**
- Open the Twingate Client -> **More** menu -> enable **SSH Server Configuration Auto-Sync**
- Syncs the SSH CA's public key into `~/.ssh/known_hosts` automatically
- Result: no Trust-On-First-Use (TOFU) prompts when connecting -- the Gateway's host certificates are pre-trusted
- Without this: OpenSSH shows a TOFU warning on the first connection to each host

**VS Code Steps:**
1. Install the **Remote - SSH** extension (`ms-vscode-remote.remote-ssh`)
2. Command Palette: `Cmd+Shift+P` (macOS) / `Ctrl+Shift+P` (Windows/Linux)
3. Run **Remote-SSH: Connect to Host**
4. Enter the SSH Resource address -- private IP (`10.124.16.7`) or alias/FQDN (`my-server.int`)
5. VS Code opens a new window connected to the remote host
   - First connection: VS Code installs its server component on the remote VM (a few seconds)
6. Click **Open Folder** -> navigate to the project directory
7. IntelliSense, debugging, and integrated terminal all work as if local

**Why It Works Seamlessly:**
- Twingate Client routes SSH traffic to the in-environment Gateway
- Gateway authenticates the user via the IdP (no SSH keys on the dev machine)
- Gateway issues a short-lived cert per connection to authenticate to the target host
- VS Code Remote SSH sees a normal SSH endpoint -- no VS Code-specific config required

**Other Supported IDEs (per /docs/ssh-privileged-access-overview):**
- JetBrains Gateway
- Cursor
- Any tool that uses standard `ssh` works (rsync, sftp, custom CLIs)

**Gotchas:**
- Skipping SSH Auto-Sync results in TOFU prompts that may be incorrectly accepted by users -- always enable
- VS Code's remote server requires a writable home dir on the target -- ensure the user account has one
- File transfer (sftp) and TCP port forwarding work; X11 forwarding does NOT (per IDFW SSH limitations)

**Related Docs:**
- /docs/ssh-privileged-access-overview -- IDFW SSH overview
- /docs/ssh-installation -- Gateway deployment
- /docs/identity-firewall -- IDFW concept overview
