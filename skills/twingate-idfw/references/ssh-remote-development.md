# Remote Development with Twingate SSH and VS Code

## Summary
Configures VS Code Remote SSH extension to connect to private SSH Resources managed by Twingate Privileged Access. Enables full IDE functionality (IntelliSense, debugging, terminal) on remote VMs without public IPs, VPNs, or SSH key files.

## Key Information
- Uses VS Code Remote SSH extension (`ms-vscode-remote.remote-ssh`)
- Remote host is a private Twingate SSH Resource (no public IP required)
- SSH config sync eliminates TOFU prompts by auto-trusting Gateway-issued certificates
- First connection installs VS Code server component on remote VM (brief delay expected)

## Prerequisites
- Twingate Client installed and running (must meet minimum version requirements)
- Privileged Access for SSH configured:
  - Gateway and Connector deployed in same network as target VM
  - SSH Resource configured and accessible to your group
- VS Code with Remote - SSH extension installed

## Step-by-Step

### Enable SSH Config Sync (one-time setup)
1. Open Twingate Client → **More**
2. Enable **SSH Server Configuration Auto-Sync**
3. Syncs SSH CA public key to `~/.ssh/known_hosts` automatically

### Connect to Remote Host
1. Open VS Code
2. Install extension `ms-vscode-remote.remote-ssh` if not present
3. Open Command Palette (`Cmd+Shift+P` / `Ctrl+Shift+P`)
4. Run **Remote-SSH: Connect to Host**
5. Enter SSH Resource address or alias (e.g., `10.124.16.7` or `my-server.int`)
6. Wait for VS Code server installation on first connect

### Open a Project
1. Click **Open Folder** in VS Code welcome screen
2. Navigate to project directory on remote VM

## Configuration Values
| Item | Value/Location |
|------|----------------|
| Known hosts file | `~/.ssh/known_hosts` |
| SSH config sync setting | Twingate Client → More → SSH Server Configuration Auto-Sync |
| VS Code extension ID | `ms-vscode-remote.remote-ssh` |

## Gotchas
- SSH config sync must be enabled **before** connecting to avoid TOFU certificate trust prompts
- First connection is slower due to VS Code server component installation on remote VM
- Gateway and Connector must be in the **same network** as the target VM

## Related Docs
- [Privileged Access for SSH](https://www.twingate.com/docs/privileged-access-ssh) — architecture, certificate authorities, session recording
- [Minimum version requirements](https://www.twingate.com/docs/client-requirements)
- [SSH setup guide](https://www.twingate.com/docs/ssh-setup)
- [User configuration](https://www.twingate.com/docs/ssh-user-configuration)