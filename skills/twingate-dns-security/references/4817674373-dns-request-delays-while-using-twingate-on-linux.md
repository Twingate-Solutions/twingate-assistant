---
source: https://help.twingate.com/articles/4817674373-dns-request-delays-while-using-twingate-on-linux
type: help
fetched: 2026-09-06
source_version: 81856fc2d506de3b83393e03cd33ccb6bcabad52aa90dc1b5dccb49b064108f5
---

# DNS Request Delays While Using Twingate on Linux

## Summary
Some Linux users (notably Arch Linux) experience sporadic 5-second DNS timeouts when Twingate is active. The root cause is glibc's parallel IPv4/IPv6 DNS query resolution, which times out when responses arrive out of order.

## Key Information
- **Affected component:** Twingate Client
- **Platform:** Linux (particularly Arch Linux)
- **Symptom:** Sporadic 5-second timeouts on network requests caused by DNS resolution delays
- **Root cause:** glibc's `libresolv` sends parallel IPv4 and IPv6 DNS requests; out-of-order responses trigger a 5-second timeout before falling back to sequential retry

## Prerequisites
- Linux system using glibc
- Twingate client installed and active

## Resolution

Edit `/etc/resolv.conf` to add the `single-request` option:

```
options single-request
```

This forces glibc to perform IPv4 and IPv6 DNS lookups **sequentially** instead of in parallel, eliminating the out-of-order response timeout.

## Configuration Values

| File | Option | Effect |
|------|--------|--------|
| `/etc/resolv.conf` | `single-request` | Forces sequential IPv4/IPv6 DNS resolution |

## Gotchas
- `/etc/resolv.conf` may be overwritten by `systemd-resolved`, `NetworkManager`, or `resolvconf` on system events — the change may not persist across network restarts or reboots without additional configuration
- Sequential resolution may slightly increase total DNS lookup time compared to parallel resolution under ideal conditions, but eliminates the 5-second timeout penalty

## Related Docs
- [`resolv.conf` man page](https://man7.org/linux/man-pages/man5/resolv.conf.5.html)