---
source: https://help.twingate.com/articles/7071403289-handling-internal-domains-ending-in-local
type: help
fetched: 2026-09-06
source_version: ab080a5af81bc80b99992c09b5a6df27b0c7f29f08b3038c057ecd0f4fbf6cb8
---

# Handling Internal Domains Ending in .local

## Summary
The `.local` TLD is reserved for multicast DNS (mDNS/Bonjour) per RFC 6762, causing conflicts when Twingate Resources use `.local` domains—especially on Linux and macOS. Three escalating solutions are available: subdomain restructuring, Twingate aliases, DNS reprioritization, or disabling mDNS entirely.

## Key Information
- `.local` conflicts with mDNS on Linux (systemd-resolved) and macOS (Bonjour/mDNSResponder)
- Apple recommends avoiding `.local` for internal networks entirely
- Solutions range from non-destructive (alias) to high-impact (disable mDNS)

## Prerequisites
- Twingate Resources already configured in a Remote Network
- Admin access to Connector host (Linux solutions)
- macOS: Recovery Mode access + willingness to disable SIP

## Solutions (Escalating Impact)

### Option 1: Subdomain Restructuring
Add a company subdomain to push `.local` to a sub-level:
- `fileshare.local` → `fileshare.companyname.local`
- Allows gradual migration; keep old entries during transition

### Option 2: Twingate Alias
1. Open Resource in Twingate console → **Edit**
2. Click **Alias** next to the domain name
3. Enter alternate domain (e.g., `resource.int`)
4. Verify change propagates to local Client
5. Test access via both original `.local` and new alias

### Option 3: Reprioritize DNS on Connector Host (Linux)
```bash
sudo nano /etc/nsswitch.conf
```
Change:
```
hosts: files mdns4_minimal [NOTFOUND=return] dns
```
To:
```
hosts: files dns mdns4_minimal [NOTFOUND=return]
```
```bash
sudo systemctl restart systemd-resolved
```

### Option 4: Disable mDNS (Last Resort)

**Linux** — Disable systemd-resolved stub listener:
```bash
sudo nano /etc/systemd/resolved.conf
# Change: #DNSStubListener=yes
# To:     DNSStubListener=no
sudo systemctl restart systemd-resolved
```

**macOS** — Requires disabling System Integrity Protection (SIP):
1. Reboot → hold `Command+R` → Utilities → Terminal
2. Run `csrutil disable`, then reboot
3. After reboot:
```bash
sudo launchctl unload -w /System/Library/LaunchDaemons/com.apple.mDNSresponder.plist
sudo launchctl unload -w /System/Library/LaunchDaemons/com.apple.mDNSresponderHelper.plist
```
To re-enable: replace `unload` with `load`, reboot, re-enable SIP via `csrutil enable`

## Configuration Values
| File | Setting | Value |
|------|---------|-------|
| `/etc/systemd/resolved.conf` | `DNSStubListener` | `no` |
| `/etc/nsswitch.conf` | `hosts` order | `files dns mdns4_minimal [NOTFOUND=return]` |

## Gotchas
- Disabling mDNS breaks network discovery: file shares, printers, screen sharing affected
- macOS SIP disable gives full root access—security risk; re-enable after
- The `-w` flag on `launchctl unload` makes changes persist across reboots
- Alias and DNS reprioritization can be combined for better results

## Related Docs
- [RFC 6762 – mDNS](https://datatracker.ietf.org/doc/html/rfc6762)
- Twingate Resource configuration (Alias feature)