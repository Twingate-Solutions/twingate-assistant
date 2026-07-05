# Device Posture Checks

## Page Title
Device Posture Checks

## Summary
Twingate Client natively collects device posture data to evaluate devices against Approved Operating Systems or Trusted Profiles. Available checks vary by platform (Windows, macOS, Linux, iOS, Android). These checks feed into Device Profiles for access control decisions.

## Key Information

### Windows Checks
- **HD encryption**: BitLocker status (system + other disks)
- **Screen lock**: Password required on screen saver return
- **Firewall**: Windows or third-party firewall via Windows Security Center
- **Antivirus**: Windows or third-party AV via Windows Security Center
- **Minimum OS version**: Windows 10, 11, Windows Server 2022

### macOS Checks
- **Screen lock**: Password required after sleep/screen saver
- **Biometric**: Touch ID/Face ID configured (clamshell mode always reports disabled)
- **Firewall**: Native firewall only; reports disabled if "Block all incoming connections" is enabled — **standalone Client only**
- **HD encryption**: FileVault status — **standalone Client only**
- **Minimum OS version**: macOS 14–26

### Linux Checks
- **Firewall**: UFW, firewalld, or iptables (Debian/Ubuntu, CentOS/Fedora, Arch Linux)
- **HD encryption**: All non-`/boot` partitions encrypted via LUKS (`libcryptsetup`)

### iOS Checks
- **Screen lock**: Passcode required
- **Biometric**: Touch ID/Face ID configured
- **Minimum OS version**: iOS 18–26

### Android Checks
- **Screen lock**: Any screen lock type configured
- **Biometric**: Fingerprint or facial recognition configured
- **HD encryption**: File-Based Encryption

## Prerequisites
- Twingate Client installed on device
- macOS firewall and FileVault checks require **standalone macOS Client** (not browser extension or other variants)

## Gotchas
- **macOS clamshell mode**: Biometric always reports as disabled when lid is closed, regardless of actual configuration
- **macOS firewall**: "Block all incoming connections" causes firewall to report as **disabled**
- **macOS firewall/FileVault**: Only available with standalone Client, not other deployment methods
- **Linux HD encryption**: Only checks non-`/boot` partitions; uses `libcryptsetup` library dependency
- **Android screen lock**: Reports any lock type (PIN, pattern, password) — no distinction between types

## Related Docs
- Device Profiles
- Approved Operating Systems
- Trusted Profiles
- macOS standalone Client documentation