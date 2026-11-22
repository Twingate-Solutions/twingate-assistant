---
source: https://help.twingate.com/articles/1900346829-twingate-client-system-requirements-and-supported-operating-systems
type: help
fetched: 2026-11-22
source_version: 69806462aab08d1737422bfd036066c2f7f4de8d062cd25f26cd588dc305dc56
trust: official
---

# Twingate Client System Requirements and Supported Operating Systems

## Summary
Lists the minimum OS versions and platforms supported by the Twingate Client on desktop (Windows, macOS, Linux) and mobile (iOS, Android). Twingate does not support OS versions that have reached end-of-life. The client may still work on them for a time, but updates may stop being available.

## Key Information
- **Windows:** Windows 10 21H2 (E) (LTS) minimum. Windows 7/8 are not supported.
- **macOS:** macOS 14 (Sequoia) minimum. Older versions (e.g. Monterey) may install older client versions but are not officially supported.
- **Linux (x86/AMD64 and ARM64 unless noted):**
  - Ubuntu 20.04, 22.04, 24.04 LTS
  - Debian 9 or later
  - Fedora 40 or later
  - CentOS Stream 9 or later
  - Oracle Linux 8 or later
  - Arch Linux, ThinPro, NixOS: x64/AMD64 only
- **iOS:** iOS 18 minimum (App Store).
- **Android:** Android 14 minimum (Google Play). Some custom ROMs or restricted devices may be unsupported.

## Prerequisites
- Admin rights for the initial install on Windows and macOS.
- Windows: .NET 8 Desktop Runtime (bundled with the .exe installer).
- macOS: the System Extension framework must be available, since the client relies on it for network extensions.

## Step-by-Step
Not applicable. This is a reference page. Use it to verify the OS version before installing.

## Configuration Values
None listed. Behaviors noted:
- Twingate sets up a local DNS resolver on the device to resolve private resources (system DNS configuration is modified).

## Gotchas
- End-of-life OS versions may work but are unsupported, and client updates may stop arriving.
- Windows 7/8 are unsupported.
- The macOS minimum is high (14); older macOS may silently receive older client builds.
- Arch Linux, ThinPro, and NixOS are x64/AMD64 only (no ARM64).
- Custom Android ROMs and restricted devices may not work.
- Because the client changes local DNS, conflicts with other DNS or VPN software are possible (inferred from the local resolver behavior; verify in your environment).

## Related Docs
No related page links appear in the source material.