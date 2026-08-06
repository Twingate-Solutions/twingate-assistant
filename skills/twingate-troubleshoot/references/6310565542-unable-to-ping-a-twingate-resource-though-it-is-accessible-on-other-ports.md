---
source: https://help.twingate.com/articles/6310565542-unable-to-ping-a-twingate-resource-though-it-is-accessible-on-other-ports
type: help
fetched: 2026-08-06
source_version: f9ffdf9e3c0299fd25e36e714d88d272a116e80bf453c55ed519a296ca3ffe45
---

# Unable to Ping a Twingate Resource (ICMP Failure)

## Summary
Linux kernels restrict ICMP Echo socket permissions by group ID. When `net.ipv4.ping_group_range` is set to the default `1 0`, no group can send ICMP packets through the Connector, causing ping failures even when TCP/UDP ports work normally.

## Key Information
- Affects Twingate Connector on Linux systems
- Default kernel value `net.ipv4.ping_group_range = 1 0` blocks all ICMP Echo sockets
- TCP/UDP resource access unaffected; only ICMP/ping fails
- Fix is a kernel-level sysctl change, applied differently per deployment method

## Prerequisites
- Connector deployed and functional on non-ICMP ports
- Sudo/root access to Connector host
- Identify deployment method: systemd, Docker, or LXC

## Step-by-Step

### systemd Deployment
1. Verify current value:
   ```bash
   sysctl net.ipv4.ping_group_range
   ```
2. If output is `1 0`, write fix to config:
   ```bash
   echo 'net.ipv4.ping_group_range = 0 2147483647' | sudo tee -a /etc/sysctl.conf
   ```
3. Apply changes:
   ```bash
   sudo sysctl -p
   ```

### Docker Deployment
Pass sysctl flag at container startup:
```bash
--sysctl net.ipv4.ping_group_range="0 2147483647"
```

### LXC Containers (e.g., Proxmox)
- Container **must be Privileged** to allow ICMP through the Connector
- Unprivileged LXC containers cannot be converted in-place; workaround:
  1. Back up the existing container
  2. Restore with **Privileged** selected in privilege level settings

## Configuration Values

| Parameter | Default (broken) | Fixed Value |
|-----------|-----------------|-------------|
| `net.ipv4.ping_group_range` | `1 0` | `0 2147483647` |

- Range format: `<min_gid> <max_gid>` (inclusive)
- `0 2147483647` allows all groups (GID 0 through max signed 32-bit int)

## Gotchas
- The default `1 0` is intentionally restrictive (min > max = no groups allowed)
- Docker: flag must be passed at container creation/run time, not post-deploy
- LXC: no in-place privilege upgrade; requires backup + restore workflow
- `sysctl -p` only reloads `/etc/sysctl.conf`; confirm the correct file for your distro (some use `/etc/sysctl.d/`)

## Related Docs
- Twingate Connector deployment (systemd)
- Twingate Connector deployment (Docker)
- Proxmox/LXC Connector setup