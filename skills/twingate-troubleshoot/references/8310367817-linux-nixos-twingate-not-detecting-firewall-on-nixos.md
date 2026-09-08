---
source: https://help.twingate.com/articles/8310367817-linux-nixos-twingate-not-detecting-firewall-on-nixos
type: help
fetched: 2026-09-06
source_version: 15116114b28cbc83e34432d5c79fc6b1c719b5365e6c053986def86da33026b9
---

# [Linux - NixOS] Twingate Not Detecting Firewall on NixOS

## Summary
The Twingate Client cannot detect NixOS's native firewall when configured via `networking.firewall`, even though NixOS uses `iptables` as its backend. To satisfy Twingate's device posture firewall check, `networking.firewall` must be disabled and `iptables` configured directly.

## Key Information
- **Component**: Twingate Client
- **Platform**: Linux (NixOS)
- **Issue**: Twingate detects `iptables` as its supported firewall mechanism, but cannot recognize NixOS's abstraction layer (`networking.firewall`) over `iptables`

## Prerequisites
- Access to NixOS system configuration
- Ability to modify `configuration.nix`
- Understanding of your organization's security policies before making changes

## Firewall Requirements for Twingate Detection

All three conditions must be met:

1. `networking.firewall` must be **disabled**
2. `iptables` must be **installed**
3. The `INPUT` chain's default policy must be set to **`DROP`**

## Configuration Steps

1. **Disable NixOS native firewall** in `configuration.nix`:
   ```nix
   networking.firewall.enable = false;
   ```

2. **Ensure `iptables` is installed** (add to system packages if needed):
   ```nix
   environment.systemPackages = with pkgs; [ iptables ];
   ```

3. **Set INPUT chain default policy to DROP** via `iptables`:
   ```bash
   iptables -P INPUT DROP
   ```
   Or configure this persistently through NixOS (e.g., using `networking.nftables` or custom scripts).

## Configuration Values
| Parameter | Required Value |
|-----------|---------------|
| `networking.firewall.enable` | `false` |
| `iptables` INPUT chain policy | `DROP` |

## Gotchas
- ⚠️ Setting `INPUT` policy to `DROP` **will block all inbound traffic by default** — explicitly allow SSH, DNS, and other essential traffic before applying
- Test changes in a controlled environment before production deployment
- NixOS rebuilds may reset `iptables` rules; ensure rules are applied persistently
- Simply having `iptables` installed is insufficient — the INPUT chain policy must explicitly be `DROP`

## Reference Links
- [`iptables` man page](https://linux.die.net/man/8/iptables)
- Local: `man iptables`

## Related Docs
- Twingate Device Posture (firewall checks)
- NixOS `networking.firewall` documentation
- NixOS `iptables` persistence configuration