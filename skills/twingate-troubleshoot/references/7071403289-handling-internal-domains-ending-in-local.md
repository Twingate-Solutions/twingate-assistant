---
source: https://help.twingate.com/articles/7071403289-handling-internal-domains-ending-in-local
type: help
fetched: 2026-08-06
source_version: 30323019557a1783cd824629d5b5bd50793341a1e55941105f9faa08b6e3c3d6
---

# Handling Internal Domains Ending in .local

## Summary
The `.local` TLD is reserved for mDNS/Bonjour and conflicts with Twingate DNS resolution on Linux and macOS. This doc covers four approaches to resolve `.local` domain conflicts, ranging from minor configuration changes to disabling mDNS entirely.

## Key Information
- `.local` TLD conflicts arise because client OS mDNS services intercept resolution before Twingate can handle it
- Linux's `systemd-resolved` stub listener won't forward `.local` DNS requests upstream
- macOS Bonjour service similarly captures `.local` requests
- Apple recommends using registered domains instead of `.local` for internal networks

## Solutions (Ordered by Invasiveness)

### 1. Use Subdomains
Restructure `resource.local` → `resource.companyname.local`
- Allows gradual migration without removing existing entries
- Effectiveness depends on OS/client application

### 2. Add a Twingate Alias
In Twingate console: Resource → Edit → Alias → enter alternative domain (e.g., `resource.int`)
- Avoids direct `.local` access from client
- Test both the `.local` and aliased versions after applying

### 3. Reprioritize DNS in nsswitch.conf (Linux)
Edit `/etc/nsswitch.conf`:
```
# Before
hosts: files mdns4_minimal [NOTFOUND=return] dns

# After
hosts: files dns mdns4_minimal [NOTFOUND=return]
```
Then: `sudo systemctl restart systemd-resolved`

### 4. Disable mDNS (Last Resort)

**Linux** — Edit `/etc/systemd/resolved.conf`:
```ini
# Change from:
#DNSStubListener=yes
# To:
DNSStubListener=no
```
Then: `sudo systemctl restart systemd-resolved`

**macOS:**
1. Boot into Recovery Mode (`Command+R`)
2. Run `csrutil disable` in Recovery Terminal
3. Reboot, then run:
```bash
sudo launchctl unload -w /System/Library/LaunchDaemons/com.apple.mDNSresponder.plist
sudo launchctl unload -w /System/Library/LaunchDaemons/com.apple.mDNSresponderHelper.plist
```

## Configuration Values
| File | Setting | Value |
|------|---------|-------|
| `/etc/nsswitch.conf` | `hosts:` order | `files dns mdns4_minimal [NOTFOUND=return]` |
| `/etc/systemd/resolved.conf` | `DNSStubListener` | `no` |

## Gotchas
- Disabling mDNS breaks network discovery, file shares, printers, and screen sharing
- macOS mDNS disable requires disabling System Integrity Protection (SIP) — significant security trade-off
- Re-enable SIP after re-enabling mDNS on macOS (`csrutil enable` in Recovery)
- Changes to `launchctl unload -w` persist across reboots; use `load` to reverse

## Prerequisites
- Linux: `systemd-resolved` service
- macOS: Admin access; SIP disable requires physical access for Recovery Mode boot

## Related Docs
- [RFC 6762](https://tools.ietf.org/html/rfc6762) — `.local` mDNS specification
- Twingate Resource configuration (Alias feature)