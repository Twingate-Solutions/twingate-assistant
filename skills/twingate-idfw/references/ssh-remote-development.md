---
source: https://www.twingate.com/docs/ssh-remote-development
type: docs
fetched: 2026-08-14
source_version: 39a2be8858fc1c3085ede54a3418bbdfd79568edea88d1e2750cd44e7ed1801a
---

# Remote Development with Twingate SSH and VS Code

## Summary
Configures VS Code Remote SSH extension to connect to private SSH Resources via Twingate without public IPs, VPNs, or key files. Requires Privileged Access for SSH to be pre-configured with Gateway, Connector, and SSH Resource.

## Key Information
- Remote development uses VS Code's Remote - SSH extension against Twingate SSH Resources
- No public IP, VPN, or SSH key files required on the client side
- SSH Config Auto-Sync eliminates TOFU prompts by pre-trusting the Gateway's CA public key
- First connection installs VS Code server component on remote VM (may take a few seconds)
- Full IntelliSense, debugging, and terminal access available once connected

## Prerequisites
- Twingate Client installed and running (minimum version requirements must be met)
- Privileged Access for SSH fully configured:
  - Gateway and Connector deployed in same network as target VM
  - SSH Resource configured and accessible to your group
- VS Code with Remote - SSH extension (`ms-vscode-remote.remote-ssh`)

## Step-by-Step

### Enable SSH Config Sync
1. Open Twingate Client → **More**
2. Enable **SSH Server Configuration Auto-Sync**
3. This syncs SSH CA public key to `~/.ssh/known_hosts` automatically

### Connect via VS Code Remote SSH
1. Open VS Code
2. Install extension `ms-vscode-remote.remote-ssh` if not present
3. Open Command Palette (`Cmd+Shift+P` macOS / `Ctrl+Shift+P` Windows/Linux)
4. Run `Remote-SSH: Connect to Host`
5. Enter SSH Resource address or alias (e.g., `10.124.16.7` or `my-server.int`)
6. Click **Open Folder** → navigate to project directory on remote VM

## Configuration Values
| Setting | Location | Value |
|---|---|---|
| SSH Config Auto-Sync | Twingate Client → More | Enable toggle |
| Known hosts file | Local machine | `~/.ssh/known_hosts` |
| VS Code extension ID | VS Code marketplace | `ms-vscode-remote.remote-ssh` |

## Gotchas
- SSH Config Auto-Sync must be enabled **before** first connection to avoid TOFU prompts; without it, SSH client won't automatically trust Gateway-issued certificates
- First connection is slower than subsequent connections due to VS Code server installation on the remote VM
- Gateway and Connector must be in the **same network** as the target VM — cross-network deployments won't work

## Related Docs
- [Privileged Access for SSH](https://www.twingate.com/docs/privileged-access-ssh) — architecture, CAs, session recording
- [SSH Setup Guide](https://www.twingate.com/docs/privileged-access-ssh#setup)
- [User Configuration / SSH Config Sync](https://www.twingate.com/docs/privileged-access-ssh#user-configuration)
- [Twingate Client minimum version requirements](https://www.twingate.com/docs/client-version-requirements)