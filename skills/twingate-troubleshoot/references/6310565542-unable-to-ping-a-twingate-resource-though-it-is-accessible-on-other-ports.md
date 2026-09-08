---
source: https://help.twingate.com/articles/6310565542-unable-to-ping-a-twingate-resource-though-it-is-accessible-on-other-ports
type: help
fetched: 2026-09-06
source_version: 300d8b6d88f2e7ed4eaaef4136f7ff4d3e0ede012fd77cbc04eabef5e023db92
---

# Unable to Ping a Twingate Resource (ICMP Fails, Other Ports Work)

## Summary
Linux kernels restrict ICMP Echo socket creation by group ID. The default `net.ipv4.ping_group_range="1 0"` blocks all groups, preventing the Twingate Connector from sending ping/ICMP packets even when TCP/UDP connections work normally.

## Key Information
- Affects only ICMP/ping; TCP/UDP connections to the resource work fine
- Issue is at kernel level via `sysctl`, not Twingate configuration
- Applies to systemd deployments, Docker containers, and LXC containers
- Default value `1 0` means **no group** is permitted to create ICMP Echo sockets

## Prerequisites
- Twingate Connector deployed and functioning (non-ICMP ports accessible)
- sudo/root access on Connector host

## Step-by-Step

### Verify the Issue
```bash
sysctl net.ipv4.ping_group_range
# If output is "1 0", apply fix below
```

### Fix: systemd Deployment
```bash
# Persist setting to config file
echo 'net.ipv4.ping_group_range = 0 2147483647' | sudo tee -a /etc/sysctl.conf

# Apply immediately without reboot
sudo sysctl -p
```

### Fix: Docker Deployment
Pass sysctl at container startup:
```bash
--sysctl net.ipv4.ping_group_range="0 2147483647"
```

### Fix: LXC Containers (Proxmox, etc.)
- Container **must be Privileged** — unprivileged LXC containers cannot grant ping access
- If container is currently unprivileged:
  1. Create a backup
  2. Restore with **Privileged** selected in privilege level settings

## Configuration Values

| Parameter | Value | Meaning |
|-----------|-------|---------|
| `net.ipv4.ping_group_range` | `1 0` (default) | No groups allowed |
| `net.ipv4.ping_group_range` | `0 2147483647` | All groups allowed |

- Config file path: `/etc/sysctl.conf`

## Gotchas
- The default value `1 0` is intentionally inverted (min > max) to represent an empty range — this is not a typo
- Docker containers require the flag at **deploy time**; it cannot be applied to a running container without restart
- LXC unprivileged containers cannot be converted in-place — backup/restore required to change privilege level
- `sysctl -p` applies changes immediately but changes only persist across reboots if written to `/etc/sysctl.conf`

## Related Docs
- Twingate Connector deployment documentation
- Linux `sysctl(8)` man page
- Docker `--sysctl` runtime flag documentation