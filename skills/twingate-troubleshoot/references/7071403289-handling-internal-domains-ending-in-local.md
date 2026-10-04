---
source: https://help.twingate.com/articles/7071403289-handling-internal-domains-ending-in-local
type: help
fetched: 2026-10-04
source_version: 9dc27cd54acea4fb53caaaa50214c41649b7581b156fdc3aed8f22f157f43d46
trust: official
---

# Handling Internal Domains Ending in .local

## Summary
The `.local` TLD is reserved for multicast DNS (mDNS/Bonjour) per RFC 6762, which causes conflicts when Twingate Resources use `.local` domains. This page covers four workaround approaches in order of invasiveness.

## Key Information
- Linux `systemd-resolved` and macOS Bonjour intercept `.local` DNS queries before they reach upstream resolvers
- Apple recommends avoiding `.local` for internal networks; use a registered domain or non-reserved TLD instead
- Solutions range from non-destructive (aliases, subdomains) to system-altering (disabling mDNS entirely)

## Prerequisites
- Twingate Connector deployed on Linux or macOS
- Resources configured in a Twingate Remote Network with `.local` domain names

---

## Solutions (ordered by invasiveness)

### 1. Use Subdomains (least disruptive)
Restructure `.local` hostnames to use a company subdomain:
- `fileshare.local` → `fileshare.companyname.local`
- `grafana.local` → `grafana.companyname.local`

Allows gradual migration; old entries can remain in DNS alongside new ones.

### 2. Assign an Alias in Twingate Console
In the Resource edit screen → click **Alias** next to the domain → enter alternate domain (e.g., `resource.int`).
Test access via both the `.local` and alias domain after Client syncs.

### 3. Reprioritize DNS in `/etc/nsswitch.conf` (Linux)
Edit `/etc/nsswitch.conf`:
```
# Before
hosts: files mdns4_minimal [NOTFOUND=return] dns

# After
hosts: files dns mdns4_minimal [NOTFOUND=return]
```
Then restart: `sudo systemctl restart systemd-resolved`

### 4. Disable mDNS Stub Listener (Linux — last resort)
Edit `/etc/systemd/resolved.conf`:
```ini
# Change from:
#DNSStubListener=yes
# To:
DNSStubListener=no
```
Then restart: `sudo systemctl restart systemd-resolved`

### 5. Disable mDNS on macOS (last resort)
1. Boot into Recovery Mode (`Command+R` on startup)
2. Open Terminal → `csrutil disable` (disables System Integrity Protection)
3. Reboot, then run:
```
sudo launchctl unload -w /System/Library/LaunchDaemons/com.apple.mDNSresponder.plist
sudo launchctl unload -w /System/Library/LaunchDaemons/com.apple.mDNSresponderHelper.plist
```
To re-enable: replace `unload` with `load`, reboot, then re-enable SIP via `csrutil enable` in Recovery Mode.

---

## Configuration Values
| File | Key | Value |
|------|-----|-------|
| `/etc/nsswitch.conf` | `hosts:` order | `files dns mdns4_minimal [NOTFOUND=return]` |
| `/etc/systemd/resolved.conf` | `DNSStubListener` | `no` |

## Gotchas
- Disabling mDNS breaks network discovery: file shares, printers, and screen sharing may stop working
- macOS fix requires disabling System Integrity Protection — significant security reduction
- Alias/subdomain approaches affect only Twingate routing; local mDNS still intercepts if client resolves before Twingate

## Related Docs
- [RFC 6762 – mDNS specification](https://www.rfc-editor.org/rfc/rfc6762)
- Twingate Resource configuration (aliases)