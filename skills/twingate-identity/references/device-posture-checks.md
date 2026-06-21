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
- **Firewall**: Native firewall only; standalone Client required; "Block all incoming connections" reports as disabled
- **HD encryption**: FileVault status; standalone Client required
- **Minimum OS version**: macOS 14–26

### Linux Checks
- **Firewall**: UFW, firewalld, or iptables; supported on Debian/Ubuntu, CentOS/Fedora, Arch Linux
- **HD encryption**: LUKS encryption via `libcryptsetup`; all partitions except `/boot` must be encrypted

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
- macOS Firewall and HD encryption checks require **macOS standalone Client** (not browser extension or other variants)
- Linux HD encryption requires `libcryptsetup` library present

## Gotchas
- **macOS clamshell mode**: Biometric always reported as disabled when lid is closed, regardless of actual configuration
- **macOS Firewall**: "Block all incoming connections" setting causes firewall to report as **disabled**
- **macOS Firewall/FileVault**: Only available with standalone Client — not other Client types
- **Linux HD encryption**: `/boot` partition exempted; all other partitions must use LUKS
- **Linux Firewall**: Only specific distro families supported (Debian/Ubuntu, CentOS/Fedora, Arch)
- Minimum OS version ranges are bounded — verify current supported versions as they update

## Related Docs
- Device Profiles
- Approved Operating Systems
- Trusted Profiles
- macOS standalone Client documentation