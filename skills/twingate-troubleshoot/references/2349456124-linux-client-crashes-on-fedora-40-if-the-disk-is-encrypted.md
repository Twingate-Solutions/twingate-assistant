---
source: https://help.twingate.com/articles/2349456124-linux-client-crashes-on-fedora-40-if-the-disk-is-encrypted
type: help
fetched: 2026-09-06
source_version: 9e423c1494840a69ac1b7c550e8071b5025799694e05eaf9ab164168ab595f1a
---

# Linux Client Crashes on Fedora 40 (Encrypted Disk)

## Page Title
Linux Client crashes on Fedora 40 if the disk is encrypted

## Summary
The Twingate Linux Client fails to start on Fedora 40 systems (which are encrypted by default) due to an incompatibility with OpenSSL 3.2.1 introduced in that OS version. The only current workaround is downgrading the OpenSSL library to the Fedora 39 version.

## Key Information
- Crash occurs on fresh installs of Fedora 40 with disk encryption enabled
- Fedora 40 enables disk encryption by default, making this a widespread issue
- Root cause: incompatibility with **OpenSSL 3.2.1** (shipped with Fedora 40)
- Fix is under investigation by Twingate development team

## Affected Components
- **Component:** Twingate Client
- **Platform:** Linux
- **OS:** Fedora Linux 40 (encrypted disk)

## Prerequisites
- Twingate Client installed on Fedora 40
- `dnf` package manager available
- sudo/root access

## Workaround: Downgrade OpenSSL

```bash
sudo dnf downgrade --releasever=39 openssl-libs
```

This downgrades `openssl-libs` to the Fedora 39 version (3.1.1), which is compatible with the Twingate Client.

## Gotchas
- Disk encryption is **on by default** in Fedora 40 — this affects standard installations, not just explicitly encrypted setups
- Downgrading system OpenSSL libraries may affect other applications or security posture; evaluate before applying in production
- No permanent fix available at time of publication; monitor Twingate release notes for updates
- The workaround targets `openssl-libs` specifically, not the full `openssl` package

## Related Docs
- Twingate Linux Client installation documentation
- Fedora 40 release notes (OpenSSL 3.2.1 changes)