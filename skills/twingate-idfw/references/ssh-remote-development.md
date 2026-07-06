# Remote Development with Twingate SSH and VS Code

## Summary
Configure VS Code Remote SSH extension to connect to private SSH Resources protected by Twingate. Eliminates need for public IPs, VPNs, or SSH key files by leveraging Twingate's Privileged Access SSH infrastructure.

## Key Information
- Uses VS Code's Remote-SSH extension (`ms-vscode-remote.remote-ssh`)
- Remote host is a private Twingate SSH Resource (no public IP required)
- Full IntelliSense, debugging, and terminal access available once connected
- First connection installs VS Code server component on remote VM (takes a few seconds)

## Prerequisites
- Twingate Client installed and running (meeting minimum version requirements)
- Privileged Access for SSH configured:
  - Gateway and Connector deployed in same network as target VM
  - SSH Resource configured and accessible to your group
- VS Code with Remote-SSH extension installed

## Step-by-Step

### Enable SSH Config Sync
1. Open Twingate Client → **More**
2. Enable **SSH Server Configuration Auto-Sync**
3. This syncs SSH CA public key to `~/.ssh/known_hosts`, avoiding TOFU prompts

### Connect to Remote Host
1. Open VS Code
2. Install extension: `ms-vscode-remote.remote-ssh`
3. Open Command Palette (`Cmd+Shift+P` macOS / `Ctrl+Shift+P` Windows/Linux)
4. Type and select `Remote-SSH: Connect to Host`
5. Enter SSH Resource address or alias (e.g., `10.124.16.7` or `my-server.int`)

### Open a Project
1. Click **Open Folder** in VS Code welcome screen
2. Navigate to project directory on remote VM

## Configuration Values
| Item | Value |
|------|-------|
| VS Code Extension ID | `ms-vscode-remote.remote-ssh` |
| SSH known_hosts path | `~/.ssh/known_hosts` |
| Twingate setting | SSH Server Configuration Auto-Sync (under More) |

## Gotchas
- SSH Config Sync must be enabled to avoid Trust On First Use (TOFU) prompts on each connection
- Gateway and Connector must be deployed in the **same network** as the target VM
- First connection has extra latency due to VS Code server installation on remote VM

## Related Docs
- [Privileged Access for SSH](https://www.twingate.com/docs/privileged-access-ssh) — architecture, CAs, session recording
- [Minimum version requirements](https://www.twingate.com/docs/client-requirements)
- [User configuration](https://www.twingate.com/docs/ssh-user-configuration) — SSH config sync details