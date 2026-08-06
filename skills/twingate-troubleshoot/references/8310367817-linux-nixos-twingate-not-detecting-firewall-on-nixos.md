---
source: https://help.twingate.com/articles/8310367817-linux-nixos-twingate-not-detecting-firewall-on-nixos
type: help
fetched: 2026-08-06
source_version: fbdb401f24d79376e4a4ba008b220a077007be75f5b901e93c1b1bcff6f17ab0
---

# [Linux - NixOS] Twingate Not Detecting Firewall on NixOS

## Summary
The Twingate Client cannot detect firewall configuration on NixOS when `networking.firewall` is used, even though it uses `iptables` in the backend. To enable device posture firewall checks, NixOS's built-in firewall must be disabled and `iptables` configured directly.

## Key Information
- **Affected component:** Twingate Client
- **Platform:** Linux (NixOS) only
- **Issue:** Twingate Client does not recognize `networking.firewall` as a valid firewall for device posture checks
- **Root cause:** NixOS abstracts `iptables` through `networking.firewall`; Twingate cannot detect this abstraction layer

## Prerequisites
- NixOS system with Twingate Client installed
- Administrative access to modify NixOS configuration
- Review of organization security policies before making changes

## Requirements to Fix

Three conditions must ALL be met for Twingate to detect the firewall:

1. `networking.firewall` must be **disabled**
2. `iptables` must be **installed**
3. `INPUT` chain default policy must be set to **DROP**

## Configuration Steps

1. Disable NixOS built-in firewall in `/etc/nixos/configuration.nix`:
   ```nix
   networking.firewall.enable = false;
   ```

2. Install `iptables` via NixOS configuration or ensure it is available

3. Set `INPUT` chain default policy to `DROP`:
   ```bash
   iptables -P INPUT DROP
   ```

4. Rebuild NixOS configuration:
   ```bash
   nixos-rebuild switch
   ```

## ⚠️ Gotchas

- **SSH lockout risk:** Setting `INPUT` policy to `DROP` without explicitly allowing SSH will block remote access — ensure port 22 (or your SSH port) is allowed before applying
- **DNS breakage:** DNS traffic must be explicitly allowed or resolution will fail
- **Essential services:** All required traffic must have explicit ALLOW rules before switching to a DROP default policy
- Always test in a controlled environment before applying to production systems
- Changes are not automatically persistent across reboots unless configured in NixOS declarative config or a startup script

## Related Docs
- [iptables man page](https://linux.die.net/man/8/iptables)
- `man iptables` (local system reference)
- Twingate device posture / firewall check documentation