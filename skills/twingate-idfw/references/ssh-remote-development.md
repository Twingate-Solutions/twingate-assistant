# Remote Development with Twingate SSH and VS Code

## Summary
Configures VS Code Remote SSH extension to connect to private SSH Resources managed by Twingate. Enables full IDE functionality (IntelliSense, debugging, terminal) on remote VMs without public IPs, VPNs, or SSH key files.

## Key Information
- Uses VS Code's Remote-SSH extension against Twingate SSH Resources
- Twingate handles authentication via certificates; no SSH key management required
- SSH Config Auto-Sync eliminates TOFU prompts by pre-trusting the Gateway's CA

## Prerequisites
- Twingate Client installed and running (minimum version requirements apply)
- Privileged Access for SSH configured:
  - Gateway and Connector deployed in same network as target VM
  - SSH Resource configured and accessible to your user group
- VS Code with Remote-SSH extension (`ms-vscode-remote.remote-ssh`)

## Configuration Values
| Setting | Location | Value |
|---|---|---|
| SSH Server Configuration Auto-Sync | Twingate Client → More | Enable |
| Known hosts file updated | `~/.ssh/known_hosts` | Auto-populated by sync |

## Step-by-Step

### Enable SSH Config Sync
1. Open Twingate Client → **More**
2. Enable **SSH Server Configuration Auto-Sync**
3. Gateway CA public key syncs to `~/.ssh/known_hosts` automatically

### Connect via VS Code
1. Open VS Code
2. Install extension: `ms-vscode-remote.remote-ssh`
3. Open Command Palette (`Cmd+Shift+P` / `Ctrl+Shift+P`)
4. Run `Remote-SSH: Connect to Host`
5. Enter SSH Resource address (IP or hostname, e.g., `10.124.16.7` or `my-server.int`)
6. VS Code installs server component on remote VM (first connection only)
7. Click **Open Folder** → navigate to project directory

## Gotchas
- First connection is slow — VS Code installs its server component on the remote VM on initial connect
- SSH Config Auto-Sync must be enabled or you'll receive TOFU certificate trust prompts on each connection
- The Twingate Client must be running on the development machine before attempting SSH connections

## Related Docs
- [Privileged Access for SSH](https://www.twingate.com/docs/privileged-access-ssh) — architecture, CAs, session recording
- [Minimum version requirements](https://www.twingate.com/docs/client-versions)
- [User configuration](https://www.twingate.com/docs/ssh-user-configuration) — SSH config sync details
- SSH Resource setup and Gateway/Connector deployment