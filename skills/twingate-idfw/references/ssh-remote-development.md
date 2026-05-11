# Remote Development with Twingate SSH and VS Code

## Summary
Configures VS Code Remote SSH extension to connect to private SSH Resources managed by Twingate. No public IP, VPN, or SSH key files required. Assumes Privileged Access for SSH is already configured.

## Key Information
- Uses VS Code's Remote - SSH extension (`ms-vscode-remote.remote-ssh`)
- Remote host is a Twingate SSH Resource (private IP or internal hostname)
- SSH config auto-sync eliminates TOFU prompts by pre-trusting the Gateway CA
- VS Code installs a server component on the remote VM on first connection (slight delay expected)
- Full IntelliSense, debugging, and terminal access available once connected

## Prerequisites
- Twingate Client installed and running (minimum version required — check version requirements doc)
- Privileged Access for SSH configured:
  - Gateway and Connector deployed in same network as target VM
  - SSH Resource configured and accessible to your group
- VS Code with Remote - SSH extension installed

## Step-by-Step

### Enable SSH Config Auto-Sync
1. Open Twingate Client → **More**
2. Enable **SSH Server Configuration Auto-Sync**
3. This syncs SSH CA public key to `~/.ssh/known_hosts` automatically

### Connect to Remote Host
1. Open VS Code
2. Install extension `ms-vscode-remote.remote-ssh` if not present
3. Open Command Palette (`Cmd+Shift+P` / `Ctrl+Shift+P`)
4. Run `Remote-SSH: Connect to Host`
5. Enter SSH Resource address (e.g., `10.124.16.7` or `my-server.int`)
6. VS Code opens new window; wait for server component installation on first connect

### Open a Project
1. Click **Open Folder** in the welcome screen
2. Navigate to project directory on remote VM

## Configuration Values
| Item | Value |
|------|-------|
| VS Code extension ID | `ms-vscode-remote.remote-ssh` |
| Auto-sync setting location | Twingate Client → More → SSH Server Configuration Auto-Sync |
| Known hosts file modified | `~/.ssh/known_hosts` |

## Gotchas
- Auto-sync must be enabled **before** connecting or TOFU prompts will appear on first connection
- First connection is slower — VS Code installs server components on the remote VM
- Gateway and Connector must be in the **same network** as the target VM (not just reachable)
- This guide covers IDE setup only; SSH architecture/CAs/session recording are in the Privileged Access for SSH doc

## Related Docs
- [Privileged Access for SSH](https://www.twingate.com/docs/privileged-access-ssh) — architecture, CAs, session recording
- Twingate Client minimum version requirements
- User configuration (SSH config sync details)