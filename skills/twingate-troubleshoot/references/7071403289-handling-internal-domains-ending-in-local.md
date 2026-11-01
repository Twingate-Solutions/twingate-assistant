---
source: https://help.twingate.com/articles/7071403289-handling-internal-domains-ending-in-local
type: help
fetched: 2026-11-01
source_version: 538d929611ba8361f9161767f8a0496833a82802c38f686adf63ca83755aa5c1
trust: official
---

# Handling Internal Domains Ending in .local

## Page Title
Handling Internal Domains Ending in .local

## Summary
The `.local` TLD is reserved for multicast DNS (mDNS/Bonjour) per RFC 6762, which causes conflicts when using `.local` domains with Twingate Resources on Linux and macOS. Several workarounds exist ranging from DNS config tweaks to disabling mDNS entirely.

## Key Information
- `.local` domains are intercepted by the OS mDNS stack before reaching Twingate's DNS resolver
- Problem is most pronounced on Linux (systemd-resolved) and macOS (Bonjour/mDNSResponder)
- Apple recommends avoiding `.local` for internal networks entirely
- Solutions range from low-impact (subdomain restructuring, aliases) to high-impact (disabling mDNS)

## Prerequisites
- Twingate Connector deployed on Linux or macOS host
- Admin/sudo access to connector or client machines
- Access to Twingate Admin Console to configure Resource aliases

## Solutions (in order of recommended approach)

### Option 1: Use Subdomains
Restructure `.local` hostnames to include a company subdomain:
- `fileshare.local` → `fileshare.companyname.local`
- Allows gradual migration; existing entries remain functional

### Option 2: Configure a Twingate Alias
1. Open Twingate Admin Console → Resource → Edit
2. Click **Alias** next to the defined domain name
3. Enter an alternative domain (e.g., `resource.int`)
4. Save and verify the change propagated to the local client
5. Test access via both the original `.local` and new alias

### Option 3: Reprioritize DNS in nsswitch.conf (Linux)
Edit `/etc/nsswitch.conf` on the Connector host:
```
# Change from:
hosts: files mdns4_minimal [NOTFOUND=return] dns

# To:
hosts: files dns mdns4_minimal [NOTFOUND=return]
```
Then restart: `sudo systemctl restart systemd-resolved`

### Option 4: Disable mDNS Stub Listener — Linux (Last Resort)
Edit `/etc/systemd/resolved.conf`:
```
# Change:
#DNSStubListener=yes
# To:
DNSStubListener=no
```
Restart: `sudo systemctl restart systemd-resolved`

### Option 5: Disable mDNS on macOS (Last Resort)
1. Boot into Recovery Mode (`Command+R`)
2. Open Utilities → Terminal
3. Run `csrutil disable` to disable System Integrity Protection
4. Reboot, then run:
   - `sudo launchctl unload -w /System/Library/LaunchDaemons/com.apple.mDNSresponder.plist`
   - `sudo launchctl unload -w /System/Library/LaunchDaemons/com.apple.mDNSresponderHelper.plist`

## Configuration Values
| File | Key | Value |
|------|-----|-------|
| `/etc/nsswitch.conf` | `hosts` order | `files dns mdns4_minimal [NOTFOUND=return]` |
| `/etc/systemd/resolved.conf` | `DNSStubListener` | `no` |

## Gotchas
- Disabling mDNS breaks network discovery features: file shares, printers, screen sharing
- macOS fix requires disabling System Integrity Protection — significant security risk; re-enable after changes
- Alias approach depends on OS/client behavior; test both the `.local` and alias domains after applying
- Changes to `nsswitch.conf` affect the Connector host, not end-user clients

## Related Docs
- [RFC 6762 – Multicast DNS](https://www.rfc-editor.org/rfc/rfc6762)
- Twingate Resource configuration (Admin Console)