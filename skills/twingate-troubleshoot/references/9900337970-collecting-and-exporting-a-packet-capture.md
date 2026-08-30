---
source: https://help.twingate.com/articles/9900337970-collecting-and-exporting-a-packet-capture
type: help
fetched: 2026-08-30
source_version: 0319f29f7aa9edcb3c4dcd017c779447f87959201dd81106ced2c2cd3f163c85
---

# Collecting and Exporting a Packet Capture

## Summary
Guide for capturing network traffic PCAPs using Wireshark or tcpdump for troubleshooting Twingate networking issues. Covers both single captures and rolling captures for intermittent problems.

## Key Information
- Two tool options: Wireshark (GUI, cross-platform) or tcpdump (CLI, Linux/macOS)
- Rolling PCAPs useful for intermittent issues that are hard to reproduce
- Rolling config: up to 5 files × 100MB each; oldest file overwritten when full
- Share **all** generated PCAP files with Twingate support
- Compress files before sharing if large

## Prerequisites
- **Wireshark**: Download from [wireshark.org/download](https://www.wireshark.org/download.html)
- **tcpdump**: Pre-installed on macOS; Linux install:
  - Debian: `sudo apt-get install tcpdump`
  - RPM: `sudo yum install tcpdump`

## Step-by-Step

### Wireshark — Single Capture
1. Open Wireshark, select all interfaces (click first, Shift+click last)
2. Click **Start capture** (top left)
3. Reproduce the issue
4. Click **Stop capture** (top left)
5. **File → Save As** → name file, ensure `pcapng` format selected

### Wireshark — Rolling Capture
1. Select all interfaces
2. **Capture → Options → Output tab**
3. Set filename (e.g., `tg_pcaps`) and configure rolling settings
4. Click **Start** (bottom right)
5. Stop via **Stop capture** button; no manual save needed

### tcpdump — Single Capture
```bash
sudo tcpdump -i any -s 0 -w $(hostname).cap
```
Stop: `Ctrl+C` (Linux) / `Cmd+C` (macOS)  
Output: `<hostname>.cap` in current directory

### tcpdump — Rolling Capture
```bash
sudo tcpdump -i any -s 0 -w $(hostname).cap -C 100 -W 5 -z root
```
Stop: `Ctrl+C` or kill by PID  
Output: `<hostname>.cap*` (multiple numbered files)

## Configuration Values

| Flag | Value | Meaning |
|------|-------|---------|
| `-i` | `any` | Capture all interfaces |
| `-s` | `0` | Full packet snaplen |
| `-w` | `$(hostname).cap` | Output filename |
| `-C` | `100` | Max file size (MB) |
| `-W` | `5` | Max number of rolling files |
| `-z` | `root` | Post-rotation compression command |

## Gotchas
- Wireshark may show error popups about unsupported operations — accept and continue, capture still works
- For rolling tcpdump, background processes must be stopped via PID; remember to stop them
- Rolling Wireshark captures save automatically — no `File → Save As` needed
- `-z root` in tcpdump rolling command runs as root post-rotation; verify this is appropriate for your environment

## Related Docs
- Twingate Support (for sharing PCAPs)
- [Wireshark Download Page](https://www.wireshark.org/download.html)