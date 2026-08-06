---
source: https://help.twingate.com/articles/9900337970-collecting-and-exporting-a-packet-capture
type: help
fetched: 2026-08-06
source_version: 1215d9395444c73baa1fb2bfc937f490ab99590e156c5b4c3f12fa0fa88941a7
---

# Collecting and Exporting a Packet Capture

## Summary
Guide for capturing network traffic using Wireshark or tcpdump for Twingate troubleshooting. Covers both standard single captures and rolling captures for intermittent issues. Rolling captures limit storage usage while continuously recording traffic.

## Key Information
- Two capture tools supported: Wireshark (GUI, cross-platform) and tcpdump (CLI, Linux/macOS)
- tcpdump comes pre-installed on macOS and most Linux distributions
- Rolling PCAPs overwrite oldest data when storage limit reached
- Share **all** generated files when submitting rolling PCAPs to support

## Prerequisites
- Wireshark: Download from official site; stable releases for macOS/Windows at top of page, Linux packages under "Third-Party Packages"
- tcpdump on Debian: `sudo apt-get install tcpdump`
- tcpdump on RPM: `sudo yum install tcpdump`

## Step-by-Step

### Wireshark — Standard Capture
1. Start Wireshark
2. Select all interfaces (click first, Shift+click last)
3. Click start capture button (top left)
4. Reproduce the issue
5. Click stop capture button (top left)
6. `File → Save As` → name file → ensure `pcapng` selected as type

### tcpdump — Standard Capture
```bash
sudo tcpdump -i any -s 0 -w $(hostname).cap
```
Stop with `Ctrl+C` (Linux) or `Cmd+C` (macOS). Output file: `<hostname>.cap` in current directory.

### Wireshark — Rolling Capture
1. Select all interfaces
2. `Capture → Options → Output tab`
3. Set filename (e.g., `tg_pcaps`) and destination folder
4. Configure rolling file settings (per Twingate support guidance)
5. Click **Start** (bottom right)
6. Stop with stop button; no manual save needed

### tcpdump — Rolling Capture
```bash
sudo tcpdump -i any -s 0 -w $(hostname).cap -C 100 -W 5 -z root
```
Stop with `Ctrl+C` or by PID if backgrounded.

## Configuration Values

| Flag | Value | Description |
|------|-------|-------------|
| `-i` | `any` | Capture all interfaces |
| `-s` | `0` | Full packet capture (no truncation) |
| `-w` | `$(hostname).cap` | Output filename |
| `-C` | `100` | Max file size in MB (rolling) |
| `-W` | `5` | Max number of files (rolling) |
| `-z` | `root` | Post-rotation command (rolling) |

## Gotchas
- Wireshark may show error popups about unsupported operations — accept and dismiss; capture proceeds normally
- Rolling tcpdump creates files named `<hostname>.cap0`, `<hostname>.cap1`, etc. — share **all** of them
- Rolling capture: 5 files × 100MB = 500MB max storage; oldest file is overwritten when full
- Compress/zip large PCAP sets before sharing with Twingate support

## Related Docs
- Wireshark Download: https://www.wireshark.org/download.html
- Twingate Support (for rolling PCAP guidance and file submission)