---
source: https://help.twingate.com/articles/9900337970-collecting-and-exporting-a-packet-capture
type: help
fetched: 2026-10-04
source_version: 068d90d2427ea83a6d64be70326031fb7b42a81b5bdae58f7a9a4bffdd887cea
trust: official
---

# Collecting and Exporting a Packet Capture

## Summary
Guide for capturing network packet traces (PCAPs) for Twingate troubleshooting using Wireshark or tcpdump. Covers both single captures and rolling captures for intermittent issues.

## Key Information
- Two tool options: Wireshark (GUI, cross-platform) or tcpdump (CLI, Linux/macOS)
- Rolling PCAPs useful for intermittent issues; limit storage while capturing continuously
- Share **all** generated PCAP files with Twingate support, not just the latest

## Prerequisites
- **Wireshark**: Download from official Wireshark Download page (stable release)
- **tcpdump**: Pre-installed on macOS and most Linux distros
  - Debian/Ubuntu: `sudo apt-get install tcpdump`
  - RHEL/CentOS: `sudo yum install tcpdump`

## Step-by-Step

### Wireshark — Single Capture
1. Open Wireshark
2. Select all interfaces (click first, Shift+click last)
3. Click Start capture button (top left)
4. Reproduce the issue
5. Click Stop capture button
6. `File → Save As` → name file → ensure `pcapng` format selected

### tcpdump — Single Capture
```bash
sudo tcpdump -i any -s 0 -w $(hostname).cap
```
Stop with `Ctrl+C` (Linux) or `Cmd+C` (macOS). Output: `<hostname>.cap` in current directory.

### Wireshark — Rolling Capture
1. Select all interfaces
2. `Capture → Options → Output tab`
3. Set filename (e.g., `tg_pcaps`), enable rolling file settings:
   - **File size**: 100 MB per file
   - **Number of files**: 5
4. Click Start → Stop when done (no manual save needed)

### tcpdump — Rolling Capture
```bash
sudo tcpdump -i any -s 0 -w $(hostname).cap -C 100 -W 5 -z root
```
Stop with `Ctrl+C` or via PID if backgrounded.

## Configuration Values

| Flag | Value | Meaning |
|------|-------|---------|
| `-i any` | `any` | Capture all interfaces |
| `-s 0` | `0` | Full packet snaplen |
| `-C` | `100` | Max file size (MB) per rolling file |
| `-W` | `5` | Max number of rolling files |
| `-z root` | `root` | Post-rotation compression command |

## Gotchas
- Wireshark may show error popups about unsupported operations — dismiss them; capture proceeds normally
- Rolling tcpdump overwrites oldest file once all 5 slots are full (circular buffer)
- Compress files before sharing if PCAPs are large (zip recommended)
- Run tcpdump from a directory with sufficient disk space (up to 500 MB for rolling captures)
- `-z root` in tcpdump rolling captures invokes root for post-rotation; verify this is acceptable in your environment

## Related Docs
- Twingate Support (for sharing PCAPs)
- Wireshark official download page