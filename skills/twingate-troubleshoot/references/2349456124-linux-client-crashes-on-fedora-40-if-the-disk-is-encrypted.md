---
source: https://help.twingate.com/articles/2349456124-linux-client-crashes-on-fedora-40-if-the-disk-is-encrypted
type: help
fetched: 2026-08-06
source_version: e0ef27df9148fab95ac7e766468c2bb59383bc6d9618c6ba0452a9bf26be6b84
---

# Linux Client Crashes on Fedora 40 (Encrypted Disk)

## Page Title
Linux Client Crashes on Fedora 40 if the Disk is Encrypted

## Summary
The Twingate Linux client fails to start on Fedora 40 systems due to an incompatibility with OpenSSL 3.2.1, which ships by default in Fedora 40. Encrypted disk installations are particularly noted as affected since Fedora 40 enables encryption by default.

## Key Information
- **Affected component:** Twingate Linux Client
- **Affected OS:** Fedora Linux 40 (encrypted or unencrypted)
- **Root cause:** Incompatibility with OpenSSL version 3.2.1 introduced in Fedora 40
- **Status:** Known issue reported to development team; no permanent fix available at time of publication

## Prerequisites
- Twingate Client installed on Fedora 40
- `dnf` package manager available
- Sudo/root access to downgrade system packages

## Workaround (Step-by-Step)

Downgrade `openssl-libs` to the Fedora 39 version:

```bash
sudo dnf downgrade --releasever=39 openssl-libs
```

After downgrade, attempt to start the Twingate client normally.

## Configuration Values
| Parameter | Value |
|---|---|
| Incompatible OpenSSL version | 3.2.1 (Fedora 40 default) |
| Target downgrade version | 3.1.1 (from Fedora 39) |
| `--releasever` flag value | `39` |

## Gotchas
- Fedora 40 enables full disk encryption **by default** on fresh installs — most Fedora 40 users are likely affected regardless of whether they explicitly chose encryption
- Downgrading `openssl-libs` is a system-wide change and may affect other applications depending on OpenSSL 3.2.x features
- Future system updates via `dnf upgrade` may re-upgrade `openssl-libs` back to 3.2.x, breaking the client again — consider pinning or excluding the package after downgrade
- No permanent fix ETA provided in documentation

## Related Docs
- Twingate Linux Client installation documentation
- Fedora 40 release notes (OpenSSL 3.2.1 inclusion)