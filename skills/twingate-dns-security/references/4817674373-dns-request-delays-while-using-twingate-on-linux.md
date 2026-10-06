---
source: https://help.twingate.com/articles/4817674373-dns-request-delays-while-using-twingate-on-linux
type: help
fetched: 2026-10-04
source_version: 481a28a428928b99915784a92cb6f10a1b688e15b30151cf71810214c6fab957
trust: official
---

# DNS Request Delays While Using Twingate on Linux

## Summary
Some Linux users (notably Arch Linux) experience sporadic 5-second DNS timeouts when Twingate is active. The cause is glibc's parallel IPv4/IPv6 DNS query behavior where out-of-order server responses trigger a timeout before sequential retry.

## Key Information
- **Affected component:** Twingate Client
- **Platform:** Linux (particularly Arch Linux)
- **Root cause:** glibc `libresolv` sends parallel IPv4 (A) and IPv6 (AAAA) DNS queries; if responses arrive out of order, a 5-second timeout occurs before sequential retry begins
- **Symptom:** Sporadic 5-second network request delays while Twingate is running

## Prerequisites
- Linux system using glibc (libresolv)
- Twingate Client installed and active

## Resolution

Add the `single-request` option to `/etc/resolv.conf`:

```
options single-request
```

This forces glibc to send IPv4 and IPv6 DNS requests **sequentially** instead of in parallel, eliminating the out-of-order response timeout.

**Example `/etc/resolv.conf` entry:**
```
# existing nameserver lines...
nameserver 127.0.0.1
options single-request
```

## Gotchas
- `/etc/resolv.conf` may be overwritten by `systemd-resolved`, `NetworkManager`, or `resolvconf` on system restart or network changes — changes may need to be made in the managing service's configuration instead
- `single-request` trades timeout elimination for slightly increased sequential DNS lookup latency; this is generally preferable to 5-second sporadic delays
- This is a system-level workaround, not a Twingate configuration change

## Configuration Values
| Option | File | Effect |
|--------|------|--------|
| `single-request` | `/etc/resolv.conf` | Disables parallel A/AAAA queries in glibc |

## Related Docs
- [`resolv.conf` man page](https://man7.org/linux/man-pages/man5/resolv.conf.5.html)
- Twingate Linux Client documentation