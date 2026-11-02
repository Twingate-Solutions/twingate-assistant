---
source: https://help.twingate.com/articles/8310367817-linux-nixos-twingate-not-detecting-firewall-on-nixos
type: help
fetched: 2026-11-01
source_version: 230bba40b3d80fad95fffb3d9f012059a2c4c06c511a3200676bb10bb9416208
trust: official
---

# [Linux - NixOS] Twingate Not Detecting Firewall on NixOS

## Summary
The Twingate Client cannot detect a firewall configured via NixOS's `networking.firewall`, even though it uses `iptables` as its backend. To satisfy Twingate's device posture firewall check on NixOS, you must disable `networking.firewall` and configure `iptables` directly.

## Key Information
- **Affected component:** Twingate Client
- **Platform:** Linux (NixOS)
- **Root cause:** Twingate detects `iptables` usage directly; it does not recognize NixOS's `networking.firewall` abstraction, even though that abstraction calls `iptables` internally
- **Impact:** Device posture firewall check fails when `networking.firewall` is the only firewall configured

## Prerequisites
- Access to NixOS system configuration
- Understanding of your organization's security policies
- Ability to test in a controlled/non-production environment before applying changes

## Firewall Requirements (for Twingate Detection)

Three conditions must all be met:

1. `networking.firewall` must be **disabled**
2. `iptables` must be **installed**
3. The `INPUT` chain's default policy must be set to **`DROP`**

## Configuration Steps

1. **Disable NixOS firewall abstraction** in your NixOS configuration:
   ```nix
   networking.firewall.enable = false;
   ```

2. **Ensure `iptables` is installed** (add to your NixOS packages or environment).

3. **Set the INPUT chain default policy to DROP** using `iptables` directly:
   ```bash
   iptables -P INPUT DROP
   ```
   Refer to `man iptables` or [linux.die.net/man/8/iptables](https://linux.die.net/man/8/iptables) for full policy configuration details.

## ⚠️ Gotchas

- **SSH lockout risk:** Setting `INPUT` policy to `DROP` without explicitly allowing SSH traffic (`port 22`) will block SSH access. Ensure SSH is explicitly permitted before applying the DROP policy.
- **DNS traffic:** DNS traffic may also be blocked. Explicitly allow required DNS ports.
- **Test first:** Always validate changes in a controlled environment before applying to production.
- **Not a drop-in replacement:** Disabling `networking.firewall` removes NixOS-managed rules; you must manually recreate all previously managed rules using `iptables`.

## Related Docs
- [iptables manual](https://linux.die.net/man/8/iptables)
- Twingate Device Posture documentation (Twingate Help Center)