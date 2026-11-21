---
source: https://www.twingate.com/docs/ssh-remote-development
type: docs
fetched: 2026-11-13
source_version: 025f3a5d7232d32fab696fe4ba668d131874f66352252fc93adb481dc420ef03
trust: official
---

# Remote Development with VS Code (Privileged Access for SSH)

## Summary
Explains how to use VS Code's Remote - SSH extension to work on a remote VM that is exposed as a private Twingate SSH Resource. No public IP, VPN, or key files are needed; authentication goes through Twingate Privileged Access for SSH.

## Key Information
- Remote host is a private SSH Resource reachable through the Twingate Client.
- VS Code Remote SSH lets you open remote folders and work as if they were local (IntelliSense, debugging, terminal).
- On first connection, VS Code installs its server component on the remote VM, which can take a few seconds.
- Enabling SSH Server Configuration Auto-Sync avoids Trust On First Use (TOFU) prompts.

## Prerequisites
- Twingate Client meeting the minimum version requirements, installed and running on the dev machine.
- Privileged Access for SSH set up:
  - Gateway and Connector deployed in the same network as the target VM.
  - SSH Resource configured and accessible to your group.
- VS Code with the `ms-vscode-remote.remote-ssh` extension (Remote - SSH).

## Step-by-Step
1. In the Twingate Client, go to **More** and enable **SSH Server Configuration Auto-Sync**. This syncs the SSH CA public key to `~/.ssh/known_hosts` so your SSH client trusts certificates issued by the Gateway.
2. Open VS Code and install **Remote - SSH** if not already installed.
3. Open the Command Palette (`Cmd+Shift+P` on macOS, `Ctrl+Shift+P` on Windows/Linux).
4. Run **Remote-SSH: Connect to Host**.
5. Enter the SSH Resource address or alias (e.g., `10.124.16.7` or `my-server.int`).
6. A new VS Code window opens connected to the remote host.
7. Click **Open Folder** and select the project directory on the remote VM.

## Configuration Values
- Extension ID: `ms-vscode-remote.remote-ssh`
- Known hosts file: `~/.ssh/known_hosts` (updated by Auto-Sync)
- Command Palette command: `Remote-SSH: Connect to Host`
- Client setting: **More > SSH Server Configuration Auto-Sync**

## Gotchas
- Without Auto-Sync, you may see TOFU host-key prompts.
- First connection is slower while the VS Code server installs on the VM.
- The address entered must match an SSH Resource your group has access to; the Twingate Client must be running.
- Gateway and Connector must be in the same network as the target VM.

## Related Docs
- Privileged Access for SSH (architecture, certificate authorities, session recording)
- Privileged Access for SSH setup guide
- User configuration (SSH config sync details)
- Twingate Client minimum version requirements