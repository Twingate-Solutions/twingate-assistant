# Remote Development with Twingate SSH and VS Code

## Summary
Configures VS Code Remote SSH for development against private SSH Resources protected by Twingate Privileged Access. No public IP, VPN, or SSH key files required. Relies on Twingate's certificate-based SSH auth and config sync.

## Key Information
- VS Code Remote SSH opens remote folders as if local, with full IntelliSense, debugging, and terminal
- Twingate handles authentication via certificates—no manual key management
- SSH config sync eliminates TOFU prompts by pre-trusting the Gateway's CA public key
- First connection has a delay while VS Code installs its server component on the remote VM

## Prerequisites
- Twingate Client installed and running (minimum version requirements met)
- Privileged Access for SSH configured:
  - Gateway and Connector deployed in same network as target VM
  - SSH Resource configured and accessible to your group
- VS Code with **Remote - SSH** extension (`ms-vscode-remote.remote-ssh`)

## Step-by-Step

### Enable SSH Config Sync (one-time)
1. Open Twingate Client → **More**
2. Enable **SSH Server Configuration Auto-Sync**
3. This writes the SSH CA's public key to `~/.ssh/known_hosts`

### Connect via VS Code
1. Open VS Code
2. Open Command Palette (`Cmd+Shift+P` / `Ctrl+Shift+P`)
3. Run `Remote-SSH: Connect to Host`
4. Enter SSH Resource address or alias (e.g., `10.124.16.7` or `my-server.int`)
5. VS Code opens new window connected to remote host

### Open a Project
1. Click **Open Folder** in welcome screen
2. Navigate to project directory on remote VM

## Configuration Values
| Item | Value/Location |
|------|---------------|
| VS Code extension ID | `ms-vscode-remote.remote-ssh` |
| SSH known_hosts path | `~/.ssh/known_hosts` |
| Config sync toggle | Twingate Client → More → SSH Server Configuration Auto-Sync |

## Gotchas
- **Config sync must be enabled** before connecting, or you'll get TOFU certificate trust prompts on first connection
- First connection is slower—VS Code installs a server component on the remote VM; subsequent connections are faster
- Remote host must be an SSH Resource configured in Twingate, not an arbitrary host

## Related Docs
- Privileged Access for SSH (architecture, CAs, session recording)
- SSH Minimum Version Requirements
- Privileged Access Setup Guide
- User Configuration (SSH config sync details)