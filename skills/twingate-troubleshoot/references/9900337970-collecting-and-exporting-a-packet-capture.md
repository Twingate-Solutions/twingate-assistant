---
source: https://help.twingate.com/articles/9900337970-collecting-and-exporting-a-packet-capture
type: help
fetched: 2026-09-06
source_version: 0319f29f7aa9edcb3c4dcd017c779447f87959201dd81106ced2c2cd3f163c85
---

# Collecting and Exporting a Packet Capture

## Summary
Guide for capturing network traffic (PCAP) using Wireshark or tcpdump for troubleshooting Twingate networking issues. Covers both standard single captures and rolling captures for intermittent problems.

## Key Information
- Two tools supported: Wireshark (cross-platform GUI) and tcpdump (CLI, Linux/macOS)
- Rolling PCAPs are recommended for intermittent issues where reproduction steps are unclear
- Share **all** generated files with Twingate support; compress large files before sharing

## Prerequisites
- **Wireshark**: Download from [wireshark.org](https://www.wireshark.org/download.html)
- **tcpdump**: Pre-installed on macOS; Linux install via package manager

```bash
# Debian/Ubuntu
sudo apt-get install tcpdump

# RHEL/CentOS
sudo yum install tcpdump
```

## Step-by-Step

### Standard PCAP — tcpdump
```bash
sudo tcpdump -i any -s 0 -w $(hostname).cap
# Stop with Ctrl+C (Linux) or Cmd+C (macOS)
# Output: my_device.cap in current directory
```

### Rolling PCAP — tcpdump
```bash
sudo tcpdump -i any -s 0 -w $(hostname).cap -C 100 -W 5 -z root
# Creates up to 5 files × 100MB each
# Oldest file overwritten when all 5 are full
# Output files: my_device.cap* in current directory
```

### Standard PCAP — Wireshark
1. Open Wireshark → select all interfaces (click first, Shift+click last)
2. Press **Start** (top left)
3. Reproduce the issue
4. Press **Stop** (top left)
5. **File → Save As** → set type to `pcapng`

### Rolling PCAP — Wireshark
1. Select all interfaces
2. **Capture → Options → Output tab**
3. Set filename (e.g., `tg_pcaps`) and configure rolling settings:
   - **Use multiple files**: enabled
   - **Next file every**: 100 MB
   - **Ring buffer**: 5 files
4. Click **Start**
5. Press **Stop** when done — no manual save needed

## Configuration Values

| Parameter | tcpdump flag | Value |
|-----------|-------------|-------|
| Capture all interfaces | `-i any` | — |
| Full packet capture | `-s 0` | snaplen = 0 (unlimited) |
| Max file size (rolling) | `-C` | 100 MB |
| Max file count (rolling) | `-W` | 5 |
| Post-rotate command | `-z` | `root` |

## Gotchas
- Wireshark may show error popups about unsupported operations — accept and dismiss; capture will still start
- Rolling PCAP: share **all** generated files, not just the most recent
- tcpdump rolling output files are named with a numeric suffix (e.g., `my_device.cap0`, `my_device.cap1`)
- Run tcpdump from a directory where you have write access and sufficient disk space (up to 500MB for rolling captures)

## Related Docs
- Twingate Support contact (for sharing PCAPs)
- Wireshark Download: https://www.wireshark.org/download.html