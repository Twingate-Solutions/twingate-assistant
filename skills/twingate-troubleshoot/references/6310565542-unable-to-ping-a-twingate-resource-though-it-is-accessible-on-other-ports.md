---
source: https://help.twingate.com/articles/6310565542-unable-to-ping-a-twingate-resource-though-it-is-accessible-on-other-ports
type: help
fetched: 2026-11-01
source_version: 7a695d1dd84f4c03aa0446286da8cfd9b539d77b542e49d245b98f42b0f3dd97
trust: official
---

# Unable to Ping a Twingate Resource (ICMP Fails, Other Ports Work)

## Summary
On some Linux distributions, kernel-level restrictions prevent ICMP Echo socket creation based on group ID. This causes ping to fail through a Twingate Connector even when TCP/UDP connections to the same resource succeed. The fix requires adjusting `net.ipv4.ping_group_range` via sysctl.

## Key Information
- Affects: Twingate Connector (Linux deployments)
- Root cause: `net.ipv4.ping_group_range` defaults to `1 0` (no group permitted to send ICMP Echo)
- Symptom confirmation: Ping works directly from the Connector host's SSH/terminal but fails through Twingate

## Prerequisites
- Connector deployed via systemd or Docker
- sudo/root access on Connector host

## Step-by-Step

### Systemd Connector

1. **Check current value:**
   ```bash
   sysctl net.ipv4.ping_group_range
   ```

2. **If output shows `1 0`, persist the fix:**
   ```bash
   echo 'net.ipv4.ping_group_range = 0 2147483647' | sudo tee -a /etc/sysctl.conf
   ```

3. **Apply immediately:**
   ```bash
   sudo sysctl -p
   ```

### Docker Connector

Pass the sysctl flag at container startup:
```
--sysctl net.ipv4.ping_group_range="0 2147483647"
```

## Configuration Values

| Setting | Default (broken) | Fixed value |
|---|---|---|
| `net.ipv4.ping_group_range` | `1 0` | `0 2147483647` |

- `0 2147483647` = all group IDs allowed to create ICMP Echo sockets

## Gotchas

- **LXC containers (e.g., Proxmox):** Must be a **Privileged** container. Unprivileged LXC containers cannot grant ping access regardless of sysctl settings.
  - Workaround: Backup unprivileged container → restore as Privileged, selecting "Privileged" in privilege level settings.
- The `tee -a` command appends to `/etc/sysctl.conf`; running it multiple times will add duplicate entries.
- Docker containers require the flag at deploy time; existing containers must be redeployed.

## Related Docs
- Twingate Connector deployment (systemd and Docker)
- Proxmox LXC container configuration