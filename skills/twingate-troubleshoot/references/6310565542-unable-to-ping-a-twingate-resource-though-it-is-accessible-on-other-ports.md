---
source: https://help.twingate.com/articles/6310565542-unable-to-ping-a-twingate-resource-though-it-is-accessible-on-other-ports
type: help
fetched: 2026-10-04
source_version: 3aff4f47fc56ebbbefc06fbc40acbb99fa341fe8e9f4659f8479dbee973b3278
trust: official
---

# Unable to Ping a Twingate Resource (ICMP Fails, Other Ports Work)

## Summary
On some Linux distributions, kernel-level permissions restrict ICMP Echo socket creation by group ID. The default `net.ipv4.ping_group_range="1 0"` blocks all groups, preventing ping through the Twingate Connector even when TCP/UDP ports work normally.

## Key Information
- Issue is OS-level, not Twingate-specific
- Default `ping_group_range = 1 0` means **no group** is permitted to send ICMP Echo
- Fix requires setting an inclusive min/max group ID range via `sysctl`
- Affects Connector component only

## Symptoms
- Resource accessible on expected ports (TCP/UDP)
- Ping/ICMP to resource fails through Twingate
- Direct ping from Connector host succeeds

## Prerequisites
- `sudo` access on the Connector host
- Know your Connector deployment method: systemd, Docker, or LXC

---

## Resolution by Deployment Type

### systemd Connector
1. **Verify current value:**
   ```bash
   sysctl net.ipv4.ping_group_range
   ```
2. **If output is `1 0`, persist the fix:**
   ```bash
   echo 'net.ipv4.ping_group_range = 0 2147483647' | sudo tee -a /etc/sysctl.conf
   ```
3. **Apply immediately:**
   ```bash
   sudo sysctl -p
   ```

### Docker Connector
Pass the sysctl flag at container startup:
```bash
--sysctl net.ipv4.ping_group_range="0 2147483647"
```

### LXC Container (e.g., Proxmox)
- Container **must be Privileged** to allow ICMP through the Connector
- If currently unprivileged: back up the container, then restore selecting **Privileged** for privilege level

---

## Configuration Values
| Parameter | Value | Meaning |
|---|---|---|
| `net.ipv4.ping_group_range` | `0 2147483647` | Allow all groups to send ICMP Echo |
| Default value | `1 0` | No group allowed (blocks ping) |

---

## Gotchas
- `tee -a` appends to `/etc/sysctl.conf`; verify no duplicate entries if run multiple times
- Docker: flag must be added at container creation/run time, not patched into a running container
- LXC unprivileged → privileged conversion requires a backup/restore cycle; there is no in-place toggle
- Change applies per-host; each Connector host must be configured independently

## Related Docs
- Twingate Connector deployment guides (systemd, Docker)
- Proxmox LXC container privilege documentation