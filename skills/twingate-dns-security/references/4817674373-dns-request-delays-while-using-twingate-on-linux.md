---
source: https://help.twingate.com/articles/4817674373-dns-request-delays-while-using-twingate-on-linux
type: help
fetched: 2026-08-06
source_version: 18744d5ccc30a1022210976ed6a1ae0b15e3a35770061add721d24ca0f746975
---

# DNS Request Delays While Using Twingate on Linux

## Summary
Some Linux users (particularly Arch Linux) experience sporadic 5-second DNS timeout delays when Twingate is active. The root cause is glibc's parallel IPv4/IPv6 DNS query resolution causing out-of-order responses. Setting `single-request` in `resolv.conf` resolves the issue.

## Key Information
- **Component:** Twingate Client
- **Platform:** Linux (notably Arch Linux)
- **Root cause:** glibc `libresolv` sends parallel IPv4 (A) and IPv6 (AAAA) DNS queries; out-of-order server responses trigger a 5-second timeout before sequential retry

## Symptoms
- Sporadic 5-second timeouts on network requests while Twingate is active
- Slow DNS resolution causing degraded network performance

## Fix

Edit `/etc/resolv.conf` and add the `single-request` option:

```
options single-request
```

**Example `/etc/resolv.conf`:**
```
nameserver 127.0.0.1
options single-request
```

This forces glibc to send IPv4 and IPv6 DNS requests sequentially instead of in parallel, eliminating the race condition that causes timeouts.

## Gotchas
- `/etc/resolv.conf` may be overwritten by `systemd-resolved`, `NetworkManager`, or `resolvconf` on system updates or network changes — ensure the option persists through your distro's DNS management mechanism
- This fix trades parallel query speed for reliability; DNS lookups may be marginally slower in ideal conditions
- Arch Linux users are specifically cited, but the issue can affect any Linux distro using glibc

## Related Docs
- [`resolv.conf` man page](https://man7.org/linux/man-pages/man5/resolv.conf.5.html)