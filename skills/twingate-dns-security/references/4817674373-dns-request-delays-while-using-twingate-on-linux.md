---
source: https://help.twingate.com/articles/4817674373-dns-request-delays-while-using-twingate-on-linux
type: help
fetched: 2026-11-01
source_version: caf382dc22f70696943e4087853590c8f18dc4840856327f68d57c089bc1fe30
trust: official
---

# DNS Request Delays While Using Twingate on Linux

## Page Title
DNS Request Delays While Using Twingate on Linux

## Summary
Some Linux users (notably Arch Linux) experience sporadic 5-second DNS resolution timeouts when Twingate is active. The root cause is glibc's parallel IPv4/IPv6 DNS query behavior where out-of-order server responses trigger a timeout before sequential retry. Setting `single-request` in `/etc/resolv.conf` resolves the issue.

## Key Information
- Affects Linux clients, particularly Arch Linux
- Symptom: sporadic 5-second timeouts on network requests
- Cause: glibc (`libresolv`) sends parallel A (IPv4) and AAAA (IPv6) DNS queries; out-of-order responses cause a 5-second timeout before falling back to sequential queries

## Prerequisites
- Linux system with glibc
- Twingate Client installed and active
- Write access to `/etc/resolv.conf`

## Step-by-Step Fix

1. Open `/etc/resolv.conf` in a text editor with root privileges:
   ```
   sudo nano /etc/resolv.conf
   ```

2. Add the `single-request` option:
   ```
   options single-request
   ```

3. Save the file. No restart required for new DNS queries to use the setting.

## Configuration Values

| File | Option | Effect |
|------|--------|--------|
| `/etc/resolv.conf` | `options single-request` | Forces sequential IPv4/IPv6 DNS lookups instead of parallel |

## Gotchas
- **resolv.conf may be overwritten**: Many Linux systems manage `/etc/resolv.conf` automatically via `systemd-resolved`, `NetworkManager`, or `resolvconf`. Changes may be lost on network restart or reboot. Persist the option through your network manager's configuration instead.
- `single-request` trades parallelism for reliability — DNS lookups may be marginally slower in the happy path, but eliminates the 5-second penalty on out-of-order responses.
- This is a system-wide change affecting all DNS resolution, not just Twingate traffic.

## Related Docs
- [`resolv.conf` man page](https://man7.org/linux/man-pages/man5/resolv.conf.5.html)
- Twingate Linux Client documentation