# Remote Development with Twingate SSH and VS Code

## Summary
Configures VS Code Remote SSH to connect to private SSH Resources through Twingate without public IPs, VPNs, or key files. Requires Privileged Access for SSH to be fully configured before IDE setup. SSH config sync eliminates TOFU prompts by auto-trusting Gateway-issued certificates.

## Key Information
- Works with private SSH Resources (no public IP required)
- No SSH key files needed — certificates issued by the Gateway
- VS Code installs a server component on the remote VM on first connection (slight delay expected)
- Full IntelliSense, debugging, and terminal access available once connected

## Prerequisites
- Twingate Client installed and running (minimum version requirements must be met)
- Privileged Access for SSH configured:
  - Gateway and Connector deployed in same network as target VM
  - SSH Resource configured and accessible to your group
- VS Code with Remote - SSH extension (`ms-vscode-remote.remote-ssh`)

## Step-by-Step

### Enable SSH Config Sync
1. Open Twingate Client → **More**
2. Enable **SSH Server Configuration Auto-Sync**
3. Gateway's SSH CA public key syncs to `~/.ssh/known_hosts`

### Connect to Remote Host
1. Open VS Code
2. Install Remote - SSH extension if not present
3. Open Command Palette (`Cmd+Shift+P` / `Ctrl+Shift+P`)
4. Run `Remote-SSH: Connect to Host`
5. Enter SSH Resource address or alias (e.g., `10.124.16.7` or `my-server.int`)

### Open a Project
1. Click **Open Folder** in the VS Code welcome screen
2. Navigate to project directory on the remote VM

## Configuration Values
| Item | Value |
|------|-------|
| VS Code extension ID | `ms-vscode-remote.remote-ssh` |
| Known hosts file | `~/.ssh/known_hosts` |
| SSH config sync setting | **SSH Server Configuration Auto-Sync** (Twingate Client → More) |

## Gotchas
- **SSH config sync must be enabled** before connecting — without it, TOFU prompts will appear on each new host connection
- First connection is slower than subsequent ones (VS Code server installation on remote VM)
- This guide covers IDE setup only — Privileged Access for SSH (Gateway, Connector, Resource) must be configured separately before these steps work

## Related Docs
- Privileged Access for SSH (architecture, CAs, session recording)
- Minimum version requirements for Twingate Client
- User configuration (SSH config sync details)
- SSH setup guide (Gateway, Connector, Resource configuration)