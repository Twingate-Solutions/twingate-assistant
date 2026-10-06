---
source: https://help.twingate.com/articles/8310367817-linux-nixos-twingate-not-detecting-firewall-on-nixos
type: help
fetched: 2026-10-04
source_version: 30c27d9ea82354b2d67ca9ff95fb14f39253c2e5285a3850b1284565ac08d28d
trust: official
---

# [Linux - NixOS] Twingate Not Detecting Firewall on NixOS

## Summary
The Twingate Client cannot detect a firewall configured via NixOS's `networking.firewall` module, even though it uses `iptables` under the hood. To satisfy Twingate's device posture firewall check on NixOS, the native NixOS firewall must be disabled and `iptables` configured directly.

## Key Information
- **Affected component:** Twingate Client
- **Platform:** Linux (NixOS)
- **Root cause:** Twingate detects `iptables` directly; it does not recognize NixOS's `networking.firewall` abstraction layer, even though that abstraction uses `iptables` internally.

## Prerequisites
- Administrative/root access to the NixOS system
- Understanding of your organization's security policies before changing firewall rules
- `iptables` available on the system

## Firewall Requirements for Twingate Detection

All three conditions must be met:

| Requirement | Detail |
|---|---|
| `networking.firewall` disabled | NixOS native firewall module must be off |
| `iptables` installed | Must be explicitly present |
| `INPUT` chain default policy = `DROP` | Must be set at the `iptables` level |

## Step-by-Step

1. **Disable NixOS native firewall** in your NixOS configuration:
   ```nix
   networking.firewall.enable = false;
   ```

2. **Install `iptables`** (ensure it is present in your NixOS configuration):
   ```nix
   networking.nftables.enable = false;  # if applicable
   # ensure iptables package is available
   ```

3. **Set `INPUT` chain default policy to `DROP`** via `iptables`:
   ```bash
   iptables -P INPUT DROP
   ```
   Ensure all essential traffic (SSH, DNS, etc.) is explicitly **allowed** before applying this policy.

4. Rebuild and switch NixOS configuration:
   ```bash
   nixos-rebuild switch
   ```

## ⚠️ Gotchas

- **SSH lockout risk:** Setting `INPUT` policy to `DROP` without explicitly allowing SSH will cut off remote access. Add an `ACCEPT` rule for port 22 before applying.
- **DNS breakage:** DNS traffic must also be explicitly permitted.
- **Not a drop-in replacement:** Disabling `networking.firewall` removes NixOS-managed rules; you are fully responsible for recreating all needed rules in `iptables`.
- **NixOS rebuilds may reset rules:** Manage `iptables` rules persistently (e.g., via `networking.firewall = false` + a custom systemd service or `iptables-restore`).

## Configuration Values
- NixOS option to disable: `networking.firewall.enable = false`
- Required `iptables` policy: `INPUT` chain → `DROP`

## Related Docs
- [`iptables` man page (online)](https://linux.die.net/man/8/iptables)
- Local: `man iptables`
- Twingate Device Posture (firewall check) documentation — consult your Twingate admin portal