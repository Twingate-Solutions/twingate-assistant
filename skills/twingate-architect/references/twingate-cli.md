---
source: https://www.twingate.com/docs/twingate-cli
type: docs
fetched: 2026-11-22
source_version: 53f2ab25a64df20ab02f7fe85f64a6832ea62e3b13e29a5bd33ddd68d4dc1f0d
trust: official
---

# Twingate CLI

## Summary
The `twingate` command ships with the Twingate Client on macOS, Windows, and Linux and controls the same Client as the desktop app. It handles connecting, account management, Resource listing and auth, Exit Networks, Client settings, and updates. It replaces the classic Linux commands (`setup`, `start`, `stop`, `resources`).

## Key Information
- No separate install. Installing the Client provides the CLI. Verify with `twingate --version`.
- macOS CLI path: `/usr/local/bin/twingate`.
- Changes made in the CLI also show up in the desktop app.
- Commands: `connect`, `disconnect`, `status`, `resource list|auth|sync`, `account add|list|switch|remove`, `config ...`, `exit-network list|set|off|status`, `update`, `completion`, `help`.
- Data commands (`status`, `resource list`, `account list`, `exit-network list`) accept `-o/--output text|json` and `-v/--verbose`. Use `json` in scripts, because the text format can change between versions.
- Global options: `-h/--help`, `-V/--version`.
- `twingate account add [NETWORK | FILE]` takes a slug (`acme`), a full network name, or a service key file. With no argument, it reads a service key from stdin.
- `twingate account switch|remove <ACCOUNT>` accepts a slug, a full name, or a short ID. Use the short ID from `account list` when several accounts share a network.
- `resource auth <RESOURCE>` accepts a name, address, or alias. Use it when a Security Policy requires re-authentication.
- `resource sync [RESOURCE] [--type kube|ssh]` syncs Kubernetes and SSH Resources once, on demand.
- `resource list --all` includes background Resources.
- `update --check` only checks for an update without installing.
- Exit Networks require the Enterprise plan. Quote names that contain spaces.

## Prerequisites
- Twingate Client installed.
- For headless use, a Service Account and service key.
- Shell completion requires PowerShell 7+ on Windows.

## Configuration Values
`twingate config <setting> [true|false]` prints the current value when no value is given.
- `collect-detailed-logs`: debug-level logs, for troubleshooting with support.
- `share-crash-report`
- `enable-local-telemetry`
- `ssh`: automatic SSH Resource sync.
- `kube`: automatic Kubernetes kubeconfig sync.
- `tun [true|false]` (Linux only)
- `http-proxy [IP:PORT|off]` (Linux only). Prints `(disabled)` when off.

Shell completion lines (`twingate completion [bash|zsh|powershell]` prints the setup steps and changes no files):
- bash (`~/.bashrc`): `source <(COMPLETE=bash twingate)`
- zsh (`~/.zshrc`): `autoload -Uz compinit && compinit`, then `source <(COMPLETE=zsh twingate)`
- PowerShell (`$PROFILE`): `$env:COMPLETE = "powershell"; twingate | Out-String | Invoke-Expression; Remove-Item Env:\COMPLETE`

## Step-by-Step: Headless device with a service key
1. `twingate account add ./service-key.json`
2. `twingate connect`
3. `twingate resource list --output json`

## Step-by-Step: Switch Linux from TUN to HTTP Proxy only
1. `twingate config http-proxy 127.0.0.1:9999`
2. `twingate config tun false`
3. `twingate connect`

## Gotchas
- On Linux, `tun` and `http-proxy` changes take effect only after the next `twingate connect`.
- At least one Linux mode must stay on, so enable the proxy before disabling TUN.
- A proxy listening on `0.0.0.0` accepts connections from any host that can reach the device. Use `127.0.0.1` unless other hosts need it.
- TUN mode requires root. HTTP Proxy Mode does not, but applications must be configured to use the proxy.
- A service key grants access to every Resource assigned to its Service Account. Keep it in a secrets manager, not in source control.
- In scripts, check that `state` is `Connected` in `status --output json` before running commands that depend on Resources.
- `auth_expires_at` is a Unix timestamp in seconds, or `null`.
- Turn off detailed logs after troubleshooting.

## Related Docs
- Linux Client (https://www.twingate.com/docs/linux): classic commands
- Twingate Client (https://www.twingate.com/docs/clients)
- Security Policies (https://www.twingate.com/docs/security-policies)
- Headless Clients (https://www.twingate.com/docs/services-headless-clients)
- Exit Networks (https://www.twingate.com/docs/exit-networks)
- Userspace Networking (https://www.twingate.com/docs/linux-userspace-networking)
- Kubeconfig Sync (https://www.twingate.com/docs/kubernetes-kubeconfig-sync)
- Privileged Access for SSH (https://www.twingate.com/docs/ssh-privileged-access-overview)
- Troubleshooting (https://www.twingate.com/docs/how-to-troubleshoot)