---
source: https://help.twingate.com/articles/9900337970-collecting-and-exporting-a-packet-capture
type: help
fetched: 2026-10-28
source_version: 7e52ce1ae385ca731b2a579781716d3d037f22abcd9bc45c606678fbd1495fd8
trust: official
---

# Collecting and Exporting a Packet Capture

## Summary
Guide for capturing network traffic PCAPs using Wireshark or tcpdump for Twingate troubleshooting. Covers both standard captures and rolling captures for intermittent issues. PCAPs are shared with Twingate support for diagnosing network problems.

## Key Information
- Two tool options: **Wireshark** (GUI, cross-platform) or **tcpdump** (CLI, Linux/macOS)
- Two capture modes: **standard** (reproduce and stop) or **rolling** (background, bounded storage)
- Rolling PCAPs recommended when issues are intermittent or hard to reproduce
- Share **all** generated files with Twingate support; zip/compress large captures first

## Prerequisites
- **Wireshark**: Download from official Wireshark Download page (stable releases for macOS/Windows at top; Linux under "Third-Party Packages")
- **tcpdump**: Pre-installed on macOS and most Linux distros
  - Debian/Ubuntu: `sudo apt-get install tcpdump`
  - RHEL/CentOS: `sudo yum install tcpdump`

## Step-by-Step

### Wireshark — Standard Capture
1. Open Wireshark → select all interfaces (click first, Shift+click last)
2. Click **Start capture** (top left)
3. Reproduce the issue
4. Click **Stop capture**
5. **File → Save As** → name file, ensure `pcapng` format selected

### Wireshark — Rolling Capture
1. Select all interfaces → **Capture > Options > Output tab**
2. Set output folder and filename (e.g., `tg_pcaps`)
3. Configure rolling file settings (per Twingate support guidance)
4. Click **Start** → reproduce issue → click **Stop**
5. No manual save needed; files stored in configured folder

### tcpdump — Standard Capture
```bash
sudo tcpdump -i any -s 0 -w $(hostname).cap
```
Stop with `Ctrl+C` (Linux) or `Cmd+C` (macOS). Output: `<hostname>.cap` in current directory.

### tcpdump — Rolling Capture
```bash
sudo tcpdump -i any -s 0 -w $(hostname).cap -C 100 -W 5 -z root
```
Stop with `Ctrl+C` or by PID if backgrounded. Output: `<hostname>.cap*` series of files.

## Configuration Values (tcpdump Rolling Capture)

| Flag | Value | Meaning |
|------|-------|---------|
| `-i` | `any` | Capture all interfaces |
| `-s` | `0` | Full packet capture (no truncation) |
| `-C` | `100` | Max 100 MB per file |
| `-W` | `5` | Max 5 files (oldest overwritten when full) |
| `-z` | `root` | Post-rotation compression command |

**Max storage**: 5 × 100 MB = 500 MB total

## Gotchas
- Wireshark may show error popups on start — dismiss them; capture proceeds normally
- Rolling tcpdump creates files with pattern `hostname.cap0`, `hostname.cap1`, etc. — share **all** of them
- Zip/compress before sharing large PCAP sets

## Related Docs
- Wireshark Download: https://www.wireshark.org/download.html