```markdown
# Remote Development with Twingate SSH and VS Code

## Summary
Configures VS Code Remote SSH to connect to private SSH Resources via Twingate's Privileged Access for SSH — no public IP, no VPN, no key files required. The Twingate Client handles certificate trust automatically via SSH config sync, eliminating TOFU prompts.

## Key Information
- VS Code Remote SSH extension (`ms-vscode-remote.remote-ssh`) is the only IDE tooling required
- SSH Resources are accessed by IP or internal FQDN (e.g., `10.124.16.7` or `my-server.int`)
- First connection installs VS Code Server on the remote VM — takes a few extra seconds
- Full IntelliSense, debugging, and terminal access work once connected

## Prerequisites
- Twingate Client installed and running on the development machine (must meet minimum version requirements)
- Privileged Access for SSH fully configured:
  - Gateway and Connector deployed in the same network as the target VM
  - SSH Resource created and accessible to the user's group
- VS Code with Remote - SSH extension installed

## Step-by-Step

### Enable SSH Config Sync (one-time)
1. Open Twingate Client → **More**
2. Enable **SSH Server Configuration Auto-Sync**
3. This writes the Gateway's CA public key to `~/.ssh/known_hosts` automatically

### Connect via VS Code Remote SSH
1. Open VS Code
2. Open Command Palette (`Cmd+Shift+P` / `Ctrl+Shift+P`)
3. Run `Remote-SSH: Connect to Host`
4. Enter the SSH Resource address or alias
5. VS Code opens a remote window and installs its server component on first connect
6. Click **Open Folder** → navigate to project directory

## Configuration Values
| Setting | Location | Purpose |
|---|---|---|
| SSH Server Configuration Auto-Sync | Twingate Client → More | Syncs CA public key to `~/.ssh/known_hosts` |
| `ms-vscode-remote.remote-ssh` | VS Code extension ID | Required extension |

## Gotchas
- SSH config sync must be enabled **before** connecting — otherwise TOFU prompts will appear and the CA cert won't be trusted automatically
- First connection is slower than subsequent ones (VS Code Server installation on remote)
- This guide covers IDE setup only — the underlying Privileged Access for SSH infrastructure must already be operational

## Related Docs
- Privileged Access for SSH (architecture, CAs, session recording)
- User configuration (SSH config sync details)
- Minimum version requirements (Twingate Client)
```