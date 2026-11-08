---
source: https://help.twingate.com/articles/7071403289-handling-internal-domains-ending-in-local
type: help
fetched: 2026-11-08
source_version: 9ea91b3cf8363a53ec477b1ddb73124f66f46412ec486267b5c8efd493a6c17f
trust: official
---

# Handling Internal Domains Ending in .local

## Page Title
Handling Internal Domains Ending in .local

## Summary
`.local` is a reserved TLD (RFC 6762) for multicast DNS/Bonjour, causing conflicts when Twingate Resources use `.local` domains—especially on Linux and macOS. Several workarounds exist ranging from DNS config changes to disabling mDNS entirely.

## Key Information
- mDNS intercepts `.local` queries before they reach Twingate's DNS resolver
- Linux's `systemd-resolved` stub listener blocks `.local` forwarding to upstream DNS
- macOS Bonjour (`mDNSresponder`) handles `.local` at OS level, bypassing Twingate
- Apple recommends avoiding `.local` for internal networks entirely

## Solutions (Ordered by Invasiveness)

### 1. Use Subdomains (Least Disruptive)
Inject a company name as an intermediate domain:
- `fileshare.local` → `fileshare.companyname.local`
- `grafana.local` → `grafana.companyname.local`
Allows gradual migration without removing existing entries.

### 2. Assign a Twingate Alias
In Twingate console: Resource → Edit → click "Alias" next to the domain → add an alternative domain (e.g., `resource.int`). Users can then access via the alias instead of the `.local` domain.

### 3. Reprioritize DNS Precedence (Linux)
Edit `/etc/nsswitch.conf`:
```
# Before:
hosts: files mdns4_minimal [NOTFOUND=return] dns

# After:
hosts: files dns mdns4_minimal [NOTFOUND=return]
```
Then restart: `sudo systemctl restart systemd-resolved`

### 4. Disable mDNS Stub Listener (Linux — Last Resort)
Edit `/etc/systemd/resolved.conf`:
```
# Change:
#DNSStubListener=yes
# To:
DNSStubListener=no
```
Then: `sudo systemctl restart systemd-resolved`

### 5. Disable mDNS on macOS (Last Resort)
Requires disabling System Integrity Protection (SIP) first via Recovery Mode (`Command+R` on boot → Utilities → Terminal → `csrutil disable`). After reboot:
```
sudo launchctl unload -w /System/Library/LaunchDaemons/com.apple.mDNSresponder.plist
sudo launchctl unload -w /System/Library/LaunchDaemons/com.apple.mDNSresponderHelper.plist
```
To re-enable: replace `unload` with `load`, reboot, then re-enable SIP via `csrutil enable` in Recovery Mode.

## Gotchas
- Disabling mDNS breaks network discovery: file shares, printers, and screen sharing may stop working
- macOS SIP disable gives full root access to OS — significant security risk
- Changes in `/etc/nsswitch.conf` apply to the Connector host, not client machines
- The `-w` flag in `launchctl unload` persists changes across reboots
- Test both `.local` and alias domains after applying Twingate alias changes

## Prerequisites
- Access to Twingate admin console (for alias configuration)
- `sudo`/root access on Linux hosts
- macOS Recovery Mode access (for mDNS disable)

## Related Docs
- [RFC 6762](https://www.rfc-editor.org/rfc/rfc6762) — Multicast DNS specification
- Twingate Resource configuration (Alias feature)